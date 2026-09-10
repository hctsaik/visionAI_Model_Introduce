# WI-031：58課依Markdown標準重新審查

審查完成日期：2026-09-11。審查的是當前58個Topic，另外兩個補充單元不計入。教材與發布檔未修改。

## 判斷結果

| 整課分類 | 課數 | 意義 |
| --- | ---: | --- |
| 符合標準 | **0** | 本輪沒有一課能連同展開工程圖一起判定全課符合。 |
| 局部修正 | **52** | 主線故事、機制及反例可保留；工程圖、指定深讀圖或手機排版需修正。局部可能包含整組工程圖重畫。 |
| 需要重建 | **6** | ChArUco、ECC、SIFT、LightGlue、DINO detector、YOLO-World；核心機制或主要閱讀路徑需要重建。 |

**這個結論不代表58課都要推倒重來。** 52課新版首讀主線多數已有具體案例、可追的中間變化及反例；主要落差是仍然啟用的舊工程圖。6課的問題則已影響首讀教學本身。先前某一輪首讀自評通過，不等於本輪包含所有展開層的整課合格。

## 標準與判定方式

以專案五份權威Markdown為準：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_WEBPAGE_GUIDE.md、TEACHING_SCORING_RUBRIC.md、TEACHING_REVIEW_LOG.md，並參照閱讀層契約。基準檔案hash見[baseline.json](baseline.json)。本輪未改量表權重或門檻。

- 圖片：案例25／機制25／人的行動20／閱讀20／一致性10；頁面：工作20／機制20／交付20／比較20／閱讀10／遷移自測10。原標準要求頁與每張圖各大於90、完整度達標且無否決項。
- 本輪是重新診斷與分類，**沒有替644個資產各編一個分數**。發現「只有名詞沒有可見機制」、「輸出類型畫錯」、「替代方案誤串成流程」等實質缺口，即不能宣稱已符合嚴格整課門檻。逐課指出缺口，而不靠舊分數推算通過。
- 比較要在同一工作與相同條件下成立；圖要看得到方法造成的改變，不能只換模型名稱。主線、工程、深讀分開判斷；有來源的實測與生成示意分開。
- 小頁碼徽章或單純間距擁擠不是主線重建理由；進階公式及有因果必要的第五節點也不一律否決。自評、技術檢查與使用者成品核准分開，本輪未推定使用者核准。

## 家族統計

| 家族 | 課數 | 符合 | 局部修正 | 主線重建 |
| --- | ---: | ---: | ---: | ---: |
| 幾何／校正 | 4 | 0 | 0 | 4 |
| 分類／分割／姿態 | 8 | 0 | 8 | 0 |
| 物件偵測 | 6 | 0 | 4 | 2 |
| 異常偵測 | 17 | 0 | 17 | 0 |
| 影片／時序 | 8 | 0 | 8 | 0 |
| 視覺基礎／多模態 | 7 | 0 | 7 | 0 |
| 生成／影像復原 | 8 | 0 | 8 | 0 |

## 逐課總表

每課名稱連到本輪保存的主線正文；「主圖／手機／工程」連到實際截圖。更多同課圖、自測、操作卡與互動紀錄位於同一資料夾。共享圖以[相同路徑及hash清單](shared-image-evidence.json)重用視覺證據，各課正文和引用仍逐課檢查。全部機器可讀結果見[results.json](results.json)。

### 幾何／校正

| 課程 | 分類 | 可保留 | 需要修正／重建的範圍 | 截圖證據 |
| --- | --- | --- | --- | --- |
| [ChArUco](pages/charuco/1440-reading.txt) | **需要重建** | 標靶ID、已知座標、覆蓋率與重投影驗證概念 | 重建核心與手機閱讀路徑；R07英文密圖與舊SVG混用，校正求內參／已知內參求姿態未清楚分流；移除正文candidate製作註記。 | [主圖](pages/charuco/panel-desktop-1.png)／[手機](pages/charuco/panel-mobile-1.png)／[工程1–2](pages/charuco/panel-engineering-1.png)／[工程3–4](pages/charuco/panel-engineering-2.png) |
| [ECC](pages/ecc/1440-reading.txt) | **需要重建** | 32/12位移與遠起點217px失敗證據；工程4反光／遮擋／視差案例可保留 | 主圖反覆縮小同照片，0.2px殘差無放大證據；重建迭代對齊的中間變化與工作比較，遷移題增加新條件；工程1–3重畫，勿丟棄工程4。 | [主圖](pages/ecc/panel-desktop-1.png)／[手機](pages/ecc/panel-mobile-1.png)／[工程1–2](pages/ecc/panel-engineering-1.png)／[工程3–4](pages/ecc/panel-engineering-2.png) |
| [SIFT](pages/sift/1440-reading.txt) | **需要重建** | 120點／104匹配與模糊46點／4匹配案例 | 描述子只有名稱與點線，未顯示梯度／方向／描述與篩選；重建核心圖和手機圖，修正「4條線約束不住」的過度絕對說法，補錯配與退化条件。 | [主圖](pages/sift/panel-desktop-1.png)／[手機](pages/sift/panel-mobile-1.png)／[工程1–2](pages/sift/panel-engineering-1.png)／[工程3–4](pages/sift/panel-engineering-2.png) |
| [LightGlue](pages/lightglue/1440-reading.txt) | **需要重建** | extractor→matcher→幾何求解分工，以及未載入LightGlue權重的示意聲明 | 注意力、信心、修剪只換標籤，候選關係沒有可見變化；重建核心／比較／遷移題；反例圖說重複金屬與實際模糊案例不一致。 | [主圖](pages/lightglue/panel-desktop-1.png)／[手機](pages/lightglue/panel-mobile-1.png)／[工程1–2](pages/lightglue/panel-engineering-1.png)／[工程3–4](pages/lightglue/panel-engineering-2.png) |

