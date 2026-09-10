# WI-032 SIFT：用局部方向線索，找兩張圖的對應
- lesson objective: SIFT找的是對應點；幾何變換還要另行估計與驗證。
- page type: C — 以具體機制或同條件對照說明工作選擇。
- primary reading path: 找穩定局部 → 方向描述與比對 → 交出匹配點 → 依可見證據採取下一步
- major visual nodes:
  1. 找穩定局部
  2. 方向描述與比對
  3. 交出匹配點
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，借材質、細框、主體比例；模型內容另設計。
- pale-yellow takeaway: #FFF4CC：SIFT找的是對應點；幾何變換還要另行估計與驗證。
- source: https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html
- evidence: AI生成教學示意；不冒充模型輸出、效能比較或可列印標靶。
- generation: built-in imagegen；桌機16:9／手機直向另排；actual PNG review pending；user approval pending。

## Visual brief／不變條件與可見證據
Same asymmetric two-hole metal bracket with an upper-right notch, two views one rotated about 20 degrees and slightly rescaled. Left paired grayscale views with 3 sparse corresponding named local corners A B C, keypoint circles denote local scale. Center enlarge SAME distinctive upper-right notch patch in both views: small gradient arrows reflect edge normals; rotate local reference frame to dominant direction, then two compact multi-bin orientation histogram strips have matching shape. Label「先對齊局部方向」「整理梯度分布」and tiny「描述子示意」. Avoid whole-image rotation claimed as actual SIFT output. RIGHT two image strips with corresponding A-A B-B C-C lines; include one ambiguous repeated-hole match as dashed orange crossed-out line labeled「含糊配對先剔除」. Output label「匹配點」then clearly separate small arrow to「幾何估計另做」. No network weights or training, subtitle「演算法｜不需訓練權重｜教學示意」. Enough feature evidence to see description not just feature dots.

## Validation
WI-031缺口轉換：方法造成的變化要能在圖上定位，不能重複同圖只换名稱；比較分支不串接。核對重複工件身份、來源箭頭、輸出責任、圖說／原生／桌機頁內／360px手機，固定v1.0逐項評。


## r02 修正
Edit SIFT diagram. Keep the 3-column mechanism and material. FIX point A identity: it must be the INNER 90-degree corner of the upper-right notch in EVERY whole-part view, magnified patch, and matching-row crop. Move the blue A dot and circle in both left whole parts to this exact concave inner notch corner, not the rounded outer top tip. The enlarged A patches and third-column A row should show the same concave corner and dot. The local dominant direction before normalization rotates WITH the part; the reference frame is then normalized, so label the two central red axis arrows「對齊後方向」and use identical reference arrows, while gradient evidence rotates appropriately. Keep descriptors conceptual, no exact degrees on histogram, label「局部梯度分布（示意）」instead. Remove excessive two-line paragraphs at top of each column, keep only short action labels. Preserve same bracket holes and geometry. Point matching outputs A-A/B-B/C-C; explicitly keep「幾何估計另做」, these three displayed pairs are representative not sufficient homography sample. No invented precision, no geometric transform claimed as SIFT output.
- checkpoint: 即將生成；原生review pending，user approval pending。
