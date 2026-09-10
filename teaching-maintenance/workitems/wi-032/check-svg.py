import asyncio,json,re
from pathlib import Path
from playwright.async_api import async_playwright
W=Path(__file__).resolve().parent
async def main():
 out=[]
 async with async_playwright() as p:
  b=await p.chromium.launch(channel='msedge',headless=True)
  page=await b.new_page(viewport={'width':1800,'height':3200})
  files=set()
  for row in json.loads((W/'selected-assets.json').read_text(encoding='utf-8')).values():
   for mode in ['desktop','mobile']:
    f=(W/row[mode]).with_suffix('.svg')
    if f.exists():files.add(f)
  for row in json.loads((W/'engineering-active-assets.json').read_text(encoding='utf-8')):
   version=re.search(r'-(r\d+)-',row['image'])[1]
   f=W/f"{row['id']}-{version}-{row['mode']}.svg";assert f.exists();files.add(f)
  for f in sorted(files):
   await page.goto(f.as_uri())
   errors=await page.evaluate('''() => {const svg=document.querySelector('svg'),w=+svg.getAttribute('width'),h=+svg.getAttribute('height'),r=svg.getBoundingClientRect();const result=[];for(const el of svg.querySelectorAll('text')){const b=el.getBoundingClientRect();let parent=el.parentElement;while(parent.parentElement&&parent.parentElement!==svg) parent=parent.parentElement;let card=parent.tagName==='g'?parent.querySelector(':scope > rect'):null;const c=card && +card.getAttribute("width")>=500 && +card.getAttribute("height")>=500 ? card.getBoundingClientRect() : null;if(b.right>r.left+w+1||b.left<r.left-1||b.bottom>r.top+h+1) result.push({text:el.textContent,kind:'canvas',box:[b.x,b.y,b.width,b.height]});if(c&&(b.right>c.right+2||b.left<c.left-2||b.bottom>c.bottom+2))result.push({text:el.textContent,kind:'panel',box:[b.x,b.y,b.width,b.height]});}return result;}''')
   if errors:out.append({'file':f.name,'errors':errors})
  await b.close()
 result={'files':len(files),'errors':out,'scope':'文字的畫布與卡片外溢；不代表語意或人工評分'}
 (W/'svg-layout-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(result,ensure_ascii=False,indent=2));assert not out
if __name__=='__main__':asyncio.run(main())
