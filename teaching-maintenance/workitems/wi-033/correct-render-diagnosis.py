from pathlib import Path
from PIL import Image,ImageChops
import json,runpy
W=Path(__file__).resolve().parent
a=Image.open(W/'ground-render-diagnostic-fresh.png');b=Image.open(W/'det-grounding-dino-interface-engineering-2-r02-desktop.png')
assert ImageChops.difference(a,b).getbbox() is None
out=dict(independent_capture='ground-render-diagnostic-fresh.png',candidate='det-grounding-dino-interface-engineering-2-r02-desktop.png',decoded_pixels_identical=True,rt_r01_pcb_pixel=list(Image.open(W/'det-rtdetr-engineering-2-r01-desktop.png').getpixel((1200,300))),finding='Apparent missing graphic in review display was not a defect in PNG. Earlier causal claim retracted; no evidence GPU setting fixed a broken asset. Keep explicit font readiness and content revisions.',user_approval='pending')
(W/'render-diagnostic-result.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
note='''### WI-033 更正第四批缺畫判斷

獨立新browser重拍Grounding r02，與候選PNG逐像素完全相同（difference bbox=None）；RT r01被認為缺圖處的像素也是PCB色(217,236,230)。因此先前「PNG缺畫」判断撤回：是審查顯示誤判，沒有證據顯示原PNG損壞或disable-gpu修復了圖。ground-render-diagnostic-fresh.png已完整實看；證據render-diagnostic-result.json。保留r02實質尺度/透明遮罩/命名修正，繼續逐張審查；不再為顯示誤判重畫教材。第三批完成17/52，第四批其餘工程及後27課持續；使用者核准pending。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('\n'+note)
