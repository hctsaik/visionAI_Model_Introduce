import json
from pathlib import Path
W=Path(__file__).resolve().parent
s=json.loads((W/'selected-assets.json').read_text(encoding='utf-8'))
rows=[
('dino-c1','r03','r05',[23,23,19,19,9],[23,23,19,18,9],'同中央孔板，整圖進鎖定DINO後才有抽象token；參考與待測兩列差異、右下刮傷熱區和原圖覆核可追。桌機上下文線索較少；手機刪掉孔/平面照片冒充特徵後，整圖輸入清楚，配對為概念距離並非數值。'),
('convnext-c1','r02','r02',[23,24,18,18,9],[23,24,18,17,9],'同內六角候選，x分支同窗逐通道再1×1混合且殘差由x接加號；最右錯誤/耗時/記憶體明列同資料核對。手機核心短標籤可读，線路較密扣閱讀；效能只給測量工作不虛構提升。'),
('vit-c1','r02','r02',[23,24,18,18,9],[23,24,18,17,9],'同內六角影像來源框到帶位置token，互相參照後CLS接分類頭，三候選與注意力非真值結論清楚。手機來源框及位置token仍可分，旁註較小扣閱讀；不把注意力當定位證據。'),
('class-d2','r01','r03',[25,23,20,19,9],[24,23,20,18,9],'同十字螺絲只换背景即有內六角錯誤候選；兩類跨兩背景四格和獨立測試箱提供下一步。手機底部已留白、同工件身份保持；機制是可能背景捷徑，未冒稱實驗證明。'),
('seg-d3','r01','r01',[24,23,19,19,9],[24,23,19,18,9],'同兩墊圈位置與孔不變，語意同藍對照實例藍橘且各有完整輸入與特徵。替代方法沒有串接；標註差異與另行校正寫在结論。桌機編碼後模型盒較抽象，手機移除製作糾錯句，328px大遮罩差異清楚。')
]
out=['\n## 2026-09-11 新增逐圖自評（量表v1.0，原生及936/328px已實看）']
for id,d,m,ds,ms,e in rows:
 s[id]={'desktop':f'{id}-{d}-desktop.png','mobile':f'{id}-{m}-mobile.png','desktop_reviewed':True,'mobile_reviewed':True,'user_review':'pending'}
 for mode,rev,score in [('desktop',d,ds),('mobile',m,ms)]:
  out.append(f'- {id}-{rev}-{mode}.png：案例/意義/行動/閱讀/一致={score}，合計{sum(score)}。證據：{e} 五完成度：美感9（薄框材質清楚）、完整9（輸入處理輸出行動俱在）、專業9（概念與示意界線）、密度{8 if mode=="mobile" else 9}（{"短標籤有密集處但主線可讀" if mode=="mobile" else "三區對照"}）、層級9（大圖與唯一燈泡）。否決項無；頁面整合與使用者核准仍pending。')
(W/'selected-assets.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('\n'.join(out)+'\n')
print('selected',len(s))
