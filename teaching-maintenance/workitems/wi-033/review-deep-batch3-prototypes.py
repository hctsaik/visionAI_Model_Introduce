from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;out=[]
for id,ver,ev,limit,scores in [
 ('resnet-deep-residual','r02','原場景、layer1.1通道93與三張3×3實際特徵完全保留；中央格1.2−1.9經ReLU為0','前後數值經四捨五入，手機第一段次字較小但重點另重述；非新推論',[23,24,19,18,9]),
 ('segformer-deep-core','r04','W-01同亮線四尺度、融合與細線比較保留；精確clipPath與避開鄰行後沒有碎字或第二條黃色框','第二段留白較多，細格只是概念場；不把示意當MiT輸出',[22,24,18,18,9])]:
 f=W/f'{id}-{ver}-mobile.png'
 out.append(dict(id=id,image=f.name,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),scores=scores,total=sum(scores),evidence=[ev,limit,'兩張選定手機PNG已實看；來源桌機保留，實頁另驗'],completion={'aesthetics':[8,'淺底三主節點'],'completeness':[9,ev],'professionalism':[9,'原實測/示意身份保留'],'density':[8,limit],'hierarchy':[9,'單讀序及單黃結論']},veto=[],native_review='passed',page_review='pending',user_approval='pending'))
(W/'batch3-deep-prototype-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
note='''### WI-033 深讀兩家族原型通過、擴展九圖

第三批56工程PNG已原生實看接入來源，尚未build。ResNet residual r02及SegFormer core r04手機原型已實看記分，精確clipPath避免viewBox留白區滲入鄰字，進一步避開半行字；來源實測數字與原場景保留。證據batch3-deep-prototype-image-assessment.json。九份擴展preflight通過，即將deep-batch3-expanded.py產出九張手機2800高PNG；未逐圖審、未整合、未驗實頁。下一步審查九图後整合指定深讀並build/驗證。完成10/52，使用者核准pending，未發布。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8')
import runpy;runpy.run_path(str(W/'append-checkpoint.py'))
