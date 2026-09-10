import json
from pathlib import Path
W=Path(__file__).resolve().parent;s=json.loads((W/'selected-assets.json').read_text(encoding='utf-8'))
rows=[
('class-d3','r05','r06',[23,24,19,18,9],[23,24,19,18,9],'同內六角分類工作，ResNet的x分岔卷積再相加、ConvNeXt同窗逐通道後混合、ViT帶位置互看再分類token均可追。手機r06補x→F(x)缺線，兩行順序保持；同資料比較錯誤延遲與維護，不憑新舊排名。抽象特徵只代表方法差異，沒有實際加速數字。'),
('pose-d2','r02','r02',[25,23,20,18,9],[25,23,20,18,9],'缺口可見→紙片遮住→兩個點名解與補視角/標記。候選左AB/DC、右CD/BA經180度旋轉核對，不是鏡射。手機同四孔幾何與大點名可讀，兩種補證據是替代選項。小誤差不保證身份正確；圖未虛構PnP數值。'),
('instance-d2','r02','r04',[25,23,20,18,9],[25,23,20,19,9],'原圖兩件、預測僅左件與人工橘框回查右件，孔洞保留；右件沒有被誤塗為另一模型輸出。手機r04刪雙重輸入/輸出標籤並恢復左孔空心。此例是有瑕疵候選，不聲稱左遮罩完美；下一步補重疊標註/視角並重驗。')
]
out=['\n## 2026-09-11 分類比較、點名歧義與漏件圖確認']
for id,d,m,ds,ms,e in rows:
 s[id]={'desktop':f'{id}-{d}-desktop.png','mobile':f'{id}-{m}-mobile.png','desktop_reviewed':True,'mobile_reviewed':True,'user_review':'pending'}
 for mode,rev,score in [('desktop',d,ds),('mobile',m,ms)]:
  out.append(f'- {id}-{rev}-{mode}.png：原生與{936 if mode=="desktop" else 328}px實看；分項{score}={sum(score)}。{e} 完成度：美感9（清楚材質）、完整9（可見差異與行動）、專業9（箭頭與身份核對）、密度8（內部短標籤仍集中）、層級9（三主區/單結論）。無否決項；使用者核准pending。')
(W/'selected-assets.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('\n'.join(out)+'\n')
print('selected',len(s))
