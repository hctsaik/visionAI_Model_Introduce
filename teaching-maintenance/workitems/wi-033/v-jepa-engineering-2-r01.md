# V-JEPA：預測同位置的目標特徵
- lesson objective: 目標特徵提供訓練訊號，部署另學任務。
- page type: C
- primary reading path: 可見區編碼並指定遮蔽位置 → 完整影片產生停止梯度目標 → 同遮蔽位置比較特徵差 → 目標特徵提供訓練訊號，部署另學任務。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 目標特徵提供訓練訊號，部署另學任務。 #FFF4CC
- major visual nodes:
  1. 可見區編碼並指定遮蔽位置
  2. 完整影片產生停止梯度目標
  3. 同遮蔽位置比較特徵差
2024原版V-JEPA；上下文編碼器讀可見tokens，預測器加遮蔽位置資訊預測目標tokens。完整影片只進目標編碼器，目標stop-gradient，其權重由上下文EMA更新。L1比較同位置特徵。作者兩維算例預測[.2,.8]目標[.4,.7]平均絕對差.15，不是異常分數。
來源：https://arxiv.org/html/2404.08471v1
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。
