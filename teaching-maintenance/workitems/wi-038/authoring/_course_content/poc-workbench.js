    // Versioned answers are isolated from preserved legacy PoC drafts.
    let pocUndo = null;
    function pocFlow() {
      const raw=validRecord(progress.poc._flow,{});
      const answers=validRecord(raw.answers,{}), clean={};
      for(const q of POC_DECISION.questions(answers)) if(q.options.some(([v])=>v===answers[q.id])) clean[q.id]=answers[q.id];
      const questions=POC_DECISION.questions(clean);
      const confirmed=Array.isArray(raw.confirmed)?raw.confirmed.filter(id=>questions.some(q=>q.id===id)&&clean[id]):[];
      return {version:1,answers:clean,confirmed,current:typeof raw.current==='string'?raw.current:''};
    }
    function pocContext() {
      const flow=pocFlow(),questions=POC_DECISION.questions(flow.answers);
      const current=questions.find(q=>q.id===flow.current)||questions.find(q=>!flow.confirmed.includes(q.id));
      return {flow,questions,current,result:POC_DECISION.evaluate(flow.answers)};
    }
    function pocSaveFlow(flow) { progress.poc._flow=flow;saveProgress(); }
    function choosePocAnswer(id,value) {
      const {flow,questions}=pocContext(),index=questions.findIndex(q=>q.id===id),question=questions[index];
      if(!question||!question.options.some(([v])=>v===value))return;
      if(flow.answers[id]!==value) {
        // Upstream changes invalidate downstream assumptions, even on the same branch.
        for(const q of questions.slice(index+1))delete flow.answers[q.id];
        flow.confirmed=flow.confirmed.filter(key=>questions.slice(0,index).some(q=>q.id===key));
      }
      flow.answers[id]=value;flow.current=id;app.pocPreview=false;pocSaveFlow(flow);
      const next=document.querySelector('[data-action="poc-next"]');if(next)next.disabled=false;
      const selected=document.getElementById('poc-selected');if(selected)selected.textContent=question.options.find(([v])=>v===value)[1];
      document.getElementById('poc-status').textContent=pocSaveMessage();
    }
    function advancePoc() {
      const {flow,current}=pocContext();if(!current||!flow.answers[current.id])return;
      if(!flow.confirmed.includes(current.id))flow.confirmed.push(current.id);
      flow.current='';pocSaveFlow(flow);render();pocFocus();
    }
    function editPoc(id) { const {flow,questions}=pocContext();if(!questions.some(q=>q.id===id))return;flow.current=id;app.pocPreview=false;pocSaveFlow(flow);render();pocFocus(); }
    function pocFocus() { const el=document.getElementById('poc-question-title')||document.getElementById('poc-result-title');el?.focus({preventScroll:true});el?.scrollIntoView({block:'start'}); }
    function pocList(items,ordered=false) { const tag=ordered?'ol':'ul';return `<${tag}>${items.map(x=>`<li>${escapeHTML(x)}</li>`).join('')}</${tag}>`; }
    function pocAnswerRows() {const {flow,questions}=pocContext();return questions.filter(q=>flow.answers[q.id]).map(q=>({id:q.id,label:q.label,value:q.options.find(([v])=>v===flow.answers[q.id])?.[1]||''}));}
    function pocSummaryHTML() {
      const {current}=pocContext(),rows=pocAnswerRows();
      return `<p class="eyebrow">你的現場條件</p><h2>${current?'釐清需求中':'已整理試做方向'}</h2><p class="poc-help">${current?'每個答案決定下一步要確認什麼。':'可回頭修改條件，重新推導方法。'}</p><ol class="poc-answer-trail">${rows.map(r=>`<li><span>${escapeHTML(r.label)}</span><strong>${escapeHTML(r.value)}</strong><button class="button" type="button" data-action="poc-edit" data-question="${r.id}">修改</button></li>`).join('')}</ol>${!rows.length?'<p>從你想解決的現場問題開始。</p>':''}`;
    }
    function pocResultHTML() {
      const {result}=pocContext();
      const courses=result.courses.map(id=>TOPIC_BY_ID[id]).filter(Boolean);
      return `<section id="poc-result" class="panel"><p class="eyebrow">${escapeHTML(result.state)}</p><h2 id="poc-result-title" tabindex="-1">${escapeHTML(result.title)}</h2><h3>先怎麼做</h3>${pocList(result.steps,true)}<h3>為什麼走這條路</h3>${pocList(result.reasons)}<h3>還要確認什麼</h3>${pocList(result.gaps.length?result.gaps:['條件已足夠規劃小規模比較；仍需用獨立現場資料驗證。'])}<h3>第一個小實驗</h3>${pocList(result.experiment,true)}${courses.length?`<details class="poc-optional"><summary>相關方法與課程（選讀）</summary><p>這些是對應方法的實作參考；不同階段可能需要搭配，並非排名或保證適用。</p><div class="action-row">${courses.map(t=>`<button class="button" type="button" data-action="lesson" data-topic="${escapeHTML(t.id)}">${escapeHTML(t.model)}</button>`).join('')}</div></details>`:''}<div class="poc-step-actions"><button class="button" data-action="poc-edit" data-question="task">修改現場問題</button><button class="button primary" data-action="poc-preview">整理成 PoC 計畫 →</button></div></section>`;
    }
    function pocPlanSections() {
      const {result,current}=pocContext();
      return [{label:'目前狀態',text:current?'尚有問題未確認；以下為暫定方向。':result.state},{label:'現場條件',text:pocAnswerRows().map(r=>r.label+'：'+r.value).join('\n')||'尚未回答'},{label:'試做方向',text:result.title},{label:'方法步驟',text:result.steps.join('\n')},{label:'推導原因',text:result.reasons.join('\n')},{label:'待確認條件',text:result.gaps.join('\n')||'用獨立現場資料驗證。'},{label:'小規模驗證',text:result.experiment.join('\n')},{label:'交接補充（選填）',text:typeof progress.poc._handoff==='string'?progress.poc._handoff:''}];
    }
    function pocPreviewHTML() {return `<h2 id="poc-preview-title" tabindex="-1">PoC 試做計畫</h2><p>這是依現場答案整理的待驗證計畫，並非上線結論。</p><dl>${pocPlanSections().map(s=>`<div><dt>${escapeHTML(s.label)}</dt><dd>${escapeHTML(s.text||'未填')}</dd></div>`).join('')}</dl>`;}
    function pocLegacyHTML() {
      const labels={task:'現場問題',output:'預期輸出',data:'資料',baseline:'比較基準',model:'原先選擇的模型',contract:'比較條件',evidence:'驗證方式',hold:'停止條件',owner:'交接負責人'};
      const rows=Object.entries(labels).filter(([key])=>typeof progress.poc[key]==='string'&&progress.poc[key]);
      const notes=Array.isArray(progress.poc._courseNotes)?progress.poc._courseNotes.filter(n=>n&&typeof n.id==='string'&&TOPIC_BY_ID[n.id]):[];
      if(!rows.length&&!notes.length)return '';
      return `<details id="poc-legacy" class="poc-backup"><summary>查看保留的舊草稿／課程筆記</summary><p>這些內容供對照，新流程會依你的回答重新推導方法。</p><dl>${rows.map(([key,label])=>`<dt>${label}</dt><dd>${escapeHTML(progress.poc[key])}${typeof progress.poc._notes?.[key]==='string'?'<br>'+escapeHTML(progress.poc._notes[key]):''}</dd>`).join('')}${notes.map(n=>`<dt>課程筆記：${escapeHTML(TOPIC_BY_ID[n.id].model)}</dt><dd>${escapeHTML(typeof n.output==='string'?n.output:'')}</dd>`).join('')}</dl></details>`;
    }
    function pocHTML() {
      const {flow,questions,current}=pocContext(),preview=Boolean(app.pocPreview),index=questions.indexOf(current);
      return `<div class="content poc-workbench"><header class="poc-header"><p class="eyebrow">需求導向・試做助手</p><h1>從現場問題，找到第一個試做方法</h1><p class="poc-intro">選擇你的情況，我們會整理方法、原因與待補條件。不確定的題目也能繼續。</p><div class="action-row"><button class="button" data-action="fill-poc-example">試看：料盤漏裝</button><button class="button" data-action="poc-undo" ${pocUndo?'':'hidden'}>撤銷上次帶入／清除</button></div></header><ol class="poc-phases" aria-label="流程階段"><li ${current?'aria-current="step"':''}>1 現場條件</li><li ${!current&&!preview?'aria-current="step"':''}>2 方法與原因</li><li ${preview?'aria-current="step"':''}>3 試做計畫</li></ol><div class="poc-layout"><div class="poc-editor">${!preview?(current?`<section id="poc-form" class="poc-step"><p class="eyebrow">第 ${index+1} 題・依答案調整後續問題</p><h2 id="poc-question-title" tabindex="-1">${escapeHTML(current.label)}</h2><p id="poc-question-help">${escapeHTML(current.hint)}</p><label for="poc-answer">請選最接近的情況</label><select id="poc-answer" data-poc-answer="${current.id}" aria-describedby="poc-question-help poc-selected"><option value="" disabled ${!flow.answers[current.id]?'selected':''}>請選擇</option>${current.options.map(([v,label])=>`<option value="${v}" ${flow.answers[current.id]===v?'selected':''}>${escapeHTML(label)}</option>`).join('')}</select><p id="poc-selected" class="poc-selected">${escapeHTML(current.options.find(([v])=>v===flow.answers[current.id])?.[1]||'選好後按「繼續」，再確認下一題。')}</p><div class="poc-step-actions">${index>0?`<button class="button" data-action="poc-edit" data-question="${questions[index-1].id}">← 上一題</button>`:'<span></span>'}<button class="button primary" data-action="poc-next" ${flow.answers[current.id]?'':'disabled'}>繼續 →</button></div></section>`:pocResultHTML()):''}<section id="poc-preview" class="panel" ${preview?'':'hidden'}>${pocPreviewHTML()}</section>${preview?`<details class="poc-optional"><summary>補充交接人、場地與目標（選填）</summary><label for="poc-handoff">現場補充</label><textarea id="poc-handoff" data-poc="_handoff" rows="3">${escapeHTML(typeof progress.poc._handoff==='string'?progress.poc._handoff:'')}</textarea></details><div class="poc-preview-actions"><button class="button" data-action="poc-result">← 回到方法</button><button class="button primary" data-action="export-poc-markdown">下載 PoC Markdown</button><button class="button" data-action="print-poc">列印／另存 PDF</button></div>`:''}</div><aside id="poc-summary" class="panel poc-summary">${pocSummaryHTML()}</aside></div><p id="poc-status" class="poc-status" role="status">${pocSaveMessage()}</p><div class="poc-takeaway">先依現場條件找到可驗證的方法，再用原始資料確認效果。</div>${pocLegacyHTML()}<details class="poc-backup"><summary>備份、還原與重新開始</summary><p>答案保存在目前瀏覽器；JSON 備份包含舊草稿與學習進度。</p><div class="poc-actions"><button class="button" data-action="export-poc-markdown">下載目前計畫</button><button class="button" data-action="export-progress">匯出進度 JSON</button><label class="button" for="import-progress">匯入進度 JSON</label><input id="import-progress" type="file" accept="application/json"><button class="button" data-action="poc-reset">重新開始 PoC</button><button class="button warn" data-action="clear-progress">清除全部本機進度</button></div></details></div>`;
    }
    function pocSaveMessage() {return storageFailed?'目前無法儲存，請下載 Markdown 或 JSON 備份。':'答案已暫存在目前瀏覽器。'}
    function updatePocUI() { const el=document.getElementById('poc-preview');if(el)el.innerHTML=pocPreviewHTML();const status=document.getElementById('poc-status');if(status)status.textContent=pocSaveMessage(); }
    function showPocPreview() {app.pocPreview=true;render();document.getElementById('poc-preview-title')?.focus();}
    function applyPocDraft(draft,message) {if(Object.keys(progress.poc).length&&!confirm('帶入範例會取代目前答案，之後可撤銷。是否繼續？'))return false;pocUndo=structuredClone(progress.poc);progress.poc=draft;app.pocPreview=false;saveProgress();notify(message);return true;}
    function sendToPoc(topicId) {const topic=TOPIC_BY_ID[topicId];if(!topic)return;pocUndo=structuredClone(progress.poc);const notes=Array.isArray(progress.poc._courseNotes)?progress.poc._courseNotes:[];progress.poc._courseNotes=[...notes.filter(n=>n?.id!==topicId),{id:topic.id,output:topic.engineeringBrief.output}];saveProgress();app.pocPreview=false;go('poc');notify('課程已保留在筆記中；請依現場條件整理試做方法。');}
    function fillPocExample() {if(applyPocDraft({_flow:{version:1,answers:{task:'count'},confirmed:['task'],current:''}},'已帶入料盤漏裝情境，請確認擺放方式。'))render();}
    function exportPocMarkdown() {const text='# PoC 試做計畫\n\n依現場答案推導，仍須實測驗證。\n\n'+pocPlanSections().map(s=>'## '+s.label+'\n\n'+(s.text||'未填')).join('\n\n')+'\n';const url=URL.createObjectURL(new Blob([text],{type:'text/markdown;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download='vision-ai-poc.md';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);notify('已下載 PoC 試做計畫。');}
