from pathlib import Path
import importlib.util,json,asyncio,runpy
from playwright.async_api import async_playwright
W=Path(__file__).resolve().parent;C=W.parents[1]
sp=importlib.util.spec_from_file_location('reflow',W/'deep-batch3-reflow.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
def panel(title,tiles,notes):return dict(title=title,tiles=tiles,notes=notes)
rows=[dict(id='patchcore-deep-features',source='_course_content/generated-concepts/ad-patchcore/patchcore-work-02-features_p03.svg',title='同來源位置，追到實際CNN回應',provenance='保留既有ResNet50記錄；工件為生成示意',takeaway='鄰域平均是一個描述分量，不是缺陷分數。',omit_arrows=True,panels=[
 panel('原工件A-01與同位置框',[([50,250,360,390],[90,105,490,530])],['整個ROI先進固定CNN','來源框對到後續特徵位置']),
 panel('layer2的一個實際通道',[([600,250,370,360],[100,115,470,470])],['保留既有28×28回應與橘框','色深只顯示此通道的回應']),
 panel('同位置3×3鄰域形成一個值',[([1100,290,215,210],[25,145,360,352]),([1425,350,185,130],[420,220,230,165])],['格內數字已四捨五入顯示','平均用原精度：4.695003 → 4.70','其他通道也提供描述分量'])]),
 dict(id='patchcore-deep-context',source='_course_content/generated-concepts/ad-patchcore/patchcore-work-02-context_p03.svg',title='同位置的兩層線索，再組成描述',provenance='沿用既有CNN記錄；非PatchCore異常推論',takeaway='兩層描述可串接；色深不能直接跨層比較。',omit_arrows=True,panels=[
 panel('同一待測工件與刮傷附近',[([50,250,370,380],[80,110,500,510])],['保留A-01原像素與同位置框','未新增CNN或異常檢測推論']),
 panel('layer2：較細網格的局部回應',[([580,260,335,355],[100,110,480,510])],['原記錄的描述分量：4.07','先在此層做3×3鄰域平均']),
 panel('layer3：較大範圍的局部線索',[([1080,260,340,355],[100,110,480,510])],['原記錄的描述分量：3.91','鄰域平均後雙線性對齊，再串接','每層色階獨立；數值保留原尺度'])])]
spec=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
async def main():
 out=[]
 for r in rows:
  path=W/(r['id']+'-r01.md')
  body='# '+r['title']+'\n- lesson objective: '+r['takeaway']+'\n- page type: C\n- primary reading path: '+' → '.join([p['title'] for p in r['panels']]+[r['takeaway']])+'\n- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`\n- pale-yellow takeaway: '+r['takeaway']+' #FFF4CC\n- major visual nodes:\n'+'\n'.join(f"  {i+1}. {p['title']}" for i,p in enumerate(r['panels']))+'\n來源：'+r['source']+'\n'+r['provenance']+'；原SVG已轉檢查圖實看，精確clipPath切既有向量證據，保留原內嵌影像及已記錄數值。p03-sources/cnn-features.json核對原精度4.695003/4.065633/3.911689。768×2800手機版；桌機與其他7章不改，保留第三方/作者案例。模式：既有SVG重排成新SVG/PNG，非點陣內容編修。\n權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。\nPNG review pending；page review pending；user approval pending。\n'
  path.write_text(body,encoding='utf-8');out.append(v.validate(path))
 (W/'batch5-deep-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch5-deep-preflight-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
 note='''### WI-033 PatchCore第二章兩手機深讀即將重排

第五批機制16PNG已原生審查，未整合；其餘24工程故事待製作。PatchCore第二章兩份preflight通過，原SVG檢查圖已實看並核對cnn-features.json的原精度4.695003/4.065633/3.911689。即將產出patchcore-deep-{features,context}-r01-mobile.svg/png（768×2800），保留原像素/特徵證據、桌機和其他章節。候選未審/整合；下一步逐圖實看。完成25/52，使用者核准pending，全部52課持續。
'''
 (W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
 async with async_playwright() as pw:
  b=await pw.chromium.launch(channel='msedge',headless=True)
  for r in rows:
   f=W/(r['id']+'-r01-mobile.svg');assert not f.exists();f.write_text(m.make(r),encoding='utf-8')
   p=await b.new_page(viewport={'width':768,'height':2800});await p.goto(f.as_uri());await p.evaluate('document.fonts.ready');await p.wait_for_timeout(300);await p.screenshot(path=str(f.with_suffix('.png')));await p.close()
  await b.close()
 print('2 deep mobile candidates rendered; actual review pending')
if __name__=='__main__':asyncio.run(main())
