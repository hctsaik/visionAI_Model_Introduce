from pathlib import Path
W=Path(__file__).resolve().parent
s=(W.parent/'wi-028/integrate.py').read_text(encoding='utf-8').replace('wi028','wi030').replace('WI028','WI030').replace('WI-028','WI-030').replace('wi-028','wi-030')
a=s.index('owners=');b=s.index('for slug in sys.argv',a)
s=s[:a]+'''owners={id:r['owner'] for id,r in plans.items()}
groups={
'ad-d3':[
 {'model':'PatchCore','normality':'正常CNN局部特徵＋代表子集庫','candidate':'局部最近鄰差異；維護庫大小與覆蓋'},
 {'model':'PaDiM','normality':'每位置平均與共變異','candidate':'位置條件距離；維護對位與分布'},
 {'model':'AnomalyDINO','normality':'DINOv2區塊特徵正常參考','candidate':'特徵相似度；維護表示與參考'},
 {'model':'EfficientAD','normality':'正常訓練教師／學生與AE關係','candidate':'局部＋全域差；維護權重及校準'}],
'class-d3':[
 {'model':'ResNet','normality':'類別標註；殘差特徵相加','candidate':'已知類別；同資料測錯誤與成本'},
 {'model':'ConvNeXt','normality':'類別標註；現代空間／通道卷積','candidate':'已知類別；不能以模型新舊排名'},
 {'model':'ViT','normality':'類別標註；區塊表示與注意力','candidate':'已知類別；注意力不是輪廓真值'}],
'seg-d3':[
 {'model':'U-Net','normality':'像素標註；編碼解碼同尺度跳接','candidate':'語意區域；邊界与尺度需另驗'},
 {'model':'SegFormer','normality':'像素標註；階層特徵多尺度融合','candidate':'語意區域；不自動提供每件ID'},
 {'model':'YOLOv8-seg例','normality':'每件標註；原型＋每件係數','candidate':'每件框與遮罩；漏檢重疊逐件驗'}],
'pose-d3':[
 {'model':'Keypoint R-CNN','normality':'每件框與點名標註；工業任務訓練','candidate':'2D點及物件歸屬'},
 {'model':'幾何與相機資料','normality':'同名3D點、內參畸變與一致單位','candidate':'把2D點接到幾何問題'},
 {'model':'PnP姿態流程','normality':'足夠正確對應；適用求解與多解驗證','candidate':'物體→相機姿態；接工站需外參'}]}
''' + s[b:]
s=s.replace("if id=='conv-d2':caption+=' 圖中的夾爪小圖用來表示狀態意義，不是記憶張量的實際外觀。'",'')
s=s.replace("t['quality_status']=", "if 'deep_dive' in t:t['deep_dive']['default_collapsed']=True\n t['quality_status']=")
s=s.replace('WI-030 八個時序主題首讀圖文與手機PNG、反例、比較及自測','WI-030 十二課首讀圖文與手機PNG、反例、比較及自測')
(W/'integrate.py').write_text(s,encoding='utf-8')
print('Prepared integration script; no authored topics mutated')
