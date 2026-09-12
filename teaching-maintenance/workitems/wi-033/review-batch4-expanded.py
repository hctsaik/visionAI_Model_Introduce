from pathlib import Path
import json,hashlib,runpy
W=Path(__file__).resolve().parent
notes={
'det-yolo-dense':'同PCB候選/去重/原圖映射分開，驗收另列定位偏移與漏框，非NMS同例矛盾。',
'det-rtdetr':'query起點與更新次數可追，訓練匹配不混入推論，與YOLO按工作成本比較。',
'det-grounding-dino-interface':'任務图以resistor對應兩框，工程2另講交互；提示和門檻一起保存。',
'yoloe':'三種模式是替代入口；SAVPE向量加權可算，同類外觀不表示103/272可互換。',
'dinov2':'同L支架、同空間距離.283/.141可核算，背景控制與下游判定分開。',
'llava':'同接頭左有右未見，任務證據與投影機制分圖，未知原因不猜測。',
'qwen-vl':'同銘牌B08欄位，位置/像素預算/原圖核對相連，OCR比較不捏造勝負。',
'gemini-vision':'欄位設計與機制分圖，只描述公開請求回覆，格式與內容分別驗。'}
out=[]
for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')):
 if r['owner'] not in notes or r['index'] not in [1,3,4]:continue
 for mode in ['desktop','mobile']:
  p=W/f"{r['id']}-{r['version']}-{mode}.png"
  out.append(dict(id=r['id'],image=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scores=[23,24,18,18,9],total=92,evidence=[r['title']+'；'+notes[r['owner']],'選定桌機與手機逐張原生實看；三節點、框/工件、算例和結論可讀','幾何簡化；部分長術語與長捲動扣分，未真人理解測試'],completion={'aesthetics':[8,'精確幾何與統一配色，質感簡化'],'completeness':[9,r['takeaway']],'professionalism':[9,notes[r['owner']]],'density':[8,'三段直讀，術語稍密'],'hierarchy':[9,'單一路徑與單黃結論']},veto=[],native_review='passed',page_review='pending',user_approval='pending'))
assert len(out)==48
(W/'batch4-expanded-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
note='''### WI-033 第四批68張選定PNG原生審查完成

32工程故事64PNG（16原型+48擴展）及兩個主反例4PNG皆逐張實看，原生自評92、五完成度>=8，使用者核准pending。證據batch4-{prototype,expanded,failure}-image-assessment.json；兩反例已接來源。即將整合八課工程並build.py建置course/docs，再跑32主頁狀態/224放大、來源HTTP一致與必要8 tests/120 subtests，逐張實頁複核。新實頁驗證未跑，完成仍17/52；後27課繼續。產物workitems/wi-033。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
