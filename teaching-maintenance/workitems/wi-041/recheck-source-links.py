from pathlib import Path
import re,json,urllib.request,urllib.error,concurrent.futures
W=Path(__file__).resolve().parent
data=json.loads((W/'recheck-external_sources.json').read_text(encoding='utf8'))
urls=sorted({u.rstrip('.,)') for r in data for u in re.findall(r'https?://[^\s；（）;<>"\u3002]+',r['url'])})
def check(url):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=20) as r:
            r.read(1024)
            return {'url':url,'status':r.status,'final_url':r.url}
    except Exception as e:return {'url':url,'status':getattr(e,'code',None),'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(check,urls))
result={'count':len(rows),'method':'GET first 1024 bytes; extract individual URLs from source prose','failures':[r for r in rows if r['status']!=200],'results':rows}
(W/'recheck-source-links.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='results'},ensure_ascii=False))
