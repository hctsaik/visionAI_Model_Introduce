# AnomalyDiffusion：外觀與位置共同引導
- lesson objective: 逐區核對合成缺陷，不能只相信指定遮罩。
- page type: C
- primary reading path: 外觀嵌入與遮罩空間嵌入 → 較弱區域得到更多注意 → 背景融合與圖像遮罩核對 → 逐區核對合成缺陷，不能只相信指定遮罩。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 逐區核對合成缺陷，不能只相信指定遮罩。 #FFF4CC
- major visual nodes:
  1. 外觀嵌入與遮罩空間嵌入
  2. 較弱區域得到更多注意
  3. 背景融合與圖像遮罩核對
同上方双孔板，大左下/小右下兩區。學異常外觀embedding及mask編碼器，固定擴散主幹；空間及外觀條件引導。AAR用生成估計與正常圖遮罩內差找較弱區域調注意力，背景與正常圖融合。給两mask只生成一傷仍是需剔除的錯標反例，不聲稱自適應必成功。 r01實看修正：恢復原板上方兩孔，保留大左下小右下雙傷；條件pill與caption分離。
來源：https://arxiv.org/html/2312.05767v1
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。
