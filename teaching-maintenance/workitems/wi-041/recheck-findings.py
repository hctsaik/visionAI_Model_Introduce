from pathlib import Path
import json
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent
URL='https://hctsaik.github.io/visionAI_Model_Introduce/'
rows=[]
with sync_playwright() as pw:
    b=pw.chromium.launch(channel='msedge',headless=True)
    p=b.new_page(viewport={'width':1440,'height':1000},reduced_motion='reduce')
    for tid in ['ad-diffad','u-net','yolo-seg','ad-efficientad','convlstm','videomae']:
        p.goto(URL+'#view=lesson&lesson='+tid+'&slide=1')
        p.locator('#lesson-title').wait_for()
        data=json.loads(p.locator('#course-data').text_content())
        t=next((t for t in data['topics'] if t['id']==tid),None)
        if t is None:
            rows.append({'requested':tid,'actual_ids':[t['id'] for t in data['topics'] if 'net' in t['id']]});continue
        before=p.locator('main').inner_text()
        p.locator('main details').evaluate_all('(els)=>els.forEach(e=>e.open=true)')
        after=p.locator('main').inner_text()
        (W/f'recheck-visible-{tid}.txt').write_text(after,encoding='utf8')
        rows.append({'topic':tid,'title':p.locator('#lesson-title').inner_text(),'mechanism':t['teachingStory']['mechanism_steps'],'default_contains_once_forward':'一次 forward' in before,'expanded_contains_once_forward':'一次 forward' in after})
        needle={'ad-diffad':'一次 forward','u-net':'像素標註教任務','yolo-seg':'先有實例標註','ad-efficientad':'正常資料教學生','convlstm':'卷積更新狀態','videomae':'只編碼可見塊再重建'}[tid]
        loc=p.get_by_text(needle,exact=False).filter(visible=True)
        if loc.count():
            loc.first.scroll_into_view_if_needed()
            p.screenshot(path=str(W/f'recheck-finding-{tid}.png'))
    b.close()
(W/'recheck-findings.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print('Confirmed rendered findings for',len(rows),'lessons; see recheck-findings.json')
