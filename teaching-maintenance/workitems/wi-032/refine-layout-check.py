from pathlib import Path
import shutil
W=Path(__file__).resolve().parent
shutil.copyfile(W/'svg-layout-check.json',W/'svg-layout-false-positive.json')
p=W/'check-svg.py';s=p.read_text(encoding='utf-8').replace('const c=card?.getBoundingClientRect();','const c=card && +card.getAttribute("width")>=500 && +card.getAttribute("height")>=500 ? card.getBoundingClientRect() : null;');p.write_text(s,encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n## 最後驗證補充\n64個啟用原生SVG檢查初報ChArUco核心2圖panel外溢；實圖正常。檢查器把第三節點內的小殘差框當成整節點背景，造成誤報。已保留svg-layout-false-positive.json，修正只辨認大型節點背景；畫布檢查仍對全部文字執行。不修改圖片，也不把該次failed寫成passed。390px來源鏈結初測另因測試工具以相對URL呼叫APIRequestContext失敗，已改用a.href絕對URL並重新通過18狀態。\n')
