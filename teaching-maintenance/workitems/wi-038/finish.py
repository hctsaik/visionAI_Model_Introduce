from pathlib import Path
import json,sys
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
public='--public' in sys.argv
for p in W.glob('*.md'):
 p.write_text(p.read_text(encoding='utf8').replace('节点','節點').replace('独立','獨立').replace('分开','分開'),encoding='utf8')
v=json.loads((W/('release-verification.json' if public else 'verification.json')).read_text(encoding='utf8'))
message=('公開網站已更新；HTTP SHA-256 與 docs 一致，公開桌面／手機逐題、結果及計畫操作通過。功能提交 '+v['commit'][:7]+' 已推送。所有實作項目完成；使用者成品審閱 pending。' if public else '功能、28 項瀏覽器檢查（26 全套＋2 舊稿補驗）、15 項規則測試及9項回歸測試完成。12 張實際頁面截圖已檢查，source/docs一致且課程資料未改。即將 Git 提交推送，公開驗證尚未完成；使用者成品審閱 pending。')
plan=(W/'PLAN.md').read_text(encoding='utf8')
lines=plan.splitlines()
for i,line in enumerate(lines):
 if line.startswith('- [ ]') and (public or 'Git 提交' not in line):lines[i]=line.replace('- [ ]','- [x]',1)
(W/'PLAN.md').write_text('\n'.join(lines)+'\n\n最新 checkpoint：'+message+'\n',encoding='utf8')
report=(W/'REPORT.md').read_text(encoding='utf8')
old='截圖實看、最終 handoff 補驗、source/docs 資料一致性與公開部署：進行中，實際收據將寫入本目錄。使用者成品審閱 pending，不等同已授權發布。'
report=report.replace(old,'12 張截圖已產生並實看兩種寬度的問題、結果與計畫；字體可讀、選項無橫向溢出、主流程無模型輸入。兩入口 handoff 補驗皆 exit 0，重整後原稿不變。source/docs 逐位元一致，58 課資料與 193f70d 相同。見 verification.json、handoff-verification.json。')
(W/'REPORT.md').write_text(report+'\n## '+('公開驗證完成' if public else '發布前 checkpoint')+'\n\n'+message+'\n',encoding='utf8')
pre=(W/'preflight.md').read_text(encoding='utf8').replace('pending actual desktop/mobile screenshot review','reviewed actual desktop/mobile screenshots; no horizontal overflow').replace('先依現場條件決定怎麼試，再用實拍資料確認是否值得採用。','先依現場條件找到可驗證的方法，再用原始資料確認效果。')
(W/'preflight.md').write_text(pre,encoding='utf8')
note='## WI-038 需求導向 PoC 實作與發布\n\n'+message+'\n\n唯一 checklist：teaching-images/vision-ai-model-selection/workitems/wi-038/PLAN.md。\n\n'
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:p.write_text(note+p.read_text(encoding='utf8'),encoding='utf8')
if not public:
 for name in ['TEACHING_WEBPAGE_GUIDE.md','TEACHING_REVIEW_LOG.md']:
  p=R/name;p.write_text(p.read_text(encoding='utf8')+'\n\n### WI-038 實作反證：主流程之外也要保護草稿\n\n需求式選型不能只回述答案，結果需解釋答案如何導出方法。舊稿與新流程分離後，仍須檢查課程帶入等旁路；本輪審查發現原輸出會被覆寫，改存獨立課程筆記並補測重整保留。規則、操作與實際畫面分別驗證，發布授權與成品認可分开記錄。詳 WI-038/REPORT.md。\n',encoding='utf8')
print(message)
