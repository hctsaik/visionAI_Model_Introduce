from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1]
s='''

## 收尾修正紀錄
- EfficientAD桌面r03在待測分支偷偷補回中件，r06刪重複輸入，只保留中缺右污完整托盤；原生/936核對後選用。
- Pose核心r02的v向上改r03向下；手機r03參數指向相機，r04改PnP直接輸出R,t，刪製作指示語。Pose比較r02中途L變U，r03統一四孔U件，保留足夠正確對應的責任。
- YOLO核心r02複製出不同原型；r03仍原型接係數；r04改單件A代表計算，但共享特徵錯接組合；r05兩支來源修正後P箭頭反向。即將r06只反轉此箭頭。手機r05流程正確但生成序號與Backbone當特徵標籤，r06去序號與改共享影像特徵。未看r06前不可打勾；YOLO課尚未整合。
- instance手機r03藍色填孔且兩種輸入輸出標籤混用，r04恢復空孔、改單一預測疊圖標籤。class比較手機r05漏x到F(x)，r06補支路且328核對通過。
目前20故事已選定、40張逐圖審查；11課來源已整合，但最後建置被新原生尺寸(1670,942)擋下，已加入具體尺寸與對應測試，待全輪最後一起重建。預期產物42PNG；本輪全頁QA、HTTP、Git／公开檢查尚未跑。
'''
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write(s)
for p in [W/'PLAN.md',C/'BEGINNER_VISUAL_STATUS.md']:
 with p.open('a',encoding='utf-8') as f:f.write('\nWI-030收尾：20故事40PNG已選，11課来源已整合，YOLO核心r06生成中；最後兩個新增精確尺寸已加validator和test，待最终重建。9 tests/10 subtests已通過（新增尺寸後需再跑tall）；全頁QA/HTTP/發布未完成。\n')
print('Checkpoints saved')
