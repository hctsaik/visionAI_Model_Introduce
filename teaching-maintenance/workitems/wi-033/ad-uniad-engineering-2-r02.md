# UniAD：限制注意力照抄，再重建
- lesson objective: 遮的是特徵取用連線，原影像仍完整。
- page type: C
- primary reading path: 同圖抽特徵，原圖不擦除 → p不能讀自己與近鄰 → query引導重建後比特徵 → 遮的是特徵取用連線，原影像仍完整。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 遮的是特徵取用連線，原影像仍完整。 #FFF4CC
- major visual nodes:
  1. 同圖抽特徵，原圖不擦除；uni-input
  2. p不能讀自己與近鄰；uni-mask
  3. query引導重建後比特徵；uni-rebuild

多類正常共同訓練重建模型，固定骨幹。neighbor-masked attention限制當前位置讀自己及近鄰的連線；layer-wise query與訓練特徵擾動降低相同捷徑。推論不做訓練擾動，將原特徵與重建同位置差異映回位置；本圖5x5只是注意力鄰域示意，不是固定輸入尺寸。
來源：https://arxiv.org/abs/2206.03687
模式：新精確SVG→1672×941/768×2304PNG，非既有點陣編修。八課原首讀桌機已實看：PatchCore無孔板、PaDiM單孔板，其餘左上大孔/右下小孔板及右側刮傷p，保持身份；先機制原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

## r02 原生桌機審查修正
八張r01桌機已實看，手機未審未啟用。PatchCore距離簡式避免超框，PaDiM縮短分布標籤且標q/縮小橢圓避免壓算式；Subspace殘差工件上移，RD瓶頸上移避免壓圖說；STFPM三層改明示已對齊網格同位置p；AE標q，DRAEM補實際合成mask小圖，UniAD明示p中心局部取用。三節點/讀序/結論不變。即將渲染16PNG；原生/頁內/user仍pending。
