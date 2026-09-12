# PatchCore：查最近正常特徵，再排回位置
- lesson objective: 局部距離來自特徵查庫，熱區要回原圖核對。
- page type: C
- primary reading path: 正常特徵挑選代表子集 → 待測p查最近正常代表 → 每個距離排回原位置 → 局部距離來自特徵查庫，熱區要回原圖核對。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 局部距離來自特徵查庫，熱區要回原圖核對。 #FFF4CC
- major visual nodes:
  1. 正常特徵挑選代表子集；pc-coreset
  2. 待測p查最近正常代表；pc-distance
  3. 每個距離排回原位置；pc-map

固定CNN抽正常局部特徵，以coreset保留代表子集；待測局部在同特徵空間查最近鄰。二維例p=[3,2]，r1=[0,0]距離3.61，r2=[2,0]距離2.24；p位置排回2.24。圖中小網格僅局部距離示意，整圖分數還有原法的重加權，不能把局部距離說成缺陷機率。
來源：https://arxiv.org/abs/2106.08265
模式：新精確SVG→1672×941/768×2304PNG，非既有點陣編修。八課原首讀桌機已實看：PatchCore無孔板、PaDiM單孔板，其餘左上大孔/右下小孔板及右側刮傷p，保持身份；先機制原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

## r02 原生桌機審查修正
八張r01桌機已實看，手機未審未啟用。PatchCore距離簡式避免超框，PaDiM縮短分布標籤且標q/縮小橢圓避免壓算式；Subspace殘差工件上移，RD瓶頸上移避免壓圖說；STFPM三層改明示已對齊網格同位置p；AE標q，DRAEM補實際合成mask小圖，UniAD明示p中心局部取用。三節點/讀序/結論不變。即將渲染16PNG；原生/頁內/user仍pending。
