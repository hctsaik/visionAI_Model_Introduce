from pathlib import Path
W=Path(__file__).resolve().parent
s=(W.parent/'wi-027/integrate.py').read_text(encoding='utf-8').replace('WI-027','WI-028').replace('wi027','wi028').replace('wi-027','wi-028')
start=s.index("plans['dinov2-c1']")
end=s.index("selected=json.loads",start)
s=s[:start]+s[end:]
start=s.index('owners=');end=s.index('for slug in sys.argv',start)
s=s[:start]+'''owners={'flow-d2':'lucas-kanade','video-d2':'videomae','change-d3':'frame-difference','flow-d3':'lucas-kanade','track-d3':'bytetrack','video-d3':'convlstm'}
groups={
'change-d3':[
 {'model':'Frame Difference','normality':'前一影格或指定時刻；選取間隔、門檻和事件規則','candidate':'像素變化；停住後可能消失'},
 {'model':'背景相減','normality':'初始化和更新背景模型；處理光照／陰影','candidate':'相對常態的前景；停久可能被吸收'},
 {'model':'工件偵測／占位感測','normality':'偵測需相應類別資料，感測器需現場安裝與驗證','candidate':'類別框或占位訊號；代價依任務比較'}],
'flow-d3':[
 {'model':'Lucas–Kanade稀疏追點','normality':'不需權重；選角點、窗口、金字塔與幀間隔','candidate':'選定點位移；需檢查追丟與錯配'},
 {'model':'原始RAFT','normality':'預訓練權重、相容前處理、迭代與運算預算','candidate':'稠密像素位移；遮擋仍可能不可靠'},
 {'model':'傳統稠密光流基準','normality':'如Farnebäck；設定尺度和局部估計參數','candidate':'稠密位移；同影片比較誤差、覆蓋及成本'}],
'track-d3':[
 {'model':'逐幀偵測','normality':'相應類別框標註與偵測器；先測漏檢','candidate':'每張框；不直接維持身分'},
 {'model':'偵測＋SORT基準','normality':'相同偵測框、運動預測與關聯設定','candidate':'軌跡ID；遮擋及漏檢可能斷軌'},
 {'model':'偵測＋ByteTrack','normality':'相同偵測器；先高分、再低分補未配對軌跡','candidate':'軌跡ID；計數另設規則並測ID切換'}],
'video-d3':[
 {'model':'ConvLSTM應用','normality':'連續片段、任務標註；訓練空間記憶與任務頭','candidate':'依任務定義的序列輸出；管理狀態／重置'},
 {'model':'VideoMAE原版','normality':'像素重建預訓練；可用現有權重，需下游標註','candidate':'影片表示＋任務頭；重建不是現場判定'},
 {'model':'V-JEPA 2024原版','normality':'特徵預測預訓練；可用現有權重，需下游標註','candidate':'影片表示＋任務頭；不是未來影片生成'}]}
''' + s[end:]
s=s.replace("[a['problem'],a['ideas'][0][1],a['ideas'][1][1],a['output']]","[a['ideas'][0][1],a['ideas'][1][1],a['output']]")
s=s.replace("desc=[a['ideas'][0][1],a['ideas'][1][1],a['output']]", "desc=[a['ideas'][0][1],a['ideas'][1][1],a['output'],a['evidence']]")
s=s.replace("zip(plans[a['assets'][0]]['nodes'],desc)","zip(plans[a['assets'][0]]['nodes']+['工作核對與接手'],desc)")
s=s.replace("'major_visual_nodes':4","'major_visual_nodes':len(plans[a['assets'][0]]['nodes'])")
s=s.replace('七課首讀圖文與手機PNG','八個時序主題首讀圖文與手機PNG')
s=s.replace('原工程slide保留','原工程slide保留')
s=s.replace("mp.write_text(s,encoding='utf-8')", "\n if '<!-- wi028-model-core:start -->' not in s:s+='\\n\\n'+section+'\\n'\n mp.write_text(s,encoding='utf-8')")
(W/'integrate.py').write_text(s,encoding='utf-8')
for name in ['qa_lesson.py','final_pages.py','verify_bundle.py']:
 s=(W.parent/'wi-027'/name).read_text(encoding='utf-8').replace('wi027','wi028').replace('WI-027','WI-028')
 (W/name).write_text(s,encoding='utf-8')
print('Prepared integration and adapted QA scripts; not executed')
