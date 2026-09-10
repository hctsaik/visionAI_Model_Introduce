# WI-030 正常資料相同，四種方法怎麼留下知識？
- lesson objective: 先看資料與維護方式，再用同一工作測品質和成本。
- page type: D — 依具體因果／條件差異教工作判斷。
- primary reading path: PatchCore代表庫 → PaDiM位置統計 → AnomalyDINO特徵庫 → EfficientAD訓練回應
- major visual nodes:
  1. PatchCore代表庫
  2. PaDiM位置統計
  3. AnomalyDINO特徵庫
  4. EfficientAD訓練回應
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：先看資料與維護方式，再用同一工作測品質和成本。
- source: https://arxiv.org/abs/2106.08265
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
四大區共用同一金屬檢查任務，各區畫不同可見工作流程，不画四個相同熱圖。PatchCore正常影像→固定CNN特徵→代表子集庫→查庫；PaDiM正常同位置小框→固定CNN→每位置斜橢圓分布→依同位置判離群；AnomalyDINO正常完整圖→固定DINOv2tokens→參考庫→查相似；EfficientAD正常資料→固定教師與更新學生+AE→固定推論網路，訓練迴圈畫学生/AE，非教師。每區一短維護標籤「重建庫」「重估位置分布」「重建參考」「評估重訓」。底下共同測試資料夾與計時/記憶體小圖標，但不新增主區。手機2x2不可縮小，改四區直列。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。
