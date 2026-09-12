from pathlib import Path
import json,importlib.util,runpy
W=Path(__file__).resolve().parent;C=W.parents[1]
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
spec=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
out=[]
for r in rows:
 if not r['panels'][0]['graphic'].startswith('b4-'):continue
 r['version']='r02'
 if r['owner']=='qwen-vl':r['panels'][0]['title']='解析度不同，形成可變token數'
 p=W/(r['id']+'-r02.md');s=(W/(r['id']+'-r01.md')).read_text(encoding='utf-8')
 s=s.replace('不同長寬比形成不同token數','解析度不同，形成可變token數')
 s+='\n修訂：r01 PNG部分圖形／文字缺畫，SVG節點完整；改用disable-gpu並等字型/500ms繪製。NMS前後尺度一致，YOLOE遮罩覆蓋完整電阻並透明保留料號；DINO遮蔽視圖名稱精確。所有候選仍需逐張原生審查。\n'
 p.write_text(s,encoding='utf-8');out.append(v.validate(p))
(W/'engineering-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'batch4-r02-preflight-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
note='''### WI-033 第四批候選繪製缺畫補修

第四批r01桌機8圖及前4手機已實看，發現RT/Grounding輸出PCB與部分手機文字缺畫，SVG節點仍完整；候選不啟用。已修改渲染為disable-gpu、等待字型及500ms，八份r02 preflight通過，即將重繪16PNG。另統一NMS前後顯示尺度、YOLOE全電阻半透明遮罩、DINO遮蔽名稱及Qwen解析度標題。尚未確認修復，剩四張r01手機不浪費重審，直接檢查全部r02。第三批ResNet/ConvNeXt/ViT/U-Net/SegFormer主頁通過，另兩课QA中；完成仍10/52，使用者核准pending。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
print('8 revised preflights; rendering and actual review pending')