### 分類／分割／姿態

| 課程 | 分類 | 可保留 | 需要修正／重建的範圍 | 截圖證據 |
| --- | --- | --- | --- | --- |
| [ResNet](pages/resnet/1440-reading.txt) | **局部修正** | 同形狀x+F(x)、背景捷徑反例與方法比較 | 工程圖未呈現殘差相加及分類輸出；深讀手機2/4/8章小字與數值重排，保留實際特徵與pooling反例。 | [主圖](pages/resnet/panel-desktop-1.png)／[手機](pages/resnet/panel-mobile-1.png)／[工程1–2](pages/resnet/panel-engineering-1.png)／[工程3–4](pages/resnet/panel-engineering-2.png) |
| [ConvNeXt](pages/convnext/1440-reading.txt) | **局部修正** | 空間混合／通道混合／殘差及背景反例 | 重畫工程圖的空間與通道變化，交付分類結果，不能用通用熱點取代；主線保留。 | [主圖](pages/convnext/panel-desktop-1.png)／[手機](pages/convnext/panel-mobile-1.png)／[工程1–2](pages/convnext/panel-engineering-1.png)／[工程3–4](pages/convnext/panel-engineering-2.png) |
| [ViT](pages/vit-classifier/1440-reading.txt) | **局部修正** | patch、位置、注意力與CLS分類 | 工程圖補token如何交換資訊與分類讀出；通用PCB條塊／热點不能交代ViT機制。 | [主圖](pages/vit-classifier/panel-desktop-1.png)／[手機](pages/vit-classifier/panel-mobile-1.png)／[工程1–2](pages/vit-classifier/panel-engineering-1.png)／[工程3–4](pages/vit-classifier/panel-engineering-2.png) |
| [U-Net](pages/u-net/1440-reading.txt) | **局部修正** | 多尺度skip與細焊線分割反例 | 工程圖重畫編碼／解碼與同尺度skip，輸出語意遮罩，不能以通用熱點代替。 | [主圖](pages/u-net/panel-desktop-1.png)／[手機](pages/u-net/panel-mobile-1.png)／[工程1–2](pages/u-net/panel-engineering-1.png)／[工程3–4](pages/u-net/panel-engineering-2.png) |
| [SegFormer](pages/segformer/1440-reading.txt) | **局部修正** | 四尺度特徵、對齊與MLP融合 | 工程圖補四尺度至語意遮罩；深讀手機1章標題靠邊、3–5章細網格與標註重排。 | [主圖](pages/segformer/panel-desktop-1.png)／[手機](pages/segformer/panel-mobile-1.png)／[工程1–2](pages/segformer/panel-engineering-1.png)／[工程3–4](pages/segformer/panel-engineering-2.png) |
| [YOLO-Seg](pages/yolo-seg/1440-reading.txt) | **局部修正** | YOLOv8式prototype與每物件係數組合 | 工程圖重畫prototype×係數及實例遮罩，區分同類物件，避免通用熱點。 | [主圖](pages/yolo-seg/panel-desktop-1.png)／[手機](pages/yolo-seg/panel-mobile-1.png)／[工程1–2](pages/yolo-seg/panel-engineering-1.png)／[工程3–4](pages/yolo-seg/panel-engineering-2.png) |
| [Keypoint R-CNN](pages/keypoint-r-cnn/1440-reading.txt) | **局部修正** | ROI熱圖A/B/C與映回原圖 | 工程圖補ROI座標至原圖座標，保留每關鍵點身份與可見性，不能用無身份熱區代替。 | [主圖](pages/keypoint-r-cnn/panel-desktop-1.png)／[手機](pages/keypoint-r-cnn/panel-mobile-1.png)／[工程1–2](pages/keypoint-r-cnn/panel-engineering-1.png)／[工程3–4](pages/keypoint-r-cnn/panel-engineering-2.png) |
| [Pose Pipeline](pages/pose/1440-reading.txt) | **局部修正** | 已知K／畸變、3D–2D對應、R/t、重投影與站點交付 | 工程2把top-down與bottom-up替代方法串接，改分支；工程輸出應是座標／姿態／誤差，主線保留。 | [主圖](pages/pose/panel-desktop-1.png)／[手機](pages/pose/panel-mobile-1.png)／[工程1–2](pages/pose/panel-engineering-1.png)／[工程3–4](pages/pose/panel-engineering-2.png) |

### 物件偵測

