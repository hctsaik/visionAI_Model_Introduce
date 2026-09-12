# ControlNet：控制殘差接入去噪主幹
- lesson objective: 條件控制布局，細節仍要回原條件核對。
- page type: C
- primary reading path: 雙孔輪廓形成控制條件 → 可訓練分支經零初始化連接 → 多步條件去噪再比輪廓 → 條件控制布局，細節仍要回原條件核對。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 條件控制布局，細節仍要回原條件核對。 #FFF4CC
- major visual nodes:
  1. 雙孔輪廓形成控制條件
  2. 可訓練分支經零初始化連接
  3. 多步條件去噪再比輪廓
同上方雙孔矩形板，輪廓圖含外框/兩孔，文字指定銀色金屬。預訓練主幹固定，可訓練編碼副本接條件，zero convolution初始化0以殘差連接主幹；訓練後連接通常不為0。每步讀時間/噪聲latent與條件；不把輪廓輸出當缺陷熱點。 r01實看修正：輪廓外框與孔框同用白線。
來源：https://arxiv.org/abs/2302.05543
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。
