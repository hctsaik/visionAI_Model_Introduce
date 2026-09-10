import json
from pathlib import Path
W=Path(__file__).resolve().parent;s=json.loads((W/'selected-assets.json').read_text(encoding='utf-8'))
rows=[('yoloseg-c1','r07','r06',[24,24,19,18,9],[24,24,19,18,9],'同兩墊圈輸入、各件空心標註與藍橘結果；完整圖編碼出共享特徵，兩支各到原型P與A係數，再加權成A遮罩，B同法。桌機改側邊進P，移除反向箭頭；手機去序號與Backbone誤標後上下清楚。未展開框裁切細節，方法不滿分；以YOLOv8-seg為例，不涵蓋所有版本。')]
out=['\n## YOLO核心最終審查']
for id,d,m,ds,ms,e in rows:
 s[id]={'desktop':f'{id}-{d}-desktop.png','mobile':f'{id}-{m}-mobile.png','desktop_reviewed':True,'mobile_reviewed':True,'user_review':'pending'}
 for mode,rev,score in [('desktop',d,ds),('mobile',m,ms)]:
  out.append(f'- {id}-{rev}-{mode}.png：原生與{936 if mode=="desktop" else 328}px已實看；分項{score}={sum(score)}。{e} 完成度：美感9（薄框材質）、完整9（輸入/生成/回查）、專業9（分支來源成立）、密度8（內部必要短標集中）、層級9（三主區與單結論）。無否決項，使用者核准pending。')
(W/'selected-assets.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('\n'.join(out)+'\n')
print('selected',len(s))