| 課程 | 分類 | 可保留 | 需要修正／重建的範圍 | 截圖證據 |
| --- | --- | --- | --- | --- |
| [YOLO dense detector](pages/det-yolo-dense/1440-reading.txt) | **局部修正** | YOLOv8式密集候選、NMS與4→2框反例 | 工程圖補具體候選框、分數與去重前後；主線及與RT-DETR的工作比較保留。 | [主圖](pages/det-yolo-dense/panel-desktop-1.png)／[手機](pages/det-yolo-dense/panel-mobile-1.png)／[工程1–2](pages/det-yolo-dense/panel-engineering-1.png)／[工程3–4](pages/det-yolo-dense/panel-engineering-2.png) |
| [RT-DETR](pages/det-rtdetr/1440-reading.txt) | **局部修正** | 混合編碼、query修框與一對一訓練 | 工程圖補query和框的逐步變化，分清訓練匹配／推論；熱點不能代表偵測框。 | [主圖](pages/det-rtdetr/panel-desktop-1.png)／[手機](pages/det-rtdetr/panel-mobile-1.png)／[工程1–2](pages/det-rtdetr/panel-engineering-1.png)／[工程3–4](pages/det-rtdetr/panel-engineering-2.png) |
| [DINO detector](pages/det-dino-detector/1440-reading.txt) | **需要重建** | 正負去噪查詢僅用訓練的文字界線 | 主圖工件小而模糊、核心只有名詞；重建帶噪框如何提供學習訊號、推論如何出框；第四圖段落重複，自測需可遷移條件。 | [主圖](pages/det-dino-detector/panel-desktop-1.png)／[手機](pages/det-dino-detector/panel-mobile-1.png)／[工程1–2](pages/det-dino-detector/panel-engineering-1.png)／[工程3–4](pages/det-dino-detector/panel-engineering-2.png) |
| [Grounding DINO](pages/det-grounding-dino-interface/1440-reading.txt) | **局部修正** | 文字與影像交互作用及可見框的限制 | 工程圖把文字／影像互動改成可見token–區域對應與框；主線保留，避免通用熱點輸出。 | [主圖](pages/det-grounding-dino-interface/panel-desktop-1.png)／[手機](pages/det-grounding-dino-interface/panel-mobile-1.png)／[工程1–2](pages/det-grounding-dino-interface/panel-engineering-1.png)／[工程3–4](pages/det-grounding-dino-interface/panel-engineering-2.png) |
| [YOLO-World](pages/yolo-world/1440-reading.txt) | **需要重建** | 離線詞彙預計算／快取與文字不是布林NOT的界線 | 重建文字嵌入如何影響候選及輸出框；現主線主要靠文字和重複小PCB，手機更難讀，第四圖重複段落與自測需改。 | [主圖](pages/yolo-world/panel-desktop-1.png)／[手機](pages/yolo-world/panel-mobile-1.png)／[工程1–2](pages/yolo-world/panel-engineering-1.png)／[工程3–4](pages/yolo-world/panel-engineering-2.png) |
| [YOLOE](pages/yoloe/1440-reading.txt) | **局部修正** | 文字／視覺提示、SAVPE ROI與權重的分工 | 工程圖補提示區域如何轉為表示及對應框，勿只列提示名稱；主線保留。 | [主圖](pages/yoloe/panel-desktop-1.png)／[手機](pages/yoloe/panel-mobile-1.png)／[工程1–2](pages/yoloe/panel-engineering-1.png)／[工程3–4](pages/yoloe/panel-engineering-2.png) |

### 異常偵測

