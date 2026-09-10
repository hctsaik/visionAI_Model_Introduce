import json
from pathlib import Path
W=Path(__file__).resolve().parent
s=json.loads((W/'selected-assets.json').read_text(encoding='utf-8'))
rows=[
('efficient-c1','r06','r05',[24,23,19,17,9],[24,23,19,17,9],'完整正常三件、待測中缺右污，局部教師學生比較和全域AE/學生另一輸出，再校準融合回查。桌機刪掉兩個錯誤重複輸入後保留唯一待測盤；兩路區內留白不均扣閱讀。手機兩路上下排，必要比較與位置可讀；概念差異示意不代表實測模型必然出此圖。'),
('ad-d3','r04','r03',[23,23,19,19,9],[23,23,19,18,9],'共同正常板，代表子集、每位置橢圓分布、DINO區塊參考、教師鎖與學生AE工具符號四種保存知識方式具體不同。維護大字與同工作量品質成本結論；刪新增正常圖必然重訓過度說法。未呈現實测效能、不排名。手機四區上下可比較，教師/學生小標較密。'),
('segformer-c1','r02','r02',[24,23,19,19,9],[24,23,19,18,9],'同彎焊縫影像與人工遮罩，階層編碼器連四尺度特徵再融合；輸出紅區和來源框指出邊界需驗證，語意不編件ID。手機四尺度短字清楚，省略逐層運算以維持主線；輸出輪廓是示意非實測。'),
('seg-d2','r03','r03',[25,23,20,18,9],[24,23,20,18,9],'原圖放大與縮小模糊可見差異、遮罩斷裂紅框、完整取像/切圖及獨立人工標註比較形成回查路徑。移除第二黃底，唯一結論；第三區預測仍有斷裂，不保證改解析度就完美。手機上下三區可讀，標註和預測對照仍保有孔與縫位置。')
]
out=['\n## 2026-09-11 完成異常比較與分割反例審查']
for id,d,m,ds,ms,e in rows:
 s[id]={'desktop':f'{id}-{d}-desktop.png','mobile':f'{id}-{m}-mobile.png','desktop_reviewed':True,'mobile_reviewed':True,'user_review':'pending'}
 for mode,rev,score in [('desktop',d,ds),('mobile',m,ms)]:
  out.append(f'- {id}-{rev}-{mode}.png：原生與{936 if mode=="desktop" else 328}px實看，分項{score}={sum(score)}。{e} 五完成度：美感9（材質薄框）、完整9（輸入/差異/判讀俱在）、專業9（角色與示意界線）、密度8（局部資訊集中但主線可讀）、層級9（區題和單燈泡）。無否決項；使用者核准pending。')
(W/'selected-assets.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('\n'.join(out)+'\n')
print('selected',len(s))
