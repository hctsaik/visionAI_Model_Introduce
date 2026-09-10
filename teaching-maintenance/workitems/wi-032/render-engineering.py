"""New precise engineering diagrams; no generated raster images are edited."""
import asyncio,sys,json,math,importlib.util
from pathlib import Path
from playwright.async_api import async_playwright
from render_charuco import text,rect,line,arrow,board,grid,N,B,O,G,L
W=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('native',W/'native-main.py');nm=importlib.util.module_from_spec(spec);spec.loader.exec_module(nm)
plate,pairs,chart=nm.plate,nm.pairs,nm.chart
ROWS=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
def circle(x,y,r=7,col=O):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}"/>'
def vec(x,y,col=B,n=8):return ''.join(rect(x+j*29,y,24,35,col if j%3 else '#BED8EF','white',0) for j in range(n))
def axis(x,y,camera=False):
 if camera:return arrow(x,y,x+85,y,B)+arrow(x,y,x,y+70,G)+arrow(x,y,x-60,y-50,O)+text(x+92,y+7,'X',24,B)+text(x-7,y+97,'Y',24,G)+text(x-82,y-52,'Z',24,O)
 return arrow(x,y,x+100,y,B)+arrow(x,y,x,y-100,G)+arrow(x,y,x-65,y+50,O)+text(x+107,y+7,'X',24,B)+text(x-7,y-114,'Y',24,G)+text(x-85,y+65,'Z',24,O)
def bolt(x,y,s=1):
 out=f'<g transform="translate({x},{y}) scale({s})">'+rect(45,70,60,150,'url(#steel)','#647484',7)
 for yy in range(80,218,12):out+=line(47,yy+9,103,yy,'#647484',3)
 out+='<path d="M20,20 L50,0 H100 L130,20 V70 L100,90 H50 L20,70 Z" fill="url(#steel)" stroke="#647484" stroke-width="3"/>'+line(20,20,65,45,'#647484',3)+line(130,20,85,45,'#647484',3)
 return out+'</g>'
def washer(x,y,s=1):return f'<g transform="translate({x},{y}) scale({s})"><circle cx="70" cy="70" r="62" fill="url(#steel)" stroke="#647484" stroke-width="3"/><circle cx="70" cy="70" r="27" fill="#F8FBFF" stroke="#647484" stroke-width="3"/></g>'
def objects(box=False):
 out=bolt(80,85,1.1)+washer(280,205,1)
 if box:out+=rect(95,70,145,270,'none',B,0)+rect(280,200,142,150,'none',G,0)+text(100,55,'螺栓',29,B)+text(290,185,'墊圈',29,G)
 return out
def node(x,y,label,col=B):return circle(x,y,19,col)+text(x,y+8,label,21,'white',700,'middle')
def graph(cross=False,prune=False):
 out='';ps=[(60,65),(155,155),(60,270),(325,65),(425,155),(325,270)]
 edges=[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5)] if not cross else [(0,3),(0,4),(1,4),(1,5),(2,3),(2,5)]
 for a,b in edges:
  if prune and (a%3==2 or b%3==2):continue
  x,y=ps[a];xx,yy=ps[b];out+=line(x,y,xx,yy,L,3)
 for i,(x,y) in enumerate(ps):out+=node(x,y,'ABC'[i%3], '#BAC6D3' if prune and i%3==2 else B)
 return out
def featuregrid(x,y,n=5,size=30):
 return ''.join(rect(x+i*size,y+j*size,size,size,['#E8F2FC','#A5CAED','#699FD4'][(i+2*j)%3],'white',0) for i in range(n) for j in range(n))
def plot(y,shift=0):
 out=line(25,y+90,455,y+90,N,2)
 for off,col in [(0,B),(shift,O)]:
  pts=[(30+x,y+85-70*math.exp(-((x-165-off)/43)**2)) for x in range(0,410,5)]
  out+='<polyline points="'+' '.join(f'{x:.1f},{yy:.1f}' for x,yy in pts)+'" stroke="'+col+'" stroke-width="4" fill="none"/>'
 return out