| 課程 | 分類 | 可保留 | 需要修正／重建的範圍 | 截圖證據 |
| --- | --- | --- | --- | --- |
| [PatchCore](pages/ad-patchcore/1440-reading.txt) | **局部修正** | 正常特徵庫、coreset、最近鄰與污染反例 | 工程圖重畫實際查庫距離及熱圖來源；深讀手機2章數值與留白重排，保留作者／第三方漏檢誤報案例。 | [主圖](pages/ad-patchcore/panel-desktop-1.png)／[手機](pages/ad-patchcore/panel-mobile-1.png)／[工程1–2](pages/ad-patchcore/panel-engineering-1.png)／[工程3–4](pages/ad-patchcore/panel-engineering-2.png) |
| [PaDiM](pages/ad-padim/1440-reading.txt) | **局部修正** | 同位置均值／協方差與距離 | 工程圖須呈現同位置分布、相關方向及異常距離，通用條塊未交代位置統計。 | [主圖](pages/ad-padim/panel-desktop-1.png)／[手機](pages/ad-padim/panel-mobile-1.png)／[工程1–2](pages/ad-padim/panel-engineering-1.png)／[工程3–4](pages/ad-padim/panel-engineering-2.png) |
| [AnomalyDINO](pages/ad-anomalydino/1440-reading.txt) | **局部修正** | 固定DINOv2、參考庫與最近鄰；深讀最高1%聚合及作者反例 | 工程圖補固定特徵與查庫；深讀6章180度旋轉板仍留正向刻字，應用同一圖剛性旋轉重做該反例，手機細字重排。 | [主圖](pages/ad-anomalydino/panel-desktop-1.png)／[手機](pages/ad-anomalydino/panel-mobile-1.png)／[工程1–2](pages/ad-anomalydino/panel-engineering-1.png)／[工程3–4](pages/ad-anomalydino/panel-engineering-2.png) |
| [SubspaceAD](pages/ad-subspacead/1440-reading.txt) | **局部修正** | 正常子空間、正交殘差與全維投影反例 | 工程圖重畫投影幾何，工程2公式缺字方框需修；主線保留。 | [主圖](pages/ad-subspacead/panel-desktop-1.png)／[手機](pages/ad-subspacead/panel-mobile-1.png)／[工程1–2](pages/ad-subspacead/panel-engineering-1.png)／[工程3–4](pages/ad-subspacead/panel-engineering-2.png) |
| [STFPM](pages/ad-stfpm/1440-reading.txt) | **局部修正** | 固定教師／學生的多尺度特徵差 | 工程圖補同位置不同層的教師學生對照及差異彙整，不能只放一般熱點。 | [主圖](pages/ad-stfpm/panel-desktop-1.png)／[手機](pages/ad-stfpm/panel-mobile-1.png)／[工程1–2](pages/ad-stfpm/panel-engineering-1.png)／[工程3–4](pages/ad-stfpm/panel-engineering-2.png) |
| [RD4AD](pages/ad-rd4ad/1440-reading.txt) | **局部修正** | 瓶頸與反向特徵重建 | 工程圖補教師→瓶頸→反向解碼及各層對照；需與STFPM的直接模仿看得出差別。 | [主圖](pages/ad-rd4ad/panel-desktop-1.png)／[手機](pages/ad-rd4ad/panel-mobile-1.png)／[工程1–2](pages/ad-rd4ad/panel-engineering-1.png)／[工程3–4](pages/ad-rd4ad/panel-engineering-2.png) |
| [EfficientAD](pages/ad-efficientad/1440-reading.txt) | **局部修正** | local T/S1與global AE/S2、校正融合 | 工程圖補雙分支；主反例從圓柱托盤換金屬刮痕需統一案例；深讀手機1/2/3/4/5/7/8重排，4章替代輸出誤串接，7章維護成本需可見機制。 | [主圖](pages/ad-efficientad/panel-desktop-1.png)／[手機](pages/ad-efficientad/panel-mobile-1.png)／[工程1–2](pages/ad-efficientad/panel-engineering-1.png)／[工程3–4](pages/ad-efficientad/panel-engineering-2.png) |
| [Autoencoder (AE)](pages/ad-ae/1440-reading.txt) | **局部修正** | 原圖與重建同位置相減，40與150差110 | 工程圖須顯示重建及差值從何而來，保留主線算例，不能只貼結果熱點。 | [主圖](pages/ad-ae/panel-desktop-1.png)／[手機](pages/ad-ae/panel-mobile-1.png)／[工程1–2](pages/ad-ae/panel-engineering-1.png)／[工程3–4](pages/ad-ae/panel-engineering-2.png) |
| [DRAEM](pages/ad-draem/1440-reading.txt) | **局部修正** | 原圖＋重建進判別分割與兩種監督 | 工程圖補重建及判別的分工，避免把學習分割誤讀為單純像素相減。 | [主圖](pages/ad-draem/panel-desktop-1.png)／[手機](pages/ad-draem/panel-mobile-1.png)／[工程1–2](pages/ad-draem/panel-engineering-1.png)／[工程3–4](pages/ad-draem/panel-engineering-2.png) |
| [UniAD](pages/ad-uniad/1440-reading.txt) | **局部修正** | 近鄰注意力遮蔽、query與訓練擾動 | 工程圖補可見注意力限制及重建路徑，分清遮蔽連結與擦掉原圖。 | [主圖](pages/ad-uniad/panel-desktop-1.png)／[手機](pages/ad-uniad/panel-mobile-1.png)／[工程1–2](pages/ad-uniad/panel-engineering-1.png)／[工程3–4](pages/ad-uniad/panel-engineering-2.png) |
| [Dinomaly](pages/ad-dinomaly/1440-reading.txt) | **局部修正** | 固定DINOv2、訓練Dropout、線性聚合及分層差異 | 工程圖須呈現訓練／推論差別與層分組，通用條塊無法表達機制。 | [主圖](pages/ad-dinomaly/panel-desktop-1.png)／[手機](pages/ad-dinomaly/panel-mobile-1.png)／[工程1–2](pages/ad-dinomaly/panel-engineering-1.png)／[工程3–4](pages/ad-dinomaly/panel-engineering-2.png) |
| [InvAD](pages/ad-invad/1440-reading.txt) | **局部修正** | 輸入空間條件調制與重建 | 工程2公式缺字方框；重畫空間條件如何調制特徵，維持SSM不是state-space model的界線。 | [主圖](pages/ad-invad/panel-desktop-1.png)／[手機](pages/ad-invad/panel-mobile-1.png)／[工程1–2](pages/ad-invad/panel-engineering-1.png)／[工程3–4](pages/ad-invad/panel-engineering-2.png) |
| [DiffusionAD](pages/ad-diffad/1440-reading.txt) | **局部修正** | 兩噪聲尺度估計、引導恢復後學習定位 | 工程圖「抹掉真缺陷」警語混淆恢復圖與最後檢測目的，改成恢復→差異／分割的可追路徑。 | [主圖](pages/ad-diffad/panel-desktop-1.png)／[手機](pages/ad-diffad/panel-mobile-1.png)／[工程1–2](pages/ad-diffad/panel-engineering-1.png)／[工程3–4](pages/ad-diffad/panel-engineering-2.png) |
| [DDAD](pages/ad-ddad/1440-reading.txt) | **局部修正** | 原圖引導多步去噪與像素／適配特徵差異 | 工程2公式缺字方框；重畫原圖引導和多步變化，勿以單一熱點概括。 | [主圖](pages/ad-ddad/panel-desktop-1.png)／[手機](pages/ad-ddad/panel-mobile-1.png)／[工程1–2](pages/ad-ddad/panel-engineering-1.png)／[工程3–4](pages/ad-ddad/panel-engineering-2.png) |
| [WinCLIP](pages/ad-winclip/1440-reading.txt) | **局部修正** | 人工狀態提示、視窗聚合及正常參考擴充 | 工程圖補視窗分數與彙整；手機比較／反例小字減量，主線保留。 | [主圖](pages/ad-winclip/panel-desktop-1.png)／[手機](pages/ad-winclip/panel-mobile-1.png)／[工程1–2](pages/ad-winclip/panel-engineering-1.png)／[工程3–4](pages/ad-winclip/panel-engineering-2.png) |
| [AnomalyCLIP](pages/ad-anomalyclip/1440-reading.txt) | **局部修正** | 輔助資料學習物件無關提示與目標零樣本界線 | 工程圖補提示學習及定位分工；手機比較／反例細字與小圖放大。 | [主圖](pages/ad-anomalyclip/panel-desktop-1.png)／[手機](pages/ad-anomalyclip/panel-mobile-1.png)／[工程1–2](pages/ad-anomalyclip/panel-engineering-1.png)／[工程3–4](pages/ad-anomalyclip/panel-engineering-2.png) |
| [AnomalyGPT](pages/ad-anomalygpt/1440-reading.txt) | **局部修正** | 內建定位轉prompt learner再進LLM | 舊工程圖把specialist map畫成外部受控輸入，需重畫內建定位支路；手機密字減量。 | [主圖](pages/ad-anomalygpt/panel-desktop-1.png)／[手機](pages/ad-anomalygpt/panel-mobile-1.png)／[工程1–2](pages/ad-anomalygpt/panel-engineering-1.png)／[工程3–4](pages/ad-anomalygpt/panel-engineering-2.png) |

