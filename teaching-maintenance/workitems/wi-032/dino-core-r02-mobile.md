# WI-032 DINO detector：先練辨別帶噪框，再學會出框
- lesson objective: 帶噪真值只幫助訓練；正式出框時沒有真值可偷看。
- page type: C — 以具體機制或同條件對照說明工作選擇。
- primary reading path: 訓練有真值 → 正負去噪訊號 → 推論只有影像 → 依可見證據採取下一步
- major visual nodes:
  1. 訓練有真值
  2. 正負去噪訊號
  3. 推論只有影像
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，借材質、細框、主體比例；模型內容另設計。
- pale-yellow takeaway: #FFF4CC：帶噪真值只幫助訓練；正式出框時沒有真值可偷看。
- source: https://arxiv.org/abs/2203.03605
- evidence: AI生成教學示意；不冒充模型輸出、效能比較或可列印標靶。
- generation: built-in imagegen；桌機16:9／手機直向另排；actual PNG review pending；user approval pending。

## Visual brief／不變條件與可見證據
Industrial tabletop with ONE hex-head bolt and ONE washer, realistic top-down gray mat, each fixed location throughout. Three main regions. First TRAINING annotated image with tight GREEN GT rectangle around bolt, label「人工真值框」, green means known annotation not quality pass. Second TRAINING big crop same bolt with blue solid near perturbed query box and orange dashed farther perturbed query box; green thin GT remains reference. Split targets visibly: near blue box arrow toward green GT and label「正樣本：還原真值框／類別」; farther orange box points to separate empty-class symbol label「負樣本：學無物件」, it is a training query not a real negative object, bolt remains visible. Label「對比去噪訓練」. Third clearly separate INFERENCE lane below/within last region: fresh unannotated same bolt+washer image → trained detector queries refine bounding boxes → two blue class-labeled rectangles「螺栓」「墊圈」. No green GT or noisy-query arrow feeds inference input. Small weight-file arrow from training to trained detector only. Subtitle「DETR系偵測器｜不是DINOv2特徵骨幹｜示意」. Large box movement and training-only boundary, no equation or invented performance.

## Validation
WI-031缺口轉換：方法造成的變化要能在圖上定位，不能重複同圖只换名稱；比較分支不串接。核對重複工件身份、來源箭頭、輸出責任、圖說／原生／桌機頁內／360px手機，固定v1.0逐項評。

## Mobile composition
Independently reflow three groups top to bottom, 768px wide, 32px minimum text, retain mechanism and single takeaway, not cropped desktop. Actual PNG review pending; user approval pending.

## r02
Redesign for a tiny 360px PHONE. Keep three vertical regions with LARGE instructional examples and EXTREMELY FEW words. Use huge Traditional Chinese labels at least 64px on 1024px wide canvas. No explanatory paragraphs. Only these text labels allowed: title『DINO：帶噪框只用於訓練』; top『人工真值』 with same bolt and washer and green GT bolt box; middle『訓練』 with green GT plus nearby blue noisy query returning to GT labeled『還原』, and far orange query targeting『無物件』, do NOT remove physical objects; bottom『推論』 show new raw bolt+washer scene arrow to two output boxes and text『新影像 → 已訓練模型 → 框與類別』, no ground truth into inference. Single bottom yellow takeaway『推論沒有真值可偷看』. Small subtitle『僅展開一個訓練物件；教學示意』. White thin blue framing. No blue numbered badges. Keep min64px all text, allow long portrait, three rows not nested dense panels.