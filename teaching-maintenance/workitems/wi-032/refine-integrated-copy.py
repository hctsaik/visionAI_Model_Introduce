import json
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1]
for slug in json.loads((W/'lesson-content.json').read_text(encoding='utf-8')):
 p=C/'_course_content/topics'/f'{slug}.json';t=json.loads(p.read_text(encoding='utf-8'))
 t['beginner_path']['visuals'][0]['callouts']=t['beginner_path']['visuals'][0]['callouts'][:3]
 p.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=W/'integrate-main.py';s=p.read_text(encoding='utf-8').replace("a['ideas']+[['交付與接手',a['output']]]","a['ideas']");p.write_text(s,encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:
 f.write('\n## 實頁檢查checkpoint\ncourse與docs已建置；ChArUco/ECC/SIFT各4個桌機／手機URL狀態及28個放大檢查通過，其餘3課檢查中。12個focused tests與14 subtests通過。實看手機圖片後發現截圖被sticky導覽列覆蓋，這是長圖元素截圖的固定介面混入，將另存不含導覽列的圖框證據；正常頁面與互動截圖保留。展開舊技術契約有SIFT warp等舊用語，正在改為新版教學來源供給交付與家族摘要；修正後重建及核對。主線三要點移除第四個交付列（交付仍在操作卡）。未完成項目：全部圖文人工評分、更新後頁面與資產驗證、回歸及學習收尾。\n')
