from pathlib import Path
import json,runpy
W=Path(__file__).resolve().parent;p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
for r in rows:
 if r['id'] in ['dinov3-engineering-1','dinov3-main-failure','ad-diffad-engineering-2','ad-anomalygpt-engineering-2']:r['version']='r02'
 if r['id']=='dinov3-main-failure':r['mobile_height']=2304
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('\n## DINOv3／DiffusionAD／AnomalyGPT r01修訂\n\nDINOv3工程1箭頭碰到B標籤，縮短箭頭；主反例固定同件方向與取樣，但需採主線支援的2304手機高度。DiffusionAD分割結果與末句重疊，縮入圖框並將高噪聲引導線實際接到恢復路徑。AnomalyGPT已修內建支路來源，但解碼／匹配仍偏名詞；補局部表示與正常／異常文字相似順位再回位置。即將輸出r02；未整合這些候選。\n')
runpy.run_path(str(W/'plan-first-semantics.py'))
