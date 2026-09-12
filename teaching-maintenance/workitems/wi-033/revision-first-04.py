from pathlib import Path
import json,runpy
W=Path(__file__).resolve().parent;p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
for r in rows:
 if r['id']=='dinov3-main-failure':r['version']='r03'
 if r['id'] in ['ad-diffad-engineering-1','ad-diffad-engineering-4']:r['version']='r02'
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('\n## 分支圖與案例一致性再驗\n\nDiffusionAD工程1的噪聲元件預設帶刮痕，讓正常學習圖不小心多出異常；改為明確無缺陷參數，禁止沿用錯稿。工程4補A+R共同進分割，避免R到結果的簡化箭頭造成誤解。DINOv3反例粗格原先只以格中心與局部淺色表意，改用每格100個解析式幾何樣本取平均，固定同一墊圈內外徑與缺口座標，不編輯既有PNG。即將版本化重出；不沿用舊分數。\n')
runpy.run_path(str(W/'plan-first-semantics.py'))
