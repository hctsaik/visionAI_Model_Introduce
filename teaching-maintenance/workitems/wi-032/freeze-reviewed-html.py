"""Retain the reviewed serialization when a rebuild differs only in JSON key order."""
from pathlib import Path
import json,re,hashlib,shutil,urllib.request
W=Path(__file__).resolve().parent;C=W.parents[1]
pattern=r'(<script id="course-data" type="application/json">)(.*?)(</script>)'
a=(C/'interactive-learning.html').read_text(encoding='utf-8');b=(C/'docs/index.html').read_text(encoding='utf-8')
ma=re.search(pattern,a,re.S);mb=re.search(pattern,b,re.S)
assert json.loads(ma[2])==json.loads(mb[2])
assert re.sub(pattern,lambda m:m[1]+m[3],a,flags=re.S)==re.sub(pattern,lambda m:m[1]+m[3],b,flags=re.S)
old=hashlib.sha256((C/'interactive-learning.html').read_bytes()).hexdigest()
shutil.copyfile(C/'docs/index.html',C/'interactive-learning.html')
digest=hashlib.sha256((C/'interactive-learning.html').read_bytes()).hexdigest()
v=json.loads((W/'final-verification.json').read_text(encoding='utf-8'));assert digest==v['html_sha256']
checks=[]
for rel in ['interactive-learning.html','docs/index.html']:
 with urllib.request.urlopen('http://127.0.0.1:8000/'+rel,timeout=30) as r:
  assert hashlib.sha256(r.read()).hexdigest()==digest;checks.append({'url':rel,'status':r.status,'sha256':digest})
v['final_html_freeze']={'reason':'Rebuild differed only in JSON object key serialization order; all parsed data and the non-data HTML template matched exactly. Retained the fully reviewed serialization.','rebuild_sha256':old,'reviewed_sha256':digest,'http':checks}
(W/'final-verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n## 最終HTML序列化核對\n收尾重建因Python set欄位迭代次序而產生不同JSON鍵順序；全部解析資料（含58課）及移除JSON後的HTML模板完全相同。沒有教材或UI差異。已保留實頁驗證過的序列化版本並同步course/docs，兩URL HTML HTTP SHA256再次一致；詳見final-verification.json final_html_freeze。這不是內容回退，也未改動其餘52課。必要驗證均已完成。\n')
print('Reviewed HTML frozen; semantic data/template match and both HTTP hashes verified')
