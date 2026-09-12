from pathlib import Path
import json,importlib.util
W=Path(__file__).resolve().parent;C=W.parents[1]
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
def add(owner,n,title,takeaway,panels,detail,source,kind='C'):
 rid=f'{owner}-engineering-{n}'
 if any(r['id']==rid for r in rows):return
 rows.append(dict(id=rid,owner=owner,index=n,version='r01',title=title,kind=kind,takeaway=takeaway,panels=[{'title':a,'graphic':b} for a,b in panels],steps=[],detail=detail,source=source,review='pending'))
clip='https://arxiv.org/abs/2103.00020';sig='https://arxiv.org/abs/2303.15343'
add('clip',1,'CLIP：用描述整理零件照片','文字定義候選，影像與描述的相似度幫你找圖。',[
 ('照片庫裡有不同零件','catalog'),('把工作需求寫成候選','descriptions'),('用候選排名找出照片','retrieval')],
 '工件照片與候選描述各自編碼。新增描述可定義新的比較集合，無須為每次檢索重新訓練固定類別頭；預訓練及域內驗證仍不可省略。相似度排名不是缺陷位置或合格證明。',clip)
add('clip',3,'CLIP：文字可快取，改字就要更新','換文字或權重後，更新表示並重測候選排名。',[
 ('先保存文字及其表示','text-cache'),('新影像與快取表示比較','cache-match'),('更換候選後重新核對','cache-refresh')],
 '同一模型／前處理下可預先計算候選文字表示。新影像只需走影像編碼器，再與相容文字表示比較。改文字、權重或設定時更新相關快取，使用已知和未知零件重新驗證；文字快取並不是把影像直接送進文字編碼器。',clip)
add('clip',4,'CLIP：第一名也可能沒有正確答案','先確認候選涵蓋需求，再決定排序能否交付。',[
 ('待測照片確實是齒輪','gear-input'),('候選只有支架與軸承','missing-candidate'),('加入候選仍要驗證','candidate-review')],
 '同一齒輪影像遇到缺少齒輪的候選集合，仍會有第一名。補齊描述後先檢查易混淆與未知資料；若工作要求細微尺寸或缺陷差別，可準備標註資料測專用分類器。以下排名為反例示意，不代表模型實測。',clip)
add('siglip',1,'SigLIP：每個圖文配對都給學習訊號','正配對拉近、負配對分開，共同更新編碼器。',[
 ('先知道哪個描述配哪張圖','paired-training'),('逐對比較配對與不配對','pair-matrix'),('損失共同更新兩編碼器','pair-update')],
 '原始 SigLIP 的圖文編碼器分別產生表示，對正負圖文對計算 sigmoid 損失，梯度共同更新參數。每對有自己的二元目標，不需要 CLIP 式的整批 softmax 正規化；逐對計算不代表每對訓練一個獨立模型。',sig)
add('siglip',2,'SigLIP：雙路編碼，逐對計算損失','改變的是配對訓練目標，兩個編碼器仍並行。',[
 ('影像與文字分別進模型','clip-dual'),('每一對依正負標籤學習','sigmoid-pairs'),('全部配對訊號一起更新','loss-aggregate')],
 '圖文表示的內積經可學習尺度與偏移後，以正／負標籤計算 sigmoid 損失。圖中高低分僅解釋學習方向，不是模型機率校正結果；部署時不需提供正負訓練標籤。',sig)
add('siglip',3,'SigLIP：部署交出分數，不是回答','以固定模型比較候選，再用域內資料設定覆核。',[
 ('保存候選文字表示','text-cache'),('新影像與候選逐一比','siglip-match'),('依工作風險核對結果','score-review')],
 '部署用預訓練好的圖文表示比較相似性；可依实现轉換配對分數，但不把 sigmoid 值直接當作域內正確率。結果是候選分數或排名，不是逐字生成回答，也不自帶可靠未知類別拒答。',sig)
add('siglip',4,'SigLIP：逐對學習不會補出缺少的類別','選型要看本地錯誤與成本，不能只看損失名稱。',[
 ('兩種模型看同一齒輪','gear-input'),('兩者候選都缺齒輪','both-missing'),('固定條件後比較取捨','comparison-work')],
 'CLIP 與 SigLIP 使用相同工件照片、相同缺少正確答案的候選時，都不能因有最高分就判定正確。比較需固定資料及候選，測誤配、拒答和完整成本；原論文的訓練優點不保證每個域內任務較好。',sig,kind='D')
if not any(r['id']=='alignment-comparison' for r in rows):
 rows.append(dict(id='alignment-comparison',owner='clip',index=0,version='r01',title='CLIP 與 SigLIP：訓練不同，選型同題',kind='D',mobile_height=2304,takeaway='訓練目標不同，工作選型仍要同題驗證。',panels=[{'title':'CLIP：行列間比較正配對','graphic':'clip-softmax'},{'title':'SigLIP：逐對給學習訊號','graphic':'siglip-local'},{'title':'部署仍用共同條件驗證','graphic':'comparison-work'}],detail='同一圖文配對；CLIP訓練以行列softmax對比，原始SigLIP使用逐對sigmoid目標。兩者選型需固定資料與候選，核對誤配、未知樣本和完整成本。',source=clip+' ; '+sig,review='pending'))
(W/'engineering-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
reference='teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png'
spec=importlib.util.spec_from_file_location('preflight',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
results=[]
for r in rows:
 dest=W/f"{r['id']}-{r['version']}.md"
 if not dest.exists():
  nodes='\n'.join(f"  {i+1}. {p['title']}；具體視覺 {p['graphic']}" for i,p in enumerate(r['panels']))
  body=f"""# {r['title']}

- lesson objective: {r['takeaway']}
- page type: {r['kind']} — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → {r['panels'][0]['title']} → {r['panels'][1]['title']} → {r['panels'][2]['title']}
- named guide-conformant reference page: `{reference}` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: {r['takeaway']} #FFF4CC
- major visual nodes:
{nodes}

## 機制、證據與修正

{r['detail']}

來源：{r['source']} 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。
"""
  dest.write_text(body,encoding='utf-8')
 results.append(v.validate(dest))
(W/'preflight-validation.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print('Saved and validated',len(rows),'story briefs; no new images yet')
