# UniAD：訓練擾動與推論設定分開
- lesson objective: 部署讀原特徵，保存遮蔽與query設定。
- page type: C
- primary reading path: 訓練：擾動特徵再學還原 → 推論：關閉訓練擾動 → 按每個產品核對錯誤 → 部署讀原特徵，保存遮蔽與query設定。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 部署讀原特徵，保存遮蔽與query設定。 #FFF4CC
- major visual nodes:
  1. 訓練：擾動特徵再學還原；b5-uni-training
  2. 推論：關閉訓練擾動；b5-uni-eval
  3. 按每個產品核對錯誤；b5-uni-validation
保存骨幹、重建模型、逐層query、注意力鄰域與訓練擾動設定。推論使用eval設定而非繼續訓練噪聲擾動；位置圖回原圖並按類別評正常誤報/缺陷漏檢，單一平均分數可能掩蓋弱類別。
來源：https://arxiv.org/abs/2206.03687
模式：新精確SVG→1672×941/768×2304PNG，原生八家族原型已審；三節點單讀序，保留同件身份與首讀。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。
