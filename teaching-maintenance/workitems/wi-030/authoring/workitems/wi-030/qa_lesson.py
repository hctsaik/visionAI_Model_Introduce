import json,hashlib,sys
from pathlib import Path
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parent
slug=sys.argv[1]; count=int(sys.argv[2]); OUT=P/('qa-'+slug);OUT.mkdir(exist_ok=True)
records=[]
with sync_playwright() as p:
    b=p.chromium.launch(channel='msedge',headless=True)
    for name,route in [('course','interactive-learning.html'),('docs','docs/index.html')]:
        for width,height in [(1440,1000),(390,844),(360,800)]:
            page=b.new_page(viewport={'width':width,'height':height})
            errors=[];page.on('pageerror',lambda error:errors.append(str(error)))
            url=f'http://127.0.0.1:8000/{route}#view=lesson&lesson={slug}&slide=1'
            page.goto(url,wait_until='networkidle')
            page.evaluate('document.fonts.ready')
            cards=page.locator('.beginner-visual')
            assert cards.count()==count
            image_records=[]
            if page.locator('.legacy-deep-reference').count():
                assert not page.locator('.legacy-deep-reference').evaluate('(e)=>e.open')
            page.screenshot(path=str(OUT/f'{name}-{width}-top.png'))
            for n in range(count):
                card=cards.nth(n)
                fig=card.locator('figure').first
                fig.evaluate('(e)=>window.scrollTo(0,scrollY+e.getBoundingClientRect().top-100)')
                page.wait_for_timeout(100)
                visible=fig.locator('img:visible')
                assert visible.count()==1,(width,n,visible.count())
                visible.evaluate('(i)=>i.decode()')
                state=visible.evaluate('(i)=>({src:i.currentSrc,width:i.naturalWidth,height:i.naturalHeight,box:i.getBoundingClientRect().toJSON()})')
                assert 'wi030-' in state['src']
                if width<700:
                    assert state['height']>state['width']
                    assert state['box']['width']<=width
                page.screenshot(path=str(OUT/f'{name}-{width}-v{n+1}-top.png'))
                if width<700:
                    fig.evaluate('(e)=>window.scrollTo(0,scrollY+e.getBoundingClientRect().bottom-innerHeight+25)')
                    page.screenshot(path=str(OUT/f'{name}-{width}-v{n+1}-bottom.png'))
                card.get_by_role('button',name='放大完整圖',exact=True).click()
                page.locator('#lightbox[open]').wait_for()
                page.wait_for_function("()=>{let i=document.querySelector('#lightbox img');return i&&i.complete&&i.naturalWidth>0}")
                page.keyboard.press('Escape')
                assert page.locator('#lightbox[open]').count()==0
                image_records.append(state)
            answer=page.get_by_text('看解釋與可接受的取捨',exact=True)
            answer.click()
            text=answer.locator('..').inner_text()
            topic=json.loads((P.parents[1]/'_course_content/topics'/f'{slug}.json').read_text(encoding='utf-8'))
            assert topic['micro_example']['reveal'] in text
            ref=page.locator('details').filter(has=page.locator('summary').filter(has_text='工程參考：展開文字因果鏈')).first
            ref.locator('summary').first.click()
            assert ref.locator('img,object').count()==0
            overflow=page.evaluate('document.documentElement.scrollWidth>innerWidth+1')
            assert not overflow
            nxt=page.locator('.lesson-footer button').last
            nxt.click();page.wait_for_timeout(100)
            if slug=='super-resolution':
                assert '#view=poc' in page.url,page.url
            else:
                assert 'lesson=' in page.url and ('lesson='+slug+'&') not in page.url,page.url
            assert not errors,errors
            records.append({'route':route,'viewport':[width,height],'images':image_records,'zoom_loaded_escape':count,'answer':True,'engineering_images':0,'navigation':True,'page_errors':errors,'overflow':overflow})
            page.close()
    b.close()
(OUT/'report.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'{slug} PASS: 6 page states, {6*count} images/zoom, answers/navigation, no overflow/page errors')
