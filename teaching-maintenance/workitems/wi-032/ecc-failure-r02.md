# WI-032 起點太遠，ECC可能對錯位置
- lesson objective: ECC需要合理起點；對不上就先找粗定位。
- page type: D — 以具體機制或同條件對照說明工作選擇。
- primary reading path: 同一模板與待對圖 → 近起點與遠起點 → 核對整件及殘差 → 依可見證據採取下一步
- major visual nodes:
  1. 同一模板與待對圖
  2. 近起點與遠起點
  3. 核對整件及殘差
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，借材質、細框、主體比例；模型內容另設計。
- pale-yellow takeaway: #FFF4CC：ECC需要合理起點；對不上就先找粗定位。
- source: https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html
- evidence: AI生成教學示意；不冒充模型輸出、效能比較或可列印標靶。
- generation: built-in imagegen；桌機16:9／手機直向另排；actual PNG review pending；user approval pending。

## Visual brief／不變條件與可見證據
Use SAME two-hole L metal bracket and same images in both alternatives. Blue solid is template outline; orange dashed is current resampled moving outline. Common input shown once at top left, identical bracket and two holes. Two large parallel comparison regions:「合理起點」has near overlap then aligned hole pair;「起點太遠」has initial shifted bracket with only partial overlap then mismatched one hole-to-other-hole alignment. The bracket itself must not vanish or lose a hole. Show entire bracket outlines and a same-location inset to reveal wrong hole correspondence. Orange warning in wrong alignment「局部像，不代表整件對」. Final small action area shows feature point correspondences to coarse alignment then fine refinement, label「先粗定位，再微調」. No performance numbers. Do not show arbitrary failures as actual experiment. Emphasize different initialization, same source images.

## Validation
WI-031缺口轉換：方法造成的變化要能在圖上定位，不能重複同圖只换名稱；比較分支不串接。核對重複工件身份、來源箭頭、輸出責任、圖說／原生／桌機頁內／360px手機，固定v1.0逐項評。


## r02 修正
Create a NEW comparison diagram with the EXACT same bracket as attached ECC core: metal vertical plate with TWO SIDE-BY-SIDE holes, upper-right protruding tab, horizontal mounting foot. Title「起點太遠，ECC可能對錯位置」. Same template and moving source photo, same two-hole bracket. THREE large groups: common input, two alternative initializations, engineering action. Center pairs same-scale overlays blue solid template and orange dashed warped input: near start goes to correct whole-bracket overlap; far start can align LEFT orange hole with RIGHT blue hole, therefore ENTIRE ORANGE BRACKET OUTLINE must remain shifted one full hole spacing right relative to blue, including BOTH holes and outer edges. Show this clearly, never show almost-aligned whole outlines with a falsely mismatched inset. Label「合理起點」「錯誤局部解（示意）」. Final action show 3 correctly paired named plate landmarks supplying a coarse start, then ECC fine adjustment, label「先粗定位，再微調」; landmarks representative not exact solver minimum. No numbers or model measurements. Takeaway「ECC需要合理起點；對不上就先找粗定位。」. Keep one yellow #FFF4CC band, airy materials and thick blue arrows within causal alternatives, no arrows linking alternatives together.
- checkpoint: 即將生成；原生review pending，user approval pending。
