from pathlib import Path
import json
W=Path(__file__).resolve().parent;C=W.parents[1]
copy={
'det-dino-detector':'類別固定且能準備框標註時，可比較 DINO；以現場漏檢、定位與完整成本決定是否採用。',
'det-yolo-dense':'固定類別逐件偵測可從 YOLO 起步；候選篩選後仍要量漏件、定位與完整延遲。',
'det-rtdetr':'需要端到端逐件偵測時可比較 RT-DETR；省去 NMS 不代表零重複或現場一定更快。',
'det-grounding-dino-interface':'類別詞彙常變時可試 Grounding DINO；文字提示交出候選框，仍需現場標註核對。',
'yolo-world':'需要變更候選詞彙時可試 YOLO-World；詞彙快取節省重複編碼，漏檢與更新成本仍需驗證。',
'yoloe':'需要文字或範例提示及遮罩時可試 YOLOE；提示方便不等於邊界精準或免除現場驗證。',
}
for id,text in copy.items():
 p=C/f'_course_content/topics/{id}.json';d=json.loads(p.read_text(encoding='utf8'));d['takeaway']=text;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Saved six detector selection takeaways.')
