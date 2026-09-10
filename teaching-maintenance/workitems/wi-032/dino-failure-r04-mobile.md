# WI-032 訓練去噪，不能保證遮擋後仍找得到
- lesson objective: 去噪訓練改善學習訊號；現場遮擋與漏檢仍要實測。
- page type: D — 以具體機制或同條件對照說明工作選擇。
- primary reading path: 同一螺栓與墊圈 → 完整可見與遮擋 → 逐件對照人工標註 → 依可見證據採取下一步
- major visual nodes:
  1. 同一螺栓與墊圈
  2. 完整可見與遮擋
  3. 逐件對照人工標註
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，借材質、細框、主體比例；模型內容另設計。
- pale-yellow takeaway: #FFF4CC：去噪訓練改善學習訊號；現場遮擋與漏檢仍要實測。
- source: https://arxiv.org/abs/2203.03605
- evidence: AI生成教學示意；不冒充模型輸出、效能比較或可列印標靶。
- generation: built-in imagegen；桌機16:9／手機直向另排；actual PNG review pending；user approval pending。

## Visual brief／不變條件與可見證據
Same top-down gray mat ONE bolt upper-left, ONE washer lower-right. Two same-scale condition views: fully visible input yields illustrative candidate blue boxes on both; other SAME positions with opaque black fixture overlapping most washer, washer remains physically partly visible crescent and most hidden. Show only bolt candidate box in right output, missed washer identified with orange hand-review dotted locator labeled「人工核對：漏一件」, not model box. Label「完整可見」「夾具遮擋」. End third group pair overlay to GT list「螺栓／墊圈」with bolt found, washer missed and action「補遮擋樣本／改取像」. Avoid counts other than clearly 2 items/1 missed. Explicit「假設漏檢示意，非實測」. No ground-truth feed into inference, no implication DN noise equals real occlusion augmentation.

## Validation
WI-031缺口轉換：方法造成的變化要能在圖上定位，不能重複同圖只换名稱；比較分支不串接。核對重複工件身份、來源箭頭、輸出責任、圖說／原生／桌機頁內／360px手機，固定v1.0逐項評。

## r03
Create MOBILE version, 3 regions VERTICALLY. Extremely few words, huge labels minimum64px at1024width. SAME bolt and washer with exact same positions. Top『完整可見』 large scene two candidate boxes. Middle『只增加遮擋』 same scene black opaque smooth fixture covers most washer, only bolt candidate box; no extra screw in fixture. Bottom『逐件核對：漏了墊圈』 two-target annotated reference bolt/washer versus hypothetical detected bolt only, visibly missing washer. Clearly label『假設漏檢示意』 in title, ONE pale-yellow takeaway『去噪訓練不能保證不漏檢』. Small『教學示意，非模型實測』. No long explanatory paragraphs, nested miniature diagrams, or dense numbered steps. One reading path top to bottom, white thin blue frames.
## r04
Third region is an object LIST not a modified source image. Label both panels as lists and use object cutouts on plain white cards, retain washer physical pixels in occluded input. Pending review.