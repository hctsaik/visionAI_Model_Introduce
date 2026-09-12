from pathlib import Path
import json,hashlib,runpy
W=Path(__file__).resolve().parent
notes={
'det-yolo-dense':'同PCB四候選按分數及同類IoU去重為兩框；r02前後同尺度，不能補漏候選。',
'det-rtdetr':'訓練query匹配真值/背景與推論修框分段；輸出框實際存在，無NMS仍篩分數。',
'det-grounding-dino-interface':'詞與區域相容性小格及雙向互動接query框；獨立重拍與選定PNG逐像素相同且完整實看。',
'yoloe':'ROI語意特徵按權重聚合得到[1.5,.5]；全電阻半透明遮罩保留料號，視覺提示與其他模式分開。',
'dinov2':'r03目標[.2,.8]/預測[.6,.4]讓對齊有兩端對象；Teacher EMA、stopgrad和部署分開。',
'llava':'同接頭左有右未見，影像經投影與問題接LLM；未知原因不猜測。',
'qwen-vl':'解析度形成可變token，t/h/w位置與B08答案可核對；示意格數與原像素限制明示。',
'gemini-vision':'同接頭與左右JSON欄位逐一查證，右present反例改not_visible，原因unknown；不是API實測。'}
out=[]
for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')):
 if r['owner'] not in notes or r['index']!=2:continue
 for mode in ['desktop','mobile']:
  p=W/f"{r['id']}-{r['version']}-{mode}.png"
  out.append(dict(id=r['id'],image=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scores=[23,24,18,18,9],total=92,evidence=[notes[r['owner']],'逐張實看選定桌機與手機PNG；框、文字、三節點及黃色結論可追','幾何簡化與部分術語較密；未模型實測或真人理解測試'],completion={'aesthetics':[8,'統一精確幾何，質感簡化'],'completeness':[9,r['takeaway']],'professionalism':[9,notes[r['owner']]],'density':[8,'三段直讀，部分專有術語較密'],'hierarchy':[9,'單一讀序/單黃結論']},veto=[],native_review='passed',page_review='pending',user_approval='pending'))
assert len(out)==16
(W/'batch4-prototype-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
note='''### WI-033 第四批八原型原生審查完成

八課工程2選定16PNG已逐張原生實看並記錄92分自評（非使用者核准）：DINOv2 r03，其餘r02。證據batch4-prototype-image-assessment.json；Grounding缺畫判斷已透過独立重拍/逐像素比對撤回，PNG內容完整。即將建立其餘24工程故事與DINOv2/Gemini同件主反例preflight並渲染；未整合、未驗頁。完成17/52，後35課持續；使用者核准pending，未發布。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
