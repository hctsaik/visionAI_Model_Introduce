from pathlib import Path
C=Path(__file__).resolve().parents[2]; R=C.parents[1]; W=C/'workitems/wi-033'
note='''## WI-033 持續完成授權（2026-09-12）

使用者要求「一口氣完成」第二部分全部52課，批次之間持續執行。最後完成6課；第二批4課48張新PNG已接入，先前10 tests/130 subtests及16主頁驗證有紀錄。手機CSS補修後的補驗未完成。已核對沒有WI-033生成/QA程序仍執行，本機8000服務存在。
即將重建後核對58課手機圖說、第二批深讀與主頁，再完成後42課；產物與唯一checklist在workitems/wi-033/PLAN.md。使用者成品核准pending，未發布。本次新測試尚未跑。首次接續註記經PowerShell管線發生中文字編碼損失，已用UTF-8檔案修正；教材未受影響。

'''
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:
 s=p.read_text(encoding='utf-8'); end=s.find('## WI-033 最新 checkpoint')
 p.write_text(note+s[end:],encoding='utf-8')
p=W/'PLAN.md';s=p.read_text(encoding='utf-8');s=s.split('## WI-033 ???????')[0];p.write_text(s+'\n'+note,encoding='utf-8')
