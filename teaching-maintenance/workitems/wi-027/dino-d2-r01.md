# WI-027 特徵很相近，仍可能漏掉小缺口 r01
- lesson objective: 先確認缺口在輸入中看得見，再評估特徵與下游方法。
- page type: D — 依本圖解釋或對比責任選用。
- primary reading path: 工作輸入 → 方法／條件改變 → 可見結果與限制 → 下一步核對。
- major visual nodes:
  1. 同一工件的小缺口
  2. 縮圖後線索變弱
  3. 回到有效細節核對
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用物件質感、就近對應及淡細框。
- pale-yellow takeaway: #FFF4CC：先確認缺口在輸入中看得見，再評估特徵與下游方法。
- source: https://arxiv.org/abs/2304.07193
- evidence: AI生成教學示意，不是實際模型輸出或性能比較。
- generation: built-in imagegen；desktop 16:9，mobile 1:3 區內獨立重排，原生與頁內實看；actual review pending；user approval pending。
- learning applied: WI-026 來源／位置保持、候選非真值、訓練和部署分開、比較替代路線不串接。

## 視覺因果、資料身分、逐字短標籤及禁項

3major groups left-to-right. 1 realistic round metal washer with a single conspicuous small notch at right 3oclock outerrim, magnifier sourcebox correctly same3oclock notch. Label '原始細節'. 2 '縮小後' same washer and samenotch location but reducedpixels blur notch into smoothrim; next to it normalizedqualitative similar feature strips of notched/normal washers labelled '特徵可能接近'; explicitly a hypothetical failure not measured DINOoutput. 3 '保留線索再測' crop the SAME3oclock source at larger scale, retaining notch without inventing newmaterial; beside it compare actual smooth normalrim and notchedrim at same scale; arrow to '局部取樣＋下游驗證'. Not claim magnification recovers lostdata: sourcecrop uses original. Subtitle 'DINOv2／DINOv3 應用反例｜AI生成示意'. Neither backbone returns defectmask by itself.
