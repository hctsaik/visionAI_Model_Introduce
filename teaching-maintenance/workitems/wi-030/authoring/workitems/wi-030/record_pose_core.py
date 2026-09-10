import json
from pathlib import Path
W=Path(__file__).resolve().parent;p=W/'selected-assets.json';s=json.loads(p.read_text(encoding='utf-8'))
s['pose-c1']={'desktop':'pose-c1-r03-desktop.png','mobile':'pose-c1-r04-mobile.png','desktop_reviewed':True,'mobile_reviewed':True,'user_review':'pending'}
p.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('''

## Pose核心最終候選
桌機r03與手機r04原生與936/328px實看：同四孔U形件2D/3D點名一致，2D與3D加K/畸變進PnP，R,t確由PnP輸出；桌機u右v下。重投影放大同D孔、兩中心距離線正確，工站另外接外參。刪未驗證數表，手機去製作指示語與參數→相機錯箭頭。桌[24,24,19,18,9]=94；手機[23,24,19,17,9]=92。必要幾何角色完整，手機R/t說明較小且像素/工作座標標註集中扣閱讀；沒有唯一姿態或現場成功的宣稱。完成度美感9（清楚薄框）、完整9（輸入/求解/回查）、專業9（方向/單位不虛構）、密度8（手機註字集中）、層級9（三區單結論）。無否決項；使用者核准pending。
''')
print('selected',len(s))
