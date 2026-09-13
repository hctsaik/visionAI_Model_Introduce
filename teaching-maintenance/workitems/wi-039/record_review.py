from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
p=W/'PLAN.md';p.write_text(p.read_text(encoding='utf8').replace('- [ ]','- [x]')+'\n最新 checkpoint：審查完成，三份獨立報告與 REVIEW.md 已保存。18課／7家族抽查；公開版與本機一致。建議定版前收尾三项：錯檔匯入、首頁需求入口、三課展開文字一致性。產品未修改、修正未實作、未Git／發布。\n',encoding='utf8')
note='## WI-039 全站定版審查完成\n\n三位 Agent 加主 Agent 已完成本輪審查。結論：可公開使用，定版前先收尾備份錯檔保護、首頁需求入口、三課文字一致性。詳 teaching-images/vision-ai-model-selection/workitems/wi-039/REVIEW.md；唯一 checklist 為同目錄 PLAN.md。公開版本hash561617fd與本機相同；18課／7家族抽查，不宣稱319圖全驗。產品未修改，待修項未實作，沒有Git或發布。\n\n'
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:p.write_text(note+p.read_text(encoding='utf8'),encoding='utf8')
p=R/'TEACHING_REVIEW_LOG.md';p.write_text(p.read_text(encoding='utf8')+'\n\n## WI-039：全站定版審查\n\n三個獨立面向加主Agent反證：新工具內流程成立仍可能缺首頁入口；合法備份roundtrip通過不代表能拒絕錯檔；主圖改好不代表展開參考同步正確。具體證據與優先級見workitems/wi-039/REVIEW.md。沿用既有可見內容一致性與證據分層規則，不新增分數或把抽查當全面驗收。下一轮驗收應補錯檔保留、從首頁無模型名起步、主線／展開文字相互核對。此輪只審查，本機紀錄，未實作／發布。\n',encoding='utf8')
print('Review and durable checkpoints saved; product unchanged.')
