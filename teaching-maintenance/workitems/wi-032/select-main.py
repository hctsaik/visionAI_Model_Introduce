from pathlib import Path
import json,hashlib
from PIL import Image
W=Path(__file__).resolve().parent
selections={
 'charuco-core':('charuco-core-r05-desktop.png','charuco-core-r05-mobile.png'),
 'ecc-core':('ecc-core-r01-desktop.png','ecc-core-r01-mobile.png'),
 'dino-core':('dino-core-r01-desktop.png','dino-core-r02-mobile.png'),
 'world-core':('world-core-r01-desktop.png','world-core-r02-mobile.png'),
 'dino-failure':('dino-failure-r02-desktop.png','dino-failure-r04-mobile.png'),
 'world-failure':('world-failure-r03-desktop.png','world-failure-r03-mobile.png'),
 'detector-compare':('detector-compare-r01-desktop.png','detector-compare-r02-mobile.png'),
}
for id in ['charuco-failure','ecc-failure','sift-core','sift-failure','lightglue-core','lightglue-failure','geometry-compare']:
 selections[id]=tuple(f'{id}-native-r05-{m}.png' for m in ['desktop','mobile'])
notes={
 'charuco-core':'同一棋盤交點A共用座標，多視角與重投影分明；手機獨立加大標註。仿射視角示意，不是校正結果。',
 'ecc-core':'同孔雙邊及强度曲線錯位變接近，warp與獨立殘差分開；手機第三區仍需實頁核對。',
 'dino-core':'GT帶噪近正樣本與遠負樣本不同目標，推論新圖不接GT；手機減字後保留分流。',
 'world-core':'離線詞彙與線上影像兩種表示有不同來源，區域與詞彙比較後出框；手機只保留必要標註，正文補文字引導路徑。',
 'dino-failure':'同一螺栓與墊圈，夾具實際遮住後者；手機最後改物件清單，未冒稱模型會刪除原圖物件。',
 'world-failure':'同一螺栓頭部裂紋與低解析局部相比，改善原始取像另核對；觀測限制示意，非模型結果。',
 'detector-compare':'DINO標註類別訓練與YOLO-World預訓練詞彙路線並列，以同資料核對漏檢／錯類／時間。',
 'charuco-failure':'同板五視角中心集中與廣泛覆蓋不同，獨立邊角觀測／重投影核對；r03標題間距已修。',
 'ecc-failure':'精確平面兩孔件示意，整件橘線平移與孔距一致；單孔錯對時外框不合，明示錯解非實測。',
 'sift-core':'同點A變尺度方向，局部梯度到描述再到代表點對；模型几何另接，不把三條線宣稱足夠求單應。',
 'sift-failure':'同一圖形只改模糊，梯度線索示意變弱；沒有用任意直方圖冒稱實際SIFT輸出。',
 'lightglue-core':'兩個視角A/B/C同身份，含糊虛線到明確點對；上游extractor與後端幾何分工清楚。',
 'lightglue-failure':'只遮住獨特缺口，孔位不移動；不可觀測A與含糊B/C明示，不假造正確線或信心。',
 'geometry-compare':'已知板建立相機幾何、局部描述／學習上下文找點對、ECC外觀微調分開；不以不同行為分數排名。',
}
scores={'charuco-core':[23,23,19,18,10],'ecc-core':[23,23,19,19,9],'dino-core':[23,23,19,18,9],'world-core':[23,23,19,17,9],'dino-failure':[23,23,19,18,9],'world-failure':[23,23,19,19,9],'detector-compare':[23,23,19,18,9]}
result={};assessment=[]
for id,files in selections.items():
 result[id]={}
 for mode,file in zip(['desktop','mobile'],files):
  p=W/file;assert p.exists(),p
  result[id][mode]=file;result[id][mode+'_reviewed']=True
  result[id]['page_review']='pending';result[id]['user_review']='pending'
  score=scores.get(id,[22,23,19,18,10]).copy()
  if id=='ecc-core' and mode=='mobile':score=[23,23,19,18,9]
  if id=='world-core' and mode=='mobile':score=[23,23,19,18,9]
  assessment.append(dict(id=id,mode=mode,image=file,size=Image.open(p).size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),rubric='v1.0',scores=score,total=sum(score),completion=[8,9,9,8,9],observations=notes[id],deductions='示意不提供現場性能證据；局部放大／表示有意簡化，詳細設定由正文補足。原生可讀性不是實頁通過。',scope='原生檢查；最終頁寬另驗',page_review='pending',user_review='pending'))
(W/'selected-assets.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'main-original-assessment.json').write_text(json.dumps(assessment,ensure_ascii=False,indent=2),encoding='utf-8')
print('28 reviewed original candidates selected; page validation pending')
