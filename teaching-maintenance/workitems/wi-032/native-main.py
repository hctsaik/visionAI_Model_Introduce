"""New vector teaching diagrams; no editing of generated raster images."""
from pathlib import Path
import asyncio,sys,json,math,subprocess
from render_charuco import text,rect,line,arrow,board,grid,N,B,O,G,L
from playwright.async_api import async_playwright
W=Path(__file__).resolve().parent; C=W.parents[1]
P={r['id']:r for r in json.loads((W/'visual-plan.json').read_text(encoding='utf-8'))}
POINTS={'A':(200,65),'B':(80,170),'C':(230,170)}
def plate(x,y,s=1,rot=0,points=True,color='#C8D1DA',occluded=False):
 out=f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">'
 out+='<path d="M0,0 H200 V65 H310 V245 H0 Z" fill="'+color+'" stroke="#64788B" stroke-width="3"/>'
 for xx in [80,230]:out+=f'<circle cx="{xx}" cy="170" r="31" fill="#F8FBFF" stroke="#64788B" stroke-width="4"/>'
 if points:
  for k,(xx,yy) in POINTS.items():
   out+=f'<circle cx="{xx}" cy="{yy}" r="7" fill="{O}" stroke="white" stroke-width="2"/>'+text(xx+10,yy-10,k,24,O,800)
 if occluded:out+=rect(150,-15,175,115,'#364757','#364757',3)
 return out+'</g>'
def lines(x,y,items,color=N,size=28):
 return ''.join(text(x,y+40*i,v,size,color,600) for i,v in enumerate(items))
def chart(x,y,vals,col=B):
 return ''.join(rect(x+i*28,y-v,19,v,col,'none',0) for i,v in enumerate(vals))+line(x-5,y,x+28*len(vals),y,N,2)
def pairs(x,y,ambiguous=False,unknown=False):
 out=''
 for i,k in enumerate('ABC'):
  yy=y+i*70
  out+=text(x,yy,k,32,O,800)+text(x+290,yy,k,32,O,800)
  if not (unknown and i==0):out+=line(x+35,yy-10,x+278,yy-10,O if unknown else G,3 if unknown else 5,'8 7' if unknown else '')
 if ambiguous:out+=line(x+35,y+60,x+278,y+130,O,3,'8 7')+line(x+35,y+130,x+278,y+60,O,3,'8 7')
 return out
def overlay(x,y,dx=0):
 out=plate(x,y,.72,points=False,color='#F0F5FA')
 # Every moving edge and hole uses one translation, including the raised shoulder.
 out+=f'<g transform="translate({x+dx},{y}) scale(.72)" fill="none" stroke="{O}" stroke-width="4" stroke-dasharray="8 6"><path d="M0,0 H200 V65 H310 V245 H0 Z"/>'
 for xx in [80,230]:out+=f'<circle cx="{xx}" cy="170" r="31"/>'
 return out+'</g>'
