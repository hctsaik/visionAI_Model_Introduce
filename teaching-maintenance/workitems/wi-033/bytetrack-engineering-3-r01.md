# ByteTrack：幀率與丟失緩衝要配套
- lesson objective: 驗完整影片的斷軌與重複計數。
- page type: C
- primary reading path: 保存偵測與關聯設定 → 同樣緩衝幀數，時間不同 → 遮擋回來可能換ID → 驗完整影片的斷軌與重複計數。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 驗完整影片的斷軌與重複計數。 #FFF4CC
- major visual nodes:
  1. 保存偵測與關聯設定
  2. 同樣緩衝幀數，時間不同
  3. 遮擋回來可能換ID
保存偵測器、分數/匹配門檻、幀率/時間順序、track_buffer與事件規則。給定30幀在30fps是1秒，在10fps是3秒；實作可能按fps縮放，須核對有效幀數。跨攝影機切換應重置，不能沿用不相關ID。
來源：https://github.com/FoundationVision/ByteTrack
模式：新SVG→PNG；八課原首讀桌機已逐張實看，異常金屬板維持大小孔及右側刮傷，影片維持方件/ID7的L標記。先機制原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。
