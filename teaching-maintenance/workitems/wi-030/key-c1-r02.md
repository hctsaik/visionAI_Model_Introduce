# WI-030 Keypoint R-CNN：先分物件，再找有名字的點
- lesson objective: 點有身分與所屬物件；2D點還不是3D姿態。
- page type: C — 依具體因果／條件差異教工作判斷。
- primary reading path: 每件定義相同點 → 框內預測位置 → 映回原圖 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 每件定義相同點
  2. 框內預測位置
  3. 映回原圖
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：點有身分與所屬物件；2D點還不是3D姿態。
- source: https://docs.pytorch.org/vision/main/_modules/torchvision/models/detection/keypoint_rcnn.html
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
兩塊不重疊的不對稱L形金屬板，每塊有三個位置不對稱圓孔，原圖不同旋轉但不鏡射。每件指定三孔中心A/B/C，標註圖清楚一致。第二區共享特徵→每件ROI對齐→三張小熱圖，各亮峰對同一ROI A/B/C孔中心，熱圖標「點位置估計」非原圖；可只展開第一件ROI，第二件以帶ID小框保留。第三區將第一件ROI點映回原大圖，每件框中各有A/B/C同點順序，標「還原裁切座標」「檢查可見性」；不畫骨架人體、不畫已知3D或機械控制。工業改編須訓練。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

## 本版修正
重新畫核心機制以修正嚴重錯誤。两塊L形工件不可鏡射；本次都相同方向，只左右平移不同位置。兩件都是左直臂上孔A、左下轉角孔B、右水平端孔C，完全相同幾何。第一區顯示两件及相同點名並註『需工業點位標註訓練』。中央由完整兩件原圖→共享特徵→每件ROI對齊→點位熱圖，不能把裁切原圖送共享特徵。為少字可只展開物件1的三張熱圖，熱圖峰分別A左上、B左下、C右下，三張同坐標。第三區將點映回完整兩件原圖，A/B/C在相同物理孔。用小比例裁切視窗到全圖的清楚對應線，標『還原裁切座標』『2D點位置』。刪不必要的局部照片放大。3區和底部結論不變，先特徵後ROI這順序必須以箭頭畫對。
