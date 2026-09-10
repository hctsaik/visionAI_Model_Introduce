import json
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
d=json.loads((W/'public-release-verification.json').read_text(encoding='utf-8'));assert d['html_matches'] and len(d['png_checks'])==36
msg='''
## WI-028 完成紀錄 — 八個時序 Topic
- [x] Frame Difference、Background Subtraction、Lucas–Kanade、RAFT、ByteTrack、ConvLSTM、VideoMAE、V-JEPA 圖文已製作並公開。
- [x] 18個故事、36張桌機／手機PNG；每課核心、反例、比較、自測與操作卡；來源與生成提示、修正紀錄、逐圖及整頁分項自評均落盤。
- [x] 48頁面狀態／144次圖片放大Escape、自測導覽、16閱讀狀態、72本機HTTP圖片hash、1292引用資產及HTML一致；聚焦pytest 7 tests+4 subtests及bundle 1 test通過。
- [x] ca7254653d5f025617fff1885132063328adf67a 已推送；Pages run34494424414成功；公開HTML與36PNG hash符合成品。首次部署前舊HTML檢查失敗保留為歷史，完成後重查通過。
- 範圍確認：僅八課改動，其他50課相同。全站legacy verifier既有ChArUco inline schema失敗仍存在，未算通過；原工程圖未納入這輪首讀評分。
- 啟用：selected-assets.json；實證：image-review.md、page-review.md、validation-summary.json、scope-verification.json、public-release-verification.json。公開入口 https://hctsaik.github.io/visionAI_Model_Introduce/#view=lesson&lesson=frame-difference&slide=1 。
- 使用者成品核准：pending。圖像為教學示意，無模型推論／現場效能或真人學習測試。下一步僅依使用者成品回饋開新修訂，保留本輪版本與證據。
'''
for p in [W/'PLAN.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md',R/'WORKITEMS.md',R/'TEACHING_REVIEW_LOG.md']:
 s=p.read_text(encoding='utf-8')
 if p.name=='PLAN.md':s=s.replace('- [ ] 學習回寫、保存副本、Git／公開版本核對。','- [x] 學習回寫、保存副本、Git／公開版本核對。')
 p.write_text(s+'\n'+msg,encoding='utf-8')
print('Completion and user-pending status recorded')
