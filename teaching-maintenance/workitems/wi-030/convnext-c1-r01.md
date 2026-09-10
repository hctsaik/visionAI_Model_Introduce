# WI-030 ConvNeXt：用現代卷積整理局部與通道線索
- lesson objective: 仍是卷積模型；是否值得換，要連品質與成本一起測。
- page type: C — 依具體因果／條件差異教工作判斷。
- primary reading path: 有標註的工件 → 空間與通道分工 → 分類與成本核對 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 有標註的工件
  2. 空間與通道分工
  3. 分類與成本核對
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：仍是卷積模型；是否值得換，要連品質與成本一起測。
- source: https://arxiv.org/abs/2201.03545
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
同一螺絲頭分類工作，內六角螺絲完整圖進特徵。中央放大兩張抽象藍色／紫色特徵平面，較大滑動窗口在每張平面各自聚合，標「各通道看鄰域」；接短矩陣把兩個通道訊號混合成新特徵，標「再混合通道」，保留殘差旁路到合併點。第三區分類頭交出內六角候選，同一工作資料資料夾加碼表及記憶體圖標標「同資料測錯誤／耗時／記憶體」。不得畫Transformer注意力、無虛構排名。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。
