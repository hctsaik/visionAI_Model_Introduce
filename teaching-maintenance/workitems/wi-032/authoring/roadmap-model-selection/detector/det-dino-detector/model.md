# DINO detector（`det-dino-detector`）

- roadmap 分類：`detector`
- 講義對照：`03-10`～`03-13`
- 內容覆蓋狀態：`complete`
- 產生狀態：`self-reviewed-tested; user-approval-pending`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/det-dino-detector.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
要在料盤裡找出每顆螺栓與墊圈，需要物件框和類別。DINO detector在DETR式查詢出框的基礎上改善訓練訊號；它不是拿正常品特徵查庫的DINOv2骨幹。

### 它交出什麼，也不交出什麼
每個候選物件的框、類別與分數；工件計數、是否漏裝、尺寸與品質判定是後續規則與驗證。需要精確輪廓時另選分割流程，框不能當mask。

### 一句心智模型
DINO detector的對比去噪訓練，從人工真值產生帶噪查詢：較接近的正樣本學還原物件框／類別，較偏離的負樣本學無物件，提供辨別訊號。這些真值帶噪查詢只存在訓練；推論由影像特徵選取初始框位置並經decoder查詢更新，交出已學類別與框，不會拿到真值。

**限制：** 同一料盤的墊圈被夾具遮住後，模型仍可能漏檢。帶噪框訓練不等於已涵蓋所有遮擋情況；圖中是假設漏檢示意，要回到逐件標註核對，而不是只看找到的框。

### 換一個現場再推理
A線只找三種固定零件且有完整框標註；B線每週新增零件名稱，但幾乎沒有目標場景標註。

**問題：** 兩條線都應只因DINO的訓練設計而優先選它嗎？

**核對：** A線可比較DINO與既有固定類別偵測器，用同資料看漏檢和完整成本；有現成標註讓微調較可行。B線可先用YOLO-World的文字詞彙測候選，但仍需建立獨立核對集；如果新零件外觀太相近或是細缺陷，提示詞未必足夠，可能仍需取像改善與標註微調。沒有目標資料時不能替任一方法承諾現場準確率。
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


<!-- wi032-model-core:start -->
## WI-032 核心做法與工作取捨

DINO detector的對比去噪訓練，從人工真值產生帶噪查詢：較接近的正樣本學還原物件框／類別，較偏離的負樣本學無物件，提供辨別訊號。這些真值帶噪查詢只存在訓練；推論由影像特徵選取初始框位置並經decoder查詢更新，交出已學類別與框，不會拿到真值。

同一料盤的墊圈被夾具遮住後，模型仍可能漏檢。帶噪框訓練不等於已涵蓋所有遮擋情況；圖中是假設漏檢示意，要回到逐件標註核對，而不是只看找到的框。

DINO detector通常由固定類別的監督訓練建立分類頭；YOLO-World用預訓練視覺語言表示和文字詞彙產生候選。固定少數類別且能準備標註時，可比較DINO與既有YOLO／RT-DETR；類別詞彙經常變更可試YOLO-World，但仍要驗證現場資料，不能只按新舊或論文成績選。

換固定類別通常涉及標註／模型頭與微調流程，換拍攝條件也需重新驗證。DINO的訓練成本、輸入尺寸與查詢數會影響部署取捨；比較需包含前後處理及人工覆核，不借用跨硬體FPS排名。

定義螺栓／墊圈等類別和每件框標註，依實體工件與拍攝批次隔離訓練／驗證／測試；選明確DINO版本與預訓練checkpoint，再評估是否微調。

保存模型與前處理版本、原圖、逐件真值和輸出框，分別查漏檢、錯類、重複框及遮擋／小目標；量同硬體的完整延遲與覆核負擔。本輪沒有重訓或推論，去噪與漏檢圖皆為教學示意。

來源：https://arxiv.org/abs/2203.03605

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi032-model-core:end -->

<!-- wi032-engineering:start -->
## 工程層：輸入、機制、部署與限制

### 固定類別偵測：先把學習任務定清楚

本課討論DINO DETR系檢測器。模型交付物件框、類別與分數，而像素分割、毫米尺寸及業務計數規則需其他流程；訓練/驗證分組應避免同工件或連續影像泄漏。

DINO detector是偵測器，不是DINOv2特徵骨幹。

來源：https://arxiv.org/abs/2203.03605

### Mixed query selection：位置與內容分開來

DINO mixed query selection以encoder候選提供位置初始化，同時使用可學習內容queries。decoder進一步精修框與類別；與訓練專用的GT noisy queries區分，不能把二者畫在同一推論路徑。

推論起點來自影像，不是人工真值框。

來源：https://arxiv.org/abs/2203.03605

### 對比去噪：正負查詢的學習目標不同

正負帶噪查詢以不同噪聲范圍構建，正樣本學習還原對應GT框/類，負樣本學習無物件。噪聲示意不是實際采樣統計；不能將no-object目標解釋為原圖里真的沒有物件。

帶噪查詢是訓練輔助，正式推論不用真值。

來源：https://arxiv.org/abs/2203.03605

### 新增類別，不能只改顯示名稱

與YOLO-World開放詞匯路線相比，DINO固定類別通常需相應模型頭與監督訓練/微調。二者都需現場獨立數據驗證；改變標注或閾值也應重新量測錯誤與完整成本。

按類別變更與資料成本選方法，不按模型新舊。

來源：https://arxiv.org/abs/2203.03605

<!-- wi032-engineering:end -->
