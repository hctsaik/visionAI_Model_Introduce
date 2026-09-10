from pathlib import Path
R=Path(__file__).resolve().parents[4];W=Path(__file__).resolve().parent;C=W.parents[1]
msg='WI-032 checkpoint：兩部分58課與本輪學習已在Overall_Review.md。6課正文／自測草稿已保存；主線桌機／手機候選持續審查。ChArUco固定棋盤、SIFT/LightGlue固定點、ECC整件一致平移改用原生SVG→PNG；native-r03發現標題間距、張數對照及含糊線標示問題，r04已修正待完整核對。偵測手機r01仍過密，r02減字放大；反例r03簡化。所有舊稿保留，沒有把候選當通過。工程4圖尚未製作、教材尚未整合、整頁及回歸未跑、未發布、使用者核准pending。下一步完成主線原生審查，製作工程層並整合驗證。'
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:
 s=p.read_text(encoding='utf-8');p.write_text('## WI-032 最新接續狀態\n'+msg+'\n\n'+s,encoding='utf-8')
for p in [R/'Overall_Review.md',W/'PLAN.md']:
 with p.open('a',encoding='utf-8') as f:f.write('\n\n'+msg+'\n')
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf-8') as f:
 f.write('\n\n## WI-032 製作中學習：座標與手機密度\n同點／同件必須從單一幾何定義產生；ECC整件平移與局部孔位需要一致。標題與第一個子標題也要測間距。手機直向不等於可讀：1024寬候選縮到手機後文字仍太小，已改極少標註／放大主體的版本。示意候選、人工標註、模型結果必須分開；下一輪驗證須在實際頁寬完成。這些是製作中的修正學習，不是成品已過關。詳見workitems/wi-032/prototype-review.md及本輪prompts。\n')
print('Checkpoint persisted')
