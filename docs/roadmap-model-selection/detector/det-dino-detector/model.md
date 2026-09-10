# DINO detector（`det-dino-detector`）

- roadmap 分類：`detector`
- 講義對照：`03-10`～`03-13`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/det-dino-detector.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
DETR式偵測要同時學會找物件、定位置和分配預測責任，訓練不容易。DINO detector用帶噪標註的輔助練習、較好的框起點與逐層修正改善學習。這裡的DINO是有監督物件偵測器，不是自監督DINO或DINOv2。

### 它交出什麼，也不交出什麼
模型交出物件候選框與相關分數；需回映原圖供後續確認。 需要框與類別監督資料；換缺陷定義或產品後重查標註並視需要重訓。量漏件、重複、訓練成本和完整P95；不以DINO名稱推定比RT-DETR或YOLO更適合本站。

### 一句心智模型
DETR式偵測要同時學會找物件、定位置和分配預測責任，訓練不容易。DINO detector用帶噪標註的輔助練習、較好的框起點與逐層修正改善學習。這裡的DINO是有監督物件偵測器，不是自監督DINO或DINOv2。

**限制：** 需要框與類別監督資料；換缺陷定義或產品後重查標註並視需要重訓。量漏件、重複、訓練成本和完整P95；不以DINO名稱推定比RT-DETR或YOLO更適合本站。

### 換一個現場再推理
新產品只有正常影像；要先找元件位置，未來還想取得輪廓。本站另有固定節拍與漏件容許量。

**問題：** 能直接用模型名稱宣稱找出未知缺陷嗎？你會如何起步，還需要哪些資料與驗證？

**核對：** 先固定要找的物件與輸出：前三者需已知類別框監督；後三者借助預訓練與提示探索。開放詞彙不等於免驗證，只有正常品時先做物件探索與覆核，不能宣稱已建立未知缺陷偵測。 同一資料切分、輸入像素、硬體與漏件容許量下，量漏件／重複／誤框、P95、記憶體及人工覆核。換產品要重查標註、詞彙／範例與門檻；需要輪廓時選支援mask的checkpoint或另接分割，不把box當輪廓。 可先用提示模型探索並人工确认，或標註框後訓練已知類別模型；方案取決於目標、資料及驗證，不只一個正確模型名稱。
<!-- topic-learning-bridge:end -->
## 模型定位

DINO detector 是 supervised DETR-family end-to-end object detector，名稱意指 improved denoising anchor boxes。它以 contrastive denoising training、mixed query selection 與 iterative box refinement 改善 DETR 訓練與定位；不是 DINOv2/DINOv3 visual encoder，也不是 VLM。

## 必要欄位

### architecture_path

固定 image/ROI → backbone multi-scale features → encoder → mixed query selection／anchor initialization → detection object queries → decoder cross-attention → iterative box refinement → class/box set。訓練時另加入由 noisy ground-truth labels/boxes 建立的 contrastive denoising groups；推論時移除 denoising branch，只保留 detection path。

### representation_or_score

Representation 是 multi-scale encoded features、object queries/reference boxes 與逐層 refined boxes/classes；不是 patch retrieval embedding。Detection queries 以 bipartite matching/set loss 對應 targets；denoising queries 是訓練輔助責任，不得畫成推論輸入或量產輸出。

### cost_and_operating_point

鎖 implementation/checkpoint、backbone、multi-scale levels、query count、mixed query selection、denoising groups/noise、decoder layers、matching/loss、epochs/schedule、augmentation、input、precision/export/runtime。報告依 object-size/product/ROI 拆 critical recall、false alarms、VRAM、training cost 與 camera-to-decision P95；不可用 COCO AP 取代 fab qualification。

### failure_boundary

Optics/resize 欠採樣的 tiny object 無法由 denoising 補回；query capacity、密集重疊、label/ignore contract、長 schedule、memory/export operators、domain/taxonomy shift 與 OOD 都可能造成 miss、錯類或不可部署。Denoising improves training，不是 inference-time anomaly detector。

### selection_gate

