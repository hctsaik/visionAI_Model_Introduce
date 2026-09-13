from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;C=W.parents[1]
r=json.loads((W/'release-verification.json').read_text(encoding='utf8'));assert r['complete'] and len(r['pages'])==12
assert r['poc_1440']==r['poc_390']=='passed'
message=f"六課修正與新版verifier完成並公開。內容commit {r['commit'][:7]}已push，公開HTML {r['html_sha256'][:8]}與docs相同；六課12個公開桌面手機實頁及需求流程通過。本機30tests+146subtests、15規則、verifier補驗10tests+11subtests及source/docs總驗證通過。WI041必修已關閉，建議本版定版；使用者成品核准仍pending。"
p=W/'PLAN.md';p.write_text(p.read_text(encoding='utf8').replace('- [ ]','- [x]')+'\n最終發布checkpoint：'+message+'\n',encoding='utf8')
p=W/'REPORT.md';s=p.read_text(encoding='utf8');s=s.replace('狀態：實作、建置、必要測試與12張本機實頁審查完成；Git及公開部署尚未完成。','狀態：實作、建置、必要測試、本機與公開驗證完成，Git已推送；本輪定版修正無未完成項目。')
s+='\n## 公開完成與定版判斷\n\n'+message+'\n\n公開核對證據release-verification.json；首次部署前舊hash拒絕及等待保留於deployment-wait.json。前述尚待發布段落是歷史checkpoint，不代表目前狀態。公開成品已包含六課修正，維護版verifier也已通過；沒有剩餘必修阻礙，建議定版。後續選配僅依真實使用回饋另排，不以這次完成代表所有模型現場實測。\n';p.write_text(s,encoding='utf8')
result=[]
for row in r['pages']:
 a=W/row['screenshot'];b=W/row['screenshot'].replace('public-','local-',1)
 result.append({'topic':row['topic'],'width':row['width'],'public_png_sha256':hashlib.sha256(a.read_bytes()).hexdigest(),'matches_reviewed_local_png':a.read_bytes()==b.read_bytes()})
(W/'public-screenshot-comparison.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(message);print('Public screenshots equal reviewed local:',sum(x['matches_reviewed_local_png'] for x in result),'/12')
