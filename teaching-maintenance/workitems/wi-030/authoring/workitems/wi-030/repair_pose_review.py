from pathlib import Path
W=Path(__file__).resolve().parent
p=W/'prototype-review.md';s=p.read_text(encoding='utf-8');s=s.split('## Pose????')[0]
s+='''## Pose責任比較r03確認
桌機與手機原生及936/328px均實看：同四孔U件A左上B左下C右下D右上不變，影像2D、CAD3D、K畸變三資料進PnP，輸出物體→相機且工站另需外參。第一區可獨立2D覆核，非模型排名。桌機分項[24,24,19,18,9]=94；手機[24,23,19,18,9]=93（訓練字樣省略但找點角色與幾何資料清楚，中區三資料短標較密）。完成度美感9（薄框材質）、完整9（同物件全鏈）、專業9（方向和輸入核對）、密度8（局部三資料並排）、層級9（三區選擇）。無否決項，使用者核准pending。
'''
p.write_text(s,encoding='utf-8')
print('Repaired UTF-8 review record')
