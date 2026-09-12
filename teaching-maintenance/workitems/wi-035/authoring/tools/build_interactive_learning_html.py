"""Build the offline interactive teaching site for the 58-model roadmap.

The generated HTML is deliberately self-contained: it embeds the concise
teaching copy and JavaScript, while continuing to reference the canonical PNG
assets by relative path.  This means learners can open it directly with
``file://`` and still use search, progress, engineering reading cards, and
the POC canvas.

Run from anywhere::

    python tools/build_interactive_learning_html.py

The active image filenames are read from each topic's ``slide-manifest.md``;
they are never inferred from a model name.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from PIL import Image

try:
    from visual_storyboard_contract import inline_visual_relative_path, load_storyboards
except ModuleNotFoundError:  # pragma: no cover - supports importlib-based tests
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from visual_storyboard_contract import inline_visual_relative_path, load_storyboards


ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "roadmap-model-selection"
SECTION_PAGES = ROOT / "course-delivery" / "section-pages"
LEARNER_BRIEFS = ROOT / "_course_content" / "learner-briefs.json"
TEACHING_TOPICS = ROOT / "_course_content" / "topics"
CONCEPT_VISUALS_ROOT = ROOT / "_course_content" / "generated-concepts"
HOME_HERO_IMAGE = "_course_content/generated-concepts/shared/vision-ai-course-home-hero_v01.png"
SHARED_JOURNEY_IMAGES = {
    "foundations": {
        "image": "_course_content/generated-concepts/shared/vision-ai-foundations-journey_v01.png",
        "alt": "同一片 AOI 工件從原始取像、可觀測性確認、候選標記到人工 evidence review 的連續工作流程。",
        "caption": "先確認原始 evidence 看得見、條件可重播，再產生 candidate 並交由人員 review。",
    },
    "production": {
        "image": "_course_content/generated-concepts/shared/vision-ai-production-journey_v01.png",
        "alt": "同一個 AOI 工件從離線 evidence、shadow mode 檢查、人工 review 到 amber rollback 路徑的量產流程。",
        "caption": "模型先在 shadow mode 蒐集可追溯 evidence；條件改變或證據不足時，走 HOLD／rollback，而非直接影響現場。",
    },
}
STORYBOARD_DIR = ROOT / "_course_content" / "visual-storyboards"
SPECS = (
    ROOT / "_batch_specs" / "anomaly.json",
    ROOT / "_batch_specs" / "remaining.json",
    ROOT / "_batch_specs" / "vision.json",
    ROOT / "_batch_specs" / "completed-diffusion.json",
    ROOT / "_batch_specs" / "completed-anomaly.json",
    ROOT / "_batch_specs" / "completed-detector.json",
)
OUTPUT = ROOT / "interactive-learning.html"


# These approved shared pages fill the teaching gaps between individual
# models: all users need a common vocabulary, and an engineering team needs a
# visible path from a POC to production.  They are deliberately read from the
# manifest below rather than inferred from filenames.
SUPPORTING_COLLECTIONS: dict[str, dict[str, Any]] = {
    "foundations": {
        "relative_dir": "00-foundations-and-reading-guide",
        "label": "開始前：共同工程前提",
        "intro": "先建立共同語言，才不會把候選、分數或漂亮圖誤當成可直接放行的結論。",
        "items": [
            ("FDN-00-01", "先從輸出責任選路", "先寫清楚需要的是 label、box、mask、座標、heatmap、track、文字 claim 或 synthetic image，再選模型家族。"),
            ("FDN-00-02", "可觀測性先於模型", "最小 defect pixels、SNR、焦距、照明與對位殘差決定模型是否真的看得到目標。"),
            ("FDN-00-03", "raw frame 到決策的資料鏈", "把 calibration、registration、ROI、tile、resize 與回映座標寫成可重播的 transform chain。"),
            ("FDN-00-04", "輸出不等於產線決策", "模型輸出需要明確 owner 與 evidence gate；沒有可追溯證據就不能跳到 PASS／FAIL。"),
            ("FDN-00-05", "用資料狀態選合法候選", "known-bad、clean normal、few-shot feature 或 text query 的資料條件，決定可走的模型路線。"),
            ("FDN-00-06", "讀圖前先認識共通符號", "從 versioned ROI、feature、score、threshold 到 abstain signal，整套課程使用同一個工程語言。"),
            ("FDN-00-07", "四步讀懂每個模型圖", "定位、機制、建置契約、選型邊界；讀圖時始終回到輸入、輸出、證據與 owner。"),
            ("FDN-00-08", "沒有共同契約就不能排名", "固定 ROI、資料 split、輸出定義、hardware、P95 與 gate，才有公平的模型比較。"),
            ("FDN-00-09", "產線指標不是單一 AUROC", "把 critical recall、escape、false HOLD、review load、P50/P95/P99 與決策單位一起量。"),
            ("FDN-00-10", "先釐清 DINO 指的是哪一種", "DINO detector、DINOv2/v3 visual encoder 與 AnomalyDINO 的輸入、輸出與責任不同。"),
            ("FDN-00-11", "系統責任邊界", "detector、AD、VLM 與生成影像各自提供不同候選；不能互相取代物理證據。"),
            ("FDN-00-12", "freeze split 與 threshold", "把 calibration 與 future／challenge 分開，才能避免用洩漏資料證明一個看似漂亮的 threshold。"),
            ("FDN-00-13", "最小 evidence bundle", "保存 raw input、ROI、版本、threshold、輸出、錯誤案例與 reviewer，讓下游動作可稽核。"),
            ("FDN-00-14", "研究主張與量產主張不同", "paper 結果不是 camera-to-PLC 的 qualification；量產還要補 runtime、drift、owner 與 fallback。"),
            ("FDN-00-15", "POC 的最低可交付物", "漂亮 demo 不足以 go；POC 必須有基線、契約、error taxonomy、failure gallery 與 go/no-go。"),
            ("FDN-00-16", "HOLD／REVIEW 是正確設計", "超出 qualification envelope、證據衝突或不確定時，系統要有明確的停下與交回人工流程。"),
            ("FDN-00-17", "每個量化主張都附條件", "資料、split、模型、hardware、threshold 與評估條件不完整時，數字不能成為選型結論。"),
            ("FDN-00-18", "進入模型前的 readiness check", "用一個真實 AOI 問題確認可觀測性、資料 regime、SLA 與證據責任已準備好。"),
        ],
    },
    "production": {
        "relative_dir": "08-benchmark-production-cases-and-review",
        "label": "從 POC 到量產：工程實作與案例",
        "intro": "模型選型結束後，還必須經過公平比較、shadow mode、drift、rollback 與人類責任的完整工程路徑。",
        "items": [
            ("PRDSHR-08-01", "從研究主張走到量產 operating point", "先把模型結果交給有門檻、有 owner 的 qualification，而不是直接把 paper claim 變成動作。"),
            ("PRDSHR-08-02", "資料庫與證據保存", "量產決策需要可回溯的資料 vault、版本與證據，而不是散落的輸出截圖。"),
            ("PRDSHR-08-03", "定義正確的決策單位", "先定義 die、wafer、lot、event 或時間窗，才知道哪個輸出、threshold 與 owner 合理。"),
            ("PRDSHR-08-04", "任務與指標要對齊", "每個模型的 KPI 要對應實際 action、錯誤代價與人力負荷。"),
            ("PRDSHR-08-05", "threshold freeze 是受控 evidence gate", "threshold 只能在已凍結的 calibration 與 contract 下建立；改條件就要重新驗證。"),
            ("PRDSHR-08-06", "端到端成本也是證據", "把 capture、queue、model、postprocess、review 與 action 的完整延遲與資源一起量。"),
            ("PRDSHR-08-07", "版本化才能重播動作", "把 recipe、資料、model、prompt、threshold、export 與硬體版本留在同一份 evidence record。"),
            ("PRDSHR-08-08", "error taxonomy 連到 fallback", "先分類錯誤情境，再指定每種錯誤的 fallback／HOLD／人工處理，而不是只看總分。"),
            ("PRDSHR-08-09", "公平比較的前提", "只有 acquisition、split 與 action contract 對齊時，才可以比較候選模型。"),
            ("PRDSHR-08-10", "從基線開始 qualification", "用透明 baseline 建立可理解的最低性能，再逐步提升模型複雜度。"),
            ("PRDSHR-08-11", "qualification ladder", "從可觀測性、離線證據、shadow 到受控 action，逐級提高可承擔的決策責任。"),
            ("PRDSHR-08-12", "先在 shadow mode 學習", "先並行蒐集 false HOLD、escape、P95 與 review load，再考慮改變現場動作。"),
            ("PRDSHR-08-13", "漂移要有 owner", "資料與光學漂移不是事後分析；要有監控、觸發、rebuild 與復驗的明確責任。"),
            ("PRDSHR-08-14", "rollback 與 fallback 要先寫好", "任何部署都必須在失效前就決定如何退回安全流程。"),
            ("PRDSHR-08-15", "人與系統的責任分界", "先標明模型、reviewer、製程與系統各自能決定什麼，避免責任在錯誤發生後才被追問。"),
            ("PRDSHR-08-16", "資料與安全控制", "資料 egress、ACL、SOP、log 與 rollback 也屬於量產決策的一部分。"),
            ("PRDSHR-08-17", "案例：tiny known defect", "用最小 defect pixel、標註品質與決策單位治理已知小缺陷，而不是只看 detector score。"),
            ("PRDSHR-08-18", "案例：normal-only surface anomaly", "以乾淨 normal support、低 FPR、review load 與 drift 來驗收異常候選流程。"),
            ("PRDSHR-08-19", "案例：logical anomaly", "幾何／組裝關係的異常需要定義可觀測關係與下游證據，不是只靠局部 texture。"),
            ("PRDSHR-08-20", "案例：alignment drift", "把 registration residual、重建條件與安全 fallback 明確連到量測或檢測動作。"),
            ("PRDSHR-08-21", "案例：video equipment event", "事件 truth、timestamps、track continuity、end-to-end latency 與警報 owner 必須一起驗收。"),
            ("PRDSHR-08-22", "案例：text-guided SOP support", "VLM 的文字候選與 SOP assist 需要 grounding、ACL、evidence 及人類批准。"),
            ("PRDSHR-08-23", "案例：rare-defect augmentation", "合成資料可補訓練資料，但一定要保存 provenance，並以真實 holdout 證明下游改善。"),
            ("PRDSHR-08-24", "案例：repaired image 的證據邊界", "修復影像可輔助閱讀或生成資料，不能取代 raw physical evidence。"),
        ],
    },
}


# Foundations has a particularly useful legacy set of detailed engineering
# diagrams.  They are not allowed to teach the public first read any more:
# each item now exposes its image-led AOI story first and keeps the compact
# diagram behind an explicitly closed disclosure for implementation detail.
SUPPORTING_ENGINEERING_REFERENCES: dict[str, str] = {
    "FDN-00-01": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-01-course-map_v02.png",
    "FDN-00-02": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-02-observability-limit_v01.png",
    "FDN-00-03": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-03-data-transform-chain_v01.png",
    "FDN-00-04": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-04-output-responsibility_v02.png",
    "FDN-00-05": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-05-data-regime-routing_v01.png",
    "FDN-00-06": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-06-common-symbols_v01.png",
    "FDN-00-07": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-07-model-page-reading_v01.png",
    "FDN-00-08": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-08-comparison-contract_v01.png",
    "FDN-00-09": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-09-production-metrics_v01.png",
    "FDN-00-10": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-10-dino-disambiguation_v01.png",
    "FDN-00-11": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-11-system-boundaries_v01.png",
    "FDN-00-12": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-12-split-threshold-freeze_v01.png",
    "FDN-00-13": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-13-evidence-bundle_v01.png",
    "FDN-00-14": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-14-research-production-maturity_v01.png",
    "FDN-00-15": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-15-minimum-poc-output_v01.png",
    "FDN-00-16": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-16-human-abstain_v01.png",
    "FDN-00-17": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-17-citation-contract_v01.png",
    "FDN-00-18": "course-delivery/section-pages/00-foundations-and-reading-guide/images/final/FDN-00-18-reading-check_v01.png",
}


# Family maps and comparison pages make the "why this model rather than the
# neighbouring one?" decision explicit.  They are separate from the 58
# model-specific four-image lessons and therefore remain useful for route
# planning and POC design.
FAMILY_SUPPORT: dict[str, dict[str, Any]] = {
    "geometry": {
        "relative_dir": "01-geometry-alignment-measurement",
        "items": [
            ("GEO-01", "幾何路線總覽", "由可觀測條件決定應先用 ChArUco、ECC、SIFT 或 LightGlue。"),
            ("GEO-02", "共同幾何契約", "對位、量測與模型比較前，先固定相機、ROI、殘差與回映座標。"),
            ("GEO-19", "不要用單一 accuracy 排名", "把不同幾何輸出接回同一個 downstream decision，才知道能否比較。"),
            ("GEO-20", "公平幾何實驗", "以受控資料、同一評估與失效條件做公平 comparison。"),
            ("GEO-21", "從對位走到量測", "registration evidence 不等於量測證據；還要經過 calibration 與 uncertainty。"),
            ("GEO-22", "對位失敗時的安全 fallback", "遮擋、殘差或 drift 超界時，系統應停在安全流程而非硬送下游。"),
            ("GEO-23", "wafer 對位 workshop", "把困難情境拆成可觀測條件、候選方法、共同比較與 review gate。"),
        ],
    },
    "classification": {
        "relative_dir": "02-known-target-classification-segmentation",
        "items": [
            ("KNT-01", "先分清 class、mask 與 keypoint", "輸出責任不同，不能拿同一種指標或相同宣稱混在一起比較。"),
            ("KNT-02", "已知目標的共同工程 gate", "pixels、labels、OOD、P95 與 action owner 是所有 known-target 模型的共同前提。"),
            ("KNTSHR-35", "分類 backbone 的公平比較", "ResNet、ConvNeXt、ViT 必須在相同資料、pixel、訓練與 evidence contract 下比較。"),
            ("KNTSHR-36", "instance 與 semantic 的不同責任", "instance mask 與 semantic mask 不可只因視覺相似就拿來比較。"),
            ("KNTSHR-37", "從輸出走到安全決策", "box、mask、keypoint 需要 quality、coordinate、uncertainty 與人工 gate。"),
            ("KNTSHR-38", "known-target workshop", "把 solder defect 從 output responsibility 走到可追溯的 release。"),
        ],
    },
    "detector": {
        "relative_dir": "03-detectors-and-open-vocabulary",
        "items": [
            ("DET-01", "偵測路線總覽", "已知類別與文字條件候選，都必須停在 candidate ROI，而不是直接變成 defect proof。"),
            ("DETSHR-26", "dense 與 query detector 的比較", "在固定契約下比較 dense decode/NMS 與 set-prediction query，而不是只引用 paper FPS。"),
            ("DETSHR-27", "closed-set 與 open vocabulary", "class score 與 prompt-conditioned score 的意義和 release 限制不同。"),
            ("DETSHR-28", "small-object sampling", "raw、ROI、tile、stride pixels 決定 tiny defect 是否能成為可觀測證據。"),
            ("DETSHR-29", "detector 到 AD evidence", "proposal 要先 inverse map，再交給 AD 或 specialist evidence，而非自動結論。"),
            ("DETSHR-30", "detector workshop", "把 known、unknown 與 text specification 的混合情境導向可稽核選型。"),
        ],
    },
    "anomaly": {
        "relative_dir": "04-anomaly-detection",
        "items": [
            ("ADSHR-04-01", "異常檢測家族地圖", "normal reference、anomaly evidence 與工程 action 的責任，先於演算法名稱。"),
            ("ADSHR-04-02", "共通 anomaly score 契約", "從可觀測輸入、聚合到 threshold／owner，建立共用的 score 意義。"),
            ("ADCMP-71", "memory、Gaussian、subspace", "三種 normal state 在同一 AD contract 下比較，避免把內部距離混為效能。"),
            ("ADCMP-72", "teacher、reverse、EfficientAD", "區分 local／global evidence、runtime 與 student／decoder 的責任。"),
            ("ADCMP-73", "重建、diffusion、inversion", "residual 是候選 evidence，不會自動構成部署結論。"),
            ("ADCMP-74", "VLM-based AD 的 assist-only 邊界", "文字／語意 assist 必須交給可觀測的專業證據與 reviewer。"),
            ("ADCMP-75", "aggregation 與決策單位", "image score、map aggregation、die／wafer decision 都是版本化 contract 的一部分。"),
            ("ADCMP-76", "漂移、重建與 rollback", "frozen threshold、parallel evaluation、rebuild 與 rollback 需要被設計成日常流程。"),
            ("ADCMP-77", "AD evidence bundle", "在異常候選支援現場 action 前，必須保存完整資料、模型與錯誤 evidence。"),
            ("ADCMP-78", "limited-normal workshop", "把 normal data 稀少、local／global failure 與 P95 轉成可決策的選型步驟。"),
        ],
    },
    "video": {
        "relative_dir": "05-video-temporal",
        "items": [
            ("VIDFAM-01", "影片／時序路線總覽", "foreground event、flow、track 與 temporal representation 的輸出 owner 各不相同。"),
            ("VIDCMP-34", "motion、flow、track、representation", "依需要的下游責任比較，不把 motion candidate 當成 object identity。"),
            ("VIDCMP-35", "camera motion 與同步", "global camera motion、timestamps、cross-view transform 與 missing-view policy 都是必要契約。"),
            ("VIDCMP-36", "端到端 latency", "capture、buffer、model、aggregation、queue 與 action deadline 必須一起量。"),
            ("VIDCMP-37", "conveyor workshop", "先定義 event truth、ID、fallback 與允許動作，再選 temporal model。"),
        ],
    },
    "foundation": {
        "relative_dir": "06-foundation-vision-vlm",
        "items": [
            ("FDNIN-01", "foundation input contract", "raw pixels、ROI／tile、patch／token、encoder／bridge 與 output responsibility 都要先治理。"),
            ("FDNSHR-30", "visual encoder 與 dual encoder", "只有 downstream head、ROI、split、evidence 與 site action 固定，才可以公平比較。"),
            ("FDNSHR-31", "generative VLM bridge", "request schema、grounding、data policy、latency 與 fallback 一起構成 VLM route 的工程契約。"),
            ("FDNSHR-32", "grounding 與 specialist loop", "open-world candidate 或 claim 只能交給高解析 evidence 與具名 specialist。"),
            ("FDNSHR-33", "RAG、OT 與安全邊界", "SOP、ACL、injection、egress、audit、approval、rollback 都是 assist 系統的一部分。"),
            ("FDNSHR-34", "wafer foundation workshop", "從 tile／patch evidence 經 candidate route 到 evidence bundle 與 human action。"),
        ],
    },
    "diffusion": {
        "relative_dir": "07-diffusion-generation-and-restoration",
        "items": [
            ("DIFSHR-07-01", "Diffusion 家族與證據邊界", "synthetic data、controlled edit 與 restored estimate 的作用不同，但都不可取代 raw evidence。"),
            ("DIFSHR-07-34", "缺陷生成路線的比較", "只有共同 evidence contract 下，才可以比較 synthetic defect 生成方法。"),
            ("DIFSHR-07-35", "editing 與 restoration 的不同", "兩者輸出都是 estimate／edit，不能被描述成相機看到的真實物理狀態。"),
            ("DIFSHR-07-36", "生成資料的 provenance 與安全", "condition、prompt、seed、來源與後續使用範圍都必須保留下來。"),
            ("DIFSHR-07-37", "Diffusion safety workshop", "把資料增補、編輯與復原放進 raw evidence 與 owner review 的安全流程。"),
        ],
    },
}


# These are intentionally not active first-read assets.  They preserve the
# former compact dashboards for engineers who need a dense implementation
# reference after working through the image-led causal story.
FAMILY_SUPPORT_ENGINEERING_REFERENCES: dict[str, str] = {
    "ADSHR-04-01": "course-delivery/section-pages/04-anomaly-detection/images/final/ADSHR-04-01-story_v01.png",
    "ADSHR-04-02": "course-delivery/section-pages/04-anomaly-detection/images/final/ADSHR-04-02-story_v01.png",
    "ADCMP-71": "course-delivery/section-pages/04-anomaly-detection/images/final/ADCMP-71-memory-gaussian-subspace_v01.png",
    "ADCMP-72": "course-delivery/section-pages/04-anomaly-detection/images/final/ADCMP-72-teacher-reverse-efficient_v01.png",
    "ADCMP-73": "course-delivery/section-pages/04-anomaly-detection/images/final/ADCMP-73-reconstruction-diffusion-inversion_v01.png",
    "ADCMP-74": "course-delivery/section-pages/04-anomaly-detection/images/final/ADCMP-74-vlm-boundary_v01.png",
    "ADCMP-75": "course-delivery/section-pages/04-anomaly-detection/images/final/ADCMP-75-aggregation-decision-unit_v01.png",
    "ADCMP-76": "course-delivery/section-pages/04-anomaly-detection/images/final/ADCMP-76-drift-rebuild_v01.png",
    "ADCMP-77": "course-delivery/section-pages/04-anomaly-detection/images/final/ADCMP-77-evidence-bundle_v01.png",
    "ADCMP-78": "course-delivery/section-pages/04-anomaly-detection/images/final/ADCMP-78-workshop-route-selection_v01.png",
    "VIDFAM-01": "course-delivery/section-pages/05-video-temporal/images/final/VIDFAM-01-video-temporal-family-map_v01.png",
    "VIDCMP-34": "course-delivery/section-pages/05-video-temporal/images/final/VIDCMP-34-motion-flow-track-representation_v01.png",
    "VIDCMP-35": "course-delivery/section-pages/05-video-temporal/images/final/VIDCMP-35-camera-motion-and-sync_v02.png",
    "VIDCMP-36": "course-delivery/section-pages/05-video-temporal/images/final/VIDCMP-36-end-to-end-latency_v02.png",
    "VIDCMP-37": "course-delivery/section-pages/05-video-temporal/images/final/VIDCMP-37-workshop-route-selection_v02.png",
    "FDNIN-01": "course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png",
    "FDNSHR-30": "course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNSHR-30-dual-vs-visual-encoder_v01.png",
    "FDNSHR-31": "course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNSHR-31-generative-vlm-bridges_v02.png",
    "FDNSHR-32": "course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNSHR-32-grounding-specialist-loop_v01.png",
    "FDNSHR-33": "course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNSHR-33-security-rag-ot-boundary_v01.png",
    "FDNSHR-34": "course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNSHR-34-workshop-route-selection_v01.png",
}


FAMILIES: dict[str, dict[str, Any]] = {
    "geometry": {
        "label": "幾何、校正與對位",
        "icon": "⌖",
        "description": "先讓座標、相機與對位可信，再談後續檢測與量測。",
        "safety": "幾何結果必須附帶殘差、覆蓋率、拒用條件與回映座標；一張漂亮對位圖不是證據。",
        "question": "你需要的是可追溯的相機幾何、穩定的小位移對位，還是兩張影像的特徵對應？",
        "order": ["charuco", "ecc", "sift", "lightglue"],
        "anchor": ["charuco", "ecc"],
    },
    "classification": {
        "label": "已知目標：分類、分割與姿態",
        "icon": "◫",
        "description": "當類別與標註已知時，選擇 image class、box、mask 或 pose 的正確輸出責任。",
        "safety": "closed-set confidence 不保證未知缺陷檢出；mask 也不自動等於尺寸量測。",
        "question": "你的最終需求是整張圖分類、每個 instance、語意區域，還是有順序的 keypoints／姿態？",
        "order": ["resnet", "convnext", "vit-classifier", "det-yolo-dense", "det-rtdetr", "det-dino-detector", "u-net", "segformer", "yolo-seg", "keypoint-r-cnn", "pose"],
        "anchor": ["resnet", "det-yolo-dense", "u-net"],
    },
    "detector": {
        "label": "物件偵測與開放詞彙候選",
        "icon": "▣",
        "description": "分清楚 known-class boxes、query-based boxes 與 text-prompt candidate ROI 的責任範圍。",
        "safety": "box 是候選區域，不是物理量測或 defect truth；open-vocabulary score 更不能直接放行。",
        "question": "你有固定已知類別與 box labels，還是需要文字導引的探索性 candidate ROI？",
        "order": ["det-yolo-dense", "det-rtdetr", "det-dino-detector", "det-grounding-dino-interface", "yolo-world", "yoloe"],
        "anchor": ["det-yolo-dense", "det-rtdetr"],
    },
    "anomaly": {
        "label": "異常檢測：正常性建模",
        "icon": "◌",
        "description": "從乾淨 normal support、特徵差異或重建殘差形成異常候選，而不是直接宣稱缺陷真相。",
        "safety": "anomaly score 不是根因、defect probability 或自動放行依據；normal support 的乾淨度與覆蓋率是核心。",
        "question": "你有多少 clean normal data、能否訓練、可否保存 memory bank，以及異常是局部、全域還是語意問題？",
        "order": ["ad-patchcore", "ad-padim", "ad-anomalydino", "ad-subspacead", "ad-stfpm", "ad-rd4ad", "ad-efficientad", "ad-ae", "ad-draem", "ad-uniad", "ad-dinomaly", "ad-invad", "ad-diffad", "ad-ddad", "ad-winclip", "ad-anomalyclip", "ad-anomalygpt"],
        "anchor": ["ad-patchcore", "ad-stfpm", "ad-efficientad"],
    },
    "video": {
        "label": "時間序列、運動與影片理解",
        "icon": "▷",
        "description": "區分變化、前景、光流、追蹤與時序表徵；每一條路都需要時間戳與事件定義。",
        "safety": "motion／track／video embedding 不等於物件類別、身分、根因或 release；完整延遲要從 capture 算到事件處置。",
        "question": "你只要透明的變化候選、局部／密集光流、物件 ID，還是需要帶 downstream head 的時序表徵？",
        "order": ["frame-difference", "background-subtraction", "lucas-kanade", "raft", "bytetrack", "convlstm", "videomae", "v-jepa"],
        "anchor": ["frame-difference", "bytetrack"],
    },
    "foundation": {
        "label": "Foundation Vision、語意檢索與 VLM",
        "icon": "✦",
        "description": "把 embedding、相似度、文字回答與 provider service 正確放在候選、檢索或 assist 的位置。",
        "safety": "語意排名、embedding 與流暢回答不是 defect probability、定位保證或自動放行。",
        "question": "你需要的是 image-text ranking、可重用 visual features、受控本地 VLM，還是可接受 egress 的 provider service？",
        "order": ["dinov2", "dinov3", "clip", "siglip", "det-grounding-dino-interface", "yolo-world", "yoloe", "llava", "qwen-vl", "gemini-vision"],
        "anchor": ["dinov2", "clip"],
    },
    "diffusion": {
        "label": "Diffusion、合成資料與影像復原",
        "icon": "✧",
        "description": "分清 synthetic training candidate、controlled edit 與 restored estimate；三者都不覆蓋 raw evidence。",
        "safety": "生成或復原的 pixels 必須保留 raw、condition、seed、trace 與 review；不得當物理真值、量測或 release 依據。",
        "question": "你的用途是 rare-defect augmentation、受控編輯，還是非證據性的可讀性改善？是否有真實 holdout 與 no-go 規則？",
        "order": ["defectfill", "anomalydiffusion", "tf-idg", "controlnet", "inpainting", "diffusion-restoration", "deblur", "super-resolution"],
        "anchor": ["controlnet", "defectfill", "inpainting"],
    },
}


FAMILY_EVIDENCE = {
    "geometry": "保留原圖、標靶規格、相機設定、對位結果、誤差與重裝測試；由工程師確認座標能回映。",
    "classification": "保留原圖、標註規則、資料切分、輸出分數、未知或遮擋案例與人工覆核結果。",
    "detector": "保留原圖、縮放或切片規則、類別或文字描述、候選框、去重規則、回映座標與確認結果。",
    "anomaly": "保留原圖、乾淨正常品來源、畫面範圍、模型設定、可疑圖、誤報／漏失案例與人工覆核結果。",
    "video": "保留前後畫面、時間戳、事件定義、追蹤或移動結果、完整等待時間與人工確認紀錄。",
    "foundation": "保留原圖、文字問題或特徵設定、模型版本、候選排序或回答、資料政策與人工回查結果。",
    "diffusion": "保留原圖、生成或復原條件、模型版本、隨機種子、輸出用途、真實保留資料與人工覆核結果。",
}


# Short, learner-facing positioning copy.  The deeper causal and engineering
# copy comes from the reviewed batch specs below, so the HTML is not merely a
# filename catalogue.
TOPIC_SUMMARIES = {
    "charuco": "用帶 ID 的棋盤標靶建立相機內外參、姿態與可追溯的幾何基準。",
    "ecc": "直接最佳化 template 與當前 ROI 的外觀相似度，求出小位移的 warp 對位。",
    "sift": "以局部尺度不變特徵與描述子建立對應點，再交給 RANSAC 求幾何變換。",
    "lightglue": "在既有 keypoints／descriptors 之上，以 learned matching 找高可信對應點。",
    "resnet": "以 residual CNN 對固定 ROI 輸出已知類別 logits，是 image-level 分類基線。",
    "convnext": "保有 CNN 階層特性、採用現代卷積設計的 closed-set 分類架構族。",
    "vit-classifier": "把影像切為 patch tokens，以 attention 建模跨區域關係後輸出已知類別。",
    "det-yolo-dense": "在多尺度 feature locations 直接產生已知類別 box candidates，再 decode 與 NMS。",
    "det-rtdetr": "以 selected object queries 和可調 decoder layers 輸出一組 boxes 的 real-time DETR。",
    "det-dino-detector": "以 denoising training、mixed query selection 與 iterative refinement 改善 supervised DETR。",
    "u-net": "encoder-decoder 加 skip connections 的 semantic segmentation 家族，輸出每個 pixel 的類別 mask。",
    "segformer": "hierarchical Transformer encoder 搭配輕量 decoder，融合多尺度特徵做 semantic segmentation。",
    "yolo-seg": "對每個已知 instance 輸出 box、class 與獨立 mask。",
    "keypoint-r-cnn": "先找每個 instance，再在 ROI 中預測固定順序的 keypoint heatmaps。",
    "pose": "把 keypoint、association、座標轉換與幾何 solver 串成可稽核的 pose 管線。",
    "ad-patchcore": "保存代表性的 nominal patch features，以最近 normal exemplar 的距離形成 anomaly map。",
    "ad-padim": "在每個對齊位置估計 normal patch feature 的 Gaussian，以 Mahalanobis distance 找偏離。",
    "ad-anomalydino": "以 frozen DINOv2 patch tokens 建立 one/few-shot normal memory，再比較最近鄰。",
    "ad-subspacead": "以 DINOv2 patch features 擬合 compact PCA normal subspace，使用投影殘差標示異常。",
    "ad-stfpm": "以 frozen teacher 與 normal-only student 的多層 feature discrepancy 形成異常候選。",
    "ad-rd4ad": "以 one-class bottleneck 和 reverse decoder 重建 frozen teacher features，再比較差異。",
    "ad-efficientad": "輕量 teacher-student local discrepancy 加 global autoencoder evidence 的 normal-only 方法。",
    "ad-ae": "以 normal-only encoder-decoder 重建影像或 features，將 residual 作為異常候選。",
    "ad-draem": "先重建 normal appearance，再以原圖與重建圖學 discriminative anomaly segmentation。",
    "ad-uniad": "用 shared multi-class feature reconstruction model 取代每類一套 detector。",
    "ad-dinomaly": "以 Transformer、noisy bottleneck 與 loose reconstruction 做多類 feature anomaly detection。",
    "ad-invad": "以 style-modulated forward feature reconstruction 生成 normal-like features。",
    "ad-diffad": "以 norm-guided denoising 產生 normal-like restoration，再由 segmentation head 判定異常。",
    "ad-ddad": "以 diffusion reconstruction 融合 pixel 與 feature residual 形成異常 map。",
    "ad-winclip": "以 frozen CLIP 的 normal／anomaly prompts 與 window similarities 做 zero/few-shot 異常候選。",
    "ad-anomalyclip": "以 object-agnostic normal／abnormal prompts 做 target-domain zero-shot anomaly localization。",
    "ad-anomalygpt": "結合視覺語言模型、異常對話與 evidence region，適合作為工程審查 assist。",
    "frame-difference": "用兩個已宣告時間間隔的 frame 相減，形成透明的變化候選。",
    "background-subtraction": "維護可更新 background state，把不符合背景的像素標成前景候選。",
    "lucas-kanade": "在局部紋理窗口解小位移 optical flow，輸出帶可信度檢查的 `(u,v)`。",
    "raft": "以 learned all-pairs correlation 與 recurrent refinement 估計 dense optical flow。",
    "bytetrack": "先關聯 high-score detections，再以 low-score detections 補強 track continuity。",
    "convlstm": "以 convolutional gates 維持保有空間布局的 hidden／cell state，供時序 head 使用。",
    "videomae": "高比例遮罩影片 tokens 的自監督 pretraining；representation 仍需接 downstream event head。",
    "v-jepa": "預測被遮蔽 target regions 的 latent features，學習影片表徵而非直接生成 pixels。",
    "dinov2": "self-supervised ViT visual backbone，提供 global feature 與 patch-token grid 給下游任務。",
    "dinov3": "新一代 self-supervised visual feature backbone，強調 dense representation，仍須指定 downstream route。",
    "clip": "以 image encoder 與 text encoder 的共同 embedding space 排序受控文字候選。",
    "siglip": "以 pairwise sigmoid loss 訓練的 image-text dual encoder，部署仍是 embedding similarity ranking。",
    "det-grounding-dino-interface": "用文字 phrase 導引 open-set candidate boxes，適合探索 ROI，不是 defect 或 release 判斷器。",
    "yolo-world": "把 text embeddings 接到 YOLO-like dense detection，產生 open-vocabulary candidate boxes。",
    "yoloe": "支援文字、視覺與免提示路徑；以 RepRTA、SAVPE、LRPC 接到偵測／分割，輸出依 checkpoint 核對。",
    "llava": "vision encoder 加 projector 接語言模型，輸出可追問的文字或 structured assist response。",
    "qwen-vl": "以 named Qwen-VL service／deployment 的 dynamic-resolution visual tokens 處理多影像與文件問答。",
    "gemini-vision": "以 API model ID、version、region 與 data policy 管理的 provider multimodal service route。",
    "defectfill": "從少量 defect image／mask 產生 synthetic defect training candidates。",
    "anomalydiffusion": "以 anomaly appearance embedding 和 spatial embedding 產生 few-shot synthetic anomaly image／mask pairs。",
    "tf-idg": "以 frozen diffusion base 和 text／feature／region guidance 做 training-free industrial defect generation。",
    "controlnet": "把 edge、depth、segmentation 或 pose 等 spatial condition 加到 diffusion backbone 做受控生成或編輯。",
    "inpainting": "依 mask 與周邊 context 填補內容；填補區是 synthetic edit，不是相機觀測。",
    "diffusion-restoration": "依已宣告 degradation condition 從退化影像估計 restored image，輸出必須標為 estimate。",
    "deblur": "從 motion blur 或 defocus blur 估計較清晰影像，核心前提是 blur／PSF 假設。",
    "super-resolution": "由低解析影像與 scale／degradation 假設估計高解析影像，不能創造可靠 micro-defect evidence。",
}


SLIDE_META = (
    ("先看它交出什麼", "先用白話確認：它幫現場做什麼，卻不能替誰下決定？"),
    ("再看它怎麼做", "只沿著四個步驟看：影像怎麼變成這個結果？"),
    ("上線前先固定條件", "先把可重播的條件寫下來，再談分數或速度。"),
    ("選它前先看風險", "什麼情況值得試？碰到什麼情況要先停下來？"),
)


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("\n", " ")).strip()


def load_topics() -> list[dict[str, Any]]:
    topics: list[dict[str, Any]] = []
    for spec in SPECS:
        if not spec.is_file():
            raise FileNotFoundError(f"Missing course spec: {spec}")
        payload = json.loads(spec.read_text(encoding="utf-8"))
        if not isinstance(payload, list):
            raise ValueError(f"Expected JSON list: {spec}")
        topics.extend(payload)
    slugs = [str(item.get("slug", "")) for item in topics]
    if len(topics) != 58 or len(set(slugs)) != 58 or "" in slugs:
        raise ValueError(f"Expected 58 unique topics, found {len(topics)} / {len(set(slugs))}")
    return topics


def load_learner_briefs(source_topics: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Load the plain-language entry point for every model page.

    The technical batch specs remain the authoritative engineering source.
    This companion file deliberately answers the questions a new learner asks
    first: the field problem, deliverable, first check, and HOLD condition.
    Keeping it explicit prevents a generic text transformation from silently
    changing a model claim.
    """

    if not LEARNER_BRIEFS.is_file():
        raise FileNotFoundError(f"Missing learner briefs: {LEARNER_BRIEFS}")
    payload = json.loads(LEARNER_BRIEFS.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Learner briefs must be a JSON object")
    expected = {str(topic["slug"]) for topic in source_topics}
    if set(payload) != expected:
        missing = sorted(expected - set(payload))
        extra = sorted(set(payload) - expected)
        raise ValueError(f"Learner brief keys do not match topics; missing={missing}, extra={extra}")
    required = {"problem", "deliverable", "first", "hold", "terms"}
    slide_copy_fields = {"title", "question", "look", "relation", "takeaway"}
    for slug, brief in payload.items():
        if not isinstance(brief, dict) or required - set(brief):
            raise ValueError(f"Incomplete learner brief: {slug}")
        if not all(isinstance(brief[field], str) and clean(brief[field]) for field in required - {"terms"}):
            raise ValueError(f"Empty learner brief copy: {slug}")
        terms = brief["terms"]
        if not isinstance(terms, list) or len(terms) < 2 or not all(isinstance(term, str) and clean(term) for term in terms):
            raise ValueError(f"Learner brief needs two term explanations: {slug}")
        if any(len(clean(brief[field])) > 68 for field in required - {"terms"}):
            raise ValueError(f"Learner brief is too long for first-read scanning: {slug}")
        architecture = brief.get("architecture")
        if "evidence" in brief and (not isinstance(brief["evidence"], str) or not clean(brief["evidence"])):
            raise ValueError(f"Empty learner evidence: {slug}")
        if architecture is not None:
            if not isinstance(architecture, dict) or set(architecture) != slide_copy_fields:
                raise ValueError(f"Architecture reading copy is incomplete: {slug}")
            if not all(isinstance(architecture[field], str) and clean(architecture[field]) for field in slide_copy_fields):
                raise ValueError(f"Architecture reading copy is empty: {slug}")
            if any(len(clean(architecture[field])) > 110 for field in slide_copy_fields):
                raise ValueError(f"Architecture reading copy is too long: {slug}")
        architecture_terms = brief.get("architecture_terms")
        if architecture_terms is not None:
            if not isinstance(architecture_terms, list) or len(architecture_terms) < 2:
                raise ValueError(f"Architecture term explanations are incomplete: {slug}")
            if not all(isinstance(term, str) and clean(term) for term in architecture_terms):
                raise ValueError(f"Architecture term explanation is empty: {slug}")
    return {
        slug: {
            "problem": clean(str(brief["problem"])),
            "deliverable": clean(str(brief["deliverable"])),
            "first": clean(str(brief["first"])),
            "hold": clean(str(brief["hold"])),
            "terms": [clean(str(term)) for term in brief["terms"]],
            **({"evidence": clean(brief["evidence"])} if "evidence" in brief else {}),
            "architecture": {
                field: clean(str(brief["architecture"][field]))
                for field in slide_copy_fields
            } if isinstance(brief.get("architecture"), dict) else None,
            "architecture_terms": [clean(str(term)) for term in brief.get("architecture_terms", [])]
            if isinstance(brief.get("architecture_terms"), list) else [],
        }
        for slug, brief in payload.items()
    }


def _teaching_text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not clean(value):
        raise ValueError(f"Teaching topic needs non-empty text: {label}")
    return clean(value)


def _teaching_record(
    value: Any,
    fields: set[str],
    label: str,
    optional_fields: set[str] | None = None,
) -> dict[str, str]:
    optional_fields = optional_fields or set()
    if (
        not isinstance(value, dict)
        or not fields <= set(value)
        or not set(value) <= fields | optional_fields
    ):
        raise ValueError(f"Teaching topic has invalid fields for {label}")
    cleaned = {field: _teaching_text(value[field], f"{label}.{field}") for field in fields}
    cleaned.update(
        {
            field: _teaching_text(value[field], f"{label}.{field}")
            for field in optional_fields
            if field in value
        }
    )
    return cleaned


def _teaching_mechanism_step(value: Any, label: str) -> dict[str, Any]:
    """Keep the full HTML explanation and a separate, bounded diagram copy.

    Four columns in a 16:9 explanatory visual cannot safely carry the whole
    engineering paragraph.  The diagram copy is therefore deliberately
    authored rather than a renderer-side truncation of the learner text.
    """

    fields = {"title", "body", "why", "anchor", "diagram"}
    optional_fields = {"inline_image"}
    if not isinstance(value, dict) or not fields <= set(value) or set(value) - fields - optional_fields:
        raise ValueError(f"Teaching topic has invalid fields for {label}")
    cleaned = {
        **{
            field: _teaching_text(value[field], f"{label}.{field}")
            for field in ("title", "body", "why", "anchor")
        },
        "diagram": _teaching_record(
            value["diagram"], {"title", "body", "why", "anchor"}, f"{label}.diagram"
        ),
    }
    if "inline_image" in value:
        image = _teaching_text(value["inline_image"], f"{label}.inline_image").replace("\\", "/")
        image_path = Path(image)
        if (
            image_path.is_absolute()
            or ".." in image_path.parts
            or not image.startswith("_course_content/generated-concepts/")
            or image_path.suffix.lower() != ".png"
        ):
            raise ValueError(f"Teaching topic has unsafe mechanism inline_image: {label}")
        _validate_concept_visual_asset(ROOT / image_path)
        cleaned["inline_image"] = image
    return cleaned


def _validate_concept_visual_asset(path: Path) -> None:
    """Accept generated PNGs and precise, code-native SVG mechanism diagrams."""

    if not path.is_file():
        raise FileNotFoundError(f"Missing concept visual: {path}")
    if path.suffix.lower() == ".png":
        with Image.open(path) as rendered_image:
            # Native 1:3 mobile artwork keeps labels readable without raster resampling.
            if rendered_image.size not in {(768, 2304), (768, 2400), (768, 2800), (768, 3050), (941, 1672), (1672, 941), (1672, 940), (1673, 940), (1600, 1080), (1600, 900), (720, 1660), (720, 1280), (724, 2171), (724, 2172), (861, 1827), (725, 2167), (725, 2169), (725, 2170), (727, 2164), (728, 2161), (726, 2167), (768, 2046), (768, 2048), (881, 1785), (887, 1774), (836, 1881), (836, 1882), (1670, 942), (1670, 941), (1671, 941), (916, 1717), (955, 1647), (1024, 1536)}:
                raise ValueError(f"Unexpected concept visual dimensions {rendered_image.size}: {path}")
        return
    if path.suffix.lower() == ".svg":
        svg = path.read_text(encoding="utf-8")
        if not re.search(r'<svg\b[^>]*\bwidth="(?:1672|1600|720)"[^>]*\bheight="(?:941|1080|900|1660|1280)"[^>]*\bviewBox="0 0 (?:1672 941|1600 1080|1600 900|720 1660|720 1280)"', svg):
            raise ValueError(f"Unexpected SVG concept visual dimensions: {path}")
        return
    raise ValueError(f"Unsupported concept visual type: {path}")


def _clean_beginner_path(value: Any, label: str) -> dict[str, Any]:
    """Validate an optional, image-led first-read path for one topic.

    This is deliberately separate from ``concept_visuals``.  A beginner path
    is an ordered sequence of full-width 16:9 teaching images, not a small
    paragraph diagram and not a replacement for the later engineering
    reference.  Keeping the contract local to a topic lets one pilot improve
    its first read without changing the other 57 lessons.
    """

    fields = {"title", "intro", "visuals"}
    if not isinstance(value, dict) or set(value) != fields:
        raise ValueError(f"Teaching topic has invalid beginner path fields: {label}")
    raw_visuals = value["visuals"]
    # The current reading-layer contract permits 3–5 first-read images.
    # Keep longer existing paths valid; do not force filler into short lessons.
    if not isinstance(raw_visuals, list) or len(raw_visuals) < 3:
        raise ValueError(
            f"Teaching topic needs at least three ordered beginner visuals: {label}"
        )

    visual_fields = {"id", "title", "prompt", "caption", "image", "alt", "callouts"}
    visual_ids: set[str] = set()
    visuals: list[dict[str, Any]] = []
    for index, visual in enumerate(raw_visuals, start=1):
        visual_label = f"{label}.visuals[{index}]"
        if not isinstance(visual, dict) or not visual_fields <= set(visual) or set(visual) - visual_fields - {"reading_views", "core_ideas"}:
            raise ValueError(f"Teaching topic has invalid beginner visual fields: {visual_label}")
        if "core_ideas" in visual and type(visual["core_ideas"]) is not bool:
            raise ValueError(f"Teaching topic core_ideas must be boolean: {visual_label}")
        visual_id = _teaching_text(visual["id"], f"{visual_label}.id")
        if visual_id in visual_ids:
            raise ValueError(f"Teaching topic has duplicate beginner visual id: {visual_label}")
        visual_ids.add(visual_id)
        image = _teaching_text(visual["image"], f"{visual_label}.image").replace("\\", "/")
        image_path = Path(image)
        if (
            image_path.is_absolute()
            or ".." in image_path.parts
            or image_path.suffix.lower() not in {".png", ".svg"}
            or not image.startswith("_course_content/generated-concepts/")
        ):
            raise ValueError(f"Teaching topic has unsafe beginner visual path: {visual_label}")
        # A first-read story starts with a concrete workpiece, not a symbolic
        # card diagram.  Later full-size SVGs may explain one mechanism at a
        # time, but image one must be a raster AOI work example.
        if index == 1 and image_path.suffix.lower() != ".png":
            raise ValueError(
                f"Teaching topic beginner path must begin with a raster work example: {visual_label}"
            )
        absolute_image = ROOT / image_path
        try:
            absolute_image.resolve().relative_to(CONCEPT_VISUALS_ROOT.resolve())
        except ValueError as exc:
            raise ValueError(
                f"Teaching topic beginner visual is outside the approved asset directory: {visual_label}"
            ) from exc
        _validate_concept_visual_asset(absolute_image)
        callouts = visual["callouts"]
        if not isinstance(callouts, list) or len(callouts) < 2:
            raise ValueError(f"Teaching topic needs at least two beginner visual callouts: {visual_label}")
        reading_views = _clean_reading_views(visual["reading_views"], image, visual_label) if "reading_views" in visual else []
        visuals.append(
            {
                "id": visual_id,
                "title": _teaching_text(visual["title"], f"{visual_label}.title"),
                "prompt": _teaching_text(visual["prompt"], f"{visual_label}.prompt"),
                "caption": _teaching_text(visual["caption"], f"{visual_label}.caption"),
                "image": image,
                "alt": _teaching_text(visual["alt"], f"{visual_label}.alt"),
                "sequence": index,
                **({"reading_views": reading_views} if reading_views else {}),
                **({"core_ideas": True} if visual.get("core_ideas") else {}),
                "callouts": [
                    _teaching_record(
                        callout,
                        {"title", "body"},
                        f"{visual_label}.callouts[{callout_index}]",
                    )
                    for callout_index, callout in enumerate(callouts, start=1)
                ],
            }
        )
    return {
        "title": _teaching_text(value["title"], f"{label}.title"),
        "intro": _teaching_text(value["intro"], f"{label}.intro"),
        "visuals": visuals,
    }


def _clean_reading_views(value: Any, image: str, label: str) -> list[dict[str, Any]]:
    """Validate local, independently composed views without weakening asset checks."""
    fields = {"title", "image", "alt", "mobile_image", "mobile_crop"}
    optional_fields = {"mobile_display_mode", "mobile_intrinsic_width", "mobile_intrinsic_height", "desktop_intrinsic_width", "desktop_intrinsic_height"}
    if not isinstance(value, list) or not 1 <= len(value) <= 6:
        raise ValueError(f"Invalid reading views: {label}")
    result = []
    for view in value:
        if not isinstance(view, dict) or not fields <= set(view) or set(view) - fields - optional_fields:
            raise ValueError(f"Invalid reading view fields: {label}")
        clean = {key: _teaching_text(view[key], label) for key in fields - {"mobile_crop"}}
        for key in ("image", "mobile_image"):
            path = Path(clean[key])
            if path.is_absolute() or ".." in path.parts or "\\" in clean[key] or not clean[key].startswith("_course_content/generated-concepts/") or path.suffix.lower() not in {".svg", ".png"}:
                raise ValueError(f"Unsafe reading view image: {label}")
            try:
                (ROOT / path).resolve().relative_to(CONCEPT_VISUALS_ROOT.resolve())
            except ValueError as exc:
                raise ValueError(f"Reading view outside asset directory: {label}") from exc
            _validate_concept_visual_asset(ROOT / path)
        crop = view["mobile_crop"]
        if not isinstance(crop, list) or len(crop) != 4 or any(type(v) is not int for v in crop):
            raise ValueError(f"Invalid reading view crop: {label}")
        x, y, width, height = crop
        if view.get("mobile_display_mode") == "full-mobile":
            crop_width = int(view.get("mobile_intrinsic_width") or 720)
            crop_height = int(view.get("mobile_intrinsic_height") or 1660)
        else:
            crop_width, crop_height = 1672, 941
        if x < 0 or y < 0 or width <= 0 or height <= 0 or x + width > crop_width or y + height > crop_height:
            raise ValueError(f"Reading view crop outside image: {label}")
        extras = {key: view[key] for key in optional_fields if key in view}
        result.append({**clean, **extras, "mobile_crop": crop})
    if result[0]["image"] != image:
        raise ValueError(f"First reading view must match chapter image: {label}")
    return result


def _clean_deep_dive(value: Any, label: str) -> dict[str, Any]:
    """Validate one authored, source-backed model deep dive.

    Deep dives are deliberately opt-in.  They can replace a topic's generic
    first-read assembly without changing the data contract for the other
    lessons, while every chapter still points to a full-canvas local visual
    and one or more declared primary sources.
    """

    fields = {"title", "intro", "concept_path", "chapters", "sources"}
    if not isinstance(value, dict) or not fields <= set(value) or set(value) - fields - {"default_collapsed"}:
        raise ValueError(f"Teaching topic has invalid deep-dive fields: {label}")
    if "default_collapsed" in value and type(value["default_collapsed"]) is not bool:
        raise ValueError(f"Teaching topic default_collapsed must be boolean: {label}")

    concept_path = _teaching_text(value["concept_path"], f"{label}.concept_path").replace(
        "\\", "/"
    )
    concept_file = Path(concept_path)
    if (
        concept_file.is_absolute()
        or ".." in concept_file.parts
        or concept_file.suffix.lower() != ".md"
        or not concept_path.startswith("roadmap-model-selection/")
        or not (ROOT / concept_file).is_file()
    ):
        raise ValueError(f"Teaching topic has invalid deep-dive concept path: {label}")

    raw_sources = value["sources"]
    if not isinstance(raw_sources, list) or len(raw_sources) < 3:
        raise ValueError(f"Teaching topic needs at least three deep-dive sources: {label}")
    source_ids: set[str] = set()
    sources: list[dict[str, str]] = []
    allowed_source = re.compile(
        r"^https://(?:arxiv\.org|github\.com|huggingface\.co|research\.nvidia\.com)/"
    )
    for index, source in enumerate(raw_sources, start=1):
        source_label = f"{label}.sources[{index}]"
        cleaned = _teaching_record(source, {"id", "label", "url", "scope"}, source_label)
        if cleaned["id"] in source_ids:
            raise ValueError(f"Teaching topic has duplicate deep-dive source id: {source_label}")
        if not allowed_source.match(cleaned["url"]):
            raise ValueError(f"Teaching topic has unapproved deep-dive source URL: {source_label}")
        source_ids.add(cleaned["id"])
        sources.append(cleaned)

    raw_chapters = value["chapters"]
    if not isinstance(raw_chapters, list) or len(raw_chapters) != 8:
        raise ValueError(f"Teaching topic deep dive needs exactly eight chapters: {label}")
    chapter_fields = {
        "id", "nav", "title", "summary", "image", "alt", "points", "check", "source_ids"
    }
    chapter_ids: set[str] = set()
    chapters: list[dict[str, Any]] = []
    for index, chapter in enumerate(raw_chapters, start=1):
        chapter_label = f"{label}.chapters[{index}]"
        if not isinstance(chapter, dict) or not chapter_fields <= set(chapter) or set(chapter) - chapter_fields - {"mobile_steps", "reading_views"}:
            raise ValueError(f"Teaching topic has invalid deep-dive chapter fields: {chapter_label}")
        chapter_id = _teaching_text(chapter["id"], f"{chapter_label}.id")
        if chapter_id in chapter_ids:
            raise ValueError(f"Teaching topic has duplicate deep-dive chapter id: {chapter_label}")
        chapter_ids.add(chapter_id)

        image = _teaching_text(chapter["image"], f"{chapter_label}.image").replace("\\", "/")
        image_path = Path(image)
        if (
            image_path.is_absolute()
            or ".." in image_path.parts
            or image_path.suffix.lower() not in {".png", ".svg"}
            or not image.startswith("_course_content/generated-concepts/")
        ):
            raise ValueError(f"Teaching topic has unsafe deep-dive visual path: {chapter_label}")
        absolute_image = ROOT / image_path
        try:
            absolute_image.resolve().relative_to(CONCEPT_VISUALS_ROOT.resolve())
        except ValueError as exc:
            raise ValueError(
                f"Teaching topic deep-dive visual is outside the approved asset directory: {chapter_label}"
            ) from exc
        _validate_concept_visual_asset(absolute_image)

        points = chapter["points"]
        if not isinstance(points, list) or len(points) < 3:
            raise ValueError(f"Teaching topic needs at least three deep-dive points: {chapter_label}")
        raw_source_ids = chapter["source_ids"]
        if not isinstance(raw_source_ids, list) or not raw_source_ids:
            raise ValueError(f"Teaching topic deep-dive chapter needs sources: {chapter_label}")
        cleaned_source_ids = [
            _teaching_text(source_id, f"{chapter_label}.source_ids")
            for source_id in raw_source_ids
        ]
        unknown_sources = sorted(set(cleaned_source_ids) - source_ids)
        if unknown_sources:
            raise ValueError(
                f"Teaching topic deep-dive chapter has unknown sources {unknown_sources}: {chapter_label}"
            )
        reading_views = []
        if "reading_views" in chapter:
            if "mobile_steps" in chapter:
                raise ValueError(f"Choose reading views or mobile steps: {chapter_label}")
            reading_views = _clean_reading_views(chapter["reading_views"], image, chapter_label)
        mobile_steps = []
        if "mobile_steps" in chapter:
            raw_steps = chapter["mobile_steps"]
            if not isinstance(raw_steps, list) or not 2 <= len(raw_steps) <= 8:
                raise ValueError(f"Invalid mobile steps: {chapter_label}")
            for step in raw_steps:
                if not isinstance(step, dict) or set(step) != {"title", "body", "crop"}:
                    raise ValueError(f"Invalid mobile step fields: {chapter_label}")
                crop = step["crop"]
                if not isinstance(crop, list) or len(crop) != 4 or any(type(v) is not int for v in crop):
                    raise ValueError(f"Invalid mobile crop: {chapter_label}")
                x, y, width, height = crop
                if x < 0 or y < 0 or width <= 0 or height <= 0 or x + width > 1672 or y + height > 941:
                    raise ValueError(f"Mobile crop outside visual: {chapter_label}")
                mobile_steps.append({"title": _teaching_text(step["title"], chapter_label), "body": _teaching_text(step["body"], chapter_label), "crop": crop})
        chapters.append(
            {
                "id": chapter_id,
                "nav": _teaching_text(chapter["nav"], f"{chapter_label}.nav"),
                "title": _teaching_text(chapter["title"], f"{chapter_label}.title"),
                "summary": _teaching_text(chapter["summary"], f"{chapter_label}.summary"),
                "image": image,
                "alt": _teaching_text(chapter["alt"], f"{chapter_label}.alt"),
                "sequence": index,
                "points": [
                    _teaching_text(point, f"{chapter_label}.points") for point in points
                ],
                "check": _teaching_record(
                    chapter["check"], {"question", "answer"}, f"{chapter_label}.check"
                ),
                "source_ids": cleaned_source_ids,
                **({"mobile_steps": mobile_steps} if mobile_steps else {}),
                **({"reading_views": reading_views} if reading_views else {}),
            }
        )
    return {
        "title": _teaching_text(value["title"], f"{label}.title"),
        "intro": _teaching_text(value["intro"], f"{label}.intro"),
        "concept_path": concept_path,
        "chapters": chapters,
        "sources": sources,
        **({"default_collapsed": value["default_collapsed"]} if "default_collapsed" in value else {}),
    }


def _clean_review_trace(value: Any, label: str) -> dict[str, Any]:
    """Keep first-read claims traceable to the topic's engineering source.

    The trace is deliberately an engineering disclosure rather than more copy
    in the first-read path.  It lets a reviewer answer where a beginner visual
    or public boundary came from without asking the renderer to infer facts.
    """

    fields = {"authority", "scope", "claims"}
    if not isinstance(value, dict) or set(value) != fields:
        raise ValueError(f"Teaching topic has invalid review trace fields: {label}")
    authority = _teaching_text(value["authority"], f"{label}.authority").replace("\\", "/")
    authority_path = Path(authority)
    if (
        authority_path.is_absolute()
        or ".." in authority_path.parts
        or authority_path.suffix.lower() != ".md"
        or not authority.startswith("roadmap-model-selection/")
        or not (ROOT / authority_path).is_file()
    ):
        raise ValueError(f"Teaching topic has invalid review trace authority: {label}")
    raw_claims = value["claims"]
    if not isinstance(raw_claims, list) or len(raw_claims) < 6:
        raise ValueError(f"Teaching topic needs at least six traced claims: {label}")
    claim_ids: set[str] = set()
    claims: list[dict[str, str]] = []
    for index, claim in enumerate(raw_claims, start=1):
        claim_label = f"{label}.claims[{index}]"
        cleaned = _teaching_record(claim, {"id", "field", "source"}, claim_label)
        if cleaned["id"] in claim_ids:
            raise ValueError(f"Teaching topic has duplicate review trace id: {claim_label}")
        claim_ids.add(cleaned["id"])
        claims.append(cleaned)
    return {
        "authority": authority,
        "scope": _teaching_text(value["scope"], f"{label}.scope"),
        "claims": claims,
    }


def _validate_inline_visual_asset(path: Path, cue: dict[str, Any], label: str) -> None:
    """Verify the compact Blog/Wiki figure is real and tied to its paragraph."""

    if not path.is_file():
        raise FileNotFoundError(f"Missing inline explanatory visual: {path}")
    svg = path.read_text(encoding="utf-8")
    if not re.search(r'<svg\b[^>]*\bwidth="720"[^>]*\bheight="360"[^>]*\bviewBox="0 0 720 360"', svg):
        raise ValueError(f"Unexpected inline SVG dimensions: {label}")
    if f'data-visual-cue="{cue["kind"]}"' not in svg:
        raise ValueError(f"Inline SVG does not expose its authored visual cue: {label}")
    if not re.search(r"<title[^>]*>[^<]+</title>.*<desc[^>]*>[^<]+</desc>", svg, re.DOTALL):
        raise ValueError(f"Inline SVG needs a meaningful title and description: {label}")


def _clean_engineering_slides(value: Any, label: str) -> list[dict[str, Any]]:
    """Validate optional authored engineering pages and their tall mobile assets."""
    if not isinstance(value, list) or len(value) != 4:
        raise ValueError(f"Engineering override needs four pages: {label}")
    result = []
    for index, item in enumerate(value):
        context = f"{label}[{index}]"
        required = {"title", "question", "plain", "terms", "guide", "stages", "misconception", "alt", "mobile_image", "mobile_width", "mobile_height", "engineering", "source"}
        if not isinstance(item, dict) or not required <= set(item) or set(item) - required - {"evidence_links", "label"}:
            raise ValueError(f"Invalid engineering page fields: {context}")
        row = {key: _teaching_text(item[key], f"{context}.{key}") for key in ("title", "question", "misconception", "alt", "source")}
        if "label" in item:
            row["label"] = _teaching_text(item["label"], f"{context}.label")
        for key, fields in (("plain", {"look", "relation", "takeaway"}), ("engineering", {"takeaway", "nextAction", "redLine"})):
            row[key] = _teaching_record(item[key], fields, f"{context}.{key}")
        for key, minimum in (("terms", 2), ("guide", 2)):
            if not isinstance(item[key], list) or len(item[key]) < minimum:
                raise ValueError(f"Incomplete engineering {key}: {context}")
            row[key] = [_teaching_text(text, f"{context}.{key}") for text in item[key]]
        if not isinstance(item["stages"], list) or len(item["stages"]) not in (3, 4):
            raise ValueError(f"Engineering page needs 3–4 stages: {context}")
        row["stages"] = [_teaching_record(stage, {"title", "body"}, context) for stage in item["stages"]]
        def visual_path(raw: Any) -> str:
            path = _teaching_text(raw, context).replace("\\", "/")
            relative = Path(path)
            if relative.is_absolute() or ".." in relative.parts or not path.startswith("roadmap-model-selection/") or relative.suffix.lower() != ".png":
                raise ValueError(f"Unsafe engineering image: {context}")
            (ROOT / relative).resolve().relative_to(ROOT.resolve())
            if not (ROOT / relative).is_file():
                raise FileNotFoundError(ROOT / relative)
            return path
        row["mobile_image"] = visual_path(item["mobile_image"])
        size = (item["mobile_width"], item["mobile_height"])
        if not all(type(n) is int and n > 0 for n in size):
            raise ValueError(f"Invalid mobile dimensions: {context}")
        with Image.open(ROOT / row["mobile_image"]) as image:
            if image.size != size:
                raise ValueError(f"Mobile image dimension mismatch: {context}")
        row["mobile_width"], row["mobile_height"] = size
        links = item.get("evidence_links", [])
        if not isinstance(links, list):
            raise ValueError(f"Invalid evidence links: {context}")
        row["evidence_links"] = []
        for link in links:
            clean_link = _teaching_record(link, {"title", "image"}, context)
            clean_link["image"] = visual_path(clean_link["image"])
            row["evidence_links"].append(clean_link)
        result.append(row)
    return result


def load_teaching_topics(source_topics: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Load the learner-facing causal story for every model topic.

    The 58 batch specs remain the engineering source.  Teaching packets are a
    separate, required layer: they establish a model-specific mental model and
    causal story before the learner reaches the four engineering reference
    diagrams.  There is intentionally no generic fallback here.
    """

    if not TEACHING_TOPICS.is_dir():
        raise FileNotFoundError(f"Missing teaching topic directory: {TEACHING_TOPICS}")
    source_ids = {str(topic["slug"]) for topic in source_topics}
    source_models = {str(topic["slug"]): clean(str(topic["model"])) for topic in source_topics}
    storyboards = load_storyboards(STORYBOARD_DIR, source_ids)
    files = {path.stem: path for path in TEACHING_TOPICS.glob("*.json")}
    missing = sorted(source_ids - set(files))
    unexpected = sorted(set(files) - source_ids)
    if missing or unexpected:
        raise ValueError(f"Teaching-topic files mismatch; missing={missing}, unexpected={unexpected}")

    top_fields = {
        "model",
        "badge",
        "title",
        "scenario",
        "promise",
        "mental_model",
        "micro_example",
        "mechanism_steps",
        "visual_intro",
        "concept_visuals",
        "boundary_cases",
        "comparison",
        "comparison_headers",
        "selection",
        "poc",
        "teach_back",
        "transfer_check",
        "review_trace",
        "slide_reading",
    }
    optional_top_fields = {
        "takeaway",
        "engineering_slides",
        "beginner_path",
        "deep_dive",
        "quality_status",
        "teaching_preflight",
    }
    packets: dict[str, dict[str, Any]] = {}
    for slug, path in files.items():
        payload = json.loads(path.read_text(encoding="utf-8"))
        if (
            not isinstance(payload, dict)
            or not top_fields <= set(payload)
            or not set(payload) <= top_fields | optional_top_fields
        ):
            raise ValueError(f"Teaching topic has invalid top-level fields: {path}")
        mechanism = payload["mechanism_steps"]
        concept_visuals = payload["concept_visuals"]
        boundary = payload["boundary_cases"]
        comparison = payload["comparison"]
        slide_reading = payload["slide_reading"]
        if not isinstance(mechanism, list) or len(mechanism) != 4:
            raise ValueError(f"Teaching topic needs four mechanism steps: {slug}")
        if not isinstance(concept_visuals, list) or (len(concept_visuals) < 3 and not (concept_visuals == [] and "beginner_path" in payload)):
            raise ValueError(f"Teaching topic needs at least three concept visuals: {slug}")
        if not isinstance(boundary, list) or len(boundary) < 3:
            raise ValueError(f"Teaching topic needs at least three boundary cases: {slug}")
        if not isinstance(comparison, list) or len(comparison) < 3:
            raise ValueError(f"Teaching topic needs at least three comparison rows: {slug}")
        if not isinstance(slide_reading, list) or len(slide_reading) != 4:
            raise ValueError(f"Teaching topic needs four diagram-reading entries: {slug}")
        poc = payload["poc"]
        beginner_path = (
            _clean_beginner_path(payload["beginner_path"], f"{slug}.beginner_path")
            if "beginner_path" in payload
            else None
        )
        deep_dive = (
            _clean_deep_dive(payload["deep_dive"], f"{slug}.deep_dive")
            if "deep_dive" in payload
            else None
        )
        if not isinstance(poc, dict) or set(poc) != {"title", "steps", "hold", "acceptance"}:
            raise ValueError(f"Teaching topic has invalid POC payload: {slug}")
        if not isinstance(poc["steps"], list) or len(poc["steps"]) != 3:
            raise ValueError(f"Teaching topic needs three POC steps: {slug}")
        if not isinstance(poc["acceptance"], dict) or set(poc["acceptance"]) != {
            "baseline", "measure", "negative_control", "owner"
        }:
            raise ValueError(f"Teaching topic needs explicit POC acceptance: {slug}")

        concept_fields = {"id", "placement", "title", "prompt", "caption", "image", "alt", "callouts"}
        allowed_placements = {
            "after_micro_example",
            "after_causal_chain",
            "before_boundary_cases",
            "after_comparison",
        }
        concept_ids: set[str] = set()
        cleaned_concept_visuals: list[dict[str, Any]] = []
        for index, visual in enumerate(concept_visuals, start=1):
            label = f"{slug}.concept_visuals[{index}]"
            if not isinstance(visual, dict) or set(visual) != concept_fields:
                raise ValueError(f"Teaching topic has invalid concept visual fields: {label}")
            visual_id = _teaching_text(visual["id"], f"{label}.id")
            placement = _teaching_text(visual["placement"], f"{label}.placement")
            if visual_id in concept_ids:
                raise ValueError(f"Teaching topic has duplicate concept visual id: {label}")
            if placement not in allowed_placements:
                raise ValueError(f"Teaching topic has invalid concept visual placement: {label}")
            concept_ids.add(visual_id)
            image = _teaching_text(visual["image"], f"{label}.image").replace("\\", "/")
            image_path = Path(image)
            if (
                image_path.is_absolute()
                or ".." in image_path.parts
                or image_path.suffix.lower() not in {".png", ".svg"}
                or not image.startswith("_course_content/generated-concepts/")
            ):
                raise ValueError(f"Teaching topic has unsafe concept visual path: {label}")
            absolute_image = ROOT / image_path
            try:
                absolute_image.resolve().relative_to(CONCEPT_VISUALS_ROOT.resolve())
            except ValueError as exc:
                raise ValueError(f"Teaching topic concept visual is outside the approved asset directory: {label}")
            _validate_concept_visual_asset(absolute_image)
            callouts = visual["callouts"]
            if not isinstance(callouts, list) or len(callouts) < 3:
                raise ValueError(f"Teaching topic needs at least three concept callouts: {label}")
            cleaned_concept_visuals.append(
                {
                    "id": visual_id,
                    "placement": placement,
                    "title": _teaching_text(visual["title"], f"{label}.title"),
                    "prompt": _teaching_text(visual["prompt"], f"{label}.prompt"),
                    "caption": _teaching_text(visual["caption"], f"{label}.caption"),
                    "image": image,
                    "alt": _teaching_text(visual["alt"], f"{label}.alt"),
                    "sequence": index,
                    "callouts": [
                        _teaching_record(callout, {"title", "body"}, f"{label}.callouts[{callout_index}]")
                        for callout_index, callout in enumerate(callouts, start=1)
                    ],
                }
            )

        placements = {visual["placement"] for visual in cleaned_concept_visuals}
        required_placements = {"after_causal_chain", "before_boundary_cases", "after_comparison"}
        if not required_placements <= placements and not (not cleaned_concept_visuals and beginner_path is not None):
            raise ValueError(
                f"Teaching topic needs causal, boundary and comparison visuals: {slug}"
            )

        cleaned_slide_reading: list[dict[str, Any]] = []
        for index, reading in enumerate(slide_reading, start=1):
            if not isinstance(reading, dict) or set(reading) != {
                "title", "question", "look", "relation", "takeaway", "terms"
            }:
                raise ValueError(f"Teaching topic has invalid diagram-reading fields: {slug} slide {index}")
            terms = reading["terms"]
            if not isinstance(terms, list) or len(terms) < 2:
                raise ValueError(f"Teaching topic needs two diagram terms: {slug} slide {index}")
            cleaned_slide_reading.append(
                {
                    **{
                        field: _teaching_text(reading[field], f"{slug}.slide_reading[{index}].{field}")
                        for field in ("title", "question", "look", "relation", "takeaway")
                    },
                    "terms": [
                        _teaching_text(term, f"{slug}.slide_reading[{index}].terms")
                        for term in terms
                    ],
                }
            )

        model = _teaching_text(payload["model"], f"{slug}.model")
        if model != source_models[slug]:
            raise ValueError(f"Teaching topic model name does not match course spec: {slug}")
        inline_visuals: list[dict[str, str]] = []
        for index, cue in enumerate(storyboards[slug]["causal"], start=1):
            step = mechanism[index - 1] if index <= len(mechanism) else {}
            override = step.get("inline_image") if isinstance(step, dict) else None
            if override:
                image = str(override).replace("\\", "/")
                display = "full-width"
            else:
                image = inline_visual_relative_path(slug, index)
                _validate_inline_visual_asset(
                    ROOT / image,
                    cue,
                    f"{slug}.mechanism_steps[{index}].inline_visual",
                )
                display = "inline"
            inline_visuals.append(
                {
                    "id": f"mechanism-step-{index:02d}",
                    "image": image,
                    "label": cue["label"],
                    "not_claim": cue["not_claim"],
                    "alt": cue["alt"],
                    "cue": cue["kind"],
                    "display": display,
                }
            )
        packet = {
            "model": model,
            "badge": _teaching_text(payload["badge"], f"{slug}.badge"),
            "title": _teaching_text(payload["title"], f"{slug}.title"),
            "scenario": _teaching_record(payload["scenario"], {"title", "body"}, f"{slug}.scenario"),
            "promise": _teaching_record(
                payload["promise"], {"title", "body"}, f"{slug}.promise", {"visual_body"}
            ),
            "mental_model": _teaching_record(
                payload["mental_model"], {"title", "body", "limit"}, f"{slug}.mental_model", {"visual_limit"}
            ),
            "micro_example": _teaching_record(
                payload["micro_example"],
                {"title", "setup", "prediction", "reveal"},
                f"{slug}.micro_example",
                {"visual_setup", "visual_prediction", "visual_reveal"},
            ),
            "mechanism_steps": [
                _teaching_mechanism_step(step, f"{slug}.mechanism_steps[{index}]")
                for index, step in enumerate(mechanism, start=1)
            ],
            "inline_visuals": inline_visuals,
            "visual_intro": _teaching_text(payload["visual_intro"], f"{slug}.visual_intro"),
            "concept_visuals": cleaned_concept_visuals,
            "boundary_cases": [
                _teaching_record(
                    case,
                    {"condition", "effect", "action"},
                    f"{slug}.boundary_cases[{index}]",
                    {"visual_condition", "visual_effect", "visual_action"},
                )
                for index, case in enumerate(boundary, start=1)
            ],
            "comparison": [
                _teaching_record(
                    row,
                    {"model", "normality", "candidate"},
                    f"{slug}.comparison[{index}]",
                    {"visual_normality", "visual_candidate"},
                )
                for index, row in enumerate(comparison, start=1)
            ],
            "comparison_headers": _teaching_record(
                payload["comparison_headers"],
                {"title", "basis", "output"},
                f"{slug}.comparison_headers",
            ),
            "selection": _teaching_text(payload["selection"], f"{slug}.selection"),
            "poc": {
                "title": _teaching_text(poc["title"], f"{slug}.poc.title"),
                "steps": [_teaching_text(step, f"{slug}.poc.steps") for step in poc["steps"]],
                "hold": _teaching_text(poc["hold"], f"{slug}.poc.hold"),
                "acceptance": _teaching_record(
                    poc["acceptance"],
                    {"baseline", "measure", "negative_control", "owner"},
                    f"{slug}.poc.acceptance",
                ),
            },
            "teach_back": _teaching_record(
                payload["teach_back"], {"question", "answer"}, f"{slug}.teach_back"
            ),
            "transfer_check": _teaching_record(
                payload["transfer_check"],
                {"title", "scenario", "question", "answer"},
                f"{slug}.transfer_check",
            ),
            "review_trace": _clean_review_trace(payload["review_trace"], f"{slug}.review_trace"),
            "slide_reading": cleaned_slide_reading,
        }
        if beginner_path is not None:
            packet["beginner_path"] = beginner_path
        if "takeaway" in payload:
            packet["takeaway"] = _teaching_text(payload["takeaway"], f"{slug}.takeaway")
        if "engineering_slides" in payload:
            packet["engineering_slides"] = _clean_engineering_slides(payload["engineering_slides"], f"{slug}.engineering_slides")
        if deep_dive is not None:
            packet["deep_dive"] = deep_dive
        packets[slug] = packet
    return packets


def normalize_relative_dir(value: str) -> Path:
    path = Path(value)
    if path.parts and path.parts[0] == "roadmap-model-selection":
        path = Path(*path.parts[1:])
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Unsafe topic path: {value!r}")
    return path


def active_assets(relative_dir: Path) -> list[tuple[str, str]]:
    """Read active assets from the manifest rather than guessing filenames."""

    manifest = ROADMAP / relative_dir / "slide-manifest.md"
    if not manifest.is_file():
        raise FileNotFoundError(f"Missing manifest: {manifest}")
    found: dict[int, tuple[str, str]] = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        slide = re.search(r"`[^`]+-(0[1-4])`", line)
        asset = re.search(r"`(images/final/[^`]+\.png)`", line)
        if not slide or not asset:
            continue
        page = int(slide.group(1))
        relative_asset = asset.group(1).replace("\\", "/")
        absolute_asset = manifest.parent / relative_asset
        if not absolute_asset.is_file():
            raise FileNotFoundError(f"Manifest asset missing: {absolute_asset}")
        with Image.open(absolute_asset) as image:
            if image.size != (1672, 941):
                raise ValueError(f"Unexpected asset dimensions {image.size}: {absolute_asset}")
        found[page] = (relative_asset, f"roadmap-model-selection/{relative_dir.as_posix()}/{relative_asset}")
    if set(found) != {1, 2, 3, 4}:
        raise ValueError(f"Expected active pages 01-04 in {manifest}, found {sorted(found)}")
    return [found[number] for number in range(1, 5)]


def section_assets(relative_dir: str, slide_ids: list[str]) -> dict[str, str]:
    """Return exact approved shared-course assets named in a section manifest."""

    manifest = SECTION_PAGES / relative_dir / "slide-manifest.md"
    if not manifest.is_file():
        raise FileNotFoundError(f"Missing shared-course manifest: {manifest}")
    wanted = set(slide_ids)
    found: dict[str, str] = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|") or "approved" not in line.lower():
            continue
        identifier = re.search(r"`([^`]+)`", line)
        asset = re.search(r"`?(images/final/[^`|]+\.png)`?", line)
        if not identifier or not asset or identifier.group(1) not in wanted:
            continue
        slide_id = identifier.group(1)
        relative_asset = asset.group(1).strip()
        absolute_asset = manifest.parent / relative_asset
        if not absolute_asset.is_file():
            raise FileNotFoundError(f"Shared-course asset missing: {absolute_asset}")
        with Image.open(absolute_asset) as image:
            if image.size != (1672, 941):
                raise ValueError(f"Unexpected shared-course asset dimensions {image.size}: {absolute_asset}")
        # The curated IDs are unique.  Keeping the first approved row also
        # mirrors the manifest's declared active row should historical rows
        # with the same logical ID be retained below it.
        normalised_asset = relative_asset.replace("\\", "/")
        found.setdefault(
            slide_id,
            f"course-delivery/section-pages/{relative_dir}/{normalised_asset}",
        )
    missing = wanted - set(found)
    if missing:
        raise ValueError(f"Shared-course manifest did not expose approved assets for: {sorted(missing)}")
    return found


def shared_collection_payload(collection_id: str, spec: dict[str, Any]) -> dict[str, Any]:
    items = list(spec["items"])
    assets = section_assets(str(spec["relative_dir"]), [item[0] for item in items])
    for slide_id, _, _ in items:
        engineering_image = SUPPORTING_ENGINEERING_REFERENCES.get(slide_id)
        if not engineering_image:
            continue
        if "image-led_" in engineering_image:
            raise ValueError(f"Supporting engineering reference must remain a legacy asset: {engineering_image}")
        absolute_engineering_image = ROOT / engineering_image
        if not absolute_engineering_image.is_file():
            raise FileNotFoundError(f"Missing supporting engineering reference: {absolute_engineering_image}")
        with Image.open(absolute_engineering_image) as image:
            if image.size != (1672, 941):
                raise ValueError(f"Unexpected supporting engineering-reference dimensions {image.size}: {absolute_engineering_image}")
    return {
        "id": collection_id,
        "label": clean(str(spec["label"])),
        "intro": clean(str(spec["intro"])),
        "items": [
            {
                "id": slide_id,
                "title": clean(title),
                "summary": clean(summary),
                "image": assets[slide_id],
                # Shared-image migrations use an explicit filename marker so
                # the renderer can preserve the distinct first-read treatment
                # (and audits can distinguish it from legacy references).
                "imageLed": is_image_led_shared_asset(assets[slide_id]),
                "engineeringImage": SUPPORTING_ENGINEERING_REFERENCES.get(slide_id, ""),
                "alt": f"{title}：Vision AI 工程教學圖。",
            }
            for slide_id, title, summary in items
        ],
    }


def is_image_led_shared_asset(asset: str) -> bool:
    """Identify active full-canvas shared-story assets without renaming them.

    Earlier migrations use ``-image-led_`` in the filename.  The shared
    Video/Foundation P0 migration uses ``_image-led_`` while keeping the
    existing slide IDs readable.  Chapter 04 uses the explicit ``ADLED-``
    prefix so it can retain the original ADCMP/ADSHR file names as optional
    engineering references.
    """

    name = Path(asset).name
    return "-image-led_" in name or "_image-led_" in name or name.startswith("ADLED-")


def family_support_payload(family_id: str, spec: dict[str, Any]) -> list[dict[str, str]]:
    items = list(spec["items"])
    assets = section_assets(str(spec["relative_dir"]), [item[0] for item in items])
    for slide_id, _, _ in items:
        engineering_image = FAMILY_SUPPORT_ENGINEERING_REFERENCES.get(slide_id)
        if not engineering_image:
            continue
        if "image-led_" in engineering_image:
            raise ValueError(f"Engineering reference must remain a legacy asset: {engineering_image}")
        absolute_engineering_image = ROOT / engineering_image
        if not absolute_engineering_image.is_file():
            raise FileNotFoundError(f"Missing engineering reference: {absolute_engineering_image}")
        with Image.open(absolute_engineering_image) as image:
            if image.size != (1672, 941):
                raise ValueError(f"Unexpected engineering-reference dimensions {image.size}: {absolute_engineering_image}")
    return [
        {
            "id": slide_id,
            "title": clean(title),
            "summary": clean(summary),
            "image": assets[slide_id],
            "imageLed": is_image_led_shared_asset(assets[slide_id]),
            "engineeringImage": FAMILY_SUPPORT_ENGINEERING_REFERENCES.get(slide_id, ""),
            "alt": f"{FAMILIES[family_id]['label']}：{title}。",
        }
        for slide_id, title, summary in items
    ]


def learner_slide_copy(
    model: str,
    brief: dict[str, Any],
    page_index: int,
    teaching_story: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Create the three short reading handles shown before technical detail."""

    if teaching_story is None:
        raise ValueError(f"{model} is missing its required model-specific teaching story")
    return teaching_story["slide_reading"][page_index]


def page_payload(
    topic: dict[str, Any],
    brief: dict[str, Any],
    page_index: int,
    asset: tuple[str, str],
    teaching_story: dict[str, Any] | None = None,
) -> dict[str, Any]:
    label, prompt = SLIDE_META[page_index]
    revised = (teaching_story or {}).get("engineering_slides", [])
    if revised:
        if len(revised) != 4:
            raise ValueError("engineering_slides must contain all four lessons")
        item = revised[page_index]
        return {
            "index": page_index + 1, "label": item.get("label", label),
            "prompt": item["title"], "question": item["question"],
            "plain": item["plain"], "terms": item.get("terms", []),
            "guide": item["guide"], "stages": item["stages"],
            "misconception": item["misconception"],
            "image": asset[1], "activeAsset": asset[0], "alt": item["alt"],
            "mobileImage": item["mobile_image"],
            "mobileWidth": item["mobile_width"], "mobileHeight": item["mobile_height"],
            "engineering": item["engineering"],
            "evidenceLinks": item.get("evidence_links", []),
        }
    learner = learner_slide_copy(clean(str(topic["model"])), brief, page_index, teaching_story)
    page_keys = ("identity", "architecture", "build")
    if page_index < 3:
        page = topic[page_keys[page_index]]
        stages = [
            {"title": clean(card["title"]), "body": clean(card["body"])}
            for card in page["cards"]
        ]
        guide = [
            clean(page["context"]),
            "讀圖順序：" + " → ".join(stage["title"] for stage in stages),
            "帶走：" + clean(page["takeaway"]),
        ]
        question = learner["question"]
        misconception = clean(topic["failure"])
        engineering_takeaway = clean(page["takeaway"])
    else:
        stages = [
            {"title": "不要直接採用", "body": clean(topic["failure"])},
            {"title": "成立的工程條件", "body": clean(topic["selection"])},
            {"title": "最後仍要回看證據", "body": clean(topic["takeaway"])},
        ]
        guide = [
            "先看左側：它在哪些資料、輸入、語意或 runtime 條件下會失效。",
            "再看右側：只有固定共同契約、保存 evidence、並交回 owner review，模型比較才成立。",
            "帶走：" + clean(topic["takeaway"]),
        ]
        question = learner["question"]
        misconception = clean(topic["failure"])
        engineering_takeaway = clean(topic["takeaway"])
    alt = f"{topic['model']} 的第 {page_index + 1} 張教學圖：{label}。"
    return {
        "index": page_index + 1,
        "label": label,
        "prompt": learner["title"],
        "question": question,
        "plain": {
            "look": learner["look"],
            "relation": learner["relation"],
            "takeaway": learner["takeaway"],
        },
        "terms": learner.get(
            "terms",
            brief["terms"] if page_index == 0 else brief.get("architecture_terms", []) if page_index == 1 else [],
        ),
        "guide": guide,
        "stages": stages,
        "misconception": misconception,
        "image": asset[1],
        "activeAsset": asset[0],
        "alt": alt,
        "engineering": {
            "takeaway": engineering_takeaway,
            "nextAction": clean(topic["selection"]),
            "redLine": clean(topic["failure"]),
        },
    }


def make_course_data() -> dict[str, Any]:
    # The landing page must not inherit whichever legacy PPT card happened to
    # be last visited.  It uses one stable work-example scene that teaches the
    # course-wide contract: raw AOI evidence → candidate → human review.
    _validate_concept_visual_asset(ROOT / HOME_HERO_IMAGE)
    for visual in SHARED_JOURNEY_IMAGES.values():
        _validate_concept_visual_asset(ROOT / str(visual["image"]))
    source_topics = load_topics()
    learner_briefs = load_learner_briefs(source_topics)
    teaching_topics = load_teaching_topics(source_topics)
    by_slug = {str(topic["slug"]): topic for topic in source_topics}
    unknown_families = {str(topic["family"]) for topic in source_topics} - set(FAMILIES)
    if unknown_families:
        raise ValueError(f"No family metadata for: {sorted(unknown_families)}")

    topics: list[dict[str, Any]] = []
    used: set[str] = set()
    for family_id, family in FAMILIES.items():
        for slug in family["order"]:
            topic = by_slug.get(slug)
            if topic is None:
                continue  # Cross-family references such as Grounding DINO are shown in their native family.
            if slug in used:
                continue
            if topic["family"] != family_id:
                continue
            used.add(slug)
            relative_dir = normalize_relative_dir(str(topic["relative_dir"]))
            assets = active_assets(relative_dir)
            learner_brief = learner_briefs[slug]
            teaching_story = teaching_topics.get(slug)
            slides = [
                page_payload(topic, learner_brief, index, asset, teaching_story)
                for index, asset in enumerate(assets)
            ]
            identity = topic["identity"]
            build = topic["build"]
            summary = learner_brief["problem"]
            keywords = [family["label"], *[stage["title"] for stage in slides[0]["stages"]], topic["model"]]
            topics.append(
                {
                    "id": slug,
                    "model": clean(topic["model"]),
                    "family": family_id,
                    "familyLabel": family["label"],
                    "familyIcon": family["icon"],
                    "summary": summary,
                    "learnerBrief": learner_brief,
                    "teachingStory": teaching_story,
                    "selectionQuestion": learner_brief["first"],
                    "takeaway": clean(topic["takeaway"]),
                    "failure": clean(topic["failure"]),
                    "selection": clean(topic["selection"]),
                    "keywords": [clean(value) for value in keywords],
                    "objectives": [
                        f"說清楚 {clean(topic['model'])} 的輸出責任與不可主張的事。",
                        f"沿著「{' → '.join(stage['title'] for stage in slides[1]['stages'])}」說出它如何形成候選。",
                        f"在導入前鎖定：{'、'.join(clean(card['title']) for card in build['cards'][:3])}。",
                    ],
                    "checklist": [
                        f"{clean(card['title'])}：{clean(card['body'])}"
                        for card in build["cards"]
                    ],
                    "engineeringBrief": {
                        "output": learner_brief["deliverable"],
                        "useWhen": learner_brief["first"],
                        "locks": [
                            {
                                "title": clean(card["title"]),
                                "body": clean(card["body"]),
                            }
                            for card in build["cards"]
                        ],
                        "evidence": learner_brief.get("evidence", FAMILY_EVIDENCE[family_id]),
                        "hold": learner_brief["hold"],
                        "handoff": clean(topic["takeaway"]),
                        "technicalSelection": clean(topic["selection"]),
                        "technicalFailure": clean(topic["failure"]),
                    },
                    "slides": slides,
                    "modelPath": f"roadmap-model-selection/{relative_dir.as_posix()}/model.md",
                    "manifestPath": f"roadmap-model-selection/{relative_dir.as_posix()}/slide-manifest.md",
                }
            )

    # Any missing ordering entries should still be visible to a learner.
    for topic in source_topics:
        slug = str(topic["slug"])
        if slug in used:
            continue
        family_id = str(topic["family"])
        family = FAMILIES[family_id]
        relative_dir = normalize_relative_dir(str(topic["relative_dir"]))
        assets = active_assets(relative_dir)
        learner_brief = learner_briefs[slug]
        teaching_story = teaching_topics.get(slug)
        slides = [
            page_payload(topic, learner_brief, index, asset, teaching_story)
            for index, asset in enumerate(assets)
        ]
        topics.append(
            {
                "id": slug,
                "model": clean(topic["model"]),
                "family": family_id,
                "familyLabel": family["label"],
                "familyIcon": family["icon"],
                "summary": learner_brief["problem"],
                "learnerBrief": learner_brief,
                "teachingStory": teaching_story,
                "selectionQuestion": learner_brief["first"],
                "takeaway": clean(topic["takeaway"]),
                "failure": clean(topic["failure"]),
                "selection": clean(topic["selection"]),
                "keywords": [family["label"], clean(topic["model"])],
                "objectives": ["辨識輸出責任", "沿圖說明資料流", "寫出工程 gate"],
                "checklist": [clean(card["body"]) for card in topic["build"]["cards"]],
                "engineeringBrief": {
                    "output": learner_brief["deliverable"],
                    "useWhen": learner_brief["first"],
                    "locks": [
                        {"title": clean(card["title"]), "body": clean(card["body"])}
                        for card in topic["build"]["cards"]
                    ],
                    "evidence": learner_brief.get("evidence", FAMILY_EVIDENCE[family_id]),
                    "hold": learner_brief["hold"],
                    "handoff": clean(topic["takeaway"]),
                    "technicalSelection": clean(topic["selection"]),
                    "technicalFailure": clean(topic["failure"]),
                },
                "slides": slides,
                "modelPath": f"roadmap-model-selection/{relative_dir.as_posix()}/model.md",
                "manifestPath": f"roadmap-model-selection/{relative_dir.as_posix()}/slide-manifest.md",
            }
        )
        used.add(slug)

    if len(topics) != 58:
        raise ValueError(f"Expected 58 course topics, produced {len(topics)}")

    # A full authored engineering revision also owns the handoff and catalog
    # copy. Otherwise old batch-spec claims could contradict its new pages.
    for topic in topics:
        story = topic.get("teachingStory") or {}
        if not story.get("engineering_slides"):
            continue
        learner = topic["learnerBrief"]
        topic.update(takeaway=story.get("takeaway", story["promise"]["body"]), failure=story["mental_model"]["limit"], selection=story["selection"])
        locks = [
            {"title": "輸入與版本", "body": learner["first"]},
            {"title": "關鍵機制", "body": story["mental_model"]["body"]},
            {"title": "獨立驗證", "body": story["poc"]["acceptance"]["measure"]},
            {"title": "失敗處理", "body": learner["hold"]},
        ]
        topic["checklist"] = [f"{card['title']}：{card['body']}" for card in locks]
        topic["objectives"] = [f"說清楚 {topic['model']} 的機制與交付。", "由反例判斷何時更換輸入或方法。", "保存輸入設定，以獨立資料核對結果與完整成本。"]
        topic["engineeringBrief"].update(locks=locks, handoff=topic["takeaway"], technicalSelection=topic["selection"], technicalFailure=topic["failure"])

    counts: dict[str, int] = defaultdict(int)
    for topic in topics:
        counts[topic["family"]] += 1
    families = []
    for family_id, meta in FAMILIES.items():
        families.append({"id": family_id, **meta, "count": counts[family_id]})

    tracks = [
        {"id": "geometry", "label": "先讓畫面位置可信", "duration": "20–35 分鐘", "description": "先讓相機和產品位置對得上，再做後續檢查或量測。", "topics": ["charuco", "ecc", "sift", "lightglue"]},
        {"id": "known", "label": "你已知道要找什麼", "duration": "35–55 分鐘", "description": "已知類別或標註時，選整張判斷、位置、輪廓或位置點。", "topics": ["resnet", "det-yolo-dense", "u-net", "keypoint-r-cnn"]},
        {"id": "anomaly", "label": "你只知道什麼是正常", "duration": "45–70 分鐘", "description": "先收集乾淨正常品，再找出新影像不像正常的地方。", "topics": ["ad-patchcore", "ad-stfpm", "ad-efficientad"]},
        {"id": "temporal", "label": "你要看影片中的變化", "duration": "30–50 分鐘", "description": "先分清是看變化、移動、同一物件，還是完整事件。", "topics": ["frame-difference", "bytetrack", "raft"]},
        {"id": "semantic", "label": "你要用文字或圖片輔助", "duration": "30–50 分鐘", "description": "把影像特徵、文字搜尋和看圖問答當成候選與協助，不是決策。", "topics": ["dinov2", "clip", "det-grounding-dino-interface", "llava"]},
        {"id": "generation", "label": "你要生成或看清畫面", "duration": "25–45 分鐘", "description": "生成、編修和復原只做訓練或閱讀輔助，原圖仍是證據。", "topics": ["controlnet", "defectfill", "inpainting"]},
    ]
    supporting = {
        collection_id: shared_collection_payload(collection_id, spec)
        for collection_id, spec in SUPPORTING_COLLECTIONS.items()
    }
    family_support = {
        family_id: family_support_payload(family_id, spec)
        for family_id, spec in FAMILY_SUPPORT.items()
    }
    return {
        "version": 2,
        "homeHero": {
            "image": HOME_HERO_IMAGE,
            "alt": "半導體 AOI 現場：相機檢查晶圓與 PCB，候選 ROI 經由 evidence record 交給人員 review。",
            "caption": "從 raw AOI evidence → candidate → human review；模型輸出不會直接變成產線動作。",
        },
        "sharedJourneys": SHARED_JOURNEY_IMAGES,
        "workplaceLessons": __import__("supporting_lessons").load_lessons(ROOT),
        "families": families,
        "topics": topics,
        "tracks": tracks,
        "supporting": supporting,
        "familySupport": family_support,
    }


HTML_TEMPLATE = r'''<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Vision AI 模型選型互動教學：58 個主題、232 張參考插圖、離線可開啟。">
  <title>Vision AI 選型學習地圖｜58 個模型主題</title>
  <style>
    :root {
      --ink: #102a5b;
      --ink-strong: #071a3b;
      --blue: #1769e0;
      --blue-2: #e8f2ff;
      --cyan: #12b7d8;
      --green: #13a866;
      --green-bg: #eaf8ef;
      --orange: #ec9200;
      --yellow: #fff4cc;
      --red: #dd4850;
      --red-bg: #fff0f1;
      --line: #a7c9ff;
      --paper: #ffffff;
      --canvas: #f3f7fc;
      --muted: #52647f;
      --shadow: 0 14px 34px rgba(18, 54, 112, .11);
      --radius: 18px;
      color-scheme: light;
    }
    :root[data-theme="dark"] {
      --ink: #d9e8ff;
      --ink-strong: #ffffff;
      --blue: #72adff;
      --blue-2: #132b55;
      --cyan: #55d9f1;
      --green: #46d78f;
      --green-bg: #103b2a;
      --orange: #ffc04e;
      --yellow: #4d3a08;
      --red: #ff7d83;
      --red-bg: #4a2028;
      --line: #3a629b;
      --paper: #10213f;
      --canvas: #081426;
      --muted: #b1c0d7;
      --shadow: 0 14px 34px rgba(0, 0, 0, .3);
      color-scheme: dark;
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; background: var(--canvas); }
    body { margin: 0; min-width: 320px; background: var(--canvas); color: var(--ink); font-family: Inter, "Noto Sans TC", "Microsoft JhengHei", system-ui, -apple-system, BlinkMacSystemFont, sans-serif; line-height: 1.58; }
    button, input, select, textarea { font: inherit; }
    button, a { -webkit-tap-highlight-color: transparent; }
    button { cursor: pointer; }
    a { color: var(--blue); }
    img { max-width: 100%; }
    .skip-link { position: fixed; z-index: 100; left: 16px; top: -64px; background: var(--ink-strong); color: #fff; padding: 10px 16px; border-radius: 10px; transition: top .15s; }
    .skip-link:focus { top: 16px; }
    :focus-visible { outline: 3px solid var(--orange); outline-offset: 3px; }
    .topbar { position: sticky; top: 0; z-index: 30; display: grid; grid-template-columns: minmax(190px, 1fr) minmax(230px, 520px) auto; gap: 16px; align-items: center; min-height: 76px; padding: 10px clamp(16px, 3vw, 42px); background: color-mix(in srgb, var(--paper) 94%, transparent); border-top: 4px solid var(--ink-strong); border-bottom: 1px solid var(--line); backdrop-filter: blur(14px); }
    .brand { display: inline-flex; align-items: center; gap: 10px; color: var(--ink-strong); font-weight: 900; text-decoration: none; letter-spacing: -.02em; }
    .brand-mark { display: grid; place-items: center; width: 34px; height: 34px; border-radius: 10px; background: var(--blue); color: #fff; font-size: 18px; box-shadow: 0 4px 12px rgba(23,105,224,.3); }
    .brand small { display: block; color: var(--muted); font-size: 11px; font-weight: 800; letter-spacing: .1em; }
    .search-box { position: relative; display: flex; align-items: center; }
    .search-box span { position: absolute; left: 14px; color: var(--muted); pointer-events: none; }
    .search-box input { width: 100%; border: 1px solid var(--line); border-radius: 12px; background: var(--paper); color: var(--ink); padding: 11px 44px 11px 40px; }
    .search-box kbd { position: absolute; right: 10px; padding: 2px 6px; border: 1px solid var(--line); border-radius: 5px; color: var(--muted); font-size: 11px; }
    .top-actions { display: flex; align-items: center; gap: 8px; }
    .icon-button, .button { border: 1px solid var(--line); border-radius: 10px; background: var(--paper); color: var(--ink); padding: 9px 12px; font-weight: 750; }
    .icon-button:hover, .button:hover { border-color: var(--blue); background: var(--blue-2); }
    .button.primary { border-color: var(--blue); background: var(--blue); color: #fff; }
    .button.primary:hover { filter: brightness(1.06); }
    .button.warn { color: #fff; border-color: var(--red); background: var(--red); }
    .app-shell { display: grid; grid-template-columns: 304px minmax(0, 1fr); max-width: 1800px; margin: 0 auto; min-height: calc(100vh - 76px); }
    .sidebar { position: sticky; top: 76px; height: calc(100vh - 76px); overflow-y: auto; padding: 20px 14px 36px; border-right: 1px solid var(--line); background: var(--paper); }
    .sidebar-heading { margin: 4px 8px 8px; color: var(--muted); font-size: 11px; font-weight: 900; letter-spacing: .1em; text-transform: uppercase; }
    .nav-button, .topic-link { width: 100%; display: flex; gap: 10px; align-items: center; border: 0; border-radius: 10px; background: transparent; color: var(--ink); padding: 10px 12px; text-align: left; }
    .nav-button:hover, .topic-link:hover, .topic-link.active { background: var(--blue-2); color: var(--ink-strong); }
    .nav-button.active { background: var(--blue); color: #fff; }
    .nav-button .nav-number { margin-left: auto; min-width: 24px; border-radius: 99px; background: color-mix(in srgb, var(--blue) 15%, transparent); padding: 1px 7px; color: var(--blue); font-size: 12px; text-align: center; }
    .nav-button.active .nav-number { background: rgba(255,255,255,.22); color: #fff; }
    .nav-family { margin: 16px 0 0; border-top: 1px solid color-mix(in srgb, var(--line) 52%, transparent); padding-top: 10px; }
    .nav-family summary { display: flex; align-items: center; gap: 7px; padding: 8px 10px; color: var(--ink-strong); cursor: pointer; font-size: 13px; font-weight: 850; }
    .nav-family summary::marker { color: var(--blue); }
    .nav-progress { margin-left: auto; color: var(--muted); font-size: 11px; font-weight: 700; }
    .topic-link { padding: 7px 10px 7px 26px; font-size: 13px; line-height: 1.3; }
    .topic-link .complete-dot { width: 8px; height: 8px; flex: 0 0 8px; border: 1px solid var(--line); border-radius: 999px; }
    .topic-link.done .complete-dot { background: var(--green); border-color: var(--green); }
    .sidebar-help { margin: 24px 7px; padding: 13px; border-radius: 12px; background: var(--yellow); color: var(--ink-strong); font-size: 12px; }
    main { min-width: 0; padding: clamp(22px, 3vw, 46px); }
    .content { width: min(1260px, 100%); margin: 0 auto; }
    .hero { padding: clamp(24px, 4vw, 56px); overflow: hidden; border: 1px solid var(--line); border-radius: 24px; background: linear-gradient(120deg, var(--paper) 0%, var(--paper) 54%, var(--blue-2) 54%, color-mix(in srgb, var(--blue-2) 40%, var(--paper)) 100%); box-shadow: var(--shadow); }
    .hero-grid { display: grid; grid-template-columns: minmax(0, 1.08fr) minmax(330px, .92fr); gap: clamp(22px, 4vw, 54px); align-items: center; }
    .hero-preview { overflow: hidden; margin: 0; border: 1px solid var(--line); border-radius: 16px; background: #fff; box-shadow: 0 12px 28px rgba(17,52,109,.15); }
    .hero-preview button { display: block; width: 100%; border: 0; background: #fff; padding: 0; text-align: left; }
    .hero-preview img { display: block; width: 100%; height: auto; aspect-ratio: 1672 / 941; object-fit: contain; }
    .hero-preview figcaption { display: flex; justify-content: space-between; gap: 12px; padding: 10px 12px; color: #23426f; font-size: 12px; font-weight: 800; }
    .eyebrow { margin: 0 0 8px; color: var(--blue); font-size: 12px; font-weight: 900; letter-spacing: .12em; text-transform: uppercase; }
    h1, h2, h3, p { margin-top: 0; }
    h1 { max-width: 880px; margin-bottom: 14px; color: var(--ink-strong); font-size: clamp(33px, 5.1vw, 64px); line-height: 1.08; letter-spacing: -.05em; }
    h2 { color: var(--ink-strong); font-size: clamp(23px, 3vw, 34px); letter-spacing: -.035em; }
    h3 { color: var(--ink-strong); }
    .lead { max-width: 760px; color: var(--muted); font-size: clamp(17px, 2vw, 21px); }
    .hero-actions, .action-row { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 22px; }
    .stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; max-width: 640px; margin-top: 30px; }
    .stat { padding: 13px 14px; border: 1px solid var(--line); border-radius: 13px; background: color-mix(in srgb, var(--paper) 86%, transparent); }
    .stat strong { display: block; color: var(--ink-strong); font-size: 24px; line-height: 1.05; }
    .stat span { color: var(--muted); font-size: 12px; font-weight: 700; }
    .section { margin-top: clamp(32px, 5vw, 64px); }
    .section-heading { display: flex; justify-content: space-between; gap: 18px; align-items: flex-end; margin-bottom: 18px; }
    .section-heading p { max-width: 620px; margin: 0; color: var(--muted); }
    .route-grid, .family-grid, .topic-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(236px, 1fr)); gap: 15px; }
    .route-card, .family-card, .topic-card { display: flex; flex-direction: column; align-items: flex-start; min-height: 190px; border: 1px solid var(--line); border-radius: var(--radius); background: var(--paper); color: var(--ink); padding: 19px; text-align: left; box-shadow: 0 5px 18px rgba(25,55,102,.04); transition: transform .16s, box-shadow .16s, border-color .16s; }
    .route-card:hover, .family-card:hover, .topic-card:hover { transform: translateY(-3px); border-color: var(--blue); box-shadow: var(--shadow); }
    .route-card .route-number { display: grid; place-items: center; width: 31px; height: 31px; margin-bottom: 12px; border-radius: 50%; background: var(--blue-2); color: var(--blue); font-size: 13px; font-weight: 900; }
    .route-card strong, .family-card strong, .topic-card h3 { color: var(--ink-strong); font-size: 18px; line-height: 1.25; }
    .route-card p, .family-card p, .topic-card p { color: var(--muted); font-size: 14px; }
    .route-card small, .topic-card small { margin-top: auto; color: var(--blue); font-weight: 850; }
    .family-card .family-icon { display: grid; place-items: center; width: 38px; height: 38px; margin-bottom: 12px; border-radius: 11px; background: var(--blue); color: #fff; font-size: 20px; }
    .learn-steps { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; }
    .learn-step { position: relative; min-height: 142px; padding: 18px; border-radius: 16px; border: 1px solid var(--line); background: var(--paper); }
    .learn-step span { display: inline-grid; place-items: center; width: 27px; height: 27px; margin-bottom: 10px; border-radius: 50%; background: var(--blue); color: #fff; font-size: 12px; font-weight: 900; }
    .learn-step strong { display: block; color: var(--ink-strong); }
    .learn-step p { margin: 5px 0 0; color: var(--muted); font-size: 13px; }
    .notice { display: grid; grid-template-columns: auto 1fr; gap: 12px; padding: 17px; border: 1px solid #e8bd48; border-radius: 15px; background: var(--yellow); color: var(--ink-strong); }
    .notice .notice-icon { font-size: 26px; }
    .notice strong { display: block; }
    .breadcrumb { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; color: var(--muted); font-size: 14px; }
    .breadcrumb button { border: 0; background: transparent; color: var(--blue); padding: 0; text-decoration: underline; }
    .lesson-head { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 18px; align-items: start; margin-bottom: 14px; }
    .lesson-head h1 { margin: 7px 0 8px; font-size: clamp(31px, 4vw, 51px); }
    .chips { display: flex; flex-wrap: wrap; gap: 7px; }
    .chip { display: inline-flex; align-items: center; gap: 5px; border: 1px solid var(--line); border-radius: 999px; background: var(--blue-2); color: var(--ink); padding: 4px 10px; font-size: 12px; font-weight: 800; }
    .chip.green { border-color: color-mix(in srgb, var(--green) 45%, var(--line)); background: var(--green-bg); color: var(--green); }
    .lesson-lead { max-width: 900px; color: var(--muted); font-size: 18px; }
    .lesson-quickline { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; max-width: 980px; margin-top: 11px; }
    .lesson-quickline div { border-left: 3px solid var(--cyan); padding: 5px 9px; background: color-mix(in srgb, var(--blue-2) 40%, var(--paper)); color: var(--ink-strong); font-size: 13px; line-height: 1.5; }
    .lesson-quickline div:last-child { border-left-color: var(--orange); }
    .lesson-quickline strong { color: var(--blue); }
    .selection-question { max-width: 900px; margin: 10px 0 0; padding: 9px 12px; border-left: 4px solid var(--cyan); background: color-mix(in srgb, var(--blue-2) 45%, var(--paper)); color: var(--ink-strong); font-size: 14px; }
    .lesson-actions { display: flex; flex-direction: column; gap: 8px; min-width: 130px; }
    .slide-tabs { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; margin: 17px 0 18px; border-bottom: 1px solid var(--line); padding-bottom: 14px; }
    .slide-tab { min-height: 60px; display: flex; align-items: center; gap: 9px; border: 1px solid var(--line); border-radius: 12px; background: var(--paper); color: var(--ink); padding: 9px; text-align: left; }
    .slide-tab:hover { border-color: var(--blue); }
    .slide-tab[aria-selected="true"] { border-color: var(--blue); background: var(--blue); color: #fff; box-shadow: 0 6px 15px rgba(23,105,224,.22); }
    .slide-tab strong { display: grid; place-items: center; width: 25px; height: 25px; border-radius: 50%; background: color-mix(in srgb, var(--blue) 13%, var(--paper)); color: var(--blue); font-size: 12px; }
    .slide-tab[aria-selected="true"] strong { background: rgba(255,255,255,.2); color: #fff; }
    .slide-tab span { display: block; font-size: 12px; font-weight: 800; line-height: 1.18; }
    .viewer-grid { display: grid; grid-template-columns: minmax(0, 1.64fr) minmax(300px, .86fr); gap: 21px; align-items: start; }
    .figure-card { overflow: hidden; border: 1px solid var(--line); border-radius: 17px; background: #fff; box-shadow: var(--shadow); }
    .image-button { display: block; width: 100%; border: 0; background: #fff; padding: 0; }
    .image-button img { display: block; width: 100%; height: auto; aspect-ratio: 1672 / 941; object-fit: contain; }
    .image-caption { display: flex; justify-content: space-between; gap: 12px; padding: 10px 13px; border-top: 1px solid var(--line); color: #23426f; font-size: 12px; }
    .image-caption a { font-weight: 800; }
    .reading-panel { border: 1px solid var(--line); border-radius: 17px; background: var(--paper); padding: clamp(18px, 2vw, 26px); }
    .reading-panel h2 { margin-bottom: 9px; font-size: 25px; }
    .prompt { color: var(--blue); font-weight: 850; }
    .guide-list { padding-left: 1.15em; color: var(--muted); }
    .guide-list li + li { margin-top: 8px; }
    .callout-danger { margin-top: 19px; padding: 13px; border: 1px solid color-mix(in srgb, var(--red) 56%, var(--line)); border-radius: 12px; background: var(--red-bg); color: var(--ink); font-size: 14px; }
    .callout-danger strong { color: var(--red); }
    .stage-section { margin-top: 22px; border-top: 1px solid var(--line); padding-top: 18px; }
    .stage-list { display: grid; gap: 9px; }
    .stage { display: grid; grid-template-columns: 28px 1fr; column-gap: 10px; align-items: start; padding: 10px 0; border-bottom: 1px solid color-mix(in srgb, var(--line) 58%, transparent); }
    .stage:last-child { border-bottom: 0; }
    .stage-index { display: grid; place-items: center; width: 25px; height: 25px; border-radius: 50%; background: var(--blue-2); color: var(--blue); font-size: 12px; font-weight: 900; }
    .stage strong { color: var(--ink-strong); }
    .stage p { grid-column: 2; margin: 2px 0 0; color: var(--muted); font-size: 13px; }
    .lesson-lower { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 20px; margin-top: 21px; }
    .panel { border: 1px solid var(--line); border-radius: 17px; background: var(--paper); padding: clamp(18px, 2.2vw, 27px); }
    .panel h2 { margin-bottom: 10px; font-size: 25px; }
    .checklist { display: grid; gap: 9px; margin: 0; padding: 0; list-style: none; }
    .checklist li { display: grid; grid-template-columns: 21px 1fr; gap: 8px; color: var(--muted); font-size: 14px; }
    .checklist li::before { content: "✓"; display: grid; place-items: center; height: 21px; border-radius: 50%; background: var(--green-bg); color: var(--green); font-weight: 900; }
    .lesson-footer { display: flex; justify-content: space-between; gap: 12px; margin-top: 22px; }
    .lesson-footer .button { max-width: 42%; text-align: left; }
    .related { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }
    .related .button { font-size: 13px; }
    .lesson-path { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; margin: 16px 0 12px; }
    .lesson-path button { display: flex; align-items: center; gap: 8px; min-height: 42px; border: 1px solid var(--line); border-radius: 12px; background: var(--paper); color: var(--ink); padding: 7px 10px; text-align: left; }
    .lesson-path button:hover { border-color: var(--blue); background: var(--blue-2); }
    .lesson-path strong { display: grid; place-items: center; flex: 0 0 25px; width: 25px; height: 25px; border-radius: 50%; background: var(--blue-2); color: var(--blue); font-size: 12px; }
    .lesson-path span { font-size: 12px; font-weight: 850; line-height: 1.2; }
    .lesson-hint { margin: 0 0 20px; color: var(--muted); font-size: 13px; }
    .teaching-primer, .teaching-synthesis { margin: 22px 0 30px; border: 1px solid color-mix(in srgb, var(--cyan) 52%, var(--line)); border-radius: 20px; background: linear-gradient(145deg, color-mix(in srgb, var(--cyan-bg) 36%, var(--paper)), var(--paper) 56%); padding: clamp(20px, 3vw, 34px); box-shadow: 0 8px 26px rgba(23,105,224,.08); }
    .teaching-synthesis { margin-top: clamp(42px, 6vw, 72px); border-color: var(--line); background: var(--paper); }
    .teaching-primer-heading { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 13px; align-items: start; margin-bottom: 18px; }
    .teaching-primer-heading .step-badge { background: var(--cyan); box-shadow: none; }
    .teaching-primer-heading h2, .teaching-synthesis h2 { margin: 2px 0 6px; font-size: clamp(25px, 3.2vw, 38px); }
    .teaching-primer-heading p:last-child { margin: 0; color: var(--muted); font-size: 16px; }
    .primer-summary { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 11px; }
    .primer-card { min-height: 135px; border: 1px solid var(--line); border-radius: 15px; background: var(--paper); padding: 16px; }
    .primer-card strong, .micro-example strong, .mental-model strong { display: block; margin-bottom: 6px; color: var(--blue); font-size: 14px; }
    .primer-card p, .micro-example p, .mental-model p { margin: 0; color: var(--ink-strong); line-height: 1.68; }
    .micro-example { margin-top: 14px; border: 1px solid color-mix(in srgb, var(--orange) 52%, var(--line)); border-radius: 16px; background: color-mix(in srgb, var(--orange-bg) 48%, var(--paper)); padding: 17px; }
    .micro-example h3, .mental-model h3, .causal-chain h3, .teaching-synthesis h3 { margin-bottom: 8px; font-size: 20px; }
    .micro-example .prediction { margin-top: 11px; padding: 10px 12px; border-left: 4px solid var(--orange); background: var(--paper); color: var(--ink-strong); font-weight: 750; }
    .micro-example details { margin-top: 11px; border-top: 1px solid color-mix(in srgb, var(--orange) 34%, var(--line)); padding-top: 10px; }
    .micro-example summary, .teach-back summary, .transfer-check summary { cursor: pointer; color: var(--blue); font-weight: 850; }
    .concept-visuals { display: grid; gap: 18px; margin: 22px 0; }
    .concept-visual { border: 1px solid color-mix(in srgb, var(--cyan) 42%, var(--line)); border-radius: 17px; background: var(--paper); overflow: hidden; }
    .concept-visual-heading { padding: 18px 18px 0; }
    .concept-visual-heading h3 { margin: 4px 0 6px; color: var(--ink-strong); font-size: clamp(21px, 2.7vw, 30px); }
    .concept-visual-prompt { margin: 0; color: var(--blue); font-weight: 780; line-height: 1.62; }
    .concept-figure { margin: 15px 18px 0; overflow: hidden; border: 1px solid var(--line); border-radius: 13px; background: #fff; }
    .concept-image-link { display: block; background: #fff; }
    .concept-image-link img, .concept-image-link .concept-svg-object { display: block; width: 100%; height: auto; aspect-ratio: 1672 / 941; object-fit: contain; }
    /* An SVG used as an <img> cannot reliably load its own photographic
       workpiece on local/offline Chromium.  <object> preserves the SVG's
       document base and lets the shared raster anchor render.  It remains a
       non-interactive visual inside the enclosing accessible image link. */
    .concept-svg-object { border: 0; background: #fff; pointer-events: none; }
    /* An image-led first read deliberately gives one teaching visual the whole
       content width.  It is not the compact paragraph-SVG treatment. */
    .beginner-path { margin: 25px 0 22px; }
    .beginner-path-heading { margin: 0 0 16px; }
    .beginner-path-heading h3 { margin: 4px 0 7px; color: var(--ink-strong); font-size: clamp(24px, 3vw, 34px); }
    .beginner-path-heading p:last-child { margin: 0; color: var(--muted); font-size: 16px; line-height: 1.68; }
    .beginner-visuals { display: grid; gap: clamp(26px, 4vw, 44px); }
    .beginner-visual { border-color: color-mix(in srgb, var(--blue) 46%, var(--line)); box-shadow: 0 8px 22px rgba(23,105,224,.08); }
    .beginner-visual .concept-visual-heading { padding: clamp(20px, 3vw, 30px) clamp(20px, 3vw, 34px) 0; }
    .core-ideas { padding: 18px 22px; margin: 14px 0; background: var(--paper); border-left: 4px solid var(--blue); line-height: 1.85; }
    .core-ideas h4 { margin: 8px 0; }
    .core-ideas li { margin-bottom: 14px; }
    .beginner-visual .concept-figure { margin: 18px clamp(14px, 2.5vw, 28px) 0; }
    .beginner-visual .concept-caption { font-size: 16px; line-height: 1.72; }
    .beginner-visual .concept-callouts { margin: 18px clamp(14px, 2.5vw, 28px) clamp(18px, 2.5vw, 28px); }
    /* The first-read image may scale down on a phone.  Keep the explanatory
       text outside the bitmap at normal reading size instead of asking a
       learner to decipher microscopic labels embedded in the image. */
    .beginner-visual .concept-callouts strong { font-size: 16px; }
    .beginner-visual .concept-callouts p { font-size: 15px; line-height: 1.62; }
    .mobile-image-hint { display: none; }
    .beginner-engineering-reference { margin-top: 22px; border: 1px solid var(--line); border-radius: 15px; background: color-mix(in srgb, var(--blue-2) 24%, var(--paper)); }
    .beginner-engineering-reference > summary { cursor: pointer; padding: 15px 17px; color: var(--blue); font-weight: 850; }
    .beginner-engineering-reference-body { padding: 0 17px 17px; }
    .concept-caption { margin: 0; padding: 12px 18px 0; color: var(--ink-strong); line-height: 1.7; }
    .concept-enlarge { margin-top: 9px; font-size: 13px; }
    .concept-callouts { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 9px; margin: 14px 18px 18px; padding: 0; list-style: none; }
    .concept-callouts li { min-width: 0; padding: 12px; border-left: 3px solid var(--cyan); border-radius: 0 11px 11px 0; background: color-mix(in srgb, var(--cyan-bg) 42%, var(--paper)); }
    .concept-callouts strong { display: block; color: var(--blue); font-size: 14px; }
    .concept-callouts p { margin: 4px 0 0; color: var(--muted); font-size: 13px; line-height: 1.55; }
    /* Model names and technical contracts routinely contain long English
       tokens.  Lesson prose must wrap rather than create a horizontal page
       scroll on a phone. */
    .teaching-primer, .teaching-primer-heading > div, .primer-card, .micro-example, .mental-model, .causal-chain, .causal-step, .causal-step-copy, .inline-explainer, .concept-visual, .concept-callouts li, .beginner-path, .beginner-engineering-reference { min-width: 0; }
    .teaching-primer h2, .teaching-primer h3, .teaching-primer h4, .teaching-primer p, .concept-visual h3, .concept-visual p, .concept-callouts p, .beginner-path h3, .beginner-path p { overflow-wrap: anywhere; }
    .concept-compare { margin-top: 19px; border: 1px solid var(--line); border-radius: 14px; background: color-mix(in srgb, var(--blue-2) 29%, var(--paper)); }
    .concept-compare > summary { cursor: pointer; padding: 14px 16px; color: var(--blue); font-weight: 850; }
    .concept-compare .concept-visuals { margin: 0; padding: 0 14px 14px; }
    .concept-compare .concept-visual { background: var(--paper); }
    .mental-model { margin-top: 14px; border: 1px solid color-mix(in srgb, var(--green) 48%, var(--line)); border-radius: 16px; background: color-mix(in srgb, var(--green-bg) 52%, var(--paper)); padding: 17px; }
    .mental-model .limit { margin-top: 10px; border-left: 4px solid var(--green); padding-left: 10px; color: var(--ink-strong); font-size: 14px; }
    .causal-chain { margin-top: 22px; }
    .causal-chain > p, .reference-intro, .synthesis-lead { margin: 0; color: var(--muted); line-height: 1.65; }
    /* A technical Blog unit: one claim, then its own visible relationship.
       The old four-column summary used only text cards; this is deliberately
       a readable paragraph → figure pairing on desktop and mobile. */
    .causal-grid { display: grid; grid-template-columns: 1fr; gap: 15px; margin-top: 13px; }
    .causal-step { display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, .9fr); gap: clamp(15px, 2.4vw, 28px); align-items: center; border: 1px solid var(--line); border-radius: 17px; background: var(--paper); padding: clamp(16px, 2.2vw, 23px); }
    .causal-step-copy { min-width: 0; }
    .causal-step-number { display: grid; place-items: center; width: 29px; height: 29px; margin-bottom: 10px; border-radius: 50%; background: var(--blue); color: #fff; font-size: 13px; font-weight: 900; }
    .causal-step h4 { margin: 0 0 8px; color: var(--ink-strong); font-size: clamp(18px, 2vw, 23px); }
    .causal-step p { margin: 0; color: var(--muted); font-size: 15px; line-height: 1.7; }
    .causal-step .because { margin-top: 10px; color: var(--ink-strong); }
    .causal-step .anchor { margin-top: 11px; color: var(--blue); font-size: 13px; font-weight: 800; }
    .inline-explainer { margin: 0; border: 1px solid color-mix(in srgb, var(--cyan) 48%, var(--line)); border-radius: 14px; overflow: hidden; background: #f5f8fe; }
    .inline-explainer img, .inline-explainer .concept-svg-object { display: block; width: 100%; height: auto; aspect-ratio: 2 / 1; object-fit: contain; }
    .causal-step-wide { grid-template-columns: 1fr; }
    .causal-step-wide .inline-explainer img { aspect-ratio: 16 / 9; object-fit: contain; background: #fff; }
    .causal-step-text { grid-template-columns: 1fr; }
    .inline-explainer figcaption { padding: 9px 11px; border-top: 1px solid var(--line); color: var(--ink-strong); font-size: 13px; font-weight: 750; line-height: 1.55; background: var(--paper); }
    .inline-explainer .not-claim { display: block; margin-top: 3px; color: #8A5600; font-size: 12px; font-weight: 650; }
    .reference-intro { margin: 0 0 16px; padding: 11px 14px; border-left: 4px solid var(--cyan); background: color-mix(in srgb, var(--cyan-bg) 39%, var(--paper)); color: var(--ink-strong); }
    .formal-slide-reference { margin: 26px 0 0; border: 1px solid var(--line); border-radius: 17px; background: var(--paper); overflow: hidden; }
    .formal-slide-reference > summary { cursor: pointer; padding: 17px 20px; color: var(--ink-strong); font-weight: 850; background: color-mix(in srgb, var(--blue-2) 30%, var(--paper)); }
    .formal-slide-reference > summary span { display: block; margin-top: 5px; color: var(--muted); font-size: 14px; font-weight: 600; line-height: 1.5; }
    .formal-slide-reference-body { padding: 18px; }
    .formal-slide-reference .lesson-path { margin-top: 0; }
    .synthesis-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 11px; margin-top: 15px; }
    .boundary-card { min-height: 205px; border: 1px solid color-mix(in srgb, var(--orange) 45%, var(--line)); border-radius: 15px; background: color-mix(in srgb, var(--orange-bg) 34%, var(--paper)); padding: 15px; }
    .boundary-card h4 { margin: 0 0 8px; color: var(--ink-strong); font-size: 16px; }
    .boundary-card p { margin: 7px 0 0; color: var(--muted); font-size: 13px; line-height: 1.58; }
    .boundary-card strong { color: var(--orange); }
    .teaching-comparison { width: 100%; margin-top: 15px; border-collapse: collapse; border: 1px solid var(--line); border-radius: 14px; overflow: hidden; }
    .teaching-comparison th, .teaching-comparison td { border-bottom: 1px solid color-mix(in srgb, var(--line) 65%, transparent); padding: 12px; text-align: left; vertical-align: top; }
    .teaching-comparison th { background: var(--blue-2); color: var(--ink-strong); font-size: 13px; }
    .teaching-comparison td { color: var(--muted); font-size: 13px; line-height: 1.55; }
    .teaching-comparison td:first-child { color: var(--ink-strong); font-weight: 850; }
    .selection-note { margin: 12px 0 0; padding: 12px 14px; border-left: 4px solid var(--blue); background: var(--blue-2); color: var(--ink-strong); line-height: 1.65; }
    .pilot-poc { margin-top: 20px; border: 1px solid color-mix(in srgb, var(--green) 48%, var(--line)); border-radius: 16px; background: color-mix(in srgb, var(--green-bg) 38%, var(--paper)); padding: 18px; }
    .pilot-poc ol { margin: 10px 0 0; padding-left: 1.3em; color: var(--ink-strong); }
    .pilot-poc li + li { margin-top: 8px; }
    .pilot-poc .hold-note { margin: 13px 0 0; padding: 10px 12px; border-left: 4px solid var(--red); background: var(--red-bg); color: var(--ink-strong); line-height: 1.6; }
    .teach-back, .transfer-check { margin-top: 15px; border: 1px solid color-mix(in srgb, var(--cyan) 50%, var(--line)); border-radius: 16px; background: color-mix(in srgb, var(--cyan-bg) 34%, var(--paper)); padding: 17px; }
    .teach-back p, .transfer-check p { margin: 7px 0 0; color: var(--ink-strong); line-height: 1.65; }
    .teach-back details, .transfer-check details { margin-top: 12px; border-top: 1px solid color-mix(in srgb, var(--cyan) 42%, var(--line)); padding-top: 10px; }
    .transfer-check { border-color: color-mix(in srgb, var(--orange) 50%, var(--line)); background: color-mix(in srgb, var(--orange-bg) 46%, var(--paper)); }
    .poc-acceptance { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; margin-top: 14px; }
    .poc-acceptance > div { border: 1px solid color-mix(in srgb, var(--line) 72%, transparent); border-radius: 12px; background: color-mix(in srgb, var(--paper) 86%, var(--blue-2)); padding: 11px; }
    .poc-acceptance strong { display: block; color: var(--ink-strong); font-size: 13px; }
    .poc-acceptance p { margin: 4px 0 0; color: var(--muted); font-size: 13px; }
    .lesson-step { scroll-margin-top: 94px; margin-top: clamp(42px, 6vw, 74px); padding-top: clamp(24px, 3vw, 40px); border-top: 1px solid var(--line); }
    .lesson-step.first { margin-top: 0; padding-top: 0; border-top: 0; }
    .lesson-step-heading { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 13px; align-items: start; margin-bottom: 14px; }
    .teaching-figure + .lesson-step-heading { margin-top: 20px; }
    .step-badge { display: grid; place-items: center; width: 48px; height: 48px; border-radius: 14px; background: var(--blue); color: #fff; font-size: 15px; font-weight: 900; box-shadow: 0 6px 16px rgba(23,105,224,.22); }
    .lesson-step-heading h2 { margin: 1px 0 5px; font-size: clamp(24px, 3.1vw, 36px); }
    .lesson-step-heading .prompt { margin: 0; }

    .engineering-media { display: block; width: 100%; }
    .image-button .engineering-media img { aspect-ratio: auto; height: auto; }
    .lightbox-image-wrap.engineering-zoom { display: block; touch-action: pan-x pan-y pinch-zoom; }
    .engineering-zoom .engineering-media { width: 1672px; max-width: none; }
    .engineering-zoom .engineering-media img { display: block; width: 100%; height: auto; max-width: none; max-height: none; }
    @media (max-width: 760px) { .engineering-zoom .engineering-media { width: 768px; } }
    .teaching-figure { width: 100%; margin: 0; }
    .teaching-figure .image-button { cursor: zoom-in; }
    .plain-reading { margin-top: 16px; border: 1px solid color-mix(in srgb, var(--cyan) 55%, var(--line)); border-radius: 16px; background: color-mix(in srgb, var(--cyan-bg) 36%, var(--paper)); padding: clamp(16px, 2vw, 24px); }
    .plain-reading h3 { margin-bottom: 11px; font-size: clamp(20px, 2.3vw, 27px); }
    .plain-reading-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; }
    .plain-reading-grid div { min-height: 94px; border: 1px solid var(--line); border-radius: 12px; background: var(--paper); padding: 12px; }
    .plain-reading-grid strong { display: block; margin-bottom: 5px; color: var(--blue); font-size: 13px; }
    .plain-reading-grid p { margin: 0; color: var(--ink-strong); font-size: 14px; line-height: 1.6; }
    .term-strip { display: flex; flex-wrap: wrap; gap: 7px; margin-top: 12px; }
    .term-strip span { border: 1px solid color-mix(in srgb, var(--cyan) 55%, var(--line)); border-radius: 999px; background: var(--paper); color: var(--ink-strong); padding: 5px 9px; font-size: 12px; font-weight: 750; }
    .technical-details { margin-top: 14px; border: 1px solid var(--line); border-radius: 16px; background: var(--paper); overflow: clip; }
    .technical-details summary { cursor: pointer; padding: 14px 17px; color: var(--blue); font-weight: 900; }
    .technical-details[open] summary { border-bottom: 1px solid var(--line); background: var(--blue-2); }
    .technical-details .diagram-reading { padding: 16px; margin-top: 0; }
    .diagram-reading { display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(300px, .9fr); gap: 16px; margin-top: 16px; }
    .diagram-summary, .diagram-stages { border: 1px solid var(--line); border-radius: 16px; background: var(--paper); padding: clamp(17px, 2vw, 25px); }
    .diagram-summary h3, .diagram-stages h3 { margin-bottom: 8px; font-size: 18px; }
    .diagram-summary .guide-list { margin-bottom: 0; }
    .diagram-stages .stage-list { margin-top: 10px; }
    .engineering-takeaway { display: grid; grid-template-columns: 1.05fr 1fr 1fr; gap: 10px; margin-top: 15px; padding: 15px; border: 1px solid var(--line); border-radius: 16px; background: color-mix(in srgb, var(--blue-2) 36%, var(--paper)); }
    .engineering-takeaway-heading { grid-column: 1 / -1; margin: 0; color: var(--ink-strong); font-size: 15px; font-weight: 900; }
    .takeaway-card { min-height: 112px; border: 1px solid var(--line); border-radius: 12px; background: var(--paper); padding: 13px; }
    .takeaway-card strong { display: block; margin-bottom: 5px; color: var(--blue); font-size: 13px; }
    .takeaway-card p { margin: 0; color: var(--muted); font-size: 14px; }
    .takeaway-card.safe strong { color: var(--green); }
    .takeaway-card.risk { border-color: color-mix(in srgb, var(--red) 55%, var(--line)); background: var(--red-bg); }
    .takeaway-card.risk strong { color: var(--red); }
    .engineer-handoff { margin-top: clamp(40px, 6vw, 74px); border: 1px solid var(--line); border-radius: 20px; background: var(--paper); padding: clamp(22px, 3.2vw, 38px); box-shadow: var(--shadow); }
    .engineer-handoff h2 { margin-bottom: 10px; }
    .operations-grid { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 10px; margin-top: 19px; }
    .operation-card { min-height: 178px; border: 1px solid var(--line); border-radius: 14px; background: var(--paper); padding: 14px; }
    .operation-card .operation-number { display: grid; place-items: center; width: 27px; height: 27px; margin-bottom: 9px; border-radius: 50%; background: var(--blue-2); color: var(--blue); font-size: 12px; font-weight: 900; }
    .operation-card h3 { margin-bottom: 6px; font-size: 16px; }
    .operation-card p { margin: 0; color: var(--muted); font-size: 13px; }
    .operation-card.warning { border-color: color-mix(in srgb, var(--red) 55%, var(--line)); background: var(--red-bg); }
    .operation-card.warning .operation-number { background: color-mix(in srgb, var(--red) 14%, var(--paper)); color: var(--red); }
    .operation-card.warning h3 { color: var(--red); }
    .supporting-hero { margin-bottom: 26px; }
    .supporting-hero h1 { max-width: 1000px; }
    .supporting-journey { margin: 22px 0 16px; overflow: hidden; border: 1px solid var(--line); border-radius: 18px; background: var(--paper); box-shadow: var(--shadow); }
    .supporting-journey a { display: block; line-height: 0; }
    .supporting-journey img { display: block; width: 100%; height: auto; }
    .supporting-journey figcaption { display: grid; grid-template-columns: minmax(180px, .7fr) minmax(0, 2.3fr); gap: 16px; padding: 13px 18px 15px; border-top: 1px solid var(--line); color: var(--muted); font-size: 15px; line-height: 1.58; }
    .supporting-journey figcaption strong { color: var(--ink-strong); }
    .supporting-intro { max-width: 900px; color: var(--muted); font-size: 18px; }
    .supporting-path { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 17px; }
    .supporting-path button { border: 1px solid var(--line); border-radius: 999px; background: var(--paper); color: var(--ink); padding: 7px 11px; font-size: 12px; font-weight: 800; }
    .supporting-path button:hover { border-color: var(--blue); background: var(--blue-2); }
    .learning-modules { display: grid; gap: 13px; margin-top: 24px; }
    .learning-module { border: 1px solid var(--line); border-radius: 18px; background: var(--paper); overflow: clip; }
    .learning-module summary { display: grid; grid-template-columns: auto minmax(0, 1fr) auto; align-items: center; gap: 12px; cursor: pointer; padding: 16px 18px; }
    .learning-module summary::marker { color: var(--blue); }
    .learning-module-index { display: grid; place-items: center; width: 30px; height: 30px; border-radius: 50%; background: var(--blue-2); color: var(--blue); font-size: 12px; font-weight: 900; }
    .learning-module summary strong { display: block; color: var(--ink-strong); }
    .learning-module summary span:not(.learning-module-index):not(.learning-module-count) { display: block; margin-top: 3px; color: var(--muted); font-size: 13px; font-weight: 400; }
    .learning-module-count { border-radius: 999px; background: var(--green-bg); color: var(--green); padding: 4px 8px; font-size: 12px; font-weight: 850; }
    .learning-module[open] summary { border-bottom: 1px solid var(--line); background: var(--blue-2); }
    .learning-module-content { padding: 0 18px 20px; }
    .supporting-story { scroll-margin-top: 94px; margin-top: 42px; padding-top: 28px; border-top: 1px solid var(--line); }
    .supporting-story:first-of-type { margin-top: 24px; }
    .supporting-story h2 { margin-bottom: 7px; }
    .supporting-story > p { color: var(--muted); }
    .supporting-figure { margin: 15px 0 0; }
    .supporting-figure.image-led-story { border-color: color-mix(in srgb, var(--cyan) 42%, var(--line)); }
    .supporting-figure.image-led-story .image-caption { background: color-mix(in srgb, var(--cyan-bg) 36%, var(--paper)); font-size: 13px; }
    .supporting-figure.image-led-story .image-caption span { font-weight: 750; }
    .supporting-engineering-reference { margin: 13px 0 0; border: 1px solid var(--line); border-radius: 14px; background: var(--paper); overflow: clip; }
    .supporting-engineering-reference summary { cursor: pointer; padding: 12px 14px; color: var(--muted); font-size: 14px; font-weight: 850; }
    .supporting-engineering-reference[open] summary { border-bottom: 1px solid var(--line); background: var(--blue-2); color: var(--blue); }
    .supporting-engineering-reference p { margin: 0; padding: 11px 14px 0; color: var(--muted); font-size: 14px; line-height: 1.6; }
    .supporting-engineering-reference a { display: block; margin-top: 12px; overflow: hidden; border-top: 1px solid var(--line); background: #fff; }
    .supporting-engineering-reference img { display: block; width: 100%; height: auto; }
    .family-overview { margin: 0 0 24px; border: 1px solid var(--line); border-radius: 18px; background: var(--paper); padding: clamp(20px, 3vw, 32px); }
    .family-overview h2 { margin-bottom: 9px; }
    .family-overview p { max-width: 920px; color: var(--muted); }
    .family-contract { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; margin-top: 18px; }
    .family-contract > div { border: 1px solid var(--line); border-radius: 12px; background: var(--blue-2); padding: 13px; }
    .family-contract strong { display: block; margin-bottom: 4px; color: var(--ink-strong); font-size: 13px; }
    .family-contract span { color: var(--muted); font-size: 13px; }
    .family-support { margin-top: 28px; }
    .family-support summary { cursor: pointer; color: var(--blue); font-weight: 900; }
    /* Shared diagrams are teaching pages, not thumbnail-gallery cards.  Keep one
       full visual story at a time so the labels inside a 1672×941 canvas remain
       large enough to read. */
    .family-support-stories { display: grid; grid-template-columns: 1fr; gap: 28px; margin-top: 19px; }
    .family-support-story { overflow: hidden; border: 1px solid var(--line); border-radius: 18px; background: var(--paper); box-shadow: 0 10px 28px rgba(27, 73, 128, .06); }
    .family-support-story figure { margin: 0; }
    .family-support-visual { display: block; overflow: hidden; background: #fff; }
    .family-support-visual img { display: block; width: 100%; height: auto; aspect-ratio: 1672 / 941; object-fit: contain; background: #fff; }
    .family-support-story figcaption { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 16px; align-items: start; padding: 17px 19px 19px; border-top: 1px solid var(--line); }
    .family-support-story h3 { margin: 0 0 5px; font-size: 20px; color: var(--ink-strong); }
    .family-support-story p { margin: 0; max-width: 820px; color: var(--muted); font-size: 15px; line-height: 1.7; }
    .family-support-story .button { align-self: center; white-space: nowrap; }
    .family-support-mobile-hint { display: none; }
    .family-engineering-reference { margin: 0 19px 19px; padding-top: 15px; border-top: 1px dashed var(--line); }
    .family-engineering-reference summary { cursor: pointer; color: var(--muted); font-size: 14px; font-weight: 850; }
    .family-engineering-reference p { margin: 9px 0 12px; max-width: 920px; color: var(--muted); font-size: 14px; line-height: 1.6; }
    .family-engineering-reference-visual { display: block; overflow: hidden; border: 1px solid var(--line); border-radius: 12px; background: #fff; }
    .family-engineering-reference-visual img { display: block; width: 100%; height: auto; }
    .comparison-wrap { overflow-x: auto; margin-top: 18px; border: 1px solid var(--line); border-radius: 14px; background: var(--paper); }
    .comparison-table { width: 100%; min-width: 760px; border-collapse: collapse; }
    .comparison-table th, .comparison-table td { border-bottom: 1px solid color-mix(in srgb, var(--line) 62%, transparent); padding: 12px; text-align: left; vertical-align: top; }
    .comparison-table th { background: var(--blue-2); color: var(--ink-strong); font-size: 13px; }
    .comparison-table td { color: var(--muted); font-size: 13px; }
    .comparison-table td:first-child { color: var(--ink-strong); font-weight: 900; }
    .foundation-flow { display: grid; grid-template-columns: repeat(6, minmax(120px, 1fr)); gap: 9px; margin: 22px 0; }
    .foundation-flow div { position: relative; min-height: 114px; border: 1px solid var(--line); border-radius: 14px; background: var(--paper); padding: 14px; }
    .foundation-flow div:not(:last-child)::after { content: "→"; position: absolute; z-index: 1; right: -17px; top: 44px; color: var(--blue); font-size: 20px; font-weight: 900; }
    .foundation-flow strong { display: block; margin-bottom: 5px; color: var(--ink-strong); font-size: 14px; }
    .foundation-flow span { color: var(--muted); font-size: 12px; }
    .glossary-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px; margin-top: 20px; }
    .glossary-card { min-height: 142px; border: 1px solid var(--line); border-radius: 14px; background: var(--paper); padding: 15px; }
    .glossary-card h3 { margin-bottom: 6px; font-size: 17px; }
    .glossary-card p { margin: 0; color: var(--muted); font-size: 13px; }
    .glossary-card .glossary-example { display: block; margin-top: 9px; color: var(--blue); font-size: 12px; font-weight: 750; }
    .library-controls { display: grid; grid-template-columns: minmax(190px, 1fr) minmax(200px, .6fr); gap: 12px; margin-bottom: 18px; }
    .field label { display: block; margin-bottom: 5px; color: var(--muted); font-size: 12px; font-weight: 850; }
    .field input, .field select, .field textarea { width: 100%; border: 1px solid var(--line); border-radius: 11px; background: var(--paper); color: var(--ink); padding: 10px 12px; }
    .field textarea { min-height: 110px; resize: vertical; }
    .topic-card { min-height: 225px; }
    .topic-card .card-top { display: flex; justify-content: space-between; width: 100%; gap: 10px; }
    .topic-card h3 { margin: 8px 0; }
    .topic-card .card-meta { display: flex; align-items: center; gap: 6px; color: var(--muted); font-size: 12px; }
    .topic-card .status-dot { width: 9px; height: 9px; border-radius: 99px; border: 1px solid var(--line); }
    .topic-card .status-dot.done { background: var(--green); border-color: var(--green); }
    .empty { padding: 40px; border: 1px dashed var(--line); border-radius: 16px; background: var(--paper); color: var(--muted); text-align: center; }
    .poc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
    .poc-grid .wide { grid-column: 1 / -1; }
    .poc-intro { max-width: 850px; color: var(--muted); }
    .poc-steps { display: grid; gap: 16px; }
    .poc-step { border: 1px solid var(--line); border-radius: 16px; background: var(--paper); padding: clamp(16px, 2.3vw, 24px); }
    .poc-step-heading { display: flex; align-items: start; gap: 10px; margin-bottom: 15px; }
    .poc-step-heading span { display: grid; place-items: center; flex: 0 0 30px; width: 30px; height: 30px; border-radius: 50%; background: var(--blue); color: #fff; font-size: 12px; font-weight: 900; }
    .poc-step-heading h2 { margin: 0 0 3px; font-size: 20px; }
    .poc-step-heading p { margin: 0; color: var(--muted); font-size: 13px; }
    .poc-status { margin: 14px 0; color: var(--green); font-size: 13px; font-weight: 800; }
    .poc-actions { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 20px; }
    dialog { width: min(1400px, calc(100vw - 28px)); max-width: 1400px; max-height: calc(100vh - 28px); border: 0; border-radius: 16px; padding: 0; background: var(--paper); color: var(--ink); box-shadow: 0 28px 90px rgba(0,0,0,.5); }
    dialog::backdrop { background: rgba(2, 12, 31, .78); }
    .lightbox { display: grid; grid-template-rows: auto minmax(0, 1fr) auto; max-height: calc(100vh - 28px); }
    .lightbox-header, .lightbox-footer { display: flex; justify-content: space-between; align-items: center; gap: 12px; padding: 12px 15px; border-bottom: 1px solid var(--line); }
    .lightbox-footer { border-top: 1px solid var(--line); border-bottom: 0; }
    .lightbox-title { color: var(--ink-strong); font-weight: 850; }
    .lightbox-image-wrap { display: grid; place-items: center; min-height: 0; overflow: auto; padding: 12px; background: #eff5ff; }
    .lightbox-image-wrap img, .lightbox-image-wrap .concept-svg-object { width: auto; max-width: 100%; max-height: calc(100vh - 175px); object-fit: contain; box-shadow: 0 8px 24px rgba(0,0,0,.25); }
    .lightbox-image-wrap.concept-mode { display: block; place-items: start; touch-action: pan-x pan-y pinch-zoom; }
    .lightbox-image-wrap.concept-mode img, .lightbox-image-wrap.concept-mode .concept-svg-object { display: block; width: 1672px; height: 941px; max-width: none; max-height: none; }
    .toast { position: fixed; z-index: 100; right: 18px; bottom: 18px; max-width: min(380px, calc(100vw - 36px)); transform: translateY(20px); opacity: 0; pointer-events: none; border-radius: 12px; background: var(--ink-strong); color: #fff; padding: 12px 15px; box-shadow: var(--shadow); transition: opacity .18s, transform .18s; }
    .toast.show { transform: translateY(0); opacity: 1; }
    .mobile-nav { display: none; }
    .model-deep-dive { margin-top: 24px; }
    .deep-dive-hero { overflow: hidden; border: 1px solid color-mix(in srgb, var(--blue) 48%, var(--line)); border-radius: 22px; background: linear-gradient(135deg, var(--paper), color-mix(in srgb, var(--blue-2) 62%, var(--paper))); padding: clamp(22px, 3.5vw, 40px); box-shadow: var(--shadow); }
    .deep-dive-hero h2 { max-width: 950px; margin: 5px 0 9px; color: var(--ink-strong); font-size: clamp(29px, 4vw, 46px); line-height: 1.16; }
    .deep-dive-hero p:last-child { max-width: 980px; margin: 0; color: var(--muted); font-size: clamp(16px, 1.8vw, 19px); line-height: 1.72; }
    .deep-dive-nav { position: sticky; z-index: 12; top: 86px; display: grid; grid-template-columns: repeat(8, minmax(104px, 1fr)); gap: 7px; margin: 14px 0 0; overflow-x: auto; padding: 9px; border: 1px solid var(--line); border-radius: 15px; background: color-mix(in srgb, var(--paper) 95%, transparent); box-shadow: 0 8px 22px rgba(18,54,112,.09); backdrop-filter: blur(12px); }
    .deep-dive-nav button { min-width: 104px; border: 1px solid transparent; border-radius: 10px; background: transparent; color: var(--muted); padding: 8px 7px; font-size: 12px; font-weight: 850; line-height: 1.35; }
    .deep-dive-nav button:hover, .deep-dive-nav button.active { border-color: var(--blue); background: var(--blue-2); color: var(--blue); }
    .deep-dive-nav strong { display: block; margin-bottom: 2px; font-size: 11px; letter-spacing: .08em; }
    .deep-dive-chapters { display: grid; gap: clamp(34px, 5vw, 62px); margin-top: clamp(32px, 5vw, 58px); }
    .deep-dive-chapter { scroll-margin-top: 176px; min-width: 0; border-top: 1px solid var(--line); padding-top: clamp(25px, 3.5vw, 39px); }
    .deep-dive-chapter:first-child { border-top: 0; padding-top: 0; }
    .deep-dive-chapter-head { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 14px; align-items: start; margin-bottom: 18px; }
    .deep-dive-chapter-number { display: grid; place-items: center; width: 54px; height: 54px; border-radius: 16px; background: var(--ink-strong); color: #fff; font-size: 16px; font-weight: 900; box-shadow: 0 7px 18px rgba(7,26,59,.2); }
    .deep-dive-chapter h3 { margin: 0 0 7px; color: var(--ink-strong); font-size: clamp(25px, 3.1vw, 37px); line-height: 1.27; overflow-wrap: anywhere; }
    .deep-dive-summary { max-width: 1040px; margin: 0; color: var(--muted); font-size: 16px; line-height: 1.72; }
    .deep-dive-figure { overflow: hidden; margin: 0; border: 1px solid color-mix(in srgb, var(--blue) 42%, var(--line)); border-radius: 17px; background: #fff; box-shadow: 0 9px 26px rgba(23,105,224,.08); }
    .deep-dive-image-link { display: block; line-height: 0; }
    .deep-dive-mobile-steps { display: none; }
    .reading-view-buttons { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; }
    .reading-view-buttons button[aria-pressed="true"] { background: #123e70; color: #fff; }
    .reading-view-panel[hidden] { display: none; }
    .reading-view-mobile { display: none; }
    .full-mobile-reading { width: 100%; height: auto; }
    .beginner-visual > .reading-views { margin: 18px 20px; }
    @media (max-width: 720px) {
      .reading-view-panel .deep-dive-image-link { display: none; }
      .reading-view-mobile { display: block; width: 100%; height: auto; }
      .beginner-focused { margin-inline: -20px; }
      .beginner-focused > .reading-views { margin-inline: 0; }
      .beginner-focused .reading-view-buttons { padding-inline: 16px; }
    }
    @media (max-width: 720px) {
      .deep-dive-figure:has(.deep-dive-mobile-steps) > .deep-dive-image-link { display: none; }
      .deep-dive-mobile-steps { display: grid; gap: 18px; list-style: none; padding: 16px; margin: 0; }
      .deep-dive-mobile-steps li { min-width: 0; padding-bottom: 16px; border-bottom: 1px solid #cddae7; }
      .deep-dive-mobile-steps strong { display: block; color: #173a5e; font-size: 18px; }
      .deep-dive-mobile-steps p { color: #173a5e; font-size: 16px; line-height: 1.7; margin: 10px 0; }
      .deep-dive-mobile-steps svg { display: block; width: 100%; height: auto; background: #fcfcfa; }
    }
    .deep-dive-image-link img, .deep-dive-image-link .concept-svg-object { display: block; width: 100%; height: auto; aspect-ratio: 1672 / 941; object-fit: contain; }
    .deep-dive-figure figcaption { display: flex; justify-content: space-between; gap: 14px; align-items: center; padding: 11px 15px; border-top: 1px solid var(--line); color: var(--muted); font-size: 13px; line-height: 1.5; }
    .deep-dive-figure figcaption strong { color: var(--ink-strong); }
    .deep-dive-points { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; margin: 15px 0 0; padding: 0; list-style: none; counter-reset: deep-point; }
    .deep-dive-points li { min-width: 0; counter-increment: deep-point; border: 1px solid var(--line); border-radius: 13px; background: var(--paper); padding: 14px; color: var(--ink-strong); font-size: 14px; line-height: 1.65; overflow-wrap: anywhere; }
    .deep-dive-points li::before { content: counter(deep-point, decimal-leading-zero); display: block; margin-bottom: 7px; color: var(--blue); font-size: 12px; font-weight: 900; letter-spacing: .08em; }
    .deep-dive-meta { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-top: 13px; }
    .deep-dive-source { display: inline-flex; align-items: center; border: 1px solid color-mix(in srgb, var(--cyan) 52%, var(--line)); border-radius: 999px; background: color-mix(in srgb, var(--blue-2) 42%, var(--paper)); color: var(--blue); padding: 5px 9px; font-size: 12px; font-weight: 800; text-decoration: none; }
    .deep-dive-check { margin-top: 14px; border: 1px solid color-mix(in srgb, var(--orange) 48%, var(--line)); border-radius: 13px; background: color-mix(in srgb, var(--yellow) 42%, var(--paper)); }
    .deep-dive-check summary { cursor: pointer; padding: 13px 15px; color: var(--ink-strong); font-weight: 850; }
    .deep-dive-check p { margin: 0; border-top: 1px solid color-mix(in srgb, var(--orange) 34%, var(--line)); padding: 13px 15px; color: var(--muted); line-height: 1.65; }
    .deep-dive-next { margin: 15px 0 0; }
    .deep-dive-footer { margin-top: 44px; border: 1px solid var(--line); border-radius: 16px; background: color-mix(in srgb, var(--blue-2) 35%, var(--paper)); padding: 18px; }
    .deep-dive-footer h3 { margin: 0 0 7px; color: var(--ink-strong); }
    .deep-dive-footer p { margin: 0 0 12px; color: var(--muted); }
    @media (max-width: 1120px) {
      .app-shell { grid-template-columns: 250px minmax(0, 1fr); }
      .sidebar { padding-left: 9px; padding-right: 9px; }
      main { padding: 25px; }
      .viewer-grid { grid-template-columns: 1fr; }
      .reading-panel { max-width: 100%; }
      .learn-steps { grid-template-columns: repeat(2, minmax(0, 1fr)); }
      .hero-grid, .diagram-reading { grid-template-columns: 1fr; }
      .hero-preview { max-width: 860px; }
      .operations-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
      .deep-dive-nav { grid-template-columns: repeat(8, minmax(112px, 1fr)); }
      .foundation-flow { grid-template-columns: repeat(3, minmax(0, 1fr)); }
      .foundation-flow div::after { display: none; }
    }
    @media (max-width: 800px) {
      .topbar { grid-template-columns: auto minmax(0, 1fr) auto; gap: 9px; min-height: 67px; padding: 9px 13px; }
      .brand span:last-child { display: none; }
      .search-box kbd { display: none; }
      .top-actions .theme-text { display: none; }
      .mobile-nav { display: inline-grid; place-items: center; }
      .app-shell { display: block; }
      .sidebar { position: fixed; z-index: 25; top: 67px; bottom: 0; left: 0; width: min(330px, 88vw); height: auto; transform: translateX(-105%); box-shadow: var(--shadow); transition: transform .2s; }
      body.nav-open .sidebar { transform: translateX(0); }
      main { padding: 20px 14px 52px; }
      .hero { padding: 27px 21px; }
      .stats, .slide-tabs, .lesson-lower, .poc-grid, .poc-acceptance, .engineering-takeaway, .family-contract, .plain-reading-grid, .lesson-quickline, .primer-summary, .causal-grid, .synthesis-grid, .concept-callouts { grid-template-columns: 1fr; }
      .supporting-journey figcaption { grid-template-columns: 1fr; gap: 5px; }
      .family-support-story figcaption { grid-template-columns: 1fr; gap: 9px; padding: 14px; }
      .family-support-story .button { justify-self: start; }
      .family-support-visual { max-width: 100%; overflow-x: auto; overscroll-behavior-x: contain; touch-action: pan-x pan-y; }
      .family-support-visual img { width: 920px; max-width: none; }
      .family-engineering-reference { margin: 0 14px 14px; }
      .family-engineering-reference-visual { max-width: 100%; overflow-x: auto; overscroll-behavior-x: contain; touch-action: pan-x pan-y; }
      .family-engineering-reference-visual img { width: 920px; max-width: none; }
      .learning-module, .learning-module-content, .supporting-story, .supporting-figure.image-led-story { min-width: 0; max-width: 100%; }
      .supporting-figure.image-led-story { margin-left: 0; margin-right: 0; }
      .supporting-figure.image-led-story .image-button { width: 100%; min-width: 0; max-width: 100%; overflow-x: auto; overscroll-behavior-x: contain; touch-action: pan-x pan-y; }
      .supporting-figure.image-led-story .image-button img { width: 920px; max-width: none; }
      .supporting-engineering-reference a { max-width: 100%; overflow-x: auto; overscroll-behavior-x: contain; touch-action: pan-x pan-y; }
      .supporting-engineering-reference img { width: 920px; max-width: none; }
      .family-support-mobile-hint { display: block; margin: 11px 14px 0; color: var(--muted); font-size: 13px; line-height: 1.5; }
      .causal-step { grid-template-columns: 1fr; gap: 13px; }
      .lesson-head { grid-template-columns: 1fr; }
      .lesson-actions { flex-direction: row; }
      .lesson-path { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 7px; min-width: 0; max-width: 100%; margin: 14px 0 10px; }
      .lesson-path button { min-width: 0; min-height: 39px; padding: 6px 9px; overflow-wrap: anywhere; }
      .slide-tabs { gap: 6px; }
      .slide-tab { min-height: 51px; }
      .slide-tab span { font-size: 11px; }
      .library-controls { grid-template-columns: 1fr; }
      .learn-steps { grid-template-columns: 1fr; }
      .lesson-footer .button { max-width: 48%; }
      .image-caption { display: block; }
      .image-caption a { display: inline-block; margin-top: 4px; }
      .operations-grid { grid-template-columns: 1fr; }
      .foundation-flow { grid-template-columns: 1fr; }
      .foundation-flow div { min-height: 0; }
      .lesson-step { margin-top: 42px; }
      /* Full-width engineering illustrations retain readable internal labels
         when a phone offers a deliberate horizontal pan instead of shrinking
         a 1672px canvas into an unreadable postcard.  Captions/callouts stay
         visible below as the accessible text equivalent. */
      .beginner-visual .concept-figure { overflow: visible; }
      .beginner-visual .concept-image-link { display: block; max-width: 100%; overflow-x: auto; overscroll-behavior-x: contain; border-radius: 12px 12px 0 0; touch-action: pan-x pan-y; }
      .beginner-visual .concept-image-link img, .beginner-visual .concept-image-link .concept-svg-object { width: 920px; max-width: none; }
      .beginner-visual .mobile-image-hint { display: block; margin: 8px 18px 0; color: var(--muted); font-size: 13px; line-height: 1.5; }
      .teaching-comparison, .teaching-comparison tbody, .teaching-comparison tr, .teaching-comparison td { display: block; width: 100%; }
      .teaching-comparison { border: 0; }
      .teaching-comparison thead { display: none; }
      .teaching-comparison tr { margin: 10px 0; border: 1px solid var(--line); border-radius: 12px; overflow: hidden; }
      .teaching-comparison td { min-width: 0; padding: 10px 12px; overflow-wrap: anywhere; }
      .teaching-comparison td::before { content: attr(data-label); display: block; margin-bottom: 3px; color: var(--blue); font-size: 12px; font-weight: 900; }
      .boundary-card, .takeaway-card { min-width: 0; overflow-wrap: anywhere; }
      .boundary-card h4, .takeaway-card p { overflow-wrap: anywhere; }
      .pilot-poc, .pilot-poc ol, .pilot-poc li, .selection-note { min-width: 0; overflow-wrap: anywhere; word-break: break-word; }
      .plain-reading, .plain-reading-grid, .plain-reading-grid > div { min-width: 0; overflow-wrap: anywhere; word-break: break-word; }
      .deep-dive-nav { top: 72px; margin-left: 0; margin-right: 0; }
      .deep-dive-chapter { scroll-margin-top: 164px; }
      .deep-dive-points { grid-template-columns: 1fr; }
      .deep-dive-figure { overflow: visible; }
      .deep-dive-image-link { max-width: 100%; overflow-x: auto; overscroll-behavior-x: contain; border-radius: 16px 16px 0 0; touch-action: pan-x pan-y; }
      .deep-dive-image-link img, .deep-dive-image-link .concept-svg-object { width: 920px; max-width: none; }
      .deep-dive-figure figcaption { display: block; }
      .deep-dive-figure figcaption strong { display: block; overflow-wrap: anywhere; }
      .deep-dive-figure figcaption a { display: inline-block; margin-top: 5px; }
    }
    @media (max-width: 430px) {
      .brand { gap: 0; }
      .top-actions { gap: 4px; }
      .icon-button { padding: 8px 9px; }
      .slide-tab { padding: 7px 4px; justify-content: center; }
      .slide-tab strong { display: none; }
      .slide-tab span { text-align: center; }
    }
    __POC_CSS__
    @media print {
      .topbar, .sidebar, .skip-link, .toast, .poc-actions { display: none !important; }
      body { background: #fff; color: #111; }
      main { padding: 0; }
      .content { width: 100%; }
      .panel { box-shadow: none; }
    }
    @media (prefers-reduced-motion: reduce) { *, *::before, *::after { scroll-behavior: auto !important; transition: none !important; } }
    __WORKPLACE_CSS__
  </style>
</head>
<body>
  <a class="skip-link" href="#main">跳到主要內容</a>
  <header class="topbar">
    <a class="brand" href="#view=home" aria-label="回到課程首頁">
      <span class="brand-mark" aria-hidden="true">◈</span>
      <span><small>VISION AI LEARNING MAP</small>模型選型教學</span>
    </a>
    <label class="search-box" for="global-search">
      <span aria-hidden="true">⌕</span>
      <input id="global-search" type="search" autocomplete="off" placeholder="搜尋模型、用途或目前問題…" aria-label="搜尋 58 個模型主題">
      <kbd aria-hidden="true">/</kbd>
    </label>
    <div class="top-actions">
      <button class="icon-button mobile-nav" type="button" data-action="toggle-nav" aria-label="開啟課程導覽" aria-expanded="false">☰</button>
      <button class="icon-button" type="button" data-action="toggle-theme" aria-label="切換深淺色主題"><span aria-hidden="true">◐</span> <span class="theme-text">主題</span></button>
    </div>
  </header>
  <div class="app-shell">
    <aside id="course-nav" class="sidebar" aria-label="課程導覽"></aside>
    <main id="main" tabindex="-1"></main>
  </div>
  <dialog id="lightbox" aria-labelledby="lightbox-title"></dialog>
  <div id="toast" class="toast" role="status" aria-live="polite"></div>
  <script id="course-data" type="application/json">__COURSE_DATA__</script>
  <script>
  (() => {
    "use strict";
    const DATA = JSON.parse(document.getElementById("course-data").textContent);
    const TOPICS = DATA.topics;
    const FAMILIES = DATA.families;
    const TRACKS = DATA.tracks;
    const SUPPORTING = DATA.supporting || {};
    const FAMILY_SUPPORT = DATA.familySupport || {};
    const FAMILY_STARTERS = {
      geometry: { question: "你需要可信座標或穩定對位嗎？", output: "座標、位移或校正誤差", guide: "先確認相機和畫面位置可信，再做後續檢查或量測。", stop: "畫面看不清、反光或對位不穩時先停。" },
      classification: { question: "你已知道要找的類別、區域或位置點嗎？", output: "類別、框、遮罩或關鍵點", guide: "先選你要的是整張分類、區域輪廓，還是固定位置點。", stop: "未知外觀或標註不一致時先交回人工。" },
      detector: { question: "你要先圈出已知物件，還是用文字探索位置？", output: "候選框或候選輪廓", guide: "固定類別就用標註訓練；只有名稱時，先用文字找候選位置。", stop: "候選框不是品質結論，必須回原圖確認。" },
      anomaly: { question: "你只有正常品，想找出不像正常的地方嗎？", output: "可疑位置圖與分數", guide: "先用乾淨正常品當基準，再找新影像不像正常的地方。", stop: "正常品不乾淨、畫面漂移或分數不穩時先 HOLD。" },
      video: { question: "你要看變化、移動、同一物件，還是事件？", output: "變化圖、移動向量、軌跡或影片特徵", guide: "先決定你只看前後變化、移動方向、同一物件，還是完整事件。", stop: "時間或畫面條件改變時，先重驗再判事件。" },
      foundation: { question: "你要拿影像特徵、文字排序，還是看圖問答？", output: "特徵、候選排序或文字建議", guide: "先分清是要給下一個模型用的特徵、文字搜尋，還是看圖協助回答。", stop: "它們不能直接代替缺陷證據或最終決策。" },
      diffusion: { question: "你要做訓練資料、示意修改，還是幫人看清畫面？", output: "合成圖或影像估計", guide: "先分清是做練習資料、示意修改，還是幫人閱讀；三者都要保留原圖。", stop: "任何生成或修復結果都不能取代原始證據。" },
    };
    const HOME_HERO = DATA.homeHero || {};
    const SHARED_JOURNEYS = DATA.sharedJourneys || {};
    const TOPIC_BY_ID = Object.fromEntries(TOPICS.map(topic => [topic.id, topic]));
    const FAMILY_BY_ID = Object.fromEntries(FAMILIES.map(family => [family.id, family]));
    const FAMILY_COMPARISON_FRAMING = {
      geometry: { title: "不要比名稱；比幾何依據與可用輸出", left: "必要依據", right: "可用輸出／回看條件" },
      classification: { title: "不要比名稱；比輸入表示與任務輸出", left: "輸入如何表示", right: "候選輸出／回看條件" },
      detector: { title: "不要比名稱；比候選如何形成", left: "候選如何形成", right: "box／mask evidence 與回看" },
      anomaly: { title: "不要比名稱；比「正常」怎麼表示", left: "正常性怎麼表示", right: "新局部何時可疑" },
      video: { title: "不要比名稱；比時間 state／對應與輸出", left: "state／對應如何維持", right: "時間輸出／回看條件" },
      foundation: { title: "不要比名稱；比 representation 路徑與 claim", left: "輸入如何表示／連接", right: "候選 claim 與證據" },
      diffusion: { title: "不要比名稱；比 condition 與 synthetic output", left: "condition 如何約束", right: "synthetic candidate／核對" },
    };
    const STORAGE_KEY = "vision-ai-model-selection-learning-v1";
    const DEFAULT_PROGRESS = { version: 2, completed: {}, visited: {}, bookmarks: [], last: "", theme: "light", poc: {} };
    const app = { search: "", familyFilter: "all", lightbox: null, concept: null };
    const main = document.getElementById("main");
    const sidebar = document.getElementById("course-nav");
    const dialog = document.getElementById("lightbox");
    const toast = document.getElementById("toast");
    let toastTimer = 0;
    let lastRenderedRouteKey = "";
    let pendingRouteNavigation = false;

    function escapeHTML(value) {
      return String(value ?? "").replace(/[&<>'"]/g, character => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[character]));
    }
    function validRecord(value, fallback) { return value && typeof value === "object" && !Array.isArray(value) ? value : fallback; }
    function loadProgress() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (!raw) return structuredClone(DEFAULT_PROGRESS);
        const parsed = JSON.parse(raw);
        const { quiz: _legacyQuiz, ...stored } = validRecord(parsed, {});
        return {
          ...structuredClone(DEFAULT_PROGRESS),
          ...stored,
          completed: validRecord(parsed.completed, {}),
          visited: validRecord(parsed.visited, {}),
          poc: validRecord(parsed.poc, {}),
          bookmarks: Array.isArray(parsed.bookmarks) ? parsed.bookmarks.filter(id => TOPIC_BY_ID[id]) : [],
        };
      } catch (_) { return structuredClone(DEFAULT_PROGRESS); }
    }
    let progress = loadProgress();
    let storageFailed = false;
    function saveProgress() { try { localStorage.setItem(STORAGE_KEY, JSON.stringify(progress)); storageFailed=false; return true; } catch (_) { storageFailed=true; return false; } }
    function notify(message) {
      toast.textContent = message;
      toast.classList.add("show");
      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => toast.classList.remove("show"), 2600);
    }
    function setTheme(theme) {
      progress.theme = theme === "dark" ? "dark" : "light";
      document.documentElement.dataset.theme = progress.theme;
      saveProgress();
    }
    setTheme(progress.theme);
    function completedCount(list = TOPICS) { return list.filter(topic => progress.completed[topic.id]).length; }
    function isBookmarked(id) { return progress.bookmarks.includes(id); }
    function familyTopics(familyId) { return TOPICS.filter(topic => topic.family === familyId); }
    function hashRoute() {
      const params = new URLSearchParams(location.hash.replace(/^#/, ""));
      const view = params.get("view") || "home";
      const lesson = params.get("lesson");
      const rawSlide = Number.parseInt(params.get("slide") || "1", 10);
      if (view === "lesson" && TOPIC_BY_ID[lesson]) {
        const maxSlide = TOPIC_BY_ID[lesson].teachingStory?.deep_dive?.chapters?.length || 4;
        return { view, lesson, slide: Math.max(1, Math.min(maxSlide, Number.isFinite(rawSlide) ? rawSlide : 1)) };
      }
      if (view === "library") {
        const family = params.get("family");
        return { view, family: FAMILY_BY_ID[family] ? family : "all" };
      }
      return { view: ["home", "library", "foundations", "production", "glossary", "poc"].includes(view) ? view : "home" };
    }
    function routeKey(route) {
      if (route.view === "lesson") return `lesson:${route.lesson}:${route.slide}`;
      if (route.view === "library") return `library:${route.family}`;
      return route.view;
    }
    function scrollToRouteStart() {
      const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      window.scrollTo({ top: 0, left: 0, behavior: reduceMotion ? "auto" : "smooth" });
      const heading = main.querySelector("h1");
      if (heading) {
        heading.setAttribute("tabindex", "-1");
        heading.focus({ preventScroll: true });
      } else {
        main.focus({ preventScroll: true });
      }
    }
    function go(view, options = {}) {
      const params = new URLSearchParams({ view });
      Object.entries(options).forEach(([key, value]) => params.set(key, String(value)));
      const nextHash = `#${params.toString()}`;
      pendingRouteNavigation = true;
      // Re-selecting the active sidebar item should still return the reader to
      // the beginning of that section; setting an identical hash has no event.
      if (location.hash === nextHash) {
        render();
        return;
      }
      location.hash = nextHash;
    }
    function visit(id) {
      progress.visited[id] = new Date().toISOString();
      progress.last = id;
      saveProgress();
    }
    function toggleComplete(id) {
      if (progress.completed[id]) { delete progress.completed[id]; notify("已標記為尚未完成。 "); }
      else { progress.completed[id] = new Date().toISOString(); notify("已完成這個主題。下一步可比較相鄰模型。 "); }
      saveProgress(); render();
    }
    function toggleBookmark(id) {
      if (isBookmarked(id)) progress.bookmarks = progress.bookmarks.filter(item => item !== id);
      else progress.bookmarks.push(id);
      saveProgress(); render();
    }
    function topicSearchText(topic) { return [topic.model, topic.familyLabel, topic.summary, topic.selectionQuestion, topic.takeaway, topic.failure, topic.selection, ...topic.keywords].join(" ").toLocaleLowerCase(); }
    function filteredTopics() {
      const query = app.search.trim().toLocaleLowerCase();
      return TOPICS.filter(topic => (app.familyFilter === "all" || topic.family === app.familyFilter) && (!query || topicSearchText(topic).includes(query)));
    }
    function familyOverviewHTML() {
      if (app.familyFilter === "all") return "";
      const family = FAMILY_BY_ID[app.familyFilter];
      if (!family) return "";
      const rows = familyTopics(family.id);
      const support = FAMILY_SUPPORT[family.id] || [];
      const starter = FAMILY_STARTERS[family.id];
      return `<section class="family-overview" aria-labelledby="family-overview-title"><p class="eyebrow">${escapeHTML(family.label)} · 先從現場問題選路</p><h2 id="family-overview-title">${escapeHTML(starter.question)}</h2><p>先選你要拿到的東西，再比較模型；不必先背模型名稱。</p><div class="family-contract"><div><strong>你會拿到</strong><span>${escapeHTML(starter.output)}</span></div><div><strong>先用哪個問題選路</strong><span>${escapeHTML(starter.guide)}</span></div><div><strong>什麼情況先停</strong><span>${escapeHTML(starter.stop)}</span></div></div><div class="comparison-wrap"><table class="comparison-table"><thead><tr><th>模型</th><th>它解什麼現場問題？</th><th>先交出什麼？</th><th>什麼情況先停？</th></tr></thead><tbody>${rows.map(topic => `<tr><td>${escapeHTML(topic.model)}</td><td>${escapeHTML(topic.summary)}</td><td>${escapeHTML(topic.learnerBrief.deliverable)}</td><td>${escapeHTML(topic.learnerBrief.hold)}</td></tr>`).join("")}</tbody></table></div>${support.length ? `<details class="family-support"><summary>想深入時，逐張閱讀 ${support.length} 張家族地圖與比較教材</summary><div class="family-support-stories">${support.map(item => `<article class="family-support-story"><figure><a class="family-support-visual" href="${escapeHTML(item.image)}" target="_blank" rel="noopener" aria-label="開啟原圖：${escapeHTML(item.title)}"><img loading="lazy" decoding="async" src="${escapeHTML(item.image)}" width="1672" height="941" alt="${escapeHTML(item.alt)}"></a><p class="family-support-mobile-hint">手機上可左右滑動閱讀圖內標示，或開啟原圖。</p><figcaption><div><h3>${escapeHTML(item.title)}</h3><p>${escapeHTML(item.summary)}</p></div><a class="button ghost" href="${escapeHTML(item.image)}" target="_blank" rel="noopener">開啟原圖 ↗</a></figcaption></figure></article>`).join("")}</div></details>` : ""}</section>`;
    }
    function sidebarHTML(route) {
      const currentLesson = route.lesson || "";
      const overall = `${completedCount()} / ${TOPICS.length}`;
      return `
        <p class="sidebar-heading">學習入口</p>
        <button class="nav-button ${route.view === "home" ? "active" : ""}" type="button" data-action="go" data-view="home">⌂ <span>從第一張模型圖開始</span></button>
        <button class="nav-button ${route.view === "foundations" ? "active" : ""}" type="button" data-action="go" data-view="foundations">◇ <span>開始前：共同工程前提</span><span class="nav-number">3</span></button>
        <button class="nav-button ${route.view === "library" ? "active" : ""}" type="button" data-action="go" data-view="library">⌕ <span>探索 58 個主題</span><span class="nav-number">${TOPICS.length}</span></button>
        <button class="nav-button ${route.view === "production" ? "active" : ""}" type="button" data-action="go" data-view="production">▤ <span>從 POC 到量產</span><span class="nav-number">3</span></button>
        <button class="nav-button ${route.view === "glossary" ? "active" : ""}" type="button" data-action="go" data-view="glossary">◎ <span>工程術語與讀圖字典</span></button>
        <button class="nav-button ${route.view === "poc" ? "active" : ""}" type="button" data-action="go" data-view="poc">▧ <span>我的 POC 選型畫布</span></button>
        <p class="sidebar-heading" style="margin-top:22px">整體進度 ${overall}</p>
        ${FAMILIES.map(family => {
          const topics = familyTopics(family.id);
          const done = completedCount(topics);
          const isOpen = currentLesson && TOPIC_BY_ID[currentLesson]?.family === family.id;
          return `<details class="nav-family" ${isOpen ? "open" : ""}>
            <summary><span aria-hidden="true">${escapeHTML(family.icon)}</span><span>${escapeHTML(family.label)}</span><span class="nav-progress">${done}/${topics.length}</span></summary>
            <button class="nav-button" type="button" data-action="start-family" data-family="${escapeHTML(family.id)}">直接讀第一張模型圖 →</button>
            <button class="nav-button" type="button" data-action="filter-family" data-family="${escapeHTML(family.id)}">查看家族比較 <span class="nav-number">${topics.length}</span></button>
            ${topics.map(topic => `<button class="topic-link ${topic.id === currentLesson ? "active" : ""} ${progress.completed[topic.id] ? "done" : ""}" type="button" data-action="lesson" data-topic="${escapeHTML(topic.id)}"><span class="complete-dot" aria-hidden="true"></span>${escapeHTML(topic.model)}</button>`).join("")}
          </details>`;
        }).join("")}
        <div class="sidebar-help"><strong>讀圖規則</strong><br>先看原始教學圖，再讀圖下工程重點。模型輸出是 candidate、score、box、mask、track 或 assist；它不會自動變成量測、根因或 PASS／FAIL。</div>`;
    }
    function homeHTML() {
      const recent = progress.last && TOPIC_BY_ID[progress.last] ? TOPIC_BY_ID[progress.last] : null;
      const startTopic = recent || TOPIC_BY_ID.charuco || TOPICS[0];
      const supportingCount = Object.values(SUPPORTING).reduce((total, collection) => total + collection.items.length, 0) + Object.values(FAMILY_SUPPORT).reduce((total, items) => total + items.length, 0);
      const routeCards = [
        ["相機位置或尺寸可信嗎？", "先讓同一個真實位置在每張畫面中對得上。", "geometry"],
        ["你已知道要找什麼嗎？", "用類別、位置、輪廓或關鍵點交付結果。", "classification"],
        ["你只知道什麼是正常嗎？", "先找出不像正常品的位置，再交給人確認。", "anomaly"],
        ["你要看移動或影片事件嗎？", "先分清是看變化、移動、軌跡還是事件。", "video"],
        ["你想用文字或圖片輔助嗎？", "先拿候選排序或文字建議，不直接做決策。", "foundation"],
        ["你想生成或讓畫面更清楚嗎？", "只做訓練或閱讀輔助，原圖仍是證據。", "diffusion"],
      ];
      return `<div class="content">
        <section class="hero" aria-labelledby="home-title">
          <div class="hero-grid"><div>
          <p class="eyebrow">從 AOI 現場問題到可驗收選型</p>
          <h1 id="home-title">先看模型圖，<br>再把它放進正確的工程位置。</h1>
           <p class="lead">這是一個可離線開啟的 Vision AI 學習地圖。先從同一個 AOI 工作例理解「原始證據 → candidate → review」，再選現場問題與模型；每頁都先用白話說明它交出什麼、第一步怎麼做、什麼情況要停下來。</p>
          <div class="hero-actions">
            <button class="button primary" type="button" data-action="lesson" data-topic="${escapeHTML(startTopic.id)}">${recent ? `繼續：${escapeHTML(startTopic.model)} 的教學圖` : `從第一張教學圖開始：${escapeHTML(startTopic.model)}`}</button>
            <button class="button" type="button" data-action="go" data-view="foundations">先看共同工程前提</button>
            <button class="button" type="button" data-action="go" data-view="library">探索模型家族</button>
          </div>
          <div class="stats" aria-label="課程摘要"><div class="stat"><strong>58</strong><span>模型主題</span></div><div class="stat"><strong>${232 + supportingCount}</strong><span>正式教學插圖</span></div><div class="stat"><strong>${completedCount()}</strong><span>已完成學習</span></div></div>
          </div><figure class="hero-preview"><button type="button" data-action="lesson" data-topic="${escapeHTML(startTopic.id)}" aria-label="直接開始 ${escapeHTML(startTopic.model)} 的第一個工作例"><img data-asset src="${escapeHTML(HOME_HERO.image || '')}" width="1672" height="941" decoding="async" alt="${escapeHTML(HOME_HERO.alt || '')}"></button><figcaption><span>${escapeHTML(HOME_HERO.caption || '從 raw evidence 到 human review')}</span><span>點圖開始：${escapeHTML(startTopic.model)} →</span></figcaption></figure></div>
        </section>
        <section class="section" aria-labelledby="route-title"><div class="section-heading"><div><p class="eyebrow">快速選路</p><h2 id="route-title">你現在需要先解哪一種問題？</h2></div><p>選卡後會直接進入該家族的第一張模型教學圖；比較頁仍可從左側隨時開啟。</p></div><div class="route-grid">${routeCards.map((card, index) => `<button class="route-card" type="button" data-action="start-family" data-family="${card[2]}"><span class="route-number">${index + 1}</span><strong>${card[0]}</strong><p>${card[1]}</p><small>直接閱讀第一張圖 →</small></button>`).join("")}</div></section>
        <section class="section"><div class="section-heading"><div><p class="eyebrow">建議導讀</p><h2>不必一次讀完 58 個模型</h2></div><p>先完成一條與你工作最接近的 POC 路線，再打開「探索主題」比較替代方案與邊界。</p></div><div class="family-grid">${TRACKS.map(track => `<button class="family-card" type="button" data-action="start-track" data-track="${track.id}"><span class="family-icon" aria-hidden="true">→</span><strong>${escapeHTML(track.label)}</strong><p>${escapeHTML(track.description)}</p><small>${escapeHTML(track.duration)} · ${track.topics.length} 個核心錨點</small></button>`).join("")}</div></section>
        <section class="section"><div class="section-heading"><div><p class="eyebrow">讀圖共同語言</p><h2>每個模型都照這四步讀</h2></div><button class="button" type="button" data-action="go" data-view="foundations">打開共同前提教學圖 →</button></div><div class="learn-steps"><div class="learn-step"><span>01</span><strong>先看它交出什麼</strong><p>它交出的是類別、位置、輪廓、可疑圖或文字建議；這些都不是最後動作。</p></div><div class="learn-step"><span>02</span><strong>再看它怎麼做</strong><p>只沿著圖中由左到右的資料流，知道前一步如何供下一步使用。</p></div><div class="learn-step"><span>03</span><strong>把條件寫下來</strong><p>固定要看的畫面、資料、模型版本、門檻、時間與人工覆核方式，才可公平比較。</p></div><div class="learn-step"><span>04</span><strong>最後設停止規則</strong><p>資料或畫面改變、模型不確定或證據不足時，先停止並交給指定的人。</p></div></div></section>
        <section class="section"><div class="notice"><div class="notice-icon" aria-hidden="true">⚑</div><div><strong>安全提醒：模型輸出不是產線動作。</strong>任何候選圖、相似度或文字回答，都要回到原始畫面、保存設定，並由負責的人確認。</div></div></section>
      </div>`;
    }
    function libraryHTML() {
      const visible = filteredTopics();
      const focused = Boolean(app.search || app.familyFilter !== "all");
      const choices = FAMILIES.map(family => {
        const starter = FAMILY_STARTERS[family.id];
        return `<button class="route-card" type="button" data-action="filter-family" data-family="${escapeHTML(family.id)}"><strong>${escapeHTML(starter.question)}</strong><p>${escapeHTML(starter.output)}</p><small>看這一族的入門比較 →</small></button>`;
      }).join("");
      const results = visible.length ? `<div class="topic-grid">${visible.map(topicCardHTML).join("")}</div>` : `<div class="empty"><h2>沒有符合的主題</h2><p>先選一個現場問題，或輸入模型名稱。</p></div>`;
      return `<div class="content"><div class="section-heading"><div><p class="eyebrow">從現場問題找模型</p><h1 style="font-size:clamp(34px,4vw,52px);margin-bottom:8px">先說你要什麼，<br>不用先背模型名字。</h1><p>先選「你想交出什麼」與「你有什麼資料」，網站再帶你進入四張圖的完整教學。</p></div></div>
        <section class="panel" aria-label="探索條件"><div class="library-controls"><div class="field"><label for="library-search">已知道模型名稱？可直接搜尋</label><input id="library-search" type="search" value="${escapeHTML(app.search)}" placeholder="例如：找正常品差異、圈出物件、看影片事件"></div><div class="field"><label for="family-filter">或選一個模型家族</label><select id="family-filter"><option value="all">先讓我選現場問題</option>${FAMILIES.map(family => `<option value="${family.id}" ${app.familyFilter === family.id ? "selected" : ""}>${escapeHTML(family.label)}（${family.count}）</option>`).join("")}</select></div></div>${focused ? `<p aria-live="polite" style="margin:0;color:var(--muted)">找到 <strong style="color:var(--ink-strong)">${visible.length}</strong> 個主題。<button class="button" style="margin-left:8px;padding:4px 8px;font-size:12px" type="button" data-action="clear-filters">重新選問題</button></p>` : ""}</section>
        ${focused ? `${familyOverviewHTML()}<section class="section">${results}</section>` : `<section class="section"><div class="section-heading"><div><p class="eyebrow">第一步</p><h2>你現在的現場最像哪一種問題？</h2></div><p>選一張卡只會縮小路徑，不會替你做決定。</p></div><div class="route-grid">${choices}</div><details class="family-support" style="margin-top:20px"><summary>我已知道模型名稱，展開全部 58 個主題</summary><div class="topic-grid" style="margin-top:16px">${results}</div></details></section>`}</div>`;
    }
    function topicCardHTML(topic) {
      const family = FAMILY_BY_ID[topic.family];
      return `<button class="topic-card" type="button" data-action="lesson" data-topic="${escapeHTML(topic.id)}"><div class="card-top"><span class="chip">${escapeHTML(family.icon)} ${escapeHTML(topic.familyLabel)}</span><span class="card-meta"><span class="status-dot ${progress.completed[topic.id] ? "done" : ""}" aria-hidden="true"></span>${progress.completed[topic.id] ? "完成" : "未完成"}</span></div><h3>${escapeHTML(topic.model)}</h3><p>${escapeHTML(topic.summary)}</p><small>${escapeHTML(topic.selectionQuestion)}</small></button>`;
    }
    function engineeringMediaHTML(slide, first = false) {
      const img = `<img data-asset src="${escapeHTML(slide.image)}" width="1672" height="941" ${first ? 'loading="eager" fetchpriority="high"' : 'loading="lazy"'} decoding="async" alt="${escapeHTML(slide.alt)}">`;
      if (!slide.mobileImage) return img;
      return `<picture class="engineering-media"><source media="(max-width: 760px)" srcset="${escapeHTML(slide.mobileImage)}" width="${slide.mobileWidth}" height="${slide.mobileHeight}">${img}</picture>`;
    }
    function lessonStepHTML(topic, slide, first) {
      const next = topic.slides[slide.index];
      const heading = `<header class="lesson-step-heading"><span class="step-badge">${String(slide.index).padStart(2, "0")}</span><div><p class="eyebrow">${escapeHTML(slide.label)}</p><h2 id="step-title-${escapeHTML(topic.id)}-${slide.index}">${escapeHTML(slide.prompt)}</h2><p class="prompt">${escapeHTML(slide.question)}</p></div></header>`;
      const figure = `<figure class="teaching-figure figure-card"><button class="image-button" type="button" data-action="open-lightbox" data-topic="${escapeHTML(topic.id)}" data-slide="${slide.index}" aria-label="放大閱讀 ${escapeHTML(topic.model)} 的第 ${slide.index} 張${escapeHTML(slide.label)}圖">${engineeringMediaHTML(slide, first)}</button><figcaption class="image-caption"><span>正式教學插圖 ${slide.index}/4 · 已可直接閱讀；點圖僅用於放大細節</span><a href="${escapeHTML(slide.image)}" target="_blank" rel="noopener">開啟原圖 ↗</a></figcaption></figure>`;
      const termHelp = Array.isArray(slide.terms) && slide.terms.length ? `<div class="term-strip" aria-label="本圖名詞提示">${slide.terms.map(term => `<span>${escapeHTML(term)}</span>`).join("")}</div>` : "";
      const plain = `<section class="plain-reading" aria-label="白話讀圖"><p class="eyebrow">30 秒讀懂這張圖</p><h3>${escapeHTML(slide.question)}</h3><div class="plain-reading-grid"><div><strong>先看哪裡</strong><p>${escapeHTML(slide.plain.look)}</p></div><div><strong>框與框的關係</strong><p>${escapeHTML(slide.plain.relation)}</p></div><div><strong>本圖只要帶走</strong><p>${escapeHTML(slide.plain.takeaway)}</p></div></div>${termHelp}</section>`;
      const technical = `<details class="technical-details"><summary>想深入，再看工程細節與完整名詞</summary><div class="diagram-reading"><section class="diagram-summary"><p class="eyebrow">技術版讀圖</p><h3>沿著資料流確認</h3><ol class="guide-list">${slide.guide.map(item => `<li>${escapeHTML(item)}</li>`).join("")}</ol><div class="callout-danger"><strong>技術上不可誤讀</strong><br>${escapeHTML(slide.misconception)}</div></section><section class="diagram-stages"><p class="eyebrow">完整節點</p><h3>原始工程節點</h3><div class="stage-list">${slide.stages.map((stage, index) => `<div class="stage"><span class="stage-index">${index + 1}</span><strong>${escapeHTML(stage.title)}</strong><p>${escapeHTML(stage.body)}</p></div>`).join("")}</div></section></div></details>`;
      const takeaways = `<section class="engineering-takeaway" aria-label="本圖工程重點"><p class="engineering-takeaway-heading">工程師先帶走：不用作答，先把這三句話記住。</p><div class="takeaway-card"><strong>先看哪裡</strong><p>${escapeHTML(slide.plain.look)}</p></div><div class="takeaway-card safe"><strong>怎麼理解</strong><p>${escapeHTML(slide.plain.relation)}</p></div><div class="takeaway-card risk"><strong>不要誤用</strong><p>${escapeHTML(topic.learnerBrief.hold)}</p></div></section>`;
      const firstSequence = topic.teachingStory ? `${heading}${figure}` : `${figure}${heading}`;
      return `<section id="step-${escapeHTML(topic.id)}-${slide.index}" class="lesson-step ${first ? "first" : ""}" aria-labelledby="step-title-${escapeHTML(topic.id)}-${slide.index}">${first ? firstSequence : `${heading}${figure}`}${plain}${(slide.evidenceLinks || []).map(link => `<p class="retained-evidence"><a href="${escapeHTML(link.image)}" target="_blank" rel="noopener">${escapeHTML(link.title)} ↗</a></p>`).join("")}${technical}${takeaways}${next ? `<p class="action-row"><button class="button" type="button" data-action="jump-step" data-topic="${escapeHTML(topic.id)}" data-step="${next.index}">繼續看第 ${next.index} 張：${escapeHTML(next.label)} ↓</button></p>` : ""}</section>`;
    }
    function isSvgVisual(image) {
      return /\.svg(?:$|[?#])/i.test(String(image || ""));
    }
    function visualMediaHTML(visual, options = {}) {
      const image = escapeHTML(visual.image);
      const alt = escapeHTML(visual.alt);
      const loading = options.loading || "lazy";
      const priority = options.priority ? ' fetchpriority="high"' : "";
      if (isSvgVisual(visual.image)) {
        return `<object data-asset class="concept-svg-object" data="${image}" type="image/svg+xml" width="1672" height="941" loading="${loading}" role="img" aria-label="${alt}" tabindex="-1"></object>`;
      }
      return `<img data-asset src="${image}" width="1672" height="941" loading="${loading}"${priority} decoding="async" alt="${alt}">`;
    }
    function conceptVisualsHTML(topic, placement) {
      const story = topic.teachingStory;
      if (!story || !Array.isArray(story.concept_visuals)) return "";
      const visuals = story.concept_visuals
        .filter(visual => visual.placement === placement)
        .sort((left, right) => (left.sequence || 0) - (right.sequence || 0));
      if (!visuals.length) return "";
      const rendered = visuals.map(visual => `<section class="concept-visual" aria-labelledby="concept-title-${escapeHTML(topic.id)}-${escapeHTML(visual.id)}"><header class="concept-visual-heading"><p class="eyebrow">概念橋接圖 · 先看同一個工作例</p><h3 id="concept-title-${escapeHTML(topic.id)}-${escapeHTML(visual.id)}">${escapeHTML(visual.title)}</h3><p class="concept-visual-prompt">${escapeHTML(visual.prompt)}</p></header><figure class="concept-figure"><a class="concept-image-link" href="${escapeHTML(visual.image)}" target="_blank" rel="noopener" aria-label="開啟 ${escapeHTML(visual.title)} 原圖">${visualMediaHTML(visual)}</a><figcaption class="concept-caption">${escapeHTML(visual.caption)}<br><button class="button concept-enlarge" type="button" data-action="open-concept" data-title="${escapeHTML(visual.title)}" data-image="${escapeHTML(visual.image)}" data-alt="${escapeHTML(visual.alt)}">放大閱讀概念圖</button></figcaption></figure><ol class="concept-callouts" aria-label="圖中重點">${visual.callouts.map(callout => `<li><strong>${escapeHTML(callout.title)}</strong><p>${escapeHTML(callout.body)}</p></li>`).join("")}</ol></section>`).join("");
      // Comparison is a first-read teaching relationship, not optional
      // decoration.  Keep it adjacent to its paragraph instead of hiding it
      // behind an extra interaction.
      return `<div class="concept-visuals">${rendered}</div>`;
    }
    function firstReadPathFor(topic) {
      const authored = topic.teachingStory?.beginner_path;
      return authored?.visuals?.length
        ? { source: "authored", path: authored }
        : { source: null, path: null };
    }
    function beginnerPlainCopy(topic, index) {
      const brief = topic.learnerBrief;
      const steps = [
        {
          eyebrow: "先看現場與輸入",
          title: "先確認模型看見的是什麼",
          prompt: brief.first,
          focusTitle: "這張先看",
          focus: "確認影像、工作範圍和比較條件是否固定。",
          stopTitle: "先不要急著判斷",
          stop: "輸入條件還沒固定時，結果不同不一定是模型能力造成的。",
        },
        {
          eyebrow: "再看處理方式",
          title: "沿著箭頭看資料怎麼被整理",
          prompt: "先掌握輸入、處理和輸出的順序；圖中的完整名詞可以稍後再查。",
          focusTitle: "這張先看",
          focus: "找出影像中的資訊經過哪些主要步驟。",
          stopTitle: "不必先背名詞",
          stop: "只要能說出前一步如何影響下一步，就已掌握這張圖的主線。",
        },
        {
          eyebrow: "看懂模型輸出",
          title: "分清楚模型結果和最終決定",
          prompt: brief.deliverable,
          focusTitle: "模型交出的東西",
          focus: brief.deliverable,
          stopTitle: "還需要確認",
          stop: "模型結果通常是候選或估計值，仍要回到原圖和現場規則檢查。",
        },
        {
          eyebrow: "檢查風險",
          title: "看到哪些情況要停下來？",
          prompt: brief.hold,
          focusTitle: "停止條件",
          focus: brief.hold,
          stopTitle: "安全做法",
          stop: "條件未通過時交給人工確認，不讓系統自動做合格判定。",
        },
        {
          eyebrow: "最後再比較方法",
          title: "用相同條件比較其他方法",
          prompt: "固定同一批影像、輸出需求和驗收方式，再比較哪一條路比較適合。",
          focusTitle: "公平比較",
          focus: "比較時使用相同資料、畫面範圍、硬體和錯誤成本。",
          stopTitle: "避免誤選",
          stop: "不要只看模型名稱、單一分數或最快的一次速度。",
        },
      ];
      return steps[Math.min(index, steps.length - 1)];
    }
    function beginnerVisualsHTML(topic, pathInfo = firstReadPathFor(topic), options = {}) {
      const path = pathInfo?.path;
      if (!path || !Array.isArray(path.visuals) || !path.visuals.length) return "";
      const allVisuals = [...path.visuals].sort((left, right) => (left.sequence || 0) - (right.sequence || 0));
      const start = Math.max(0, options.start || 0);
      const end = options.end === undefined ? allVisuals.length : Math.min(allVisuals.length, options.end);
      const visuals = allVisuals.slice(start, end);
      if (!visuals.length) return "";
      const rendered = visuals.map((visual, localIndex) => {
        const index = start + localIndex;
        // Authored focused views carry their own case-specific first-read copy.
        const focused = Boolean(visual.reading_views?.length);
        const plain = focused ? {
          eyebrow: "看案例，再做判斷", title: visual.title, prompt: visual.prompt,
          focusTitle: visual.callouts[0].title, focus: visual.caption,
          stopTitle: visual.callouts[1].title, stop: visual.callouts[1].body,
        } : beginnerPlainCopy(topic, index);
        const engineeringCallouts = visual.callouts.map(callout => `<li><strong>${escapeHTML(callout.title)}</strong><p>${escapeHTML(callout.body)}</p></li>`).join("");
        const coreSummary = visual.core_ideas === true ? `<section class="core-ideas" aria-label="模型中心思想"><h4>為什麼需要這個設計？</h4><p>${escapeHTML(visual.caption)}</p><h4>讀完要能說清楚的三個要點</h4><ol class="guide-list">${engineeringCallouts}</ol></section>` : "";
        return `<section id="beginner-${escapeHTML(topic.id)}-${escapeHTML(visual.id)}" class="concept-visual beginner-visual${focused ? " beginner-focused" : ""}" aria-labelledby="beginner-title-${escapeHTML(topic.id)}-${escapeHTML(visual.id)}"><header class="concept-visual-heading"><p class="eyebrow">第 ${String(index + 1).padStart(2, "0")} 張 · ${escapeHTML(plain.eyebrow)}</p><h3 id="beginner-title-${escapeHTML(topic.id)}-${escapeHTML(visual.id)}">${escapeHTML(plain.title)}</h3><p class="concept-visual-prompt">${escapeHTML(plain.prompt)}</p></header>${focused ? readingViewsHTML(visual, `beginner-${topic.id}-${index + 1}`) : `<figure class="concept-figure"><a class="concept-image-link" href="${escapeHTML(visual.image)}" target="_blank" rel="noopener" aria-label="開啟 ${escapeHTML(topic.model)} 第 ${String(index + 1)} 張教學圖原圖">${visualMediaHTML(visual, { loading: index === 0 ? "eager" : "lazy", priority: index === 0 })}</a><figcaption class="concept-caption"><strong>白話重點：</strong>${escapeHTML(plain.focus)}<br><button class="button concept-enlarge" type="button" data-action="open-concept" data-title="${escapeHTML(plain.title)}" data-image="${escapeHTML(visual.image)}" data-alt="${escapeHTML(visual.alt)}">放大閱讀這張圖</button></figcaption></figure><p class="mobile-image-hint">手機閱讀提示：可在圖面上左右滑動查看標示；重點也會在下方以正常字級說明。</p>`}${coreSummary || `<div class="primer-summary" aria-label="第 ${String(index + 1)} 張圖的白話重點"><section class="primer-card"><strong>${escapeHTML(plain.focusTitle)}</strong><p>${escapeHTML(plain.focus)}</p></section><section class="primer-card"><strong>${escapeHTML(plain.stopTitle)}</strong><p>${escapeHTML(plain.stop)}</p></section></div>`}<details class="beginner-engineering-reference beginner-engineering-copy"><summary>想深入，再看這張圖的完整工程說明</summary><div class="beginner-engineering-reference-body"><h4>${escapeHTML(visual.title)}</h4><p><strong>原始問題：</strong>${escapeHTML(visual.prompt)}</p><p>${escapeHTML(visual.caption)}</p><ol class="concept-callouts" aria-label="第 ${String(index + 1)} 張圖的工程重點">${engineeringCallouts}</ol></div></details></section>`;
      }).join("");
      if (options.includePathHeading === false) {
        return `<div class="beginner-visuals beginner-visuals-continuation">${rendered}</div>`;
      }
      const brief = topic.learnerBrief;
      const engineeringIntro = `<details class="beginner-engineering-reference beginner-engineering-copy"><summary>工程師需要時，再展開完整流程摘要</summary><div class="beginner-engineering-reference-body"><h4>${escapeHTML(path.title)}</h4><p>${escapeHTML(path.intro)}</p></div></details>`;
      if (allVisuals.every(visual => visual.reading_views?.length)) {
        return `<section class="beginner-path" data-learning-path="image-led" data-image-source="${escapeHTML(pathInfo.source || "unknown")}" aria-labelledby="beginner-path-title-${escapeHTML(topic.id)}"><header class="beginner-path-heading"><h3 id="beginner-path-title-${escapeHTML(topic.id)}">${escapeHTML(path.title)}</h3><p>${escapeHTML(path.intro)}</p></header><div class="beginner-visuals">${rendered}</div></section>`;
      }
      return `<section class="beginner-path" data-learning-path="image-led" data-image-source="${escapeHTML(pathInfo.source || "unknown")}" aria-labelledby="beginner-path-title-${escapeHTML(topic.id)}"><header class="beginner-path-heading"><p class="eyebrow">第一遍：先看完整工作例</p><h3 id="beginner-path-title-${escapeHTML(topic.id)}">用完整工作例看懂 ${escapeHTML(topic.model)}</h3><p>先看它要解決什麼、會交出什麼，以及何時必須停下來。完整工程名詞保留在每張圖下方，需要時再展開。</p></header><div class="primer-summary" aria-label="${escapeHTML(topic.model)} 白話摘要"><section class="primer-card"><strong>它要解決什麼？</strong><p>${escapeHTML(brief.problem)}</p></section><section class="primer-card"><strong>它會交出什麼？</strong><p>${escapeHTML(brief.deliverable)}</p></section></div>${engineeringIntro}<div class="beginner-visuals">${rendered}</div></section>`;
    }
    function causalChainHTML(topic, options = {}) {
      const story = topic.teachingStory;
      if (!story) return "";
      const textOnly = Boolean(options.textOnly);
      const causalSteps = story.mechanism_steps.map((step, index) => {
        const visual = story.inline_visuals?.[index];
        if (!textOnly && !visual) return "";
        const cue = visual?.cue || `mechanism-step-${index + 1}`;
        const copy = `<div class="causal-step-copy"><span class="causal-step-number">${index + 1}</span><h4>${escapeHTML(step.title)}</h4><p>${escapeHTML(step.body)}</p><p class="because"><strong>因為：</strong>${escapeHTML(step.why)}</p><p class="anchor">設定核對：${escapeHTML(step.anchor)}</p></div>`;
        if (textOnly) {
          return `<article class="causal-step causal-step-text explanation-unit" data-explains="mechanism-step-${index + 1}" data-visual-cue="${escapeHTML(cue)}">${copy}</article>`;
        }
        const wide = visual.display === "full-width";
        return `<article class="causal-step${wide ? " causal-step-wide" : ""} explanation-unit" data-explains="mechanism-step-${index + 1}" data-visual-cue="${escapeHTML(cue)}">${copy}<figure class="inline-explainer">${visualMediaHTML(visual)}<figcaption><strong>看圖：</strong>${escapeHTML(visual.label)}<span class="not-claim">不可多推論：${escapeHTML(visual.not_claim)}</span></figcaption></figure></article>`;
      }).join("");
      const lead = textOnly
        ? "主圖已在上方第一遍。這裡只核對每一步要鎖定的設定與為什麼，不再重貼同一張圖。"
        : "每一段先說一個因果主張，緊接的圖只畫這一段需要看見的關係；後面的工程圖用來核對設定與證據契約。";
      return `<section class="causal-chain" aria-labelledby="causal-title-${escapeHTML(topic.id)}"><p class="eyebrow">模型專屬因果鏈</p><h3 id="causal-title-${escapeHTML(topic.id)}">${textOnly ? "實作時逐步核對" : "每一步都回答「為什麼」"}</h3><p>${lead}</p><div class="causal-grid">${causalSteps}</div></section>`;
    }
   function legacyCausalReferenceHTML(topic) {
      return `<details class="beginner-engineering-reference"><summary>工程參考：展開文字因果鏈與設定核對點<span>不重複主圖；只核對每步要鎖定的設定。</span></summary><div class="beginner-engineering-reference-body">${causalChainHTML(topic, { textOnly: true })}</div></details>`;
    }
    function teachingPrimerHTML(topic) {
      const story = topic.teachingStory;
      if (!story) return "";
      const brief = topic.learnerBrief;
      const pathInfo = firstReadPathFor(topic);
      const usesImageLedPath = Boolean(pathInfo.path?.visuals?.length);
      const firstReadVisual = usesImageLedPath
        ? beginnerVisualsHTML(topic, pathInfo, { end: 1 })
        : "";
      const remainingFirstReadVisuals = usesImageLedPath
        ? beginnerVisualsHTML(topic, pathInfo, { start: 1, includePathHeading: false })
        : conceptVisualsHTML(topic, "after_micro_example");
      const laterEngineeringReference = usesImageLedPath
        ? legacyCausalReferenceHTML(topic)
        : `${causalChainHTML(topic)}${conceptVisualsHTML(topic, "after_causal_chain")}`;
       const terms = brief.terms.map(term => `<li>${escapeHTML(term)}</li>`).join("");
       if (pathInfo.path?.visuals?.[0]?.core_ideas || pathInfo.path?.visuals?.every(visual => visual.reading_views?.length)) {
         const exercise = story.micro_example;
         return `<section class="teaching-primer" data-primer-style="image-led" aria-labelledby="primer-title-${escapeHTML(topic.id)}"><header class="teaching-primer-heading"><h2 id="primer-title-${escapeHTML(topic.id)}">從案例理解 ${escapeHTML(topic.model)}</h2></header>${firstReadVisual}${remainingFirstReadVisuals}<section class="micro-example focused-transfer" aria-label="換情境試著判斷"><p class="eyebrow">換情境試著判斷</p><h3>${escapeHTML(exercise.title)}</h3><p>${escapeHTML(exercise.setup)}</p><p class="prediction">${escapeHTML(exercise.prediction)}</p><details><summary>看解釋與可接受的取捨</summary><p>${escapeHTML(exercise.reveal)}</p></details></section><details class="beginner-engineering-reference"><summary>需要時查看基本名詞與模型背景</summary><div class="beginner-engineering-reference-body"><ul class="guide-list">${terms}</ul><h3>${escapeHTML(story.mental_model.title)}</h3><p>${escapeHTML(story.mental_model.body)}</p><p>${escapeHTML(story.mental_model.limit)}</p></div></details>${laterEngineeringReference}</section>`;
       }
       const deeperPrimer = `<details class="beginner-engineering-reference beginner-engineering-copy"><summary>想深入，再展開模型比喻與預測題</summary><div class="beginner-engineering-reference-body"><div class="primer-summary"><section class="primer-card"><strong>${escapeHTML(story.scenario.title)}</strong><p>${escapeHTML(story.scenario.body)}</p></section><section class="primer-card"><strong>${escapeHTML(story.promise.title)}</strong><p>${escapeHTML(story.promise.body)}</p></section></div><section class="micro-example" aria-label="同一個工作例"><p class="eyebrow">先預測，再揭示</p><h3>${escapeHTML(story.micro_example.title)}</h3><p>${escapeHTML(story.micro_example.setup)}</p><p class="prediction">${escapeHTML(story.micro_example.prediction)}</p><details><summary>看這個例子的解釋</summary><p>${escapeHTML(story.micro_example.reveal)}</p></details></section><section class="mental-model" aria-label="一句心智模型"><p class="eyebrow">一句心智模型</p><h3>${escapeHTML(story.mental_model.title)}</h3><p>${escapeHTML(story.mental_model.body)}</p><p class="limit"><strong>這個比喻的限制：</strong>${escapeHTML(story.mental_model.limit)}</p></section></div></details>`;
       return `<section class="teaching-primer" data-primer-style="${usesImageLedPath ? "image-led" : "standard"}" aria-labelledby="primer-title-${escapeHTML(topic.id)}"><header class="teaching-primer-heading"><span class="step-badge">01</span><div><p class="eyebrow">初學者先讀</p><h2 id="primer-title-${escapeHTML(topic.id)}">先用四句話看懂 ${escapeHTML(topic.model)}</h2><p>先抓住用途與停止條件；工程縮寫和完整設定需要時再展開。</p></div></header><div class="primer-summary"><section class="primer-card"><strong>它要解決什麼？</strong><p>${escapeHTML(brief.problem)}</p></section><section class="primer-card"><strong>它會交出什麼？</strong><p>${escapeHTML(brief.deliverable)}</p></section><section class="primer-card"><strong>開始先做什麼？</strong><p>${escapeHTML(brief.first)}</p></section><section class="primer-card"><strong>什麼情況要停下？</strong><p>${escapeHTML(brief.hold)}</p></section></div><section class="mental-model beginner-terms" aria-label="本頁基本名詞"><p class="eyebrow">先認識兩個詞</p><h3>看到這些詞時，可以這樣理解</h3><ul class="guide-list">${terms}</ul></section>${deeperPrimer}${firstReadVisual}${remainingFirstReadVisuals}${laterEngineeringReference}</section>`;
    }
   function teachingSynthesisHTML(topic) {
     const story = topic.teachingStory;
     if (!story) return "";
      const usesImageLedPath = Boolean(firstReadPathFor(topic).path?.visuals?.length);
      const boundaryCases = story.boundary_cases.map(item => `<article class="boundary-card"><h4>${escapeHTML(item.condition)}</h4><p><strong>可能看到：</strong>${escapeHTML(item.effect)}</p><p><strong>正確下一步：</strong>${escapeHTML(item.action)}</p></article>`).join("");
       const comparisonHeaders = story.comparison_headers;
       const comparisonRows = story.comparison.map(row => `<tr><td data-label="方法">${escapeHTML(row.model)}</td><td data-label="${escapeHTML(comparisonHeaders.basis)}">${escapeHTML(row.normality)}</td><td data-label="${escapeHTML(comparisonHeaders.output)}">${escapeHTML(row.candidate)}</td></tr>`).join("");
      const pocSteps = story.poc.steps.map(step => `<li>${escapeHTML(step)}</li>`).join("");
      // An authored beginner path has already taught the visual story at a
      // readable scale. Legacy comparison/boundary cards stay available in
      // engineering-reference details instead of returning to first read.
      const boundaryVisuals = usesImageLedPath ? "" : conceptVisualsHTML(topic, "before_boundary_cases");
      const comparisonVisuals = usesImageLedPath ? "" : conceptVisualsHTML(topic, "after_comparison");
       const acceptance = story.poc.acceptance;
       const trace = story.review_trace;
       const traceHTML = `<details class="technical-details"><summary>內容依據：展開這頁主張的 model.md 可追溯範圍</summary><p><a href="${escapeHTML(trace.authority)}" target="_blank" rel="noopener">${escapeHTML(trace.authority)} ↗</a></p><p>${escapeHTML(trace.scope)}</p><ul>${trace.claims.map(claim => `<li><strong>${escapeHTML(claim.field)}</strong>：${escapeHTML(claim.source)}</li>`).join("")}</ul></details>`;
       const synthesis = `<section class="teaching-synthesis" aria-labelledby="synthesis-title-${escapeHTML(topic.id)}"><p class="eyebrow">失效案例、選型與小規模試做</p><h2 id="synthesis-title-${escapeHTML(topic.id)}">什麼情況不能相信它？</h2><p class="synthesis-lead">這一區保留完整工程條件，供準備實作或驗收的人逐項核對。</p>${boundaryVisuals}<div class="synthesis-grid">${boundaryCases}</div><section aria-labelledby="comparison-title-${escapeHTML(topic.id)}"><p class="eyebrow" style="margin-top:24px">相鄰方法比較</p><h3 id="comparison-title-${escapeHTML(topic.id)}">${escapeHTML(comparisonHeaders.title)}</h3><table class="teaching-comparison"><thead><tr><th>方法</th><th>${escapeHTML(comparisonHeaders.basis)}</th><th>${escapeHTML(comparisonHeaders.output)}</th></tr></thead><tbody>${comparisonRows}</tbody></table><p class="selection-note">${escapeHTML(story.selection)}</p>${comparisonVisuals}</section><section class="pilot-poc" aria-labelledby="pilot-poc-title-${escapeHTML(topic.id)}"><p class="eyebrow">工程第一步</p><h3 id="pilot-poc-title-${escapeHTML(topic.id)}">${escapeHTML(story.poc.title)}</h3><ol>${pocSteps}</ol><div class="poc-acceptance" aria-label="POC 驗收設計"><div><strong>目前做法</strong><p>${escapeHTML(acceptance.baseline)}</p></div><div><strong>要量什麼</strong><p>${escapeHTML(acceptance.measure)}</p></div><div><strong>反例測試</strong><p>${escapeHTML(acceptance.negative_control)}</p></div><div><strong>誰確認</strong><p>${escapeHTML(acceptance.owner)}</p></div></div><p class="hold-note"><strong>先停下來的訊號：</strong>${escapeHTML(story.poc.hold)}</p></section><section class="teach-back" aria-labelledby="teachback-title-${escapeHTML(topic.id)}"><p class="eyebrow">讀完請自己講回來</p><h3 id="teachback-title-${escapeHTML(topic.id)}">${escapeHTML(story.teach_back.question)}</h3><details><summary>看本頁練習的核對說明</summary><p>${escapeHTML(story.teach_back.answer)}</p></details></section><section class="transfer-check" aria-labelledby="transfer-title-${escapeHTML(topic.id)}"><p class="eyebrow">換一個現場再推理</p><h3 id="transfer-title-${escapeHTML(topic.id)}">${escapeHTML(story.transfer_check.title)}</h3><p><strong>情境：</strong>${escapeHTML(story.transfer_check.scenario)}</p><p><strong>請先回答：</strong>${escapeHTML(story.transfer_check.question)}</p><details><summary>核對這個遷移題</summary><p>${escapeHTML(story.transfer_check.answer)}</p></details></section>${traceHTML}</section>`;
       return usesImageLedPath
         ? `<details class="formal-slide-reference synthesis-reference"><summary>想深入：展開失效案例、模型比較與小規模試做（POC）<span>初學者可先跳過；準備實作或驗收時再逐項核對。</span></summary><div class="formal-slide-reference-body">${synthesis}</div></details>`
         : synthesis;
    }
    function engineerHandoffHTML(topic) {
      const brief = topic.engineeringBrief;
      const technicalLocks = brief.locks.map(item => `${item.title}：${item.body}`).join("；");
      const cards = [
        ["它會交出什麼？", brief.output, ""],
        ["開始先做什麼？", brief.useWhen, ""],
        ["開始前要寫下來的四件事", "固定畫面範圍、資料來源、模型版本和驗收方式；詳細項目可在下方展開。", ""],
        ["怎樣才算真的有用？", brief.evidence, ""],
        ["碰到什麼先停下來？", brief.hold, "warning"],
      ];
      const technical = `<details class="technical-details"><summary>工程師需要時，再展開原始技術契約</summary><div class="diagram-reading"><section class="diagram-summary"><p class="eyebrow">原始建置項目</p><h3>這些設定要一併保存</h3><p>${escapeHTML(technicalLocks)}</p><p><strong>原始選型條件：</strong>${escapeHTML(brief.technicalSelection)}</p></section><section class="diagram-stages"><p class="eyebrow">原始失效邊界</p><h3>下列情況不可忽略</h3><p>${escapeHTML(brief.technicalFailure)}</p><div class="callout-danger"><strong>工程結論</strong><br>${escapeHTML(brief.handoff)}</div></section></div></details>`;
      return `<section class="engineer-handoff" aria-labelledby="engineer-handoff-title"><p class="eyebrow">工程師操作卡</p><h2 id="engineer-handoff-title">把 ${escapeHTML(topic.model)} 放進小規模試做（POC）前，先回答這五個問題。</h2><p style="max-width:900px;color:var(--muted)">先讀白話版就能開始溝通；需要實作、驗證或交接時，再展開下方技術契約。</p><div class="operations-grid">${cards.map((card, index) => `<section class="operation-card ${card[2]}"><span class="operation-number">${index + 1}</span><h3>${escapeHTML(card[0])}</h3><p>${escapeHTML(card[1])}</p></section>`).join("")}</div>${technical}<div class="action-row"><button class="button primary" type="button" data-action="send-to-poc" data-topic="${escapeHTML(topic.id)}">把這張操作卡帶入 POC 畫布 →</button><a class="button" href="${escapeHTML(topic.modelPath)}" target="_blank" rel="noopener">查看 model.md ↗</a><a class="button" href="${escapeHTML(topic.manifestPath)}" target="_blank" rel="noopener">查看圖檔 manifest ↗</a></div></section>`;
    }
    function mobileStepsHTML(chapter) {
      if (!chapter.mobile_steps?.length) return "";
      return `<ol class="deep-dive-mobile-steps" aria-label="直向分段讀圖">${chapter.mobile_steps.map((step, i) => `<li><strong>${i + 1}. ${escapeHTML(step.title)}</strong><svg viewBox="${step.crop.join(" ")}" role="img" aria-label="${escapeHTML(step.title)}"><image href="${escapeHTML(chapter.image)}" width="1672" height="941" /></svg><p>${escapeHTML(step.body)}</p></li>`).join("")}</ol>`;
    }
    function readingViewsHTML(chapter, number) {
      const views = chapter.reading_views;
      const buttons = views.length > 1 ? `<div class="reading-view-buttons" role="group" aria-label="本章閱讀視圖">${views.map((v, i) => `<button class="button" type="button" data-action="reading-view" data-view="${i}" aria-pressed="${i === 0}" aria-controls="reading-view-${number}-${i}">${escapeHTML(v.title)}</button>`).join("")}</div>` : "";
      return `<div class="reading-views">${buttons}${views.map((v, i) => `<div class="reading-view-panel" id="reading-view-${number}-${i}" ${i ? "hidden" : ""}><figure class="deep-dive-figure"><a class="deep-dive-image-link" href="${escapeHTML(v.image)}" target="_blank" rel="noopener" aria-label="開啟 ${escapeHTML(v.title)} 原圖">${visualMediaHTML(v, {loading: "lazy"})}</a><svg class="reading-view-mobile" viewBox="${v.mobile_crop.join(" ")}" role="img" aria-label="${escapeHTML(v.alt)}"><image href="${escapeHTML(v.mobile_image)}" width="1672" height="941" /></svg><figcaption><strong>${escapeHTML(v.title)}</strong><button class="button concept-enlarge" type="button" data-action="open-concept" data-title="${escapeHTML(v.title)}" data-image="${escapeHTML(v.image)}" data-alt="${escapeHTML(v.alt)}">放大完整圖</button></figcaption></figure></div>`).join("")}</div>`;
    }
    function readingViewsHTML(chapter, number) {
      const views = chapter.reading_views;
      const buttons = views.length > 1 ? `<div class="reading-view-buttons" role="group" aria-label="Reading views">${views.map((v, i) => `<button class="button" type="button" data-action="reading-view" data-view="${i}" aria-pressed="${i === 0}" aria-controls="reading-view-${number}-${i}">${escapeHTML(v.title)}</button>`).join("")}</div>` : "";
      return `<div class="reading-views">${buttons}${views.map((v, i) => `<div class="reading-view-panel" id="reading-view-${number}-${i}" ${i ? "hidden" : ""}><figure class="deep-dive-figure"><a class="deep-dive-image-link" href="${escapeHTML(v.image)}" target="_blank" rel="noopener">${visualMediaHTML(v, {loading: "lazy"})}</a>${v.mobile_display_mode === "full-mobile" ? `<img class="reading-view-mobile full-mobile-reading" src="${escapeHTML(v.mobile_image)}" width="${v.mobile_intrinsic_width || 720}" height="${v.mobile_intrinsic_height || 1660}" alt="${escapeHTML(v.alt)}">` : `<svg class="reading-view-mobile" viewBox="${v.mobile_crop.join(" ")}" role="img" aria-label="${escapeHTML(v.alt)}"><image href="${escapeHTML(v.mobile_image)}" width="1672" height="941" /></svg>`}<figcaption><strong>${escapeHTML(v.title)}</strong><button class="button concept-enlarge" type="button" data-action="open-concept" data-title="${escapeHTML(v.title)}" data-image="${escapeHTML(v.image)}" data-alt="${escapeHTML(v.alt)}">放大完整圖</button></figcaption></figure></div>`).join("")}</div>`;
    }
    function modelDeepDiveHTML(topic, activeChapter = 1) {
      const deep = topic.teachingStory?.deep_dive;
      if (!deep?.chapters?.length) return "";
      const sourceById = Object.fromEntries((deep.sources || []).map(source => [source.id, source]));
      const nav = deep.chapters.map((chapter, index) => `<button class="${index + 1 === activeChapter ? "active" : ""}" type="button" data-action="deep-dive-chapter" data-topic="${escapeHTML(topic.id)}" data-chapter="${index + 1}" ${index + 1 === activeChapter ? 'aria-current="step"' : ""}><strong>${String(index + 1).padStart(2, "0")}</strong>${escapeHTML(chapter.nav)}</button>`).join("");
      const chapters = deep.chapters.map((chapter, index) => {
        const number = index + 1;
        const sources = chapter.source_ids.map(sourceId => sourceById[sourceId]).filter(Boolean);
        const sourceLinks = sources.map(source => `<a class="deep-dive-source" href="${escapeHTML(source.url)}" target="_blank" rel="noopener" title="${escapeHTML(source.scope)}">依據：${escapeHTML(source.label)} ↗</a>`).join("");
        const next = deep.chapters[index + 1];
        const readingHint = chapter.mobile_steps?.length ? "手機直向分段 · 完整圖可放大" : "手機可左右滑讀圖";
        return `<section id="deep-dive-${escapeHTML(topic.id)}-${number}" class="deep-dive-chapter" data-deep-dive-chapter="${number}" aria-labelledby="deep-dive-title-${escapeHTML(topic.id)}-${number}"><header class="deep-dive-chapter-head"><span class="deep-dive-chapter-number">${String(number).padStart(2, "0")}</span><div><h3 id="deep-dive-title-${escapeHTML(topic.id)}-${number}">${escapeHTML(chapter.title)}</h3><p class="deep-dive-summary">${escapeHTML(chapter.summary)}</p></div></header>${chapter.reading_views?.length ? readingViewsHTML(chapter, number) : `<figure class="deep-dive-figure">${mobileStepsHTML(chapter)}<a class="deep-dive-image-link" href="${escapeHTML(chapter.image)}" target="_blank" rel="noopener" aria-label="開啟 ${escapeHTML(chapter.title)} 原圖">${visualMediaHTML(chapter, { loading: number === 1 ? "eager" : "lazy", priority: number === 1 })}</a><figcaption><strong>本章機制圖 ${String(number).padStart(2, "0")} / ${deep.chapters.length}</strong><span>${readingHint} · <button class="button concept-enlarge" type="button" data-action="open-concept" data-title="${escapeHTML(chapter.title)}" data-image="${escapeHTML(chapter.image)}" data-alt="${escapeHTML(chapter.alt)}">放大閱讀</button></span></figcaption></figure>`}<ol class="deep-dive-points" aria-label="${escapeHTML(chapter.nav)} 的三個重點">${chapter.points.map(point => `<li>${escapeHTML(point)}</li>`).join("")}</ol><div class="deep-dive-meta" aria-label="本章資料來源">${sourceLinks}</div><details class="deep-dive-check"><summary>自我檢查：${escapeHTML(chapter.check.question)}</summary><p><strong>核對：</strong>${escapeHTML(chapter.check.answer)}</p></details>${next ? `<p class="deep-dive-next"><button class="button" type="button" data-action="deep-dive-chapter" data-topic="${escapeHTML(topic.id)}" data-chapter="${number + 1}">下一章：${escapeHTML(next.nav)} ↓</button></p>` : ""}</section>`;
      }).join("");
      const allSources = (deep.sources || []).map(source => `<a class="deep-dive-source" href="${escapeHTML(source.url)}" target="_blank" rel="noopener" title="${escapeHTML(source.scope)}">${escapeHTML(source.label)} ↗</a>`).join("");
      return `<section class="model-deep-dive" data-deep-dive="${escapeHTML(topic.id)}" aria-labelledby="deep-dive-heading-${escapeHTML(topic.id)}"><header class="deep-dive-hero"><p class="eyebrow">模型專屬完整導讀 · 8 章</p><h2 id="deep-dive-heading-${escapeHTML(topic.id)}">${escapeHTML(deep.title)}</h2><p>${escapeHTML(deep.intro)}</p></header><nav class="deep-dive-nav" aria-label="${escapeHTML(topic.model)} 八章導覽">${nav}</nav><div class="deep-dive-chapters">${chapters}</div><footer class="deep-dive-footer"><h3>延伸閱讀與主張邊界</h3><p>架構事實優先連到論文與官方原始碼；AOI accuracy、boundary、runtime、授權與量產決策仍需依你的資料、硬體與使用情境重新確認。</p><div class="deep-dive-meta">${allSources}<a class="button" href="${escapeHTML(deep.concept_path)}" target="_blank" rel="noopener">閱讀完整 model concept ↗</a></div></footer></section>`;
    }
    function lessonHTML(topic, slideNumber) {
      visit(topic.id);
      const courseIndex = TOPICS.findIndex(item => item.id === topic.id);
      const previous = TOPICS[courseIndex - 1];
      const next = TOPICS[courseIndex + 1];
      const related = familyTopics(topic.family).filter(item => item.id !== topic.id).slice(0, 4);
      const completion = Boolean(progress.completed[topic.id]);
      const learner = topic.learnerBrief;
      const pathInfo = firstReadPathFor(topic);
      const officialSlidesArePrimary = pathInfo.source === "official-slides";
      const teachingPrimer = teachingPrimerHTML(topic);
      const teachingSynthesis = teachingSynthesisHTML(topic);
      const deepDive = topic.teachingStory?.deep_dive;
      const deepDiveIsPrimary = deepDive && !deepDive.default_collapsed;
      const referenceIntro = topic.teachingStory && !officialSlidesArePrimary ? `<p class="reference-intro">${escapeHTML(topic.teachingStory.visual_intro)}</p>` : "";
      const usesImageLedPath = Boolean(pathInfo.path?.visuals?.length);
      const slideNavigator = `<nav class="lesson-path" aria-label="${escapeHTML(topic.model)} 的四張工程參考圖">${topic.slides.map(item => `<button type="button" data-action="jump-step" data-topic="${escapeHTML(topic.id)}" data-step="${item.index}"><strong>${String(item.index).padStart(2, "0")}</strong><span>${escapeHTML(item.label)}</span></button>`).join("")}</nav>`;
      const rawFormalSlides = officialSlidesArePrimary ? "" : topic.slides.map((slide, index) => lessonStepHTML(topic, slide, index === 0)).join("");
      const formalSlides = officialSlidesArePrimary ? "" : usesImageLedPath
        ? `<details class="formal-slide-reference" ${slideNumber > 1 ? "open" : ""}><summary>${topic.teachingStory?.engineering_slides ? "工程參考：展開四張工程圖與完整節點" : "工程參考：展開原有四張模型圖與完整節點"}<span>${topic.teachingStory?.engineering_slides ? "從輸入、機制、交付到限制，核對實作與驗證方式。" : "首讀主線已改用全幅工作例；這裡保留原圖，供設定、證據與術語核對。"}</span></summary><div class="formal-slide-reference-body">${referenceIntro}${slideNavigator}${rawFormalSlides}</div></details>`
        : `${slideNavigator}${rawFormalSlides}`;
      const advancedReference = deepDive?.default_collapsed
        ? `<details class="formal-slide-reference legacy-deep-reference" ${slideNumber > 1 ? "open" : ""}><summary>進階：既有實測與工程資料<span>展開八章內容與來源，核對原有實驗條件。</span></summary><div class="formal-slide-reference-body">${modelDeepDiveHTML(topic, slideNumber)}</div></details>`
        : "";
      const learningSequence = deepDiveIsPrimary
        ? modelDeepDiveHTML(topic, slideNumber)
        : usesImageLedPath
          ? `${teachingPrimer}${teachingSynthesis}${advancedReference}${formalSlides}`
          : `${teachingPrimer}${referenceIntro}${formalSlides}${teachingSynthesis}${advancedReference}`;
      const lessonMode = deepDiveIsPrimary ? "8 章完整導讀" : topic.teachingStory ? "先理解，再看工程圖" : "四圖連續導讀";
      return `<div class="content"><nav class="breadcrumb" aria-label="階層導覽"><button type="button" data-action="go" data-view="home">首頁</button><span>/</span><button type="button" data-action="filter-family" data-family="${escapeHTML(topic.family)}">${escapeHTML(topic.familyLabel)}</button><span>/</span><span>${escapeHTML(topic.model)}</span></nav><article aria-labelledby="lesson-title"><header class="lesson-head"><div><div class="chips"><span class="chip">${escapeHTML(topic.familyIcon)} ${escapeHTML(topic.familyLabel)}</span><span class="chip green">${lessonMode}</span></div><h1 id="lesson-title">${escapeHTML(topic.model)}</h1><p class="lesson-lead">${escapeHTML(topic.summary)}</p><div class="lesson-quickline" aria-label="先讀兩個重點"><div><strong>你會拿到：</strong>${escapeHTML(learner.deliverable)}</div><div><strong>先停下來：</strong>${escapeHTML(learner.hold)}</div></div></div><div class="lesson-actions"><button class="button ${completion ? "primary" : ""}" type="button" data-action="toggle-complete" data-topic="${escapeHTML(topic.id)}">${completion ? "✓ 已完成" : "完成本主題"}</button><button class="button" type="button" data-action="bookmark" data-topic="${escapeHTML(topic.id)}">${isBookmarked(topic.id) ? "★ 已收藏" : "☆ 收藏"}</button></div></header>${learningSequence}${engineerHandoffHTML(topic)}<section class="panel" style="margin-top:20px"><p class="eyebrow">相鄰比較</p><h2>下一個可比較的模型</h2><p style="color:var(--muted)">比較前，先把「看哪段畫面、用哪些資料、交出什麼、多久完成、誰覆核」固定；再到家族頁看共同條件與差異。</p><div class="related">${related.map(item => `<button class="button" type="button" data-action="lesson" data-topic="${escapeHTML(item.id)}">${escapeHTML(item.model)} →</button>`).join("")}<button class="button" type="button" data-action="filter-family" data-family="${escapeHTML(topic.family)}">查看家族比較 →</button></div></section><footer class="lesson-footer">${previous ? `<button class="button" type="button" data-action="lesson" data-topic="${escapeHTML(previous.id)}">← ${escapeHTML(previous.model)}</button>` : `<button class="button" type="button" data-action="go" data-view="home">← 回課程首頁</button>`}${next ? `<button class="button primary" type="button" data-action="lesson" data-topic="${escapeHTML(next.id)}">${escapeHTML(next.model)} →</button>` : `<button class="button primary" type="button" data-action="go" data-view="poc">建立 POC 畫布 →</button>`}</footer></article></div>`;
    }
    function supportingStoryHTML(item, index, collection) {
      const isImageLed = Boolean(item.imageLed);
      const firstRead = isImageLed ? "首讀主線 · 同一 AOI 的 image-led 因果故事（手機可左右滑讀圖）" : "已批准的共同教材 · 原圖可直接閱讀";
      const engineeringReference = item.engineeringImage ? `<details class="supporting-engineering-reference"><summary>工程參考：展開舊版節點／比較細節</summary><p>首讀請先看上方同一 AOI 的因果故事；這張舊圖只保留給需要核對術語與完整節點的工程閱讀。</p><a href="${escapeHTML(item.engineeringImage)}" target="_blank" rel="noopener" aria-label="開啟 ${escapeHTML(item.title)} 的舊版工程參考圖"><img loading="lazy" decoding="async" src="${escapeHTML(item.engineeringImage)}" width="1672" height="941" alt="${escapeHTML(item.title)} 的舊版工程參考圖"></a></details>` : "";
      return `<section id="support-${escapeHTML(collection.id)}-${escapeHTML(item.id)}" class="supporting-story" aria-labelledby="support-title-${escapeHTML(item.id)}"><p class="eyebrow">${escapeHTML(collection.label)} · ${String(index + 1).padStart(2, "0")}</p><h2 id="support-title-${escapeHTML(item.id)}">${escapeHTML(item.title)}</h2><p>${escapeHTML(item.summary)}</p><figure class="supporting-figure figure-card ${isImageLed ? "image-led-story" : ""}" data-image-led="${isImageLed ? "true" : "false"}"><a class="image-button" href="${escapeHTML(item.image)}" target="_blank" rel="noopener" aria-label="開啟 ${escapeHTML(item.title)} 原圖"><img data-asset src="${escapeHTML(item.image)}" width="1672" height="941" loading="lazy" decoding="async" alt="${escapeHTML(item.alt)}"></a><figcaption class="image-caption"><span>${firstRead}</span><a href="${escapeHTML(item.image)}" target="_blank" rel="noopener">開啟原圖 ↗</a></figcaption></figure>${engineeringReference}</section>`;
    }
    function supportingCollectionHTML(collectionId, selectedItems = null) {
      const collection = SUPPORTING[collectionId];
      if (!collection) return `<div class="content"><div class="empty"><h2>共同教材尚未載入</h2></div></div>`;
      const items = selectedItems || collection.items;
      return items.map((item, index) => supportingStoryHTML(item, index, collection)).join("");
    }
    function learningModulesHTML(collectionId, modules) {
      const collection = SUPPORTING[collectionId];
      return `<div class="learning-modules">${modules.map((module, index) => {
        const items = collection.items.slice(module.start, module.end);
        return `<details class="learning-module" ${index === 0 ? "open" : ""}><summary><span class="learning-module-index">${String(index + 1).padStart(2, "0")}</span><span><strong>${escapeHTML(module.title)}</strong><span>${escapeHTML(module.summary)}</span></span><span class="learning-module-count">${items.length} 張圖</span></summary><div class="learning-module-content">${supportingCollectionHTML(collectionId, items)}</div></details>`;
      }).join("")}</div>`;
    }
    function sharedJourneyHTML(id, title) {
      const journey = SHARED_JOURNEYS[id];
      if (!journey?.image) return "";
      return `<figure class="supporting-journey"><a href="${escapeHTML(journey.image)}" target="_blank" rel="noopener" aria-label="開啟 ${escapeHTML(title)} 的完整工作例"><img data-asset src="${escapeHTML(journey.image)}" width="1672" height="941" decoding="async" alt="${escapeHTML(journey.alt || '')}"></a><figcaption><strong>${escapeHTML(title)}</strong><span>${escapeHTML(journey.caption || '')}</span></figcaption></figure>`;
    }
    __WORKPLACE_UI__
    function glossaryHTML() {
      const terms = [
        ["ROI", "這次要分析的固定畫面範圍。範圍一變，分數就要重新驗證。", "例：只看晶圓上的同一個 die。"],
        ["模型交付物", "模型交出的東西，例如類別、方框、遮罩、可疑圖或文字建議；它不是最後動作。", "例：可疑圖送人工看，不直接停機。"],
        ["正常品參考", "用來告訴異常模型「平常長什麼樣」的乾淨樣本。", "例：只收沒有缺陷、光線正常的產品圖。"],
        ["候選", "值得再確認的區域、排序或圖；它還不是結論。", "例：框到一個零件後，再由專用檢查確認。"],
        ["門檻", "分數到多少時，下一步要送人看或暫停的規則。", "例：可疑分數超過 0.7 就送人工覆核。"],
        ["P95", "20 次作業裡最慢的一次，大約要多久完成。", "例：不是只量模型時間，要從拍照量到人工收到結果。"],
        ["超出範圍／漂移", "現場畫面慢慢變得不像測試時資料，模型可能不再可靠。", "例：換了鏡頭、照明或產品外觀後先停下驗證。"],
        ["人工覆核量", "每天有多少結果要人看，以及人是否來得及正確處理。", "例：誤報太多會讓真正的重要案例被淹沒。"],
        ["校正／對位", "讓同一個真實位置在不同畫面中能對得上的前提。", "例：晶圓轉了一點，先對齊再比較瑕疵。"],
        ["證據包", "能回查這次為何這樣判的一組資料與紀錄。", "例：原圖、模型版本、門檻、輸出、覆核人與結果。"],
        ["HOLD／REVIEW", "先停止自動往下走，保存資料並交給指定的人確認。", "例：畫面太暗、模型不確定或服務失敗時。"],
        ["原始證據", "感測器真正拍到或量到的資料。生成、修復和文字回答都不能取代它。", "例：放大後的影像可幫人看，但原圖才可回查。"],
      ];
      return `<div class="content"><header class="supporting-hero"><p class="eyebrow">讀圖字典 · 先懂再用</p><h1>不用背英文，<br>先說得出它在現場代表什麼。</h1><p class="supporting-intro">每張卡都只有三件事：這個詞的白話意思、它會影響什麼，以及一個 AOI 例子。看不懂技術詞時，先回這裡，不必硬讀完整研究名詞。</p><div class="action-row"><button class="button primary" type="button" data-action="go" data-view="foundations">回到共同前提教學圖 →</button></div></header><section class="glossary-grid">${terms.map(term => `<article class="glossary-card"><h3>${escapeHTML(term[0])}</h3><p>${escapeHTML(term[1])}</p><span class="glossary-example">${escapeHTML(term[2])}</span></article>`).join("")}</section></div>`;
    }
    __POC_WORKBENCH__

    function lightboxHTML(topic, slideNumber) {
      const index = slideNumber - 1;
      const slide = topic.slides[index];
      return `<div class="lightbox"><header class="lightbox-header"><span id="lightbox-title" class="lightbox-title">${escapeHTML(topic.model)} · ${String(slide.index).padStart(2, "0")} ${escapeHTML(slide.label)}</span><button class="icon-button" type="button" data-action="close-lightbox" aria-label="關閉圖片檢視">✕</button></header><div class="lightbox-image-wrap${slide.mobileImage ? ' engineering-zoom' : ''}">${engineeringMediaHTML(slide, true)}</div><footer class="lightbox-footer"><button class="button" type="button" data-action="lightbox-prev" ${slide.index === 1 ? "disabled" : ""}>← 上一張</button><span>${slide.index} / 4 · <a href="${escapeHTML(slide.image)}" target="_blank" rel="noopener">開啟原圖 ↗</a></span><button class="button" type="button" data-action="lightbox-next" ${slide.index === 4 ? "disabled" : ""}>下一張 →</button></footer></div>`;
    }
    function conceptLightboxHTML(visual) {
      return `<div class="lightbox"><header class="lightbox-header"><span id="lightbox-title" class="lightbox-title">${escapeHTML(visual.title)}</span><button class="icon-button" type="button" data-action="close-lightbox" aria-label="關閉概念圖檢視">✕</button></header><div class="lightbox-image-wrap concept-mode">${visualMediaHTML(visual, { loading: "eager", priority: true })}</div><footer class="lightbox-footer"><span>可在圖上左右滑動閱讀；完整文字仍在原頁。</span><a href="${escapeHTML(visual.image)}" target="_blank" rel="noopener">開啟原圖 ↗</a></footer></div>`;
    }
    function applyFamilyComparisonFraming(topic) {
      const authored = topic?.teachingStory?.comparison_headers;
      const framing = authored
        ? { title: authored.title, left: authored.basis, right: authored.output }
        : FAMILY_COMPARISON_FRAMING[topic?.family];
      const synthesis = main.querySelector(".teaching-synthesis");
      if (!framing || !synthesis) return;
      const title = synthesis.querySelector('[id^="comparison-title-"]');
      if (title) title.textContent = framing.title;
      const headings = synthesis.querySelectorAll(".teaching-comparison thead th");
      if (headings.length === 3) {
        headings[0].textContent = "方法";
        headings[1].textContent = framing.left;
        headings[2].textContent = framing.right;
      }
    }
    function injectFamilyEngineeringReferences() {
      const support = FAMILY_SUPPORT[app.familyFilter] || [];
      const stories = [...document.querySelectorAll(".family-support-story")];
      stories.forEach((story, index) => {
        const item = support[index];
        if (!item || !item.engineeringImage) return;
        const details = document.createElement("details");
        details.className = "family-engineering-reference";
        const summary = document.createElement("summary");
        summary.textContent = "工程參考：展開舊版 compact dashboard";
        const copy = document.createElement("p");
        copy.textContent = "上方 AOI 因果圖是首讀教材；舊版密集 dashboard 僅保留給工程交叉核對。";
        const anchor = document.createElement("a");
        anchor.className = "family-engineering-reference-visual";
        anchor.href = item.engineeringImage;
        anchor.target = "_blank";
        anchor.rel = "noopener";
        anchor.setAttribute("aria-label", `開啟工程參考：${item.title}`);
        const image = document.createElement("img");
        image.loading = "lazy";
        image.decoding = "async";
        image.src = item.engineeringImage;
        image.width = 1672;
        image.height = 941;
        image.alt = `舊版 compact dashboard：${item.title}`;
        anchor.append(image);
        details.append(summary, copy, anchor);
        story.append(details);
      });
    }
    function render() {
      const route = hashRoute();
      const currentRouteKey = routeKey(route);
      const routeChanged = Boolean(lastRenderedRouteKey) && currentRouteKey !== lastRenderedRouteKey;
      const shouldMoveToPageStart = (pendingRouteNavigation || routeChanged)
        && !(route.view === "lesson" && route.slide > 1);
      if (route.view === "library") app.familyFilter = route.family;
      sidebar.innerHTML = sidebarHTML(route);
      document.body.classList.remove("nav-open");
      const activeMobileButton = document.querySelector('[data-action="toggle-nav"]');
      if (activeMobileButton) activeMobileButton.setAttribute("aria-expanded", "false");
      if (route.view === "home") main.innerHTML = homeHTML();
      else if (route.view === "library") main.innerHTML = libraryHTML();
      else if (route.view === "foundations") main.innerHTML = foundationsHTML();
      else if (route.view === "production") main.innerHTML = productionHTML();
      else if (route.view === "glossary") main.innerHTML = glossaryHTML();
      else if (route.view === "poc") main.innerHTML = pocHTML();
      else main.innerHTML = lessonHTML(TOPIC_BY_ID[route.lesson], route.slide);
      if (route.view === "library") injectFamilyEngineeringReferences();
      if (route.view === "lesson") applyFamilyComparisonFraming(TOPIC_BY_ID[route.lesson]);
      document.querySelectorAll("img[data-asset]").forEach(image => image.addEventListener("error", () => {
        image.alt = "參考插圖無法載入；請確認 HTML 與 teaching-images 資料夾的相對位置未被改變。";
        image.style.minHeight = "160px";
      }, { once: true }));
      if (route.view === "lesson" && route.slide > 1) {
        requestAnimationFrame(() => jumpStep(route.lesson, route.slide));
      } else if (shouldMoveToPageStart) {
        requestAnimationFrame(scrollToRouteStart);
      }
      lastRenderedRouteKey = currentRouteKey;
      pendingRouteNavigation = false;
    }
    function chooseTrack(id) {
      const track = TRACKS.find(item => item.id === id);
      if (!track) return;
      const first = TOPIC_BY_ID[track.topics.find(topicId => TOPIC_BY_ID[topicId])];
      if (first) go("lesson", { lesson: first.id, slide: 1 });
    }
    function startFamily(id) {
      const family = FAMILY_BY_ID[id];
      if (!family) return;
      const firstId = (family.anchor || []).find(id => TOPIC_BY_ID[id]) || familyTopics(id)[0]?.id;
      if (firstId) go("lesson", { lesson: firstId, slide: 1 });
    }
    function jumpStep(topicId, rawStep, engineeringOnly = false) {
      const step = Number.parseInt(rawStep, 10);
      const activeChapter = document.querySelector(`[data-action="deep-dive-chapter"][data-topic="${CSS.escape(topicId)}"][data-chapter="${step}"]`);
      const chapterNav = activeChapter?.closest(".deep-dive-nav");
      if (activeChapter && chapterNav) {
        chapterNav.scrollTo({
          left: activeChapter.offsetLeft - (chapterNav.clientWidth - activeChapter.offsetWidth) / 2,
          behavior: "auto",
        });
      }
      const target = (!engineeringOnly && document.getElementById(`deep-dive-${topicId}-${step}`))
        || document.getElementById(`step-${topicId}-${step}`)
        || document.getElementById(`beginner-${topicId}-official-slide-${step}`);
      if (!target) return;
      const collapsedReference = target.closest("details");
      if (collapsedReference) collapsedReference.open = true;
      requestAnimationFrame(() => target.scrollIntoView({ behavior: "smooth", block: "start" }));
    }
    function jumpSupporting(collectionId, itemId) {
      const target = document.getElementById(`support-${collectionId}-${itemId}`);
      if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
    }
    function exportProgress() {
      const blob = new Blob([JSON.stringify(progress, null, 2)], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const anchor = document.createElement("a");
      anchor.href = url; anchor.download = "vision-ai-learning-progress.json"; anchor.click();
      setTimeout(() => URL.revokeObjectURL(url), 500);
      notify("已匯出學習與 POC 進度。 ");
    }
    function importProgress(file) {
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => {
        try {
          const parsed = JSON.parse(String(reader.result));
          if (!confirm("匯入將取代目前學習進度與 PoC 草稿，是否繼續？")) return;
          if (!parsed || typeof parsed !== "object") throw new Error("invalid");
          const { quiz: _legacyQuiz, ...stored } = parsed;
          progress = { ...structuredClone(DEFAULT_PROGRESS), ...stored, completed: validRecord(parsed.completed, {}), visited: validRecord(parsed.visited, {}), poc: validRecord(parsed.poc, {}), bookmarks: Array.isArray(parsed.bookmarks) ? parsed.bookmarks.filter(id => TOPIC_BY_ID[id]) : [] };
          pocUndo=null; app.pocPreview=false; setTheme(progress.theme); saveProgress(); notify("已匯入進度。 "); render();
        } catch (_) { notify("無法讀取這個進度檔。請確認它是本課程匯出的 JSON。 "); }
      };
      reader.readAsText(file, "utf-8");
    }
    document.addEventListener("click", event => {
      const trigger = event.target.closest("[data-action]");
      if (!trigger) return;
      const { action } = trigger.dataset;

      if (action === "workplace-scroll") { event.preventDefault(); const section = document.getElementById(trigger.dataset.workplaceAnchor); section?.scrollIntoView({behavior: "smooth", block: "start"}); return; }
      if (action === "production-candidate") {
        const example = trigger.closest(".workplace-example");
        example.querySelector(".production-example-result").innerHTML = productionExampleResult(trigger.dataset.candidate);
        example.querySelectorAll("[data-candidate]").forEach(button => { const active = button === trigger; button.setAttribute("aria-pressed", String(active)); button.classList.toggle("primary", active); });
        return;
      }

      if (action === "go") go(trigger.dataset.view);
      if (action === "lesson") go("lesson", { lesson: trigger.dataset.topic, slide: 1 });
      if (action === "filter-family") { app.search = ""; go("library", { family: trigger.dataset.family }); }
      if (action === "start-track") chooseTrack(trigger.dataset.track);
      if (action === "start-family") startFamily(trigger.dataset.family);
      if (action === "jump-step") jumpStep(trigger.dataset.topic, trigger.dataset.step, true);
      if (action === "reading-view") {
        const owner = trigger.closest(".reading-views");
        const selected = Number(trigger.dataset.view);
        owner.querySelectorAll(".reading-view-panel").forEach((panel, i) => { panel.hidden = i !== selected; });
        owner.querySelectorAll('[data-action="reading-view"]').forEach((button, i) => button.setAttribute("aria-pressed", String(i === selected)));
      }
      if (action === "deep-dive-chapter") {
        if (TOPIC_BY_ID[trigger.dataset.topic]?.teachingStory?.deep_dive?.default_collapsed) {
          jumpStep(trigger.dataset.topic, trigger.dataset.chapter);
        } else {
          go("lesson", { lesson: trigger.dataset.topic, slide: trigger.dataset.chapter });
        }
      }
      if (action === "jump-support") jumpSupporting(trigger.dataset.collection, trigger.dataset.item);
      if (action === "toggle-complete") toggleComplete(trigger.dataset.topic);
      if (action === "bookmark") toggleBookmark(trigger.dataset.topic);
      if (action === "send-to-poc") sendToPoc(trigger.dataset.topic);
      if (action === "fill-poc-example") fillPocExample();
      if (action === "clear-filters") { app.search = ""; go("library"); }
      if (action === "toggle-theme") setTheme(progress.theme === "dark" ? "light" : "dark");
      if (action === "toggle-nav") { const open = document.body.classList.toggle("nav-open"); trigger.setAttribute("aria-expanded", String(open)); }
      if (action === "open-lightbox") { const topic = TOPIC_BY_ID[trigger.dataset.topic]; app.concept = null; app.lightbox = { topic, slide: Number(trigger.dataset.slide) }; dialog.innerHTML = lightboxHTML(topic, app.lightbox.slide); if (typeof dialog.showModal === "function") dialog.showModal(); else dialog.setAttribute("open", ""); }
      if (action === "open-concept") { app.lightbox = null; const responsiveImage = trigger.closest('.workplace-figure')?.querySelector('picture img'); app.concept = { title: trigger.dataset.title, image: responsiveImage?.currentSrc || trigger.dataset.image, alt: trigger.dataset.alt }; dialog.innerHTML = conceptLightboxHTML(app.concept); if (typeof dialog.showModal === "function") dialog.showModal(); else dialog.setAttribute("open", ""); }
      if (action === "close-lightbox") { dialog.close(); app.lightbox = null; app.concept = null; }
      if (action === "lightbox-prev" && app.lightbox?.slide > 1) { app.lightbox.slide -= 1; dialog.innerHTML = lightboxHTML(app.lightbox.topic, app.lightbox.slide); }
      if (action === "lightbox-next" && app.lightbox?.slide < 4) { app.lightbox.slide += 1; dialog.innerHTML = lightboxHTML(app.lightbox.topic, app.lightbox.slide); }
      if (action === "export-progress") exportProgress();
      if (action === "clear-progress") { if (confirm("確定清除這台裝置的學習進度與 POC 草稿嗎？此操作不能復原。")) { progress = structuredClone(DEFAULT_PROGRESS); pocUndo=null; app.pocPreview=false; setTheme("light"); saveProgress(); notify("已清除本機進度。 "); render(); } }
      if (action === "poc-step") showPocStep(Number(trigger.dataset.step));
      if (action === "poc-missing") showPocStep(Number(trigger.dataset.step), trigger.dataset.field);
      if (action === "poc-preview") showPocPreview();
      if (action === "poc-model-hints") fillPocModelHints();
      if (action === "export-poc-markdown") exportPocMarkdown();
      if (action === "poc-undo" && pocUndo) { progress.poc=pocUndo; pocUndo=null; saveProgress(); render(); notify("已還原帶入前的草稿。"); }
      if (action === "poc-reset" && confirm("只清除 PoC 草稿？課程完成與收藏會保留。")) { pocUndo=structuredClone(progress.poc);progress.poc={};progress.pocStep=0;app.pocPreview=false;saveProgress();render(); }
      if (action === "print-poc") { updatePocUI(); window.print(); }
    });
    document.addEventListener("input", event => {
      if (event.target.id === "global-search" || event.target.id === "library-search") {
        app.search = event.target.value;
        if (hashRoute().view !== "library") go("library", { family: app.familyFilter }); else render();
      }
      if (event.target.id === "poc-model-search") {
        const query=event.target.value.trim().toLocaleLowerCase();const select=document.getElementById("poc-model");
        const matches=TOPICS.filter(t=>(t.model+" "+t.familyLabel).toLocaleLowerCase().includes(query));
        const selected=TOPIC_BY_ID[pocValue("model")];const options=selected&&!matches.includes(selected)?[selected,...matches]:matches;
        select.innerHTML='<option value="">尚未選擇</option>'+options.map(t=>`<option value="${escapeHTML(t.id)}" ${t.id===pocValue("model")?"selected":""}>${escapeHTML(t.model)} · ${escapeHTML(t.familyLabel)}</option>`).join("");
        document.getElementById("poc-model-count").textContent=`找到 ${matches.length} 個模型${selected&&!matches.includes(selected)?"；保留目前選擇":""}。`;
      }
      if (event.target.dataset.poc && event.target.tagName !== "SELECT") { progress.poc[event.target.dataset.poc] = event.target.value; saveProgress(); updatePocUI(); }
    });
    document.addEventListener("change", event => {
      if (event.target.id === "family-filter") { go("library", { family: event.target.value }); }
      if (event.target.dataset.poc && event.target.tagName === "SELECT") { progress.poc[event.target.dataset.poc] = event.target.value; saveProgress(); updatePocUI(true); }
      if (event.target.id === "import-progress") importProgress(event.target.files?.[0]);
    });
    document.addEventListener("keydown", event => {
      const typing = /INPUT|TEXTAREA|SELECT/.test(document.activeElement?.tagName || "");
      if (event.key === "/" && !typing && !dialog.open) { event.preventDefault(); document.getElementById("global-search")?.focus(); }
      if (event.key === "Escape" && dialog.open) { dialog.close(); app.lightbox = null; }
      if (dialog.open && app.lightbox && event.key === "ArrowLeft" && app.lightbox.slide > 1) { app.lightbox.slide -= 1; dialog.innerHTML = lightboxHTML(app.lightbox.topic, app.lightbox.slide); }
      if (dialog.open && app.lightbox && event.key === "ArrowRight" && app.lightbox.slide < 4) { app.lightbox.slide += 1; dialog.innerHTML = lightboxHTML(app.lightbox.topic, app.lightbox.slide); }
      const route = hashRoute();
      if (!typing && !dialog.open && route.view === "lesson" && (event.key === "ArrowLeft" || event.key === "ArrowRight")) {
        const next = route.slide + (event.key === "ArrowRight" ? 1 : -1);
        const maxSlide = TOPIC_BY_ID[route.lesson]?.teachingStory?.deep_dive?.chapters?.length || 4;
        if (next >= 1 && next <= maxSlide) { event.preventDefault(); go("lesson", { lesson: route.lesson, slide: next }); }
      }
    });
    dialog.addEventListener("cancel", () => { app.lightbox = null; app.concept = null; });
    window.addEventListener("hashchange", render);
    render();
  })();
  </script>
</body>
</html>
'''


def build(output: Path) -> None:
    data = make_course_data()
    serialized = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    serialized = serialized.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    document = HTML_TEMPLATE.replace("__COURSE_DATA__", serialized)
    document = document.replace("__POC_WORKBENCH__", (ROOT / "_course_content/poc-workbench.js").read_text(encoding="utf-8"))
    document = document.replace("__POC_CSS__", (ROOT / "_course_content/poc-workbench.css").read_text(encoding="utf-8"))
    document = document.replace("__WORKPLACE_UI__", (ROOT / "_course_content/supporting-lessons/ui.js").read_text(encoding="utf-8"))
    document = document.replace("__WORKPLACE_CSS__", (ROOT / "_course_content/supporting-lessons/ui.css").read_text(encoding="utf-8"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8", newline="\n")
    print(f"Wrote {output}")
    print(f"Topics: {len(data['topics'])}; images: {sum(len(topic['slides']) for topic in data['topics'])}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    data = make_course_data()
    if args.validate_only:
        print(f"Validated {len(data['topics'])} topics and {sum(len(topic['slides']) for topic in data['topics'])} active PNG references.")
        return
    build(args.output)


if __name__ == "__main__":
    main()