### 影片／時序

| 課程 | 分類 | 可保留 | 需要修正／重建的範圍 | 截圖證據 |
| --- | --- | --- | --- | --- |
| [Frame Difference](pages/frame-difference/1440-reading.txt) | **局部修正** | 兩幀差分雙帶不是兩物件、閃光不是移動 | 工程1標題／時間下標缺字；工程圖需顯示同位置相減與雙邊帶來源。 | [主圖](pages/frame-difference/panel-desktop-1.png)／[手機](pages/frame-difference/panel-mobile-1.png)／[工程1–2](pages/frame-difference/panel-engineering-1.png)／[工程3–4](pages/frame-difference/panel-engineering-2.png) |
| [Background Subtraction](pages/background-subtraction/1440-reading.txt) | **局部修正** | MOG2背景更新與停留物件吸收 | 工程圖補累積背景、更新與前景變化，勿混成兩幀差分。 | [主圖](pages/background-subtraction/panel-desktop-1.png)／[手機](pages/background-subtraction/panel-mobile-1.png)／[工程1–2](pages/background-subtraction/panel-engineering-1.png)／[工程3–4](pages/background-subtraction/panel-engineering-2.png) |
| [Lucas–Kanade](pages/lucas-kanade/1440-reading.txt) | **局部修正** | 局部紋理、角點及金字塔 | 工程2梯度下標缺字，補局部像素變化至位移向量；共用反例需讓LK／RAFT接受相同清楚與反光條件。 | [主圖](pages/lucas-kanade/panel-desktop-1.png)／[手機](pages/lucas-kanade/panel-mobile-1.png)／[工程1–2](pages/lucas-kanade/panel-engineering-1.png)／[工程3–4](pages/lucas-kanade/panel-engineering-2.png) |
| [RAFT](pages/raft/1440-reading.txt) | **局部修正** | 全配對相關與兩幀迭代光流 | 工程圖補相關查詢和向量更新；與LK反例改同條件比較，主線保留。 | [主圖](pages/raft/panel-desktop-1.png)／[手機](pages/raft/panel-mobile-1.png)／[工程1–2](pages/raft/panel-engineering-1.png)／[工程3–4](pages/raft/panel-engineering-2.png) |
| [ByteTrack](pages/bytetrack/1440-reading.txt) | **局部修正** | 高分第一次、剩餘低分第二次關聯及ID限制 | 工程圖補框–軌跡匹配、ID存續／丟失，不用熱區代替追蹤，也不把下游計數當內建保證。 | [主圖](pages/bytetrack/panel-desktop-1.png)／[手機](pages/bytetrack/panel-mobile-1.png)／[工程1–2](pages/bytetrack/panel-engineering-1.png)／[工程3–4](pages/bytetrack/panel-engineering-2.png) |
| [ConvLSTM](pages/convlstm/1440-reading.txt) | **局部修正** | 空間hidden/cell、卷積門控與序列重置 | 工程2時間下標缺字，需重畫記憶保留／更新及任務head，不能以通用熱點代表狀態。 | [主圖](pages/convlstm/panel-desktop-1.png)／[手機](pages/convlstm/panel-mobile-1.png)／[工程1–2](pages/convlstm/panel-engineering-1.png)／[工程3–4](pages/convlstm/panel-engineering-2.png) |
| [VideoMAE](pages/videomae/1440-reading.txt) | **局部修正** | tube遮蔽像素重建預訓練與下游分類 | 工程圖分清預訓練decoder和分類推論head，呈現時空遮蔽與輸出。 | [主圖](pages/videomae/panel-desktop-1.png)／[手機](pages/videomae/panel-mobile-1.png)／[工程1–2](pages/videomae/panel-engineering-1.png)／[工程3–4](pages/videomae/panel-engineering-2.png) |
| [V-JEPA](pages/v-jepa/1440-reading.txt) | **局部修正** | 2024版遮蔽目標特徵與EMA教師 | 工程圖補特徵預測及停止梯度／教師更新界線；手機圖說只需間距改善，量測未發現按鈕遮字。 | [主圖](pages/v-jepa/panel-desktop-1.png)／[手機](pages/v-jepa/panel-mobile-1.png)／[工程1–2](pages/v-jepa/panel-engineering-1.png)／[工程3–4](pages/v-jepa/panel-engineering-2.png) |