def graphic(k):
 if k=='board':return board(85,60,1)
 if k=='boardviews':return board(35,50,.55)+board(265,95,.55,-15,12)+board(120,245,.5,10,-10)
 if k=='marker':return board(55,50,1.05)+rect(62,57,55,55,'none',O,0)+text(30,375,'辨識標記 → 知道板上位置',28)
 if k=='corner':return rect(75,60,160,160,'white','#647484',0)+rect(235,60,160,160,'#293745','#647484',0)+rect(75,220,160,160,'#293745','#647484',0)+rect(235,220,160,160,'white','#647484',0)+circle(235,220,12)+text(250,260,'棋盤角點',28,O)
 if k=='pointtable':
  out=text(25,60,'角點ID    板上座標    影像座標',25)
  for i,k in enumerate('ABC'):out+=line(25,85+i*90,460,85+i*90,L,2)+text(40,138+i*90,k,34,O)+text(160,138+i*90,'X / Y / 0',27)+text(345,138+i*90,'u / v',27,B)
  return out+text(25,385,'每列是一個有身份的對應',28)
 if k in ['projection','boardpose']:
  return board(30,95,.57,0,-8)+arrow(220,180,290,180)+rect(310,85,150,210,'#F2F7FC')+circle(385,188,11)+text(330,325,'影像點',27,B)+text(45,350,'板上點',27,O)
 if k=='pose':return board(90,40,.73)+axis(95,185)+arrow(240,245,345,245)+axis(355,245,True)+text(40,400,'物體座標 → 相機座標',29)
 if k=='boardresidual':
  out=board(75,30,1)
  for x,y in [(125,80),(275,80),(125,230),(275,230)]:out+=circle(x,y,7)+f'<circle cx="{x+13}" cy="{y-8}" r="10" fill="none" stroke="{B}" stroke-width="4"/>'+line(x,y,x+13,y-8,O,2)
  return out+text(25,338,'● 觀測棋盤角點',29,O)+text(25,383,'○ 重投影位置',29,B)
 if k in ['residual','landmarks']:
  out=plate(70,25,1)
  for x,y in [(270,90),(150,195),(300,195)]:out+=f'<circle cx="{x+13}" cy="{y-8}" r="10" fill="none" stroke="{B}" stroke-width="4"/>'+line(x,y,x+13,y-8,O,2)
  return out+text(25,338,'● 觀測位置',29,O)+text(25,383,'○ 預測／對齊後位置',29,B)
 if k=='camera':return rect(65,110,290,190,'#CFD8E0','#64788B',15)+rect(115,65,150,45,'#CFD8E0','#64788B',4)+circle(260,205,80,'#5C7185')+circle(260,205,55,'#294B6C')+circle(250,188,22,'#90B9DD')+text(45,373,'取像條件也是版本的一部分',28)
 if k=='gridpair':return grid(35,50,190,250,True)+arrow(235,175,280,175)+grid(295,50,155,250,False)+text(35,370,'模型必須解釋新的像素位置',27)
 if k=='ruler':
  out=plate(65,35,.85)+rect(40,300,400,70,'#F0F4F8','#64788B',2)
  for i in range(20):out+=line(50+i*19,300,50+i*19,330+(12 if i%5==0 else 0),'#64788B',2)
  return out+text(60,405,'獨立尺寸基準',30)
 if k=='imagepair':return plate(50,25,.6)+plate(270,170,.6,12)+text(45,220,'模板',30,B)+text(290,380,'待對圖',30,O)
 if k=='curves':return plot(35,45)+text(25,180,'錯位時',28)+plot(230,5)+text(25,380,'接近時（機制示意）',28)
 if k=='warp':return text(80,105,'[ a  b  tx ]',45,B)+text(80,170,'[ c  d  ty ]',45,B)+text(60,252,'仿射warp例',30)+line(25,290,460,290,L,2)+text(45,350,'相關值  ≠  幾何殘差',30,O)
 if k=='sample':
  out=''
  for x,y,v in [(35,45,40),(130,45,80),(35,140,120),(130,140,160)]:out+=rect(x,y,95,95,f'rgb({v},{v},{v})','white',0)+text(x+47,y+56,str(v),27,'white' if v<130 else N,700,'middle')
  return out+circle(130,140,8,O)+arrow(237,140,310,140)+rect(330,100,100,100,'rgb(100,100,100)','white',0)+text(380,159,'100',32,'white',700,'middle')+text(25,305,'四鄰像素中心：平均為100',28)+text(25,367,'此例示意雙線性插值取樣',28)
 if k=='iterate':return nm.overlay(55,25,20)+arrow(270,160,330,210)+nm.overlay(155,210,3)+text(25,410,'下一輪再取樣／比較',28)
 if k=='axes':return arrow(85,80,205,80,B)+arrow(85,80,85,215,G)+arrow(335,185,455,185,B)+arrow(335,185,335,315,G)+text(210,87,'x',28,B)+text(75,249,'y',28,G)+text(459,193,'x',28,B)+text(325,349,'y',28,G)+text(30,300,'模板 T',29,B)+text(265,405,'待對圖 I',29,O)
 if k=='map':return featuregrid(35,65,4,34)+arrow(195,130,275,205)+featuregrid(300,160,4,34)+circle(103,133,9,O)+circle(368,228,9,O)+text(45,365,'xT ── W ──→ xI',38)
 if k=='occlusion':return plate(55,45,.95,occluded=True)+text(40,335,'可用共同區域變少',30)+text(40,385,'先核對起點與mask',28)
 if k=='evidence':
  out=rect(55,25,350,365,'white')
  for i,t in enumerate(['原圖／模板','初始與最終warp','取樣與停止設定','獨立地標殘差']):out+=circle(88,80+i*85,6,B)+text(112,90+i*85,t,28)
  return out
 if k=='scale':return plate(20,20,.8)+plate(170,210,.5)+plate(325,315,.3)+text(265,105,'尺度空間',28)
 if k=='orientation':return plate(65,45,.95)+circle(255,107,44,'none')+arrow(255,107,310,70,O)+rect(200,45,110,120,'none',O,0)+text(40,360,'以點的尺度與方向定義視窗',27)
 if k in ['descriptor','descriptor128']:return chart(70,150,[30,80,65,22,60,38,15,75])+arrow(220,190,220,240)+vec(55,275)+text(45,375,'局部梯度的數值表示',29)
 if k=='histgrid':
  out=''
  for i in range(4):
   for j in range(4):
    out+=rect(80+i*72,25+j*72,72,72,'white',L,0)
    for a in range(8):
     angle=a*math.pi/4;cx=116+i*72;cy=61+j*72;out+=line(cx,cy,cx+24*math.cos(angle),cy+24*math.sin(angle),O if a==(i+j)%8 else '#9DB5CE',3)
  return out+text(70,365,'4×4 空間格；每格8方向',28)
 if k=='ratio':return vec(50,30)+text(30,120,'最近候選 d1',30,B)+line(50,155,175,155,B,15)+text(30,220,'次近候選 d2',30,O)+line(50,255,315,255,O,15)+text(30,355,'比較 d1 / d2（距離示意）',29)
 if k=='homography':
  a=[(45,45),(185,45),(185,275),(45,275)];b=[(280,100),(440,65),(425,330),(285,285)]
  out='<polygon points="'+' '.join(f'{x},{y}' for x,y in a)+'" fill="#EDF5FC" stroke="'+B+'" stroke-width="3"/><polygon points="'+' '.join(f'{x},{y}' for x,y in b)+'" fill="#EDF5FC" stroke="'+B+'" stroke-width="3"/>'
  for (x,y),(xx,yy) in zip(a,b):out+=circle(x,y)+circle(xx,yy)+line(x,y,xx,yy,L,2)
  out+=line(110,160,360,310,O,3,'8 6')+text(145,225,'？',35,O)
  return out+text(30,395,'估計H；另查候選外點',29)
 if k=='spread':
  out=rect(40,30,170,280,'white')+rect(290,75,170,280,'white')
  for x,y in [(65,65),(175,65),(65,270),(175,270)]:out+=circle(x,y)+circle(x+250,y+45)+line(x,y,x+250,y+45,L,2)
  return out+text(40,400,'四組分散且正確的對應示意',27)
 if k=='pairs':return pairs(75,80)+text(25,350,'只列代表點對；未求幾何',28)
 if k=='parallax':return grid(230,40,215,230)+plate(35,140,.72)+arrow(65,110,185,110,B)+arrow(295,325,350,325,O)+text(50,75,'近：工件',27,B)+text(260,385,'遠：背景',27,O)
 if k=='planes':return plate(30,10,.54)+arrow(230,110,300,110,B)+text(330,122,'H1',40,B)+grid(35,245,175,130)+arrow(230,305,300,305,O)+text(330,320,'H2',40,O)+text(30,420,'不同平面分別建立幾何',28)
 if k=='features':return plate(30,10,.62)+plate(275,75,.55,-8)+vec(25,285,n=6)+vec(270,330,n=6)+text(40,405,'兩圖各自的點與描述',28)
 if k in ['attention','crossattention']:return graph(True)+text(30,350,'跨圖候選關係',29)
 if k=='selfattention':return graph()+text(30,350,'同圖點彼此交換資訊',29)
 if k=='assignment':return pairs(75,65,True,True)+text(35,330,'可保留未匹配點',31,O)+text(35,385,'不是所有點都要硬配對',28)
 if k=='depth':
  out=''
  for i in range(4):out+=rect(65,25+i*85,170,60,'#E8F2FC')+text(95,65+i*85,f'Layer {i+1}',29)
  return out+arrow(250,140,350,140,G)+text(310,195,'可早停',27,G)+line(150,170,150,310,L,3,'7 7')
 if k=='prune':return graph(True,True)+text(40,350,'灰點：停止參與後續計算',27)+text(40,400,'原影像不會被刪除',28)
 if k=='runtime':
  return rect(50,85,120,90,'#A9C9E9')+rect(170,85,180,90,'#B9DACF')+rect(350,85,100,90,'#E4D2B7')+text(35,225,'前處理 → 模型 → 幾何／後處理',26)+text(55,305,'同硬體、同輸入',30)+text(55,370,'沒有借用跨平臺FPS',28)
 if k=='overlap':return rect(35,50,265,265,'#EDF5FC')+rect(245,105,230,260,'none',O,0)+rect(245,105,55,210,'#BCD5EC','none',0)+text(35,405,'共有可見區域才有對應',29)
 if k=='repeated':
  out=rect(35,55,420,250,'#CFD9E2')
  for x in [105,245,385]:out+=f'<circle cx="{x}" cy="180" r="38" fill="#F8FBFF" stroke="#647484" stroke-width="3"/>'
  return out+text(35,380,'很像的局部，未必同一身份',28)
 if k=='objects':return objects(True)
 if k=='boxes':return objects(True)+text(45,405,'框／類別／分數；不是mask',27)
 if k=='proposal':
  out=featuregrid(25,30,6,32)+bolt(95,75,.52)+rect(102,65,92,145,'none',O,0)+rect(30,32,52,70,'none','#98A9BA',0)+rect(155,225,50,70,'none','#98A9BA',0)
  return out+arrow(245,145,310,145,O)+rect(330,100,110,170,'none',O,0)+text(25,375,'影像候選 → 查詢位置',29)
 if k in ['queries','boxrefine']:
  out=bolt(160,80,.95)+rect(125,65,140,265,'none',O,0)+rect(165,78,130,225,'none',B,0)+rect(179,80,104,209,'none',G,0)
  return out+text(30,365,'橘：初始 → 藍：更新',28)+text(30,410,'綠：輸出框（非真值）',28,G)
 if k=='querycontent':return rect(35,45,190,180,'none',O,0)+text(55,275,'位置初始化',29,O)+vec(245,100,n=7)+text(260,275,'可學內容',29,B)+text(40,390,'兩部分共同形成查詢',29)
 if k in ['noisy','positive','negative']:
  out=bolt(95,60,1)+rect(103,50,125,255,'none',G,0)
  if k!='negative':out+=rect(117,70,126,258,'none',B,0)
  if k!='positive':out+=rect(310,235,110,145,'none',O,0)+text(285,405,'無物件目標',27,O)
  else:out+=arrow(270,195,410,195,G)+text(280,270,'還原GT',28,G)
  return out
 if k=='classes':return objects(True)+text(35,400,'既有類別由訓練定義',29)
 if k=='newclass':return objects()+rect(275,55,160,110,'#D4DEE7','#647484',5)+text(290,115,'新零件？',30,O)+text(40,385,'新增名稱 ≠ 已學會新類別',28)
 if k in ['vocabulary','cache']:return text(45,70,'螺栓',35,B)+vec(155,42)+text(45,160,'墊圈',35,G)+vec(155,132,G)+arrow(250,225,250,290)+rect(100,315,300,65,'#E4EDF7')+text(130,360,'詞彙表示／快取',28)
 if k in ['regiontext','similarity']:
  out=text(155,45,'螺栓詞',27,B)+text(325,45,'墊圈詞',27,G)+bolt(20,70,.48)+washer(15,230,.55)
  for i in range(2):
   for j in range(2):out+=rect(155+150*j,75+130*i,125,108,B if i==j else '#E4EFF9','white',0)
  return out+text(25,360,'每列：影像區域表示',28)+text(25,410,'深色：較相似（教學示意）',28)
 if k=='pyramid':return featuregrid(35,25,6,35)+featuregrid(220,165,4,32)+featuregrid(355,300,3,27)+text(25,405,'多尺度特徵，不是分割真值',27)
 if k=='fusion':
  out=text(25,38,'影像特徵',27,B)+featuregrid(25,65,4,29)+text(255,38,'詞彙表示',27,G)+vec(245,65,G,n=7)
  out+=arrow(150,225,220,270,B)+line(350,110,455,110,G,4)+line(455,110,455,245,G,4)+arrow(455,245,290,270,G)
  for i in range(3):
   for j in range(3):out+=rect(180+39*i,270+39*j,39,39,'#377EBA' if i==j else '#E4EFF9','white',0)
  return out+text(25,207,'文字相似 → max＋sigmoid權重',25)+text(25,420,'依權重調整影像特徵（示意）',27)
 if k=='reparameterize':
  out=text(25,30,'例：詞彙整合到分類頭',28)+vec(170,58,B,n=5)+vec(170,107,G,n=5)+arrow(240,155,240,215,G)
  out+=text(150,253,'1×1 分類頭參數',27)+rect(165,270,165,95,'#ECF5F3',G,5)
  out+=vec(178,280,B,n=5)+vec(178,324,G,n=5)
  out+=featuregrid(25,290,2,23)+arrow(80,313,150,313)+arrow(342,313,392,313)
  out+=rect(403,285,65,22,B,'none',0)+rect(403,332,35,22,G,'none',0)
  return out+text(20,412,'影像特徵',26)+text(175,412,'結構示意',26)+text(380,412,'分數',26)
 if k=='refresh':return text(55,70,'舊詞彙',34)+line(40,50,220,80,O,4)+text(270,70,'新詞彙',34,B)+arrow(290,125,290,200)+vec(170,225,G)+text(55,345,'更新表示／部署產物',30)+text(55,400,'再用獨立資料核對',28)
 if k=='smallobject':
  out=bolt(45,30,.38)+arrow(135,100,220,140)+rect(245,70,195,270,'#EDF2F6')
  for j in range(14):
   for i in range(9):
    ink=(j<4 and 1+(j in [0,3])<=i<=7-(j in [0,3])) or (j>=4 and 3<=i<=5)
    if ink:out+=rect(257+i*19,83+j*17,19,17,'#899AAA' if j%2 else '#B2BDC8','none',0)
  return out+text(40,400,'低解析示意；細節需原始取像',27)
 if k=='inspection':return bolt(130,30,1.1)+rect(155,25,105,80,'none',O,0)+arrow(280,120,400,240)+text(30,350,'物件候選 → 專用檢查',29)+text(30,405,'依工作需要準備真值',28)
 raise ValueError(k)