def panel(id,i):
 # All panels use a 510 x 640 local coordinate system; mobile stacks without cropping.
 s=''
 if id=='charuco-failure':
  if i==0:s=board(95,100,1)+lines(25,440,['同一塊已知標靶','相同鏡頭與影像尺寸','改變的是採樣位置／傾角'])
  if i==1:
   for j,wide in enumerate([False,True]):
    yy=125+j*225;s+=text(25,yy-15,['只集中中心','位置與傾角都涵蓋'][j],30)+rect(25,yy,455,165,'white')
    pts=[(175,70),(185,75),(210,55),(235,90),(210,100)] if not wide else [(50,25),(310,28),(195,75),(60,100),(330,105)]
    for n,(x,y) in enumerate(pts):s+=board(25+x,yy+y,.16,0,(n-2)*8)
   s+=lines(25,574,['張數一樣，也可能覆蓋不同'],size=27)
  if i==2:
   s=rect(25,100,455,250,'white')+board(330,215,.4,0,-12)
   s+=line(325,250,235,400,O,3)+rect(45,380,395,110,'white')
   s+='<circle cx="140" cy="425" r="12" fill="'+O+'"/><circle cx="174" cy="440" r="14" fill="none" stroke="'+B+'" stroke-width="4"/>'
   s+=text(220,420,'● 觀測',29,O)+text(220,461,'○ 重投影',29,B)
   s+=lines(25,539,['用未參與估計的邊角視角','查偏差；不足就補拍'],size=28)
 elif id=='ecc-failure':
  if i==0:s=plate(95,140,1)+lines(25,460,['同一平面兩孔件','藍灰：模板','橘虛線：重採樣待對圖'])
  if i==1:
   s=text(25,95,'近起點：同身份孔靠近',29)+overlay(75,115,12)+text(25,343,'錯解示意：移動一個孔距',29,O)+overlay(45,370,108)
  if i==2:
   s=text(25,110,'左孔錯對右孔',33,O,800)+overlay(45,160,108)
   s+=lines(25,404,['一個孔局部重合，','整件外框卻沒有對齊。','先粗定位，再微調；','最後查獨立地標殘差。'])
 elif id=='sift-core':
  if i==0:s=plate(75,100,.85)+plate(160,400,.55,-18)+lines(25,575,['同一缺口A，換尺度與方向'],size=27)
  if i==1:
   s=rect(70,100,210,180,'white')+'<path d="M100,135 H200 V205 H270" stroke="#64788B" stroke-width="9" fill="none"/>'
   for x,y,xx,yy in [(150,140,150,190),(200,160,245,160),(225,200,225,250)]:s+=arrow(x,y,xx,yy,O)
   s+=text(25,325,'相對主方向，彙整局部梯度',28)
   s+=chart(95,455,[28,68,90,38,18,54,78,26])+arrow(250,480,250,520)
   for j in range(12):s+=rect(70+j*30,530,25,36,['#B6D5F5','#468DCF','#D4E6F7'][j%3],'none',0)
   s+=text(25,615,'方向分布 → 描述子（示意）',28)
  if i==2:s=pairs(90,150)+lines(25,410,['比較描述，再篩含糊候選','這裡只列代表點對。','幾何估計與驗證另做；','描述子本身不是warp。'])
 elif id=='sift-failure':
  if i==0:s=plate(80,120,1)+lines(25,460,['同一缺口A、同一取景','只改變模糊程度'])
  if i==1:
   for j,blur in enumerate([False,True]):
    yy=125+j*230;s+=text(25,yy-15,['清楚：局部方向明顯','模糊：方向線索可能變弱'][j],28)
    s+=f'<g'+(' filter="url(#blur)"' if blur else '')+'>'+plate(40,yy,.47)+'</g>'
    s+=f'<g opacity="{.22 if blur else 1}">'+arrow(245,yy+40,310,yy+40,O)+arrow(335,yy+40,335,yy+115,O)+arrow(370,yy+125,435,yy+125,O)+'</g>'
   s+=lines(25,585,['描述相近，候選更難分辨'],size=28)
  if i==2:s=pairs(90,140,True)+lines(25,410,['別只降門檻收更多線。','先改善取像與定位線索，','再查正確對應及幾何分布。'])
 elif id=='lightglue-core':
  if i==0:s=plate(75,100,.85)+plate(155,400,.55,-18)+lines(25,570,['相容extractor先交出點／描述'],size=27)
  if i==1:
   s=pairs(90,130,True)+text(25,395,'同圖與跨圖資訊更新表示',29)+arrow(250,420,250,455)
   s+=text(25,508,'A的上下文，幫助分辨B/C',28)+text(25,562,'虛線是候選，不是刪掉孔位',27,O)
  if i==2:s=pairs(90,150)+lines(25,409,['交付點對與信心','必要時修剪／提早停止','幾何求解仍需另接','不直接交付對齊影像'])
 elif id=='lightglue-failure':
  if i==0:s=plate(95,120,1)+lines(25,460,['A：獨特缺口','B/C：外觀相似的兩孔'])
  if i==1:
   s=text(25,100,'缺口可見',30)+plate(70,130,.65)+text(25,350,'只遮住缺口；孔仍原位',29,O)+plate(70,380,.65,occluded=True)
  if i==2:
   s=text(25,115,'A無法觀測；B/C可能含糊',29,O)+pairs(85,205,True,True)
   # The unavailable A is visibly crossed out rather than presented as a match.
   s+=line(80,175,410,220,O,7)
   s+=lines(25,469,['保留不確定，另拍一個視角','或增加已知定位線索','再做配對與幾何核對。'],size=27)
 elif id=='geometry-compare':
  if i==0:s=board(85,110,1)+arrow(250,405,250,440)+grid(80,470,320,100,False)+text(25,613,'已知板上點 → 內參與畸變',28)
  if i==1:
   s=text(25,115,'SIFT：局部梯度描述',30)+chart(55,230,[25,80,50,20,60])+arrow(220,200,280,200)
   s+=lines(300,191,['描述','比對'],size=28)
   s+=text(25,335,'LightGlue：上下文更新配對',27)+pairs(90,400,True)
   s+=text(25,615,'都交付點對；幾何另接',28)
  if i==2:
   s=text(25,95,'ECC：合理起點後微調',29)+overlay(50,125,12)
   s+=lines(25,393,['先建立適用相機幾何；','需要定位時另找影像對應；','外觀接近時可再微調。','各步驟都要獨立驗證。'],size=28)
 return s
