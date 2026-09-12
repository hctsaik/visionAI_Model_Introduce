# AE：同位置40與150，差值110
- lesson objective: 比較原圖與重建估計，重建不是正常真值。
- page type: C
- primary reading path: 同板刮傷p的原圖像素 → 壓縮還原成重建估計 → 同位置取絕對差值 → 比較原圖與重建估計，重建不是正常真值。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 比較原圖與重建估計，重建不是正常真值。 #FFF4CC
- major visual nodes:
  1. 同板刮傷p的原圖像素；ae-input
  2. 壓縮還原成重建估計；ae-reconstruct
  3. 同位置取絕對差值；ae-difference

本課為影像自編碼器基線：正常圖訓練壓縮與重建，推論原圖與重建同位置取差。沿用首讀原圖p灰階40、重建150、絕對差110的作者算例；AE若連刮傷一起重建可能漏檢，正常小孔模糊也會誤報。這裡的絕對像素差是明確選定基線，不概括所有AE評分。
來源：https://arxiv.org/html/2103.04257v3
模式：新精確SVG→1672×941/768×2304PNG，非既有點陣編修。八課原首讀桌機已實看：PatchCore無孔板、PaDiM單孔板，其餘左上大孔/右下小孔板及右側刮傷p，保持身份；先機制原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

## r02 原生桌機審查修正
八張r01桌機已實看，手機未審未啟用。PatchCore距離簡式避免超框，PaDiM縮短分布標籤且標q/縮小橢圓避免壓算式；Subspace殘差工件上移，RD瓶頸上移避免壓圖說；STFPM三層改明示已對齊網格同位置p；AE標q，DRAEM補實際合成mask小圖，UniAD明示p中心局部取用。三節點/讀序/結論不變。即將渲染16PNG；原生/頁內/user仍pending。
