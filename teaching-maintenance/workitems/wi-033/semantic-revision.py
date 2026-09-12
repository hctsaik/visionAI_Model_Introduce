from pathlib import Path
import json,runpy
W=Path(__file__).resolve().parent
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
for r in rows:
 if r['id'] in ['pose-engineering-1','pose-engineering-3','dinov3-engineering-2']:r['version']='r02'
 if r['id']=='dinov3-engineering-2':r['takeaway']='Gram 只約束訓練，部署仍輸出特徵。'
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('''
## Pose／DINOv3 原型複核

Pose工程2 r01 取消了錯誤串接，但top-down仍只有「估點」標籤，bottom-up先畫已分組點。r02改成框→各組A/B/C，以及未分組灰點→藍綠實例點；桌機手機實看通過，後續仍需頁內驗證。Pose工程1/3/4原生全圖已實看：1補Z=0平面例、3圖例改只稱橘色觀測點，這兩項以r02重出；4先保留候選，頁面審查仍待。

DINOv3工程2 r01把訓練教師／学生、兩個對稱Gram與共享更新分開；實看桌機手機。r02調整向量算例角度，避免0.98四捨五入成1.0被看成完全相同，並縮短手機結論避免拆開「訓練」。數字仍為示意，未做模型推論。即將生成修訂，舊版本保留，不把原型當整課完成。

SigLIP核心手機改三段配對／損失／部署，r02採已支援768×2304以保持原生尺寸契約；已實看並整合，正在四狀態頁面驗證。先前8項回歸通過但不能替代此改動後的頁面複核。
''')
runpy.run_path(str(W/'plan-first-semantics.py'))
