from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent
notes={
'resnet':{1:'完整/刮傷標註與整件分數一致；中間殘差例連到更新後表示',3:'兩張不同特徵圖平均均1，可見分類彙整丟失空間；類別映射留存',4:'同件同刮傷只换背景，分類分數與需另標像素的定位責任分開'},
'convnext':{1:'空間鄰域/通道組合分工接整件分類，不把分數作位置圖',3:'前處理、彙整與逐類錯分在同一交付鏈；平均例可追',4:'同訓練條件下比較殘差與空間通道路徑，沒有串成兩模型'},
'vit-classifier':{1:'原圖分片加位置，再由分類token讀出；同件刮傷保留',2:'刮傷片名稱已與圖一致，0.75/0.25加權得[1.5,1]且非缺陷機率',3:'粗格只標取樣位置，不再人工挖断冒充結果；4/16 token對應16/256配對',4:'明確限定ConvNeXt逐通道空間卷積，避免誤稱所有卷積不混通道'},
'u-net':{1:'同位像素標註、跳接及分類遮罩一致；縮小中間輸出避免壓字',3:'ROI/resize/padding標籤框已加寬，輸出回原圖後再談量測',4:'同位置細線對比連續/候選斷裂，孔洞與基板身份未更換'},
'segformer':{1:'同件焊線輸入逐級四尺度後輸出語意遮罩；不是實例ID',3:'同件粗格取樣及映回原圖，不能用多尺度補造細線',4:'共同標註下對比跳接與四尺度對齊，U-Net圖不再壓字'},
'yolo-seg':{1:'兩件同類支架各有框與遮罩，甲乙標籤不蓋孔洞或邊框',3:'去重前後同顯示尺度，保留框/係數配對；孔洞結果與文字分離',4:'同類兩件在語意輸出同類別，實例輸出保留甲乙；孔洞未填滿'},
'keypoint-r-cnn':{1:'A缺口角與B/C孔心具名，ROI與三張位置分布身份一致',3:'同件C遮擋仍有估計，說明估計不等於可見；已移除無目標箭頭',4:'同支架比較具名點與區域輸出，沒有把遮罩當孔心座標'}}
limits={
'resnet':'矩陣及分數為給定教學例，照片是幾何示意；不替代域內結果。',
'convnext':'比較重用共同輸入以控制條件，質感較簡單；時間需實測。',
'vit-classifier':'單頭與小格為縮小算例；粗格只示意取樣位置，沒有宣稱新推論。',
'u-net':'流程只顯示代表尺度，藍色是示意遮罩；尺寸必須另校正。',
'segformer':'細格代表解析度，不能逐格讀成實測特徵；比較文字仍較密。',
'yolo-seg':'代數原型與輪廓是示意；需要實例分離及邊界誤差實測。',
'keypoint-r-cnn':'分布格位為概念，三點是點名示意，PnP仍須檢查點數和退化。'}
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'));out=[]
for r in rows:
 if r['owner'] not in notes or r['index'] not in notes[r['owner']]:continue
 ev=notes[r['owner']][r['index']];limit=limits[r['owner']]
 for mode in ['desktop','mobile']:
  f=W/f"{r['id']}-{r['version']}-{mode}.png"
  scores=[23,24,18,18,9]
  if r['owner']=='segformer':scores=[22,24,18,18,9]
  out.append(dict(id=r['id'],image=f.name,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),scores=scores,total=sum(scores),evidence=[ev,limit,'逐張實看選定版本桌機與手機原生PNG，未用測試替代視覺審查'],completion={'aesthetics':[8,'淺底三段圖解，精確但較簡化'],'completeness':[9,r['takeaway']],'professionalism':[9,ev],'density':[8,limit],'hierarchy':[9,'三節點單讀序及單黃結論']},veto=[],native_review='passed',page_review='pending',user_approval='pending'))
assert len(out)==44
(W/'batch3-expanded-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('\n第三批擴展21故事與ViT工程2最新修訂共44PNG已逐張桌機/手機實看；語意/壓字/標籤缺口及選定版本見batch3-expanded-image-assessment.json。分數91–92為本輪原生自評，尚無頁內或使用者核准。舊錯誤版本保留，不啟用。\n')
print('44 reviewed assets recorded; page review pending')
