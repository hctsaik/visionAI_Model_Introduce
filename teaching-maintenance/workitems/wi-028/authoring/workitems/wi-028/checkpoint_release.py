from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
p=W/'PLAN.md';s=p.read_text(encoding='utf-8')
for line in ['Frame Difference、Background Subtraction、Lucas–Kanade、RAFT 桌面／手機圖文。','ByteTrack、ConvLSTM、VideoMAE、V-JEPA 桌面／手機圖文。','整合 topics、learner briefs、model.md，重建 course/docs。','逐圖／整頁證據，桌面手機、自測、放大、HTTP／資產一致與必要回歸。']:
 s=s.replace('- [ ] '+line,'- [x] '+line)
s+='\n## Release checkpoint\n- Completed: 36 PNG, eight lesson integrations and self-reviews; 48 UI states, 144 zooms, 16 final states, 72 HTTP hashes and 1292 bundle hashes. Focused tests passed; legacy ChArUco schema failure recorded as pre-existing, not a pass.\n- In progress: rebuilding metadata status, snapshotting durable sources, commit/push and public verification. User review pending; not model inference.\n'
p.write_text(s,encoding='utf-8')
msg='\n## WI-028 八課製作驗證完成、準備發布\n- 36張PNG、八課圖文／反例／比較／自測與操作卡已整合，逐圖和整頁自評通過。來源、prompt、資產hash及分項證據：workitems/wi-028。\n- 已驗證48頁面狀態、144次放大／Escape、自測／導覽，16最終閱讀狀態，72HTTP圖片hash，1292資產與HTML一致；聚焦測試7+4subtests及bundle1通過。\n- 全站舊verifier仍報既有ChArUco inline schema錯誤，歷史有相同紀錄；不宣稱全站檢查全過。\n- 下一步：保存維護快照、commit/push、公開HTML及36PNG核對。使用者核准pending。\n'
for p in [C/'BEGINNER_VISUAL_STATUS.md',C/'BEGINNER_VISUAL_TODO.md',R/'WORKITEMS.md']:
 with p.open('a',encoding='utf-8') as f:f.write(msg)
print('Durable release checkpoint saved')