### 視覺基礎／多模態

| 課程 | 分類 | 可保留 | 需要修正／重建的範圍 | 截圖證據 |
| --- | --- | --- | --- | --- |
| [DINOv2](pages/dinov2/1440-reading.txt) | **局部修正** | 跨視圖教師學生表示與下游檢索 | 工程圖補表示學習與部署兩階段；支架／接頭切至墊圈反例可局部統一案例。 | [主圖](pages/dinov2/panel-desktop-1.png)／[手機](pages/dinov2/panel-mobile-1.png)／[工程1–2](pages/dinov2/panel-engineering-1.png)／[工程3–4](pages/dinov2/panel-engineering-2.png) |
| [DINOv3](pages/dinov3/1440-reading.txt) | **局部修正** | Gram關係錨定及特徵保留 | 工程圖把訓練錨定塞入單一推論路徑，需分開；反例工件切換及手机細字局部修正。 | [主圖](pages/dinov3/panel-desktop-1.png)／[手機](pages/dinov3/panel-mobile-1.png)／[工程1–2](pages/dinov3/panel-engineering-1.png)／[工程3–4](pages/dinov3/panel-engineering-2.png) |
| [CLIP](pages/clip/1440-reading.txt) | **局部修正** | 雙編碼器、正規化與候選相似度 | 工程圖把並行編碼器畫成串接、排名画成熱點，需修；手機比較圖字太密。 | [主圖](pages/clip/panel-desktop-1.png)／[手機](pages/clip/panel-mobile-1.png)／[工程1–2](pages/clip/panel-engineering-1.png)／[工程3–4](pages/clip/panel-engineering-2.png) |
| [SigLIP](pages/siglip/1440-reading.txt) | **局部修正** | 逐對正負配對損失及候選限制 | 工程圖雙編碼器應並行，結果用配對分數／排名，不能用熱點；手機比較減量。 | [主圖](pages/siglip/panel-desktop-1.png)／[手機](pages/siglip/panel-mobile-1.png)／[工程1–2](pages/siglip/panel-engineering-1.png)／[工程3–4](pages/siglip/panel-engineering-2.png) |
| [LLaVA](pages/llava/1440-reading.txt) | **局部修正** | 原版投影橋接與可見螺絲／未知根因界線 | 工程圖補影像表示經投影與文字匯合至LLM、輸出回答，不用通用熱點。 | [主圖](pages/llava/panel-desktop-1.png)／[手機](pages/llava/panel-mobile-1.png)／[工程1–2](pages/llava/panel-engineering-1.png)／[工程3–4](pages/llava/panel-engineering-2.png) |
| [Qwen-VL](pages/qwen-vl/1440-reading.txt) | **局部修正** | 明確Qwen2-VL、動態解析度／M-RoPE與低像素限制 | 工程圖補token／位置與多模態輸出，避免通用PCB條塊；主線保留。 | [主圖](pages/qwen-vl/panel-desktop-1.png)／[手機](pages/qwen-vl/panel-mobile-1.png)／[工程1–2](pages/qwen-vl/panel-engineering-1.png)／[工程3–4](pages/qwen-vl/panel-engineering-2.png) |
| [Gemini Vision](pages/gemini-vision/1440-reading.txt) | **局部修正** | API請求、JSON解析不等於內容正確與人工覆核 | 工程圖須顯示可核對欄位／證據，不用熱點當回答；圓接頭轉方端子的反例可統一。 | [主圖](pages/gemini-vision/panel-desktop-1.png)／[手機](pages/gemini-vision/panel-mobile-1.png)／[工程1–2](pages/gemini-vision/panel-engineering-1.png)／[工程3–4](pages/gemini-vision/panel-engineering-2.png) |