def make(r,mobile):
 w,h=(768,2770) if mobile else (1672,941)
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}"><defs><linearGradient id="steel"><stop offset="0" stop-color="#B4C0CC"/><stop offset=".45" stop-color="#EDF1F4"/><stop offset="1" stop-color="#8495A5"/></linearGradient></defs><style>text{{font-family:"Microsoft JhengHei",sans-serif}}</style>'+rect(0,0,w,h,'white','none',0)
 title=r['title'];cut=title.find('：')+1 if '：' in title else 15
 parts=[title[:cut],title[cut:]] if mobile and len(title)>17 else [title]
 for j,t in enumerate(parts):s+=text(30,58+j*53,t,40 if mobile else 47,N,800)
 s+=text(30,150 if mobile else 117,'工程圖解｜機制示意，非本輪模型實測',25,'#5D7184')
 for i,p in enumerate(r['panels']):
  x,y,z=(24,180+i*800,1.4) if mobile else (24+i*557,150,1)
  s+=f'<g transform="translate({x},{y}) scale({z})">'+rect(0,0,510,560,'#F8FBFF',L,18)+text(22,47,p['title'],29,N,800)
  s+='<g transform="translate(10,68) scale(.94 .90)">'+graphic(p['graphic'])+'</g>'
  for j,t in enumerate(p['lines']):s+=text(24,492+j*42,t,27,N,650)
  s+='</g>'
  if not mobile and i<2 and r['kind']=='C' and r['id']!='det-dino-detector-engineering-3':s+=arrow(x+517,y+280,x+549,y+280)
 take=r['takeaway'];by=2600 if mobile else 805
 s+=rect(24,by,w-48,140 if mobile else 110,'#FFF4CC','#E9B54A',18)
 if mobile and len(take)>19:
  cut=min(19,len(take)//2+2);parts=[take[:cut],take[cut:]]
 else:parts=[take]
 for j,t in enumerate(parts):s+=text(45,by+50+j*48,t,31 if mobile else 34,N,800)
 return s+'</svg>',w,h
async def main():
 rows=[r for r in ROWS if not sys.argv[1:] or r['id'] in sys.argv[1:]]
 async with async_playwright() as p:
  b=await p.chromium.launch(channel='msedge',headless=True)
  for r in rows:
   for mode in ['desktop','mobile']:
    svg,w,h=make(r,mode=='mobile');f=W/(r['id']+'-r07-'+mode+'.svg');f.write_text(svg,encoding='utf-8')
    pg=await b.new_page(viewport={'width':w,'height':h},device_scale_factor=1);await pg.goto(f.as_uri());await pg.screenshot(path=str(f.with_suffix('.png')));await pg.close()
  await b.close()
 print('Rendered',len(rows)*2,'engineering PNG candidates; actual review pending')
if __name__=='__main__':asyncio.run(main())
