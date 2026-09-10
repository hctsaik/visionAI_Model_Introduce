# WI-030 同一分類工作，三種特徵整理方式
- lesson objective: 先固定資料和輸出，再比較錯誤、延遲與維護。
- page type: D — 依具體因果／條件差異教工作判斷。
- primary reading path: ResNet保留再修正 → ConvNeXt卷積分工 → ViT區塊互看 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. ResNet保留再修正
  2. ConvNeXt卷積分工
  3. ViT區塊互看
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：先固定資料和輸出，再比較錯誤、延遲與維護。
- source: https://arxiv.org/abs/1512.03385
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
共用內六角／十字螺絲分類，三區輸入小圖同需求，方法不同。ResNet藍特徵分支直接路＋卷積修正合併；ConvNeXt多特徵平面各自較大窗口，再混合通道；ViT來源塊變tokens加位置、多token之間不同粗連線匯整。三區各有分類候選（相同內六角，不造效果勝負）；下方短註每種需預訓練/工作標註/域內測試，手機三直列。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。
