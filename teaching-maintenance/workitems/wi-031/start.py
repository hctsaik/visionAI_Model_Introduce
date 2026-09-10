from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
s='''
## WI-031 當前工作：全部58課 Markdown 標準審查
使用者要求重新看58課，列哪些符合、哪些需重建。本輪審查、判斷與文件落盤，不改教材；WI-030製作已完成。唯一細項與接續入口：teaching-images/vision-ai-model-selection/workitems/wi-031/PLAN.md。預期產物為58課總表、逐課缺口與證據、重建優先順序；以五份Markdown及量表v1.0為準，首讀與進階範圍分開。正在盤點現行版本並準備實際桌機／手機檢查；尚未完成全站審查，不能沿用舊分數判通過。下一步保存基準及擷取頁面。使用者核准不由自評推定。
'''
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md',R/'TEACHING_REVIEW_LOG.md']:
 with p.open('a',encoding='utf-8') as f:f.write('\n'+s)
