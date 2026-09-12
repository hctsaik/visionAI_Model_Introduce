from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1]
p=C/'tools/build_interactive_learning_html.py';s=p.read_text(encoding='utf8')
start=s.index('    function pocHTML() {');end=s.index('\n    function ',start+10)
s=s[:start]+'    __POC_WORKBENCH__\n'+s[end:]
start=s.index('    function sendToPoc(topicId) {');end=s.index('    function exportProgress()',start)
s=s[:start]+s[end:]
s=s.replace('    @media print {','    __POC_CSS__\n    @media print {',1)
s=s.replace('    function saveProgress() { try { localStorage.setItem(STORAGE_KEY, JSON.stringify(progress)); } catch (_) {} }','    let storageFailed = false;\n    function saveProgress() { try { localStorage.setItem(STORAGE_KEY, JSON.stringify(progress)); storageFailed=false; return true; } catch (_) { storageFailed=true; return false; } }')
s=s.replace('      if (action === "print-poc") window.print();','''      if (action === "poc-step") showPocStep(Number(trigger.dataset.step));
      if (action === "poc-missing") showPocStep(Number(trigger.dataset.step), trigger.dataset.field);
      if (action === "poc-preview") showPocPreview();
      if (action === "poc-model-hints") fillPocModelHints();
      if (action === "export-poc-markdown") exportPocMarkdown();
      if (action === "poc-undo" && pocUndo) { progress.poc=pocUndo; pocUndo=null; saveProgress(); render(); notify("已還原帶入前的草稿。"); }
      if (action === "poc-reset" && confirm("只清除 PoC 草稿？課程完成與收藏會保留。")) { pocUndo=structuredClone(progress.poc);progress.poc={};progress.pocStep=0;app.pocPreview=false;saveProgress();render(); }
      if (action === "print-poc") { updatePocUI(); window.print(); }''')
s=s.replace('if (event.target.dataset.poc) { progress.poc[event.target.dataset.poc] = event.target.value; saveProgress(); const status = document.getElementById("poc-status"); if (status) status.textContent = "已儲存在這台裝置的瀏覽器中。"; }','''if (event.target.id === "poc-model-search") {
        const query=event.target.value.trim().toLocaleLowerCase();const select=document.getElementById("poc-model");
        const matches=TOPICS.filter(t=>(t.model+" "+t.familyLabel).toLocaleLowerCase().includes(query));
        const selected=TOPIC_BY_ID[pocValue("model")];const options=selected&&!matches.includes(selected)?[selected,...matches]:matches;
        select.innerHTML='<option value="">尚未選擇</option>'+options.map(t=>`<option value="${escapeHTML(t.id)}" ${t.id===pocValue("model")?"selected":""}>${escapeHTML(t.model)} · ${escapeHTML(t.familyLabel)}</option>`).join("");
        document.getElementById("poc-model-count").textContent=`找到 ${matches.length} 個模型${selected&&!matches.includes(selected)?"；保留目前選擇":""}。`;
      }
      if (event.target.dataset.poc) { progress.poc[event.target.dataset.poc] = event.target.value; saveProgress(); updatePocUI(event.target.dataset.poc === "model"); }''')
s=s.replace('if (event.target.dataset.poc) { progress.poc[event.target.dataset.poc] = event.target.value; saveProgress(); }','if (event.target.dataset.poc) { progress.poc[event.target.dataset.poc] = event.target.value; saveProgress(); updatePocUI(event.target.dataset.poc === "model"); }')
s=s.replace('setTheme(progress.theme); saveProgress(); notify("已匯入進度。 "); render();','pocUndo=null; app.pocPreview=false; setTheme(progress.theme); saveProgress(); notify("已匯入進度。 "); render();')
s=s.replace('progress = structuredClone(DEFAULT_PROGRESS); setTheme("light");','progress = structuredClone(DEFAULT_PROGRESS); pocUndo=null; app.pocPreview=false; setTheme("light");')
s=s.replace('          const parsed = JSON.parse(String(reader.result));','          const parsed = JSON.parse(String(reader.result));\n          if (!confirm("匯入將取代目前學習進度與 PoC 草稿，是否繼續？")) return;')
s=s.replace('    document = document.replace("__WORKPLACE_UI__",','    document = document.replace("__POC_WORKBENCH__", (ROOT / "_course_content/poc-workbench.js").read_text(encoding="utf-8"))\n    document = document.replace("__POC_CSS__", (ROOT / "_course_content/poc-workbench.css").read_text(encoding="utf-8"))\n    document = document.replace("__WORKPLACE_UI__",')
s=s.replace('"index": page_index + 1, "label": label,','"index": page_index + 1, "label": item.get("label", label),',1)
p.write_text(s,encoding='utf8',newline='\n')
print('Integrated PoC sources and topic-specific labels.')