IDS=['charuco-failure','ecc-failure','sift-core','sift-failure','lightglue-core','lightglue-failure','geometry-compare']
def make(id,mobile):
 r=P[id];w,h=(768,3050) if mobile else (1672,941)
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}"><defs><filter id="blur"><feGaussianBlur stdDeviation="9"/></filter></defs><style>text{{font-family:"Microsoft JhengHei",sans-serif}}</style>'+rect(0,0,w,h,'white','none',0)
 title=r['title'];cut=title.find('，') if '，' in title and title.find('，')<18 else 15
 parts=[title[:cut].rstrip('，'),title[cut:].lstrip('，')] if mobile and len(title)>16 else [title]
 for i,t in enumerate(parts):s+=text(30,60+i*53,t,42 if mobile else 48,N,800)
 s+=text(30,150 if mobile else 117,'受控幾何教學示意｜非模型實測',27,'#5D7184')
 for i,node in enumerate(r['nodes']):
  x,y,scale=(24,180+i*890,1.4) if mobile else (24+i*557,150,1)
  if id=='lightglue-core' and i==1:node='上下文分辨候選'
  if id=='geometry-compare':node=['ChArUco：建立相機幾何','SIFT／LightGlue：影像對應','ECC：微調與獨立核對'][i]
  s+=f'<g transform="translate({x},{y}) scale({scale})">'+rect(0,0,510,630,'#F8FBFF',L,18)+text(23,50,node,29,N,800)+panel(id,i)+'</g>'
  if not mobile and i<2:s+=arrow(x+517,y+320,x+549,y+320)
 by=2870 if mobile else 826
 s+=rect(24,by,w-48,140 if mobile else 90,'#FFF4CC','#E9B54A',16)
 take=r['takeaway'];cut=len(take)//2
 parts=[take[:cut],take[cut:]] if mobile and len(take)>21 else [take]
 for i,t in enumerate(parts):s+=text(48,by+50+47*i,t,31 if mobile else 33,N,800)
 return s+'</svg>',w,h
async def main():
 ids=sys.argv[1:] or IDS
 for id in ids:
  p=W/f'{id}-native-r05.md'
  p.write_text((W/f'{id}-r01.md').read_text(encoding='utf-8')+'\n## 精確原生幾何版本r03\nNew SVG→browser PNG, not editing existing raster. 同物件與A/B/C位置使用單一定義；ECC整件平移一致。桌機1672×941，手機768×3050直向。原生／頁內尚待審查，user approval pending。圖內描述子與候選連線為機制示意，非執行結果。\n',encoding='utf-8')
  v=subprocess.run([sys.executable,'-X','utf8',str(C/'tools/validate_teaching_preflight.py'),str(p)],capture_output=True,text=True,encoding='utf-8');assert v.returncode==0,v.stdout+v.stderr
 async with async_playwright() as p:
  b=await p.chromium.launch(channel='msedge',headless=True)
  for id in ids:
   for mode in ['desktop','mobile']:
    svg,w,h=make(id,mode=='mobile');path=W/f'{id}-native-r05-{mode}.svg';path.write_text(svg,encoding='utf-8')
    page=await b.new_page(viewport={'width':w,'height':h},device_scale_factor=1);await page.goto(path.as_uri());await page.screenshot(path=str(path.with_suffix('.png')));await page.close()
  await b.close()
 print('Rendered',len(ids)*2,'new PNG candidates, review pending')
if __name__=='__main__':asyncio.run(main())