### 生成／影像復原

| 課程 | 分類 | 可保留 | 需要修正／重建的範圍 | 截圖證據 |
| --- | --- | --- | --- | --- |
| [DefectFill](pages/defectfill/1440-reading.txt) | **局部修正** | 少量缺陷與mask適配、LoRA／損失及候選篩選 | 工程圖補正常圖＋指定mask→合成圖與候選篩選，區分感知差異和物理真實。 | [主圖](pages/defectfill/panel-desktop-1.png)／[手機](pages/defectfill/panel-mobile-1.png)／[工程1–2](pages/defectfill/panel-engineering-1.png)／[工程3–4](pages/defectfill/panel-engineering-2.png) |
| [AnomalyDiffusion](pages/anomalydiffusion/1440-reading.txt) | **局部修正** | 外觀／空間條件、弱區域回饋與背景融合 | 工程圖補兩種條件及生成結果，保留兩mask只生一缺陷的錯標反例。 | [主圖](pages/anomalydiffusion/panel-desktop-1.png)／[手機](pages/anomalydiffusion/panel-mobile-1.png)／[工程1–2](pages/anomalydiffusion/panel-engineering-1.png)／[工程3–4](pages/anomalydiffusion/panel-engineering-2.png) |
| [TF-IDG](pages/tf-idg/1440-reading.txt) | **局部修正** | 固定權重、生成時特徵對齊與紋理保留 | 工程圖補生成時更新對象與局部條件，避免誤示為重新訓練模型；保留跨材質失敗。 | [主圖](pages/tf-idg/panel-desktop-1.png)／[手機](pages/tf-idg/panel-mobile-1.png)／[工程1–2](pages/tf-idg/panel-engineering-1.png)／[工程3–4](pages/tf-idg/panel-engineering-2.png) |
| [ControlNet](pages/controlnet/1440-reading.txt) | **局部修正** | 固定主幹、可訓練控制分支與零初始化連接 | 工程圖需顯示控制條件如何接入去噪，不能只貼通用熱點；保留輪廓未描述裂紋反例。 | [主圖](pages/controlnet/panel-desktop-1.png)／[手機](pages/controlnet/panel-mobile-1.png)／[工程1–2](pages/controlnet/panel-engineering-1.png)／[工程3–4](pages/controlnet/panel-engineering-2.png) |
| [Inpainting](pages/inpainting/1440-reading.txt) | **局部修正** | mask＋上下文去噪及任務非單一模型 | 工程圖改成遮罩內外與修補影像，保留真孔被補平但金屬未修復的界線。 | [主圖](pages/inpainting/panel-desktop-1.png)／[手機](pages/inpainting/panel-mobile-1.png)／[工程1–2](pages/inpainting/panel-engineering-1.png)／[工程3–4](pages/inpainting/panel-engineering-2.png) |
| [Diffusion Restoration](pages/diffusion-restoration/1440-reading.txt) | **局部修正** | 先驗與觀測一致性、復原非唯一解 | 工程圖補觀測退化與候選核對，不能只畫異常熱區；保留两解退化後近似相同的反例。 | [主圖](pages/diffusion-restoration/panel-desktop-1.png)／[手機](pages/diffusion-restoration/panel-mobile-1.png)／[工程1–2](pages/diffusion-restoration/panel-engineering-1.png)／[工程3–4](pages/diffusion-restoration/panel-engineering-2.png) |
| [Deblur](pages/deblur/1440-reading.txt) | **局部修正** | 展寬訊號、估計銳利邊緣及振鈴反例 | 工程2近似符號缺字方框；工程圖補模糊／復原邊緣及獨立觀測，勿以熱點取代。 | [主圖](pages/deblur/panel-desktop-1.png)／[手機](pages/deblur/panel-mobile-1.png)／[工程1–2](pages/deblur/panel-engineering-1.png)／[工程3–4](pages/deblur/panel-engineering-2.png) |
| [Super-resolution](pages/super-resolution/1440-reading.txt) | **局部修正** | 插值與學習估計、新像素不等於新觀測 | 工程圖補低採樣至高解析候選及非唯一細節；矩形板切圓板反例可局部統一案例。 | [主圖](pages/super-resolution/panel-desktop-1.png)／[手機](pages/super-resolution/panel-mobile-1.png)／[工程1–2](pages/super-resolution/panel-engineering-1.png)／[工程3–4](pages/super-resolution/panel-engineering-2.png) |

## 五課深讀：40章另行審查

