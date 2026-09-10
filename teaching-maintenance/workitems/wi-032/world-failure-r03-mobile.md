# WI-032 文字寫了缺陷，不代表影像裡看得見
- lesson objective: 提示詞不能補回缺失像素；先確認缺陷看得見。
- page type: D — 以具體機制或同條件對照說明工作選擇。
- primary reading path: 同一螺栓細裂紋 → 可見細節與不足像素 → 回到影像及標註驗證 → 依可見證據採取下一步
- major visual nodes:
  1. 同一螺栓細裂紋
  2. 可見細節與不足像素
  3. 回到影像及標註驗證
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，借材質、細框、主體比例；模型內容另設計。
- pale-yellow takeaway: #FFF4CC：提示詞不能補回缺失像素；先確認缺陷看得見。
- source: https://arxiv.org/abs/2401.17270
- evidence: AI生成教學示意；不冒充模型輸出、效能比較或可列印標靶。
- generation: built-in imagegen；桌機16:9／手機直向另排；actual PNG review pending；user approval pending。

## Visual brief／不變條件與可見證據
Same bolt on gray mat, tiny hairline crack at exact upper-right hex head edge. LEFT enlarged high-detail head crop shows actual thin dark crack, RIGHT same crop heavily downsampled then enlarged so blocky pixels merge crack with edge, object shape stays same; literal condition「細節足夠」「像素不足」. Shared prompt chip「裂紋螺栓」feeds both same-model conditions, but do not make fabricated accurate detection on left; show candidate box around bolt and question「框到物件≠證明裂紋」. Final independent visual verification zoom at raw acquisition, capture scale change giving visible same crack and human annotation, action「提高取像解析度／標註驗證」. Three major groups common task, paired views, evidence-based action. A phrase is semantic label not boolean exclusion rule; do not illustrate a NOT operation. Explicit concept demonstration not model prediction.

## Validation
WI-031缺口轉換：方法造成的變化要能在圖上定位，不能重複同圖只换名稱；比較分支不串接。核對重複工件身份、來源箭頭、輸出責任、圖說／原生／桌機頁內／360px手機，固定v1.0逐項評。

## r03
Redesign into very readable PHONE portrait with THREE VERTICAL regions and very few words. Min64px Traditional Chinese at1024wide. SAME physical bolt and same crack. Title『文字補不回看不見的裂紋』. Top『同一螺栓』: large realistic bolt on gray grid, connected enlarged head with fine crack. Middle『取像解析度不足』: SAME head same magnification but blocky pixels with no invented precise crack; orange candidate box label『框到 ≠ 證實裂紋』. Bottom『先改善原始取像』: camera taking image of same bolt plus enlarged high-detail same crack; label『另做標註核對』. ONE pale-yellow takeaway『先確認缺陷看得見，再驗證結果』. Small『觀測限制示意，非模型實測』. Remove all other prose, tiny tables, duplicated examples. White background thin light-blueframes. Cannot digitally invent absent detail; depict recapture, not upscaling.