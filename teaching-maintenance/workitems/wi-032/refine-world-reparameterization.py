from pathlib import Path
import json,subprocess,sys,shutil,hashlib
W=Path(__file__).resolve().parent;C=W.parents[1];id='yolo-world-engineering-3'
p=W/(id+'-r07.md');p.write_text((W/(id+'-r04.md')).read_text(encoding='utf-8')+'\n## r07 原圖審查修正\n中間節點不能只有部署方框。依官方docs/reparameterize.md分類頭例，畫兩類詞彙向量下移成1×1分類頭參數，影像特徵經此頭產生類別分數；綠／藍保持詞彙身份。這是結構示意，不是所有neck模組的完整圖。三大節點、原C閱讀路徑、參考及單一#FFF4CCtakeaway不變。原生與實頁待查、user approval pending。\n',encoding='utf-8')
subprocess.run([sys.executable,'-X','utf8',str(C/'tools/validate_teaching_preflight.py'),str(p)],check=True,stdout=subprocess.DEVNULL)
p=W/'render-engineering.py';s=p.read_text(encoding='utf-8')
start=s.index(" if k=='reparameterize':");end=s.index(" if k=='refresh':",start)
s=s[:start]+''' if k=='reparameterize':
  out=text(25,30,'例：詞彙整合到分類頭',28)+vec(170,58,B,n=5)+vec(170,107,G,n=5)+arrow(240,155,240,215,G)
  out+=text(150,253,'1×1 分類頭參數',27)+rect(165,270,165,95,'#ECF5F3',G,5)
  out+=vec(178,280,B,n=5)+vec(178,324,G,n=5)
  out+=featuregrid(25,290,2,23)+arrow(80,313,150,313)+arrow(342,313,392,313)
  out+=rect(403,285,65,22,B,'none',0)+rect(403,332,35,22,G,'none',0)
  return out+text(20,412,'影像特徵',26)+text(175,412,'結構示意',26)+text(380,412,'分數',26)
''' + s[end:]
s=s.replace("+'-r06-'+mode","+'-r07-'+mode");p.write_text(s,encoding='utf-8')
subprocess.run([sys.executable,'-X','utf8',str(p),id],check=True)
p=C/'_course_content/topics/yolo-world.json';t=json.loads(p.read_text(encoding='utf-8'));folder=(C/t['review_trace']['authority']).parent
manifestp=folder/'slide-manifest.md';manifest=manifestp.read_text(encoding='utf-8')
rows=json.loads((W/'engineering-active-assets.json').read_text(encoding='utf-8'))
for row in rows:
 if row['id']!=id:continue
 old=row['image'];dest=C/old.replace('-r04-','-r07-');src=W/f"{id}-r07-{row['mode']}.png";shutil.copyfile(src,dest)
 row['image']=dest.relative_to(C).as_posix();row['sha256']=hashlib.sha256(dest.read_bytes()).hexdigest();row['actual_page_review']='pending'
 if row['mode']=='desktop':manifest=manifest.replace(Path(old).name,dest.name)
 else:t['engineering_slides'][2]['mobile_image']=row['image']
manifestp.write_text(manifest,encoding='utf-8');p.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');(W/'engineering-active-assets.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'engineering-review-notes.json';notes=json.loads(p.read_text(encoding='utf-8'));notes[id]=[[23,24,19,18,9],'兩類詞彙向量以相同顏色轉為1×1分類頭參數，影像特徵通過此頭產生類別分數；與外存快取分開。','r04部署方框不足以説明轉換，r07依官方分類頭例補可見結構；只示範head，不當作所有neck與head的完整架構。'];p.write_text(json.dumps(notes,ensure_ascii=False,indent=2),encoding='utf-8')
# Conditional wording describes the rebuilt pages without changing other lessons.
p=C/'tools/build_interactive_learning_html.py';s=p.read_text(encoding='utf-8')
s=s.replace('工程參考：展開原有四張模型圖與完整節點<span>首讀主線已改用全幅工作例；這裡保留原圖，供設定、證據與術語核對。</span>', '${topic.teachingStory?.engineering_slides ? "工程參考：展開四張工程圖與完整節點" : "工程參考：展開原有四張模型圖與完整節點"}<span>${topic.teachingStory?.engineering_slides ? "從輸入、機制、交付到限制，核對實作與驗證方式。" : "首讀主線已改用全幅工作例；這裡保留原圖，供設定、證據與術語核對。"}</span>')
p.write_text(s,encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n## 最終圖像修正\n24個第二輪頁面／168放大／24自測及導覽通過；18個390px deep-link、前後張與舊課fallback通過。1351資產course/docs hash相同、186 HTTP hash通過，6課改動、52課資料不變。實圖重評發現World工程3仍偏部署文字方框，r07新增詞彙轉1×1分類頭參數及特徵→分數可見路徑；官方來源已核對。即將實看此2張、重建並重驗該課；共用工程展開標題也改為符合實際內容。其他新圖不變。\n')
