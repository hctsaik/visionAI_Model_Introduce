import json,shutil,hashlib
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
retained=[]
for slug,names in {'sift':['sift-r06-c2-how.png','sift-r06-d4-stop.png'],'ecc':['ecc-r06-c3-get.png','ecc-r06-d4-stop.png']}.items():
 p=C/'_course_content/topics'/f'{slug}.json';t=json.loads(p.read_text(encoding='utf-8'));folder=(C/t['review_trace']['authority']).parent
 links=[v for v in t['engineering_slides'][3].get('evidence_links',[]) if 'WI032-retained-' not in v['image']]
 for name in names:
  src=C/'_course_content/generated-concepts'/slug/name;dest=folder/'images/final'/('WI032-retained-'+name);shutil.copyfile(src,dest)
  rel=dest.relative_to(C).as_posix();links.append({'title':'歷史R06教學示意原圖：'+('配對數與模糊案例' if slug=='sift' else '位移與起點案例')+'（非本輪實測）','image':rel})
  retained.append({'source':src.relative_to(C).as_posix(),'image':rel,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'evidence':'原圖標示教學示意、非實測；保留歷史案例，不沿用為新推論結果'})
 t['engineering_slides'][3]['evidence_links']=links;p.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 mp=folder/'model.md';s=mp.read_text(encoding='utf-8')
 s+='\n\n## WI-032 歷史案例的證據範圍\n\nR06原圖標示「教學示意，非實測」。原圖數字可用於查閱既有教學案例；本輪沒有重跑產生程序，也不以此宣稱現場性能。圖內舊簡寫不取代本輪機制與條件说明。\n\n'
 s+='\n'.join('- ['+link['title']+']('+Path(link['image']).relative_to(folder.relative_to(C)).as_posix()+')' for link in links)+'\n'
 mp.write_text(s,encoding='utf-8')
 with (folder/'slide-manifest.md').open('a',encoding='utf-8') as f:f.write('\n### R06歷史示意（未重評為新主線）\n\n'+'\n'.join('- ['+Path(link['image']).name+']('+Path(link['image']).relative_to(folder.relative_to(C)).as_posix()+')' for link in links if 'WI032-retained' in link['image'])+'\n')
(W/'retained-evidence.json').write_text(json.dumps(retained,ensure_ascii=False,indent=2),encoding='utf-8')
p=R/'Overall_Review.md';s=p.read_text(encoding='utf-8').replace('保留有來源且有效的既有實測，例如ECC工程4案例。','保留既有案例及來源，例如ECC工程4；R06原圖標示教學示意，不把歷史數字升級為實測。');p.write_text(s,encoding='utf-8')
lines=['# WI-032 來源、版本與示意界線','','本輪以第一手論文、官方文件及既有教材核對機制。沒有新模型推論、相機校正或真人學習測試。幾何精確圖是新SVG經瀏覽器繪製；其餘主線圖使用內建imagegen，prompt意圖、失敗稿及修正版保存在同工作項目。','', '| 課程 | 核對來源 | 版本／主張範圍 |','| --- | --- | --- |']
notes={'charuco':'OpenCV 4.13.0；板角點身份、多視角校正與已知內參求姿態分開。','ecc':'OpenCV 4.13.0 findTransformECC；函式回傳相關與warp。採樣方向以xI=W(xT)定義，常見warp用WARP_INVERSE_MAP。','sift':'OpenCV SIFT；尺度／方向、4×4×8描述與ratio test，幾何估計另接。','lightglue':'官方預訓練matcher與相容extractor；自注意力、交互注意力、提前停止與點修剪。','det-dino-detector':'DINO偵測論文（2203.03605），不是DINOv2；mixed query位置／內容、訓練專用對比去噪。','yolo-world':'YOLO-World論文2401.17270 v3第3.3節：文字引導max＋sigmoid權重，以及ImagePooling Attention；快取與官方支援的重參數化分開，版本差異需查部署實作。'}
for slug,a in json.loads((W/'lesson-content.json').read_text(encoding='utf-8')).items():
 sources=list(dict.fromkeys(a['sources']+[r['source'] for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')) if r['owner']==slug]))
 lines.append('| '+slug+' | '+'；'.join('[來源'+str(i+1)+']('+url+')' for i,url in enumerate(sources))+' | '+notes[slug]+' |')
lines+=['','## 既有證據保留','','ECC工程4原圖仍由工程4段落連結；R06的SIFT 120／104、模糊46／4及ECC 32／12、遠起點217px案例依原圖的「教學示意，非實測」界線保留，未另行確認原始演算程序。複製檔與原檔SHA256相同，見retained-evidence.json。','', '## 本輪可驗證範圍','','SVG座標能核對同一板角點／同一工件及幾何變換；4像素40、80、120、160中心的雙線性插值示例為100。相似度格、描述條、候選框、曲線、速度流程都是機制示意，不提供準確率或FPS。原生圖自評、實頁檢查、自動測試與使用者核准各自紀錄。']
(W/'sources.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n## 驗證與來源checkpoint\n修正版已通過14 tests及130 subtests；六課第二輪24頁狀態檢查接近完成。新增歷史R06來源連結：4個PNG原樣複製到formal目錄，保留SHA；原圖標示非實測，sources.md已釐清。這次僅補來源連結及model.md，不改新圖。即將重建bundle，檢查新增連結、scope、HTTP/hash與最終評分；user approval pending。\n')