在 closed-set box task、需要深入比較 query-detector 訓練/定位且可承擔 schedule/memory/export 複雜度時評估。固定 boxes/ignore zones、effective pixels、train budget、hardware、decision unit、threshold/postprocess，和 RT-DETR/YOLO/Deformable-style baseline 比 critical-size recall、overlap misses、calibration、false HOLD、P95、VRAM 與 review load。Gate 未通過時 HOLD/REVIEW。

### evidence_bundle

保存 implementation/checkpoint、backbone/levels、query count/selection、denoising configuration、decoder/refinement、matching/loss、schedule/augmentation、input/padding、label/ignore revision、product/ROI/lot split、critical-size recall、overlap misses、calibration、training cost、VRAM、export graph、P95 與 failure images。

## 視覺 primitive

- `input_roi`：不同 size/product/ROI 與 overlap 的 known objects。
- `feature_path`：multi-scale features → encoder → mixed query selection → decoder/refinement。
- `candidate_or_query`：detection queries/reference boxes；與 training-only noisy GT denoising groups 分開。
- `assignment_or_matching`：bipartite matching/set loss；denoising reconstruction responsibility。
- `box_output`：iterative refinement → set predictions → inverse mapping/ROI crops。
- `runtime_gate`：size-bin recall、schedule/memory/export、P95、shift/OOD → HOLD/REVIEW。

## 比較契約

- 比較 ID：`det-dino-deformable-rtdetr-dense-matrix`
- 固定條件：相同 image/ROI、boxes/ignore zones、effective pixels、train budget、hardware、decision unit、threshold/postprocess 與 output/query capacity。
- 共同比較輸出：critical-size recall、false alarms/HOLD、overlap misses、calibration、training cost、VRAM、P95 與 review load；不得以 COCO AP 排名。

## 來源

- Hao Zhang et al., “DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection,” arXiv:2203.03605。
- `full-model-course/03-detectors-and-open-vocabulary.md` 的 03-10～03-13。

## 產生 gate

六個必要欄位與六個 visual primitives 已完成模型專屬遷移；可開始產生 03-10～03-13 的版本化 C/D 教學頁，逐張通過 QA 後才能 approved。

## D01 核心主線與來源補正

此節是2026-09-06本輪主線的補正；舊例若只展示部分路徑，不可據此當作模型全部能力。

DETR式偵測要同時學會找物件、定位置和分配預測責任，訓練不容易。DINO detector用帶噪標註的輔助練習、較好的框起點與逐層修正改善學習。這裡的DINO是有監督物件偵測器，不是自監督DINO或DINOv2。

**對比去噪，練習辨認接近與偏離的框**：訓練時由GT類別與框製造擾動：正例學恢復目標，負例學無物件，幫助辨別同物件附近的重複候選。去噪指標註／框練習，不是把影像變乾淨；推論不用GT或去噪queries。

**Mixed query selection分開位置與內容**：從encoder選出的框提供位置起點，content query仍使用可學習表示。不是把所有query內容都直接複製影像特徵，也不是每個query預先綁定某類別。

**逐層改框，改善修正的學習**：decoder逐步更新參考框；look-forward-twice在訓練讓後續框損失也幫助前一階段框更新學習。它不是測試時看兩張未來影像，也不是去噪必然令本站更準的保證。

自測：如果正式檢查時沒有GT框，就不能使用DINO detector嗎？拿掉訓練去噪分支又少了什麼？

解釋：正式推論本來就不需要GT，走影像、queries與框修正路徑。拿掉的是訓練期間有標註依據的恢復／排除輔助練習，不是測試功能；其學習速度或準確率影響要以受控訓練比較，不能捏造曲線。

工作接法：需要框與類別監督資料；換缺陷定義或產品後重查標註並視需要重訓。量漏件、重複、訓練成本和完整P95；不以DINO名稱推定比RT-DETR或YOLO更適合本站。

[原論文／官方文件](https://arxiv.org/abs/2203.03605)。D01核心與反例圖為既有素材加受控設定，沒有新模型推論。
