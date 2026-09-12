# SubspaceAD：畫出投影與正交殘差
- lesson objective: 未被正常方向解釋的殘差，才是異常線索。
- page type: C
- primary reading path: 正常特徵擬合PCA方向 → 同一待測特徵正交投影 → 殘差長度排回局部p → 未被正常方向解釋的殘差，才是異常線索。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 未被正常方向解釋的殘差，才是異常線索。 #FFF4CC
- major visual nodes:
  1. 正常特徵擬合PCA方向；sub-fit
  2. 同一待測特徵正交投影；sub-project
  3. 殘差長度排回局部p；sub-residual

固定DINOv2提取patch特徵並用正常資料擬合PCA。給定已中心化特徵x=[3,2]與保留方向U=[1,0]，投影[3,0]，殘差[0,2]長度2。二維幾何例不代表工件平面或實際特徵維度；完整公式需保留均值，圖中明示mu=0。
來源：https://github.com/CLendering/SubspaceAD
模式：新精確SVG→1672×941/768×2304PNG，非既有點陣編修。八課原首讀桌機已實看：PatchCore無孔板、PaDiM單孔板，其餘左上大孔/右下小孔板及右側刮傷p，保持身份；先機制原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

## r02 原生桌機審查修正
八張r01桌機已實看，手機未審未啟用。PatchCore距離簡式避免超框，PaDiM縮短分布標籤且標q/縮小橢圓避免壓算式；Subspace殘差工件上移，RD瓶頸上移避免壓圖說；STFPM三層改明示已對齊網格同位置p；AE標q，DRAEM補實際合成mask小圖，UniAD明示p中心局部取用。三節點/讀序/結論不變。即將渲染16PNG；原生/頁內/user仍pending。
