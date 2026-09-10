# WI-030 EfficientAD：學正常回應，再查兩種落差 — mobile
- lesson objective: 局部差異與整體關係一起查；快不等於免驗證。
- page type: C
- primary reading path: 正常資料教學生 → 局部與全域兩路 → 校準後回查 → 核對輸出與工作條件
- major visual nodes:
  1. 正常資料教學生
  2. 局部與全域兩路
  3. 校準後回查
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：局部差異與整體關係一起查；快不等於免驗證。
- source: https://arxiv.org/abs/2303.14535
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：efficient-c1-r05-mobile.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"手機328px實看第二區字太小，本版請徹底重排第二區內的兩路，不得左右並排。畫布極高直式1:3，約768x2304，正文最小32px（768原生），大標題44px以上。保持3主要區。第一區簡潔正常三柱托盤→固定教師和可訓學生→正常回應接近，刪重複文字。第二區佔全圖一半高度：完整待測托盤中空右污點，下方第一列全寬『局部線索』，教師特徵與學生局部特徵兩大格相減→右側熱點圖；下一列全寬『整體關係線索』，AE重建教師特徵與學生另一輸出特徵兩大格相減→中間熱點圖。每條路需要單獨標模型來源，AE不產生學生特徵。局部與全域都是第二區內小節，不新增第四大區。第三區簡潔兩路校準合併中右雙熱點→同待測托盤回查。刪圖中的技術糾錯句『AE不產生學生特徵，教師不更新』改用正確圖本身表達。唯一#FFF4CC燈泡結論保留完整。少字大圖，不把兩路再擠左右，不畫章節數字徽章。"}

