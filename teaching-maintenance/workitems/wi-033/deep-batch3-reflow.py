"""Reflow existing SVG evidence without changing recorded feature values or raster anchors."""
from pathlib import Path
import json,hashlib,sys,asyncio,xml.etree.ElementTree as ET,importlib.util
from playwright.async_api import async_playwright
from render import text,rect,split
W=Path(__file__).resolve().parent;C=W.parents[1]
ROWS=[
 dict(id='resnet-deep-residual',source='_course_content/generated-concepts/resnet/resnet-e01-02-residual.svg',title='同一位置：保留訊號，再加修正',provenance='沿用本機ResNet50特徵；場景為生成示意',takeaway='同位置逐格相加；特徵值不是缺陷機率。',panels=[
  dict(title='原場景與保留值 x',tiles=[([35,195,415,490],[30,120,240,350]),([485,220,305,395],[300,120,340,440])],notes=['同一R-01，layer1.1／通道93','以下三張矩陣保留原記錄數字']),
  dict(title='同位置的主路徑修正 F(x)',tiles=[([890,220,305,395],[125,105,430,555])],notes=['負值也是修正，不是負缺陷機率']),
  dict(title='逐格相加，再經 ReLU',tiles=[([1295,220,310,395],[125,100,430,548])],notes=['中央格：1.2 + (−1.9) → 0','數字經四捨五入；不是新一輪推論'])]),
 dict(id='segformer-deep-core',source='_course_content/generated-concepts/segformer/segformer-e03-core.svg',title='多尺度理解，再融合成像素圖',provenance='沿用W-01原像素與概念；非模型推論',takeaway='保留四尺度並對齊融合，再驗證細線邊界。',panels=[
  dict(title='同一亮線需要細節與脈絡',tiles=[([25,145,730,135],[25,95,640,180]),([20,325,740,235],[25,310,640,270])],notes=['MiT逐階段縮小，仍保留四組特徵','四尺度不是四張獨立的標註遮罩']),
  dict(title='投影、對齊，再拼接融合',tiles=[([20,540,745,165],[20,150,650,235])],notes=['不是只放大最後一張粗特徵','四尺度一起影響每個像素的類別','輕量解碼器不走完整鏡像U形回程']),
  dict(title='回原亮線檢查可觀察細節',tiles=[([790,405,850,340],[15,120,660,400])],notes=['圖中差異是概念示意，不是實測輸出','注意力先縮減K/V，減少比較量','實際速度與邊界仍需驗證'])])
]

def preflight(r):
 path=W/(r['id']+'-r01.md')
 s='# '+r['title']+'\n- lesson objective: '+r['takeaway']+'\n- page type: C\n- primary reading path: '+' → '.join([p['title'] for p in r['panels']]+[r['takeaway']])+'\n- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`\n- pale-yellow takeaway: '+r['takeaway']+' #FFF4CC\n- major visual nodes:\n'
 for i,p in enumerate(r['panels']):s+=f"  {i+1}. {p['title']}\n"
 s+='\n來源：'+r['source']+'。'+r['provenance']+'。重排既有SVG的證據區塊；原內嵌場景、實測值與來源保留，不重造實測數字。三主節點手機768×2800，桌機原圖保留。每片依明確viewBox引用既有向量，不改既有PNG。先檢查兩家族原型再擴展。\n權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。\nPNG review pending；page review pending；user approval pending。\n'
 path.write_text(s,encoding='utf-8')
 spec=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v);v.validate(path)

def make(r):
 root=ET.parse(C/r['source']).getroot()
 for e in list(root):
  if e.get('marker-end') and (r.get('omit_arrows') is True or e.get('d') in r.get('omit_arrows',[])):root.remove(e)
 ET.register_namespace('','http://www.w3.org/2000/svg')
 body=''.join(ET.tostring(e,encoding='unicode') for e in root)
 s='<svg xmlns="http://www.w3.org/2000/svg" width="768" height="2800" viewBox="0 0 768 2800"><style>text{font-family:"Microsoft JhengHei",sans-serif}</style><defs><g id="original-evidence">'+body+'</g></defs>'+rect(0,0,768,2800,'white','none',0)
 for i,v in enumerate(split(r['title'],18)):s+=text(28,55+i*48,v,38,'#173650',800)
 for i,v in enumerate(split(r['provenance'],25)):s+=text(28,145+i*31,v,23,'#526B81')
 for i,p in enumerate(r['panels']):
  y=210+i*795
  s+=rect(30,y,708,770,'#F3F8FF','#BAD5EF',18)+rect(46,y+15,676,64,'#1762CD','none',13)+text(66,y+58,p['title'],30,'white',700)
  for ti,(box,dest) in enumerate(p['tiles']):
   x,dy,w,h=dest
   bx,by,bw,bh=box;cid=f'crop-{i}-{ti}'
   s+=f'<svg x="{45+x}" y="{y+dy}" width="{w}" height="{h}" viewBox="'+ ' '.join(map(str,box))+f'" preserveAspectRatio="xMidYMid meet"><defs><clipPath id="{cid}"><rect x="{bx}" y="{by}" width="{bw}" height="{bh}"/></clipPath></defs><use href="#original-evidence" clip-path="url(#{cid})"/></svg>'
  for j,n in enumerate(p['notes']):s+=text(58,y+674+j*34,n,27,'#173650',600)
  if i<2:s+=text(377,y+790,'↓',26,'#1762CD',700)
 s+=rect(24,2630,720,145,'#FFF4CC','#EAB24B',15)
 for j,v in enumerate(split(r['takeaway'],21)):s+=text(44,2680+j*44,v,30,'#173650',800)
 return s+'</svg>'

async def main():
 for r in ROWS:preflight(r)
 (W/'batch3-deep-reflow-plan.json').write_text(json.dumps(ROWS,ensure_ascii=False,indent=2),encoding='utf-8')
 if '--plan' in sys.argv:return
 async with async_playwright() as p:
  b=await p.chromium.launch(channel='msedge',headless=True)
  for r in ROWS:
   if r['id']!='segformer-deep-core':continue
   version='r04';f=W/(r['id']+'-'+version+'-mobile.svg');assert not f.exists();(W/(r['id']+'-'+version+'.md')).write_text((W/(r['id']+'-r01.md')).read_text(encoding='utf-8')+'\n修訂：viewBox採meet時仍需精確clipPath，避免鄰區文字與黃色邊框滲入；裁切避開鄰區半行字與影像碎片。待重新實看。\n',encoding='utf-8');f.write_text(make(r),encoding='utf-8')
   page=await b.new_page(viewport={'width':768,'height':2800},device_scale_factor=1);await page.goto(f.as_uri());await page.wait_for_timeout(400);await page.screenshot(path=str(f.with_suffix('.png')));await page.close()
  await b.close()
if __name__=='__main__':asyncio.run(main())
