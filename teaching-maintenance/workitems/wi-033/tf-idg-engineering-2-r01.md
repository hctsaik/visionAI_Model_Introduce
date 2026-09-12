# TF-IDG：梯度引導生成，不改模型權重
- lesson objective: 更新生成中的潛變量，模型權重保持固定。
- page type: C
- primary reading path: 正常板、缺陷參考與局部遮罩 → 特徵差的梯度引導潛變量 → 補弱區並保持背景紋理 → 更新生成中的潛變量，模型權重保持固定。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 更新生成中的潛變量，模型權重保持固定。 #FFF4CC
- major visual nodes:
  1. 正常板、缺陷參考與局部遮罩
  2. 特徵差的梯度引導潛變量
  3. 補弱區並保持背景紋理
同中部兩孔板，下方兩刮傷區。TF-IDG固定預訓練權重；生成局部特徵與參考對齊，梯度對latent求得並進入採樣更新，不是optimizer更新模型權重。自適應遮罩補弱區，AdaIN及背景融合保持紋理；跨材質參考仍可能錯。官方cldm/ddim_hacked.py autograd.grad(loss,latent)可核對；圖中z→z_next只示意引導不是完整採樣公式。
來源：https://github.com/rubymiaomiao/TF-IDG ; https://raw.githubusercontent.com/rubymiaomiao/TF-IDG/main/cldm/ddim_hacked.py
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。
