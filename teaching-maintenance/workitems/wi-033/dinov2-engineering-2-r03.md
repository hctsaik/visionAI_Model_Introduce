# DINOv2：先學表示，部署再抽特徵
- lesson objective: 訓練的Teacher目標與部署的骨幹要分開。
- page type: C
- primary reading path: 同一支架產生不同視圖 → Teacher提供目標給Student → 部署只抽取整圖與局部特徵 → 訓練的Teacher目標與部署的骨幹要分開。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 訓練的Teacher目標與部署的骨幹要分開。 #FFF4CC
- major visual nodes:
  1. 同一支架產生不同視圖；b4-dino-views
  2. Teacher提供目標給Student；b4-dino-learn
  3. 部署只抽取整圖與局部特徵；b4-dino-deploy

DINOv2組合整圖自蒸餾及局部遮蔽目標等訓練設計；Teacher用Student權重的EMA更新，目標停止梯度，Student學對齊表示而非重建原像素。部署使用選定的預訓練骨幹抽整圖和patch表示，下游分類、查庫或分割另接。圖中支架與數值皆教學示意，未重跑模型。
來源：https://arxiv.org/abs/2304.07193
生成模式：新建精確SVG→桌機1672×941、手機768×2304 PNG；不編修既有點陣素材。已實看本批原主線的具體工件，保留PCB雙電阻、L支架與雙圓接頭的身份。各家族先原型實看再擴展其他工程；DINOv2/Gemini主反例另統一同件。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂：r01 PNG部分圖形／文字缺畫，SVG節點完整；改用disable-gpu並等字型/500ms繪製。NMS前後尺度一致，YOLOE遮罩覆蓋完整電阻並透明保留料號；DINO遮蔽視圖名稱精確。所有候選仍需逐張原生審查。

新增具體Teacher目標與Student預測兩維示意，讓箭頭兩端有對齊對象。未重跑模型，PNG審查pending。
