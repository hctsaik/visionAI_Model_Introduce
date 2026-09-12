# TF-IDG：免訓練仍有反向計算
- lesson objective: 每步特徵梯度也要算進延遲與記憶體。
- page type: C
- primary reading path: 模型權重固定且不更新 → latent求導需中間激活 → 保存參考與引導設定 → 每步特徵梯度也要算進延遲與記憶體。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 每步特徵梯度也要算進延遲與記憶體。 #FFF4CC
- major visual nodes:
  1. 模型權重固定且不更新
  2. latent求導需中間激活
  3. 保存參考與引導設定
官方autograd.grad(loss,latent)是採樣引導；不要把免微調等同只有一次前向。計入特徵、梯度、採樣與背景融合時間；未實測不給速度排名。
來源：https://github.com/rubymiaomiao/TF-IDG ; https://raw.githubusercontent.com/rubymiaomiao/TF-IDG/main/cldm/ddim_hacked.py
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。
