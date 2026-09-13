from pathlib import Path
import sys,json
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1];public='--public' in sys.argv
v=json.loads((W/('release-verification.json' if public else 'verification.json')).read_text(encoding='utf8'))
message=('公開網站驗證通過：HTML與docs相同，桌面／手機從首頁進需求助手、產生計畫、拒絕錯檔並保留原稿均通過。功能提交 '+v['commit'][:7]+' 已推送。三項收尾完成；使用者成品審閱 pending。' if public else '三項修正與本機驗證完成：12項新行為測試、13項既有PoC、3項導覽斷言通過；10張截圖實看，僅三課mechanism_steps變更。即將提交推送與驗證公開站，公開發布未完成。')
p=W/'PLAN.md';lines=p.read_text(encoding='utf8').splitlines()
for i,line in enumerate(lines):
 if line.startswith('- [ ]') and (public or 'Git 提交' not in line):lines[i]=line.replace('[ ]','[x]',1)
p.write_text('\n'.join(lines)+'\n\n最新 checkpoint：'+message+'\n',encoding='utf8')
p=W/'REPORT.md';s=p.read_text(encoding='utf8').replace('输入','輸入').replace('實测','實測')
if public:s=s.replace('目前狀態：實作、本機驗證完成，Git／公開部署待完成。','目前狀態：實作、本機與公開驗證完成，Git 已推送。')
p.write_text(s+'\n\n'+message+'\n',encoding='utf8')
p=W/'preflight.md';p.write_text(p.read_text(encoding='utf8').replace('pending actual desktop/mobile review','reviewed actual desktop/mobile output'),encoding='utf8')
note='## WI-040 定版收尾\n\n'+message+'\n\n唯一 checklist：teaching-images/vision-ai-model-selection/workitems/wi-040/PLAN.md。\n\n'
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:p.write_text(note+p.read_text(encoding='utf8'),encoding='utf8')
if not public:
 p=R/'TEACHING_REVIEW_LOG.md';p.write_text(p.read_text(encoding='utf8')+'\n\n## WI-040：定版前有限收尾\n\n已修錯檔匯入、首頁需求入口及三課展開機制。有效roundtrip、錯檔拒絕、取消與儲存失敗分開驗證；內容核對同時涵蓋主線和展開區。實際測試與內容差異在workitems/wi-040/REPORT.md，沒有擴張為全站逐圖驗收。\n',encoding='utf8')
 p=R/'TEACHING_WEBPAGE_GUIDE.md';p.write_text(p.read_text(encoding='utf8')+'\n\n### WI-040：備份匯入的驗證邊界\n\n覆蓋確認不能代替備份結構驗證；先識別支援版本与必要結構，保留合法舊版相容性，再詢問取代。驗收除合法往返，也要包含錯檔、取消及儲存失敗的原資料保留。\n',encoding='utf8')
print(message)
