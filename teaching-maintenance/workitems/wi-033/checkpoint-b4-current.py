from pathlib import Path
import runpy
W=Path(__file__).resolve().parent
note='''### WI-033 第四批選定桌機已審、手機逐張複核中

選定24張擴展桌機（含8張修訂）已原生實看；YOLO、RT-DETR六張手機及Grounding工程1/3手機已實看，另16張手機待看。八原型16PNG已審；兩同件主反例4PNG已審並由promote-batch4-failures.py接入來源，未建置。下一步剩餘手機、48張擴展assessment、整合八課工程、建置與32狀態/頁內審查/HTTP及測試。產物workitems/wi-033；完成仍17/52，使用者核准pending。前述PNG缺畫判斷已撤回，以render-diagnostic-result.json為準。繼續全部52課授權。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8')
runpy.run_path(str(W/'append-checkpoint.py'))
