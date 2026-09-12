# ByteTrack：先高分，再接剩餘低分
- lesson objective: 低分框要有軌跡依據，才可能接回原ID。
- page type: C
- primary reading path: 每幀框分高分與低分 → 先高分，再補未配對軌跡 → 接回ID或標成暫時丟失 → 低分框要有軌跡依據，才可能接回原ID。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 低分框要有軌跡依據，才可能接回原ID。 #FFF4CC
- major visual nodes:
  1. 每幀框分高分與低分
  2. 先高分，再補未配對軌跡
  3. 接回ID或標成暫時丟失
偵測框分高/低分，先以高分框匹配預測軌跡，再用低分框匹配剩餘未配對的活動軌跡。給定ID7短暫遮擋造成0.3低分但位置接近，可第二輪續接；孤立低分不直接建新ID。未接回則丟失，超過保留期移除；計數線與事件由下游另訂。分數只是算例，非建議門檻。
來源：https://github.com/FoundationVision/ByteTrack
模式：新SVG→PNG；八課原首讀桌機已逐張實看，異常金屬板維持大小孔及右側刮傷，影片維持方件/ID7的L標記。先機制原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。