| 課程 | 保留的內容 | 局部修正 |
| --- | --- | --- |
| ResNet | 退化、跳接、實際特徵、BN中心化、pooling位置損失、条件取捨 | 手機2/4/8章數值與細字；[桌機](deep/resnet/panel-1440-01.png)、[手機](deep/resnet/panel-360-01.png)及同資料夾其餘視圖。 |
| SegFormer | 窗口共享、四尺度、K/V縮減、通道拼接、train/infer、工作比較 | 手機1章靠邊標題及3–5章细網格／標註；[手機](deep/segformer/panel-360-01.png)。 |
| PatchCore | 特徵來源、coreset、查庫、不同分數實作、污染及公開漏檢／誤報 | 手機2章數值偏小、部分圖工件小留白大；[手機](deep/ad-patchcore/panel-360-01.png)。保留公開原始案例。 |
| AnomalyDINO | 固定DINOv2、最高1%算術、庫污染與作者實例 | 6章旋轉反例的刻字方向不一致，應用同圖剛性旋轉重建；其他手機細圖重排；[深讀文字](deep/ad-anomalydino/1440-chapter-6.txt)。 |
| EfficientAD | T/S1、AE/S2、校正融合，第6章直式分段 | 手機1章舊視圖縮太小，2/3/4/5/7/8章依賴橫滑；4章替代輸出串接改分支；7章補可見建庫／訓練差別；[手機](deep/ad-efficientad/panel-360-01.png)。 |

各課全部深讀截圖路徑列在results.json的deep_evidence；[deep-capture.json](deep-capture.json)列出章節與視圖，[deep-recheck.json](deep-recheck.json)指向需替代初次白圖的重查截圖。

## 建議處理順序

1. **P1：6課核心重建。** 先固定同一工件、單一路徑、可见中間變化與反例；ChArUco分清校正／姿態，ECC放大殘差，SIFT顯示描述子與篩選，LightGlue顯示候選更新，DINO detector顯示去噪訓練，YOLO-World顯示文字表示如何影響出框。保留既有可追溯實例。
2. **先修會教錯的局部圖。** CLIP／SigLIP並行編碼、Pose替代流程、DINOv3訓練／推論、DiffusionAD恢復與檢測、AnomalyGPT內建定位、LK／RAFT同條件反例，以及AnomalyDINO旋轉圖、EfficientAD深讀替代輸出。
3. **P2：逐家族清理舊工程圖。** 按真實輸出畫分類分數、語意／實例遮罩、具身份的點、R/t、偵測框、查庫距離、光流、追蹤ID、回答欄位或復原影像。58課工程層都至少有實質缺口；這不是要求不分內容地重畫232張。ECC工程4等有效案例可保留，其餘按原圖驗收。
4. **P2：指定手機與深讀圖重排。** 優先EfficientAD深讀橫滑，接著小字、公式缺字、長標題遮蓋／省略及工件太小。保留已成立的直式主線。

後續製作應另建工作項，依原技能做版本化preflight、實際PNG及整頁檢查；本輪只提出可執行範圍，沒有開始換圖或发布。

## 證據與驗證界線

- 58課 × 1440／360px＝116頁面狀態，全部完成；376次主圖放大檢查、116次自測答案展開、116次導覽切換。未見page error或整頁水平溢出。容器內橫滑仍另列閱讀缺口。
- 主線圖文、比較、反例、自測／操作卡，以及每課4張工程圖均實看；5課40個深讀章節，共80章節尺寸狀態、148個視圖擷取並審讀。補看兩課inline SVG手機圖。不是只看檔名或首頁。
- 644個啟用資產在擷取時公開HTTP可達，公開HTML與本機正規化後一致；收尾再核644資產course/docs hash與基準一致、HTML未變。公開資產未逐一GET比hash，沒有宣稱644張都在公開站逐張人工評分。
- 66個主線資產路徑被多課共用；hash已重核。人工視覺證據依同圖重用，非重複算成不同設計。
- 188個360px主線圖說以逐字DOM Range量測，0處字形與放大按鈕重疊。原先擁擠截圖只列間距改善，撤回遮字推測。sticky header／skip link的擷取覆蓋不作教材缺陷。
- 深讀13張初次白圖是切換後擷取過早，等載入後13張均正常；保留初次與重查證據，不列網站空白故障。EfficientAD橫滑圖已看桌機完整內容與手機起始呈現，沒有聲稱擷取每個橫滑位置。
- 本輪未重跑模型、未重現每項論文數據、未做真人學習測試，也沒有逐張完整數字評分。幾何疑點的第一手查證見[technical-verification.md](technical-verification.md)。
- 工具／來源：內建瀏覽器不可用後改用本機Playwright Edge檢查相同發布HTML；公開核對見[public-inventory.json](public-inventory.json)，最終彙整見[final-verification.json](final-verification.json)，逐步人工發現與誤判撤回見[observations.md](observations.md)。

## 接續與保存

審查結果、58筆分類、具體修正范围與驗證已保存本資料夾。根WORKITEMS.md、BEGINNER_VISUAL_TODO.md、BEGINNER_VISUAL_STATUS.md連回本報告；可重用學習寫回根TEACHING_REVIEW_LOG.md與兩份指南。這些是本機持久Markdown，未把聊天或程序ID當唯一紀錄。本輪沒有commit、push或發布。
