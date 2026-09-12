    // All draft content uses the existing progress store; view state stays local.
    const POC_FIELDS = [
      {key:'task', label:'現場要解決什麼問題？', step:0, hint:'例如：找出料盤上漏裝的墊圈，減少人工逐件清點。'},
      {key:'output', label:'模型先交出什麼？', step:0, hint:'例如：每件候選框與類別；計數規則另行核對，不直接當品質判定。'},
      {key:'data', label:'有哪些資料？', step:1, hint:'先選最接近的資料現況；測試資料須與訓練或參考資料分開。'},
      {key:'baseline', label:'要跟目前哪種做法比較？', step:1, hint:'例如：目前人工清點，或既有檢測模型；使用同一批測試工件比較。'},
      {key:'model', label:'候選模型', step:1},
      {key:'contract', label:'比較時固定哪些條件？', step:1, hint:'例如：取像、資料切分、模型版本、門檻、硬體與覆核方式。'},
      {key:'evidence', label:'怎樣才算有幫助？', step:2, hint:'選擇主要比較方式；具體數值目標可在補充欄填寫，再與負責人確認。'},
      {key:'hold', label:'什麼情況先停下來？', step:2, hint:'例如：新產品、取像改變、結果無法回查或覆核量超限時，交回既有流程。'},
      {key:'owner', label:'誰覆核、誰接手？', step:2, hint:'先選負責角色；實際人員、覆核時間與交接方式可以選填。'},
    ];
    const POC_CHOICES = {
      task:['檢查零件有沒有漏裝／數量是否正確','判斷工件是哪一類','找出表面異常或缺陷位置','分出物件或缺陷的精確輪廓','對位、追蹤特徵或準備尺寸量測','分析影片中的動作或變化','讀取影像文字或回答影像問題','生成或復原影像作為輔助資料'],
      output:['物件候選框、類別與分數','整張影像的類別與分數','異常分數與可疑位置圖','物件或缺陷的分割遮罩','特徵對應、位置或幾何估計','軌跡、位移或事件候選','待核對的文字、欄位或回答','生成／復原影像候選'],
      data:['只有正常品影像','有正常品與少量缺陷影像','已有類別或物件框標註','已有像素遮罩或關鍵點標註','已有連續影片與事件紀錄','只有少量範例，尚未整理資料'],
      baseline:['目前由人工目視／清點','目前使用規則或傳統影像處理','已有模型，準備與新方法比較','還沒有流程，先建立人工核對基準'],
      contract:['固定取像、獨立測試資料、版本與門檻','另固定硬體及前後處理，比較完整延遲','另固定文字／範例提示，比較提示變更影響','先固定影格取樣、時間窗與狀態重設方式'],
      evidence:['比較漏檢、誤報與人工覆核量','比較定位／輪廓誤差與漏檢','比較完整延遲、記憶體與結果品質','比較文字／問答正確率與核對工時','比較下游任務效益，並核對原始影像'],
      hold:['取像、產品或資料分布改變時，交回人工','結果不確定或無法回查原圖時，停止自動處理','漏檢、誤報或覆核量超過約定範圍時，回到既有流程','服務失敗或延遲超限時，啟用備援流程'],
      owner:['品保覆核，現場工程師接手','現場操作員覆核，製程工程師接手','演算法工程師與品保共同核對','先由專案負責人協調覆核與接手角色'],
    };
    const POC_OUTPUT_ROUTES = [[0,3],[1],[2,3],[3],[4],[5,0],[6],[7]];
    function pocOptions(key) {
      if(key==='output') { const index=POC_CHOICES.task.indexOf(pocValue('task'));if(index>=0)return POC_OUTPUT_ROUTES[index].map(i=>POC_CHOICES.output[i]); }
      return POC_CHOICES[key]||[];
    }
    function pocOutputNeedsReview() { return POC_CHOICES.output.includes(pocValue('output'))&&!pocOptions('output').includes(pocValue('output')); }
    function pocText(key) {
      const note=progress.poc?._notes?.[key];
      return pocValue(key)+(typeof note==='string'&&note.trim()?'\n補充：'+note.trim():'')+(key==='output'&&pocOutputNeedsReview()?'\n任務已變更，請重新核對這項輸出。':'');
    }
    function choosePocAnswer(key,value) {
      if(!POC_CHOICES[key])return;
      progress.poc._custom=validRecord(progress.poc._custom,{});
      progress.poc._custom[key]=value==='__custom__';
      if(value!=='__custom__')progress.poc[key]=value;
      else if(POC_CHOICES[key].includes(pocValue(key)))progress.poc[key]='';
      saveProgress();render();
      document.getElementById(value==='__custom__'?`poc-custom-${key}`:`poc-${key}`)?.focus({preventScroll:true});
    }
    const POC_STEPS = ['現場問題', '比較方法', '驗收與交接'];
    let pocUndo = null;
    function pocValue(key) { const value = progress.poc?.[key]; return typeof value === 'string' ? value : ''; }
    function pocFilled(field) { return field.key === 'model' ? Boolean(TOPIC_BY_ID[pocValue('model')]) : Boolean(pocValue(field.key).trim()) && !(field.key==='output' && pocOutputNeedsReview()); }
    function pocFieldHTML(field) {
      if (field.key === 'model') return `<div class="field wide"><label for="poc-model">候選模型</label><p class="poc-help">先選一個起點；下方提示會跟著改變，並不代表已替你完成選型。</p><label class="poc-search-label" for="poc-model-search">搜尋模型或家族</label><input id="poc-model-search" type="search" placeholder="例如：DINO、異常、分割"><select id="poc-model" data-poc="model"><option value="">尚未選擇</option>${TOPICS.map(t=>`<option value="${escapeHTML(t.id)}" ${pocValue('model')===t.id?'selected':''}>${escapeHTML(t.model)} · ${escapeHTML(t.familyLabel)}</option>`).join('')}</select><p id="poc-model-count" class="poc-help"></p><section id="poc-model-guide" aria-label="候選模型提示">${pocModelGuideHTML()}</section></div>`;
      const options=pocOptions(field.key), value=pocValue(field.key);
      const known=(POC_CHOICES[field.key]||[]).includes(value), custom=Boolean(progress.poc._custom?.[field.key])||Boolean(value&&!known);
      const stale=known&&!options.includes(value);
      const note=typeof progress.poc._notes?.[field.key]==='string'?progress.poc._notes[field.key]:'';
      return `<div class="field ${field.key==='contract'?'wide':''}"><label for="poc-${field.key}">${field.label}</label><select id="poc-${field.key}" data-poc-choice="${field.key}" aria-describedby="poc-help-${field.key}"><option value="">請選擇最接近的情況</option>${stale?`<option value="${escapeHTML(value)}" selected>原選擇（請重新核對）：${escapeHTML(value)}</option>`:''}${options.map(text=>`<option value="${escapeHTML(text)}" ${!custom&&value===text?'selected':''}>${escapeHTML(text)}</option>`).join('')}<option value="__custom__" ${custom?'selected':''}>${value&&!known?'保留原有自訂內容':'其他情況／自行補充'}</option></select><p class="poc-help" id="poc-help-${field.key}">${field.key==='output'?'依現場任務顯示可比較的輸出；仍須核對模型實際能力。':field.hint}</p>${stale?'<p class="poc-choice-warning" role="status">任務已變更。已保留原選擇，請重新選擇合適的輸出。</p>':''}<details class="poc-optional" ${progress.poc._custom?.[field.key]?'open':''}><summary>${custom?'查看／修改自訂內容':'補充現場細節（選填）'}</summary>${custom?`<label for="poc-custom-${field.key}">自訂回答</label><textarea id="poc-custom-${field.key}" data-poc="${field.key}" rows="3">${escapeHTML(value)}</textarea>`:''}<label for="poc-note-${field.key}">補充說明（選填）</label><textarea id="poc-note-${field.key}" data-poc-note="${field.key}" rows="2">${escapeHTML(note)}</textarea></details></div>`;
    }
    function pocModelGuideHTML() {
      const topic=TOPIC_BY_ID[pocValue('model')];
      if (!topic) return '<p class="poc-help">還沒決定也可以繼續。選定後，這裡會顯示交付內容與使用限制。</p>';
      return `<div class="poc-model-guide"><h3>${escapeHTML(topic.model)} 的試做提示</h3><p><strong>交付：</strong>${escapeHTML(topic.engineeringBrief.output)}</p><p><strong>先核對：</strong>${escapeHTML(topic.engineeringBrief.hold)}</p><div class="action-row"><button class="button" type="button" data-action="poc-model-hints">把提示帶入尚未填寫的欄位</button><button class="button" type="button" data-action="lesson" data-topic="${escapeHTML(topic.id)}">查看這一課 →</button></div><p class="poc-help">既有文字會保留；更換模型後，請核對原草稿是否仍適用。</p></div>`;
    }
    function pocSummaryHTML() {
      const missing=POC_FIELDS.filter(f=>!pocFilled(f)), count=POC_FIELDS.length-missing.length;
      return `<p class="eyebrow">你的試做草稿</p><h2>${count} / ${POC_FIELDS.length} 項已填寫</h2><progress max="${POC_FIELDS.length}" value="${count}" aria-label="草稿填寫程度"></progress><p class="poc-help">這是填寫程度，尚未判定內容是否可驗收。</p>${missing.length?`<h3>接著可以補</h3><ul class="poc-missing">${missing.map(f=>`<li><button type="button" data-action="poc-missing" data-field="${f.key}" data-step="${f.step}">${f.label} →</button></li>`).join('')}</ul>`:'<p>欄位已填齊。請預覽並核對具體目標、比較條件及接手人。</p>'}${app.pocPreview ? `<button class="button primary" type="button" data-action="export-poc-markdown">下載 PoC Markdown</button><p><button class="button" type="button" data-action="poc-step" data-step="${progress.pocStep || 0}">← 繼續編輯</button></p>` : `<button class="button primary" type="button" data-action="poc-preview">預覽完整草稿 →</button>`}`;
    }
    function pocPreviewHTML() {
      return `<h2 id="poc-preview-title" tabindex="-1">PoC 試做草稿</h2><p>以下是待討論的試做計畫；欄位填齊不代表模型已通過驗證。</p><dl>${POC_FIELDS.map(f=>`<div><dt>${f.label}</dt><dd>${escapeHTML(f.key==='model' ? (TOPIC_BY_ID[pocValue('model')]?.model || '待選擇') : (pocText(f.key).trim() || '待補充'))}</dd></div>`).join('')}</dl>`;
    }
    function pocHTML() {
      const step=Number.isInteger(progress.pocStep) && progress.pocStep>=0 && progress.pocStep<3 ? progress.pocStep : 0;
      const preview=Boolean(app.pocPreview);
      return `<div class="content poc-workbench"><header class="poc-header"><p class="eyebrow">POC 選型畫布</p><h1>一步一步，整理你的試做計畫。</h1><p class="poc-intro">用下拉選項一步步回答，就能產生試做草稿。細節可選填，也可以從範例開始。</p><div class="action-row"><button class="button" type="button" data-action="fill-poc-example">帶入晶圓 AOI 範例</button><button class="button" type="button" data-action="poc-undo" ${pocUndo?'':'hidden'}>撤銷上次帶入</button></div></header><nav class="poc-step-nav" aria-label="試做計畫步驟">${POC_STEPS.map((name,i)=>`<button type="button" data-action="poc-step" data-step="${i}" ${!preview&&step===i?'aria-current="step"':''}><span>${i+1}</span><span>${name}<small data-poc-step-count="${i}">${POC_FIELDS.filter(f=>f.step===i&&pocFilled(f)).length} / ${POC_FIELDS.filter(f=>f.step===i).length} 項</small></span></button>`).join('')}</nav><div class="poc-layout"><div class="poc-editor"><div id="poc-form" ${preview?'hidden':''}>${POC_STEPS.map((name,i)=>`<section class="poc-step" data-poc-panel="${i}" ${step===i?'':'hidden'}><header class="poc-step-heading"><span>${i+1}</span><div><h2 tabindex="-1" id="poc-heading-${i}">${name}</h2><p>${['先選現場要解決的問題，再選希望取得的輸出。','讓候選模型和目前做法，用相同資料接受比較。','把驗收方式、停止條件與負責角色說清楚。'][i]}</p></div></header><div class="poc-grid">${POC_FIELDS.filter(f=>f.step===i).map(pocFieldHTML).join('')}</div><div class="poc-step-actions">${i>0?`<button class="button" type="button" data-action="poc-step" data-step="${i-1}">← 上一步</button>`:'<span></span>'}<button class="button primary" type="button" data-action="${i===2?'poc-preview':'poc-step'}" ${i<2?`data-step="${i+1}"`:''}>${i===2?'預覽完整草稿 →':'下一步 →'}</button></div></section>`).join('')}</div><section id="poc-preview" class="panel" ${preview?'':'hidden'}>${pocPreviewHTML()}</section><div class="poc-preview-actions" ${preview?'':'hidden'}><button class="button" type="button" data-action="poc-step" data-step="${step}">← 繼續編輯</button><button class="button primary" type="button" data-action="export-poc-markdown">下載 PoC Markdown</button><button class="button" type="button" data-action="print-poc">列印／另存 PDF</button></div></div><aside id="poc-summary" class="panel poc-summary" aria-label="填寫進度與待補項目">${pocSummaryHTML()}</aside></div><p id="poc-status" class="poc-status" role="status">${pocSaveMessage()}</p><div class="poc-takeaway">完成草稿後，仍要用現場資料驗證，才能判斷是否值得採用。</div><details class="poc-backup"><summary>備份、匯入與清除草稿</summary><p>草稿存在目前瀏覽器；換裝置時，先匯出 JSON 再於另一台匯入。Markdown 適合閱讀與交接。</p><div class="poc-actions"><button class="button" type="button" data-action="export-poc-markdown">下載 PoC Markdown</button><button class="button" type="button" data-action="export-progress">匯出學習與 POC 進度 JSON</button><label class="button" for="import-progress">匯入進度 JSON</label><input id="import-progress" type="file" accept="application/json"><button class="button" type="button" data-action="poc-reset">只清除 PoC 草稿</button><button class="button warn" type="button" data-action="clear-progress">清除全部本機進度</button></div></details></div>`;
    }
    function pocSaveMessage() { return storageFailed ? '目前無法儲存到瀏覽器；請先下載 Markdown 或匯出 JSON，離開頁面可能遺失修改。' : '草稿已儲存在目前瀏覽器。換裝置前，請先匯出備份。'; }
    function updatePocUI(modelChanged=false) {
      const summary=document.getElementById('poc-summary'); if (!summary) return;
      summary.innerHTML=pocSummaryHTML();
      document.querySelectorAll('[data-poc-step-count]').forEach(el=>{ const fields=POC_FIELDS.filter(f=>f.step===Number(el.dataset.pocStepCount)); el.textContent=`${fields.filter(pocFilled).length} / ${fields.length} 項`; });
      document.getElementById('poc-preview').innerHTML=pocPreviewHTML();
      document.getElementById('poc-status').textContent=pocSaveMessage();
      if (modelChanged) document.getElementById('poc-model-guide').innerHTML=pocModelGuideHTML();
    }
    function showPocStep(step, field) {
      if (!Number.isInteger(step)||step<0||step>2) return;
      progress.pocStep=step;app.pocPreview=false;saveProgress();render();
      const target=document.getElementById(field?`poc-${field}`:`poc-heading-${step}`);
      target?.focus({preventScroll:true});target?.scrollIntoView({block:'center',behavior:'auto'});
    }
    function showPocPreview() { app.pocPreview=true;render(); const target=document.getElementById('poc-preview-title');target?.focus({preventScroll:true});target?.scrollIntoView({block:'start'}); }
    function applyPocDraft(draft, message) {
      if (POC_FIELDS.some(pocFilled) && !confirm('帶入內容會取代目前 PoC 草稿。是否繼續？帶入後可以撤銷。')) return false;
      pocUndo=structuredClone(progress.poc);progress.poc=draft;progress.pocStep=0;app.pocPreview=false;saveProgress();notify(message);return true;
    }
    function sendToPoc(topicId) {
      const topic=TOPIC_BY_ID[topicId];if (!topic) return;
      if (!applyPocDraft({task:topic.learnerBrief.problem,model:topic.id,output:topic.engineeringBrief.output,contract:'固定取像、資料切分、模型版本、門檻、硬體與覆核方式。',evidence:topic.engineeringBrief.evidence,hold:topic.engineeringBrief.hold},'已帶入操作卡，請補上現場資料與接手人。')) return;
      go('poc');
    }
    function fillPocExample() {
      if (applyPocDraft({task:POC_CHOICES.task[2],output:POC_CHOICES.output[2],data:POC_CHOICES.data[1],model:'ad-patchcore',baseline:POC_CHOICES.baseline[0],contract:POC_CHOICES.contract[0],evidence:POC_CHOICES.evidence[0],hold:POC_CHOICES.hold[2],owner:POC_CHOICES.owner[0],_notes:{task:'晶圓 AOI：找出不像正常品的局部，交由人工確認。'}},'已帶入可調整的選項範例。')) render();
    }
    function fillPocModelHints() {
      const topic=TOPIC_BY_ID[pocValue('model')];if(!topic)return;
      pocUndo=structuredClone(progress.poc);
      const hints={output:topic.engineeringBrief.output,evidence:topic.engineeringBrief.evidence,hold:topic.engineeringBrief.hold};let count=0;
      for(const [key,value] of Object.entries(hints)) if(!pocValue(key).trim()){progress.poc[key]=value;count++;}
      saveProgress();render();notify(count?`已補入 ${count} 個空欄，請依現場調整。`:'欄位已有內容，已保留原草稿。');
    }
    function exportPocMarkdown() {
      const text='# PoC 試做草稿\n\n待討論草稿；填寫完成不代表模型通過驗證。\n\n'+POC_FIELDS.map(f=>'## '+f.label+'\n\n'+(f.key==='model'?(TOPIC_BY_ID[pocValue('model')]?.model||'待選擇'):(pocText(f.key).trim()||'待補充'))).join('\n\n')+'\n';
      const url=URL.createObjectURL(new Blob([text],{type:'text/markdown;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download='vision-ai-poc.md';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);notify('已下載可閱讀的 PoC 草稿。');
    }
