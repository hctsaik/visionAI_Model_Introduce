# WI-030 ResNet：保留原有線索，再學需要的修正 — mobile
- lesson objective: 殘差幫助深層訓練；分類答案仍限於學過的類別。
- page type: C
- primary reading path: 已知類別工件 → 殘差兩路相加 → 分類後接工作 → 核對輸出與工作條件
- major visual nodes:
  1. 已知類別工件
  2. 殘差兩路相加
  3. 分類後接工作
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：殘差幫助深層訓練；分類答案仍限於學過的類別。
- source: https://arxiv.org/abs/1512.03385
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：resnet-c1-r02-mobile.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"將ResNet參考圖獨立重排成768x2048手機直式PNG。恰好三大區域由上到下，區域內避免三欄微字。第一區已知三類範例與內六角輸入。第二區『特徵x』先從輸入建立；x分直接路徑與兩次卷積修正F(x)，兩路在加號合併成更新特徵。請將直接線沿右側彎到加號，卷積依中間往下；箭頭不交叉。第三區分類頭三類候選，選內六角，交分流規則。刪無意義分數條，內六角工件不得畫螺帽。繁體中文粗體在328px寬仍清楚，白底淡藍細框，無序號徽章。唯一#FFF4CC燈泡總結『殘差幫助深層訓練；分類答案仍限於學過的類別。』小註『需類別標註訓練／教學示意』。特徵是抽象格，不把原圖直接相加。"}

