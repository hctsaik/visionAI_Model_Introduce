from pathlib import Path
import json, shutil, re
W=Path(__file__).resolve().parent;C=W.parents[1]
changes={
'u-net':{0:('像素標註教任務','訓練時以影像和逐像素類別標註配對，讓網路學會區分焊縫與背景；標註邊界和細焊縫都要一致。推論只輸入待測影像，不會附上正確遮罩。','遮罩定義和邊界標註決定學習目標；跳接保留細節線索，不能代替可靠的監督。','影像＋像素標註 → 訓練 → 待測影像的預測遮罩')},
'yolo-seg':{
0:('先有實例標註','訓練影像需分開標出每一件物件的類別與遮罩，讓模型學會逐件偵測及分割；遮擋與重疊處須先訂清楚可見範圍的標註規則。推論不會取得人工答案。','若把兩件標成一片，模型就缺少逐件分開的監督；原型遮罩不是人工標註本身。','逐件類別／遮罩 → 偵測與分割訓練'),
1:('共享底圖，各自組合','以YOLOv8-seg為例，共享特徵產生一組原型遮罩，偵測分支為每件物件預測框、類別與遮罩係數；各件係數組合共享原型，再依框處理成各件遮罩。','A、B各自形成遮罩，不是先算A再把剩下區域當B；重疊漏檢仍須用獨立資料驗證。','共享原型＋每件係數 → 各件遮罩')},
'ad-efficientad':{0:('正常資料教學生','訓練時固定預訓練教師，以正常影像提供特徵目標，更新小型學生去模仿教師。推論時固定權重，教師與學生同看待測圖，再比较局部特徵差異。','學生主要學過正常外觀，異常處可能無法重現教師特徵；差異是待核對線索，不能直接當缺陷尺寸。','正常影像 → 教師特徵監督學生；待測圖 → 比較特徵')},
'convlstm':{1:('卷積更新狀態','每個時間點將新影格特徵與前一時刻的隱藏狀態交給卷積門控，決定舊記憶保留多少、加入哪些新線索，再更新記憶與隱藏狀態；空間位置關係仍保留。','狀態累積的是任務學到的時空線索，不是直接存放舊照片。工業取放判讀還需對應的編碼器、任務頭與訓練。','新影格特徵＋舊狀態 → 卷積門控 → 新狀態')},
'videomae':{1:('只編碼可見塊再重建','預訓練時只把少量可見的時空塊送進編碼器，再由解碼器利用這些表示重建被遮住的像素，並與原始影片比較。遮蔽位置的原像素是訓練目標，不直接交給編碼器。','只編碼可見塊可減少預訓練編碼器的運算；部署動作任務通常保留編碼器、另接任務頭，不需讓重建解碼器一直參與分類。','可見時空塊 → 編碼表示 → 重建遮蔽像素')},
'ad-diffad':{
0:('固定兩尺度的訓練與恢復設定','以正常影像訓練去噪網路，保存噪聲排程、高／低兩個時間步、引導設定、精度、影像裁切與模型版本；合成異常與遮罩另用於訓練定位網路。','去噪和定位有不同監督；兩尺度及引導設定會改變恢復品質與完整成本。','正常去噪訓練＋合成定位訓練 → 固定模型與設定'),
1:('兩個噪聲尺度各做單步估計','同一待測圖分別加入高、低尺度噪聲，各呼叫去噪網路做單步估計；高噪聲分支的正常估計引導低噪聲分支形成恢復對照。保存原圖與恢復結果，接著一同交給定位網路。','每尺度單步不等於整套只呼叫一次網路；恢復也可能保留缺陷或改動正常外觀，須獨立核對。','同一原圖 → 高／低噪聲估計與引導 → 恢復對照 → 定位')}
}
W.joinpath('baseline').mkdir(exist_ok=True)
shutil.copyfile(C/'docs/index.html',W/'baseline/index.html') if not (W/'baseline/index.html').exists() else None
for tid,items in changes.items():
 p=C/'_course_content/topics'/f'{tid}.json';backup=W/'baseline'/p.name
 if not backup.exists():shutil.copyfile(p,backup)
 d=json.loads(p.read_text(encoding='utf8'))
 for i,(title,body,why,anchor) in items.items():
  s=d['mechanism_steps'][i];s.update(title=title,body=body,why=why,anchor=anchor)
  s['diagram']={k:s[k] for k in ['title','body','why','anchor']}
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
data=json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>',(C/'docs/index.html').read_text(encoding='utf8'),re.S)[1])
t=next(t for t in data['topics'] if t['id']=='ad-diffad')
print('DiffusionAD operation document:',t['modelPath'])
(W/'changed-topics.json').write_text(json.dumps(list(changes),indent=2),encoding='utf8')
