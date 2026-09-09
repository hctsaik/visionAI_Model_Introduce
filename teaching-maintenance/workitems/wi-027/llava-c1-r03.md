# WI027 LLaVA r02 修正
- lesson objective: 看懂特徵經投影後與問題一起进入語言模型。
- page type: C — 真正橋接路徑。
- primary reading path: 影像與問題 → 編碼成特徵 → 投影接入語言模型 → 回答後核對原圖。
- major visual nodes:
  1. 原圖與問題。
  2. 編碼器及非照片的特徵示意。
  3. 特徵→投影→視覺序列→LLM，問題另入。
  4. 回答與來源核對。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已看。
- pale-yellow takeaway: #FFF4CC 視覺特徵接上問題，才形成可以追問的回答。
- correction: r01 照片加格線被標成特徵，且特徵繞過投影進LLM。改成獨立特徵示意、來源局部標示、移除旁路；不把AI圖稱真實影像。
- review: pending；user approval pending。生成prompt與來源在generation-batch2.json。

## r03 correction
Edit supplied image panel3 only. There are upper projectedvisualtokens and lower questiontokens. Label UPPER tokens 「視覺 tokens」 and LOWER tokens 「文字 tokens」 separately. Do not let one visualtokenlabel cover questiontokens. Both groups feed the SAME LLM via existingbrace. Feature→projection→visualtoken path unchanged. Otherthreepanels, takeaway, exact724x2172canvas unchanged.
Generation-batch9.json; native and CSS-size review pending; user approval pending.
