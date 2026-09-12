# DefectFill：學缺陷，再填指定區域
- lesson objective: 先學缺陷外觀，再核對合成位置與真實性。
- page type: C
- primary reading path: 少量缺陷與遮罩教LoRA → 正常板加指定遮罩生成 → 遮罩內感知差異挑候選 → 先學缺陷外觀，再核對合成位置與真實性。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 先學缺陷外觀，再核對合成位置與真實性。 #FFF4CC
- major visual nodes:
  1. 少量缺陷與遮罩教LoRA
  2. 正常板加指定遮罩生成
  3. 遮罩內感知差異挑候選
同一上方雙孔板，下方中心刮傷。少量缺陷及mask微調文字編碼器及attention LoRA；缺陷/物件/attention三損失協同。正常影像+mask進inpainting，LFS挑遮罩內相對原正常图LPIPS更大的候選（較低保真）；給定.1/.3只是示例，不等於物理真實度，仍需逐件位置及真缺陷驗證。
來源：https://arxiv.org/html/2503.13985v1
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。
