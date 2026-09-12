from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1]
p=C/'_course_content/poc-workbench.js';s=p.read_text(encoding='utf8')
insert='''    const POC_CHOICES = {
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
      return pocValue(key)+(typeof note==='string'&&note.trim()?'\\n補充：'+note.trim():'')+(key==='output'&&pocOutputNeedsReview()?'\\n任務已變更，請重新核對這項輸出。':'');
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
'''
s=s.replace('    const POC_STEPS =',insert+'    const POC_STEPS =',1)
s=s.replace("Boolean(pocValue(field.key).trim());", "Boolean(pocValue(field.key).trim()) && !(field.key==='output' && pocOutputNeedsReview());")
start=s.index('      return `<div class="field ${field.key');end=s.index('\n    }',start)
s=s[:start]+'''      const options=pocOptions(field.key), value=pocValue(field.key);
      const known=(POC_CHOICES[field.key]||[]).includes(value), custom=Boolean(progress.poc._custom?.[field.key])||Boolean(value&&!known);
      const stale=known&&!options.includes(value);
      const note=typeof progress.poc._notes?.[field.key]==='string'?progress.poc._notes[field.key]:'';
      return `<div class="field ${field.key==='contract'?'wide':''}"><label for="poc-${field.key}">${field.label}</label><select id="poc-${field.key}" data-poc-choice="${field.key}" aria-describedby="poc-help-${field.key}"><option value="">請選擇最接近的情況</option>${stale?`<option value="${escapeHTML(value)}" selected>原選擇（請重新核對）：${escapeHTML(value)}</option>`:''}${options.map(text=>`<option value="${escapeHTML(text)}" ${!custom&&value===text?'selected':''}>${escapeHTML(text)}</option>`).join('')}<option value="__custom__" ${custom?'selected':''}>${value&&!known?'保留原有自訂內容':'其他情況／自行補充'}</option></select><p class="poc-help" id="poc-help-${field.key}">${field.key==='output'?'依現場任務顯示可比較的輸出；仍須核對模型實際能力。':field.hint}</p>${stale?'<p class="poc-choice-warning" role="status">任務已變更。已保留原選擇，請重新選擇合適的輸出。</p>':''}<details class="poc-optional" ${progress.poc._custom?.[field.key]?'open':''}><summary>${custom?'查看／修改自訂內容':'補充現場細節（選填）'}</summary>${custom?`<label for="poc-custom-${field.key}">自訂回答</label><textarea id="poc-custom-${field.key}" data-poc="${field.key}" rows="3">${escapeHTML(value)}</textarea>`:''}<label for="poc-note-${field.key}">補充說明（選填）</label><textarea id="poc-note-${field.key}" data-poc-note="${field.key}" rows="2">${escapeHTML(note)}</textarea></details></div>`;'''+s[end:]
s=s.replace("(pocValue(f.key).trim() || '待補充')", "(pocText(f.key).trim() || '待補充')")
s=s.replace("(pocValue(f.key).trim()||'待補充')", "(pocText(f.key).trim()||'待補充')")
s=s.replace('先寫得出來，再一起核對。可以隨時往返、留白，或從範例開始。','用下拉選項一步步回答，就能產生試做草稿。細節可選填，也可以從範例開始。')
s=s.replace('描述你的工作與期待輸出，先不用填工程名詞。','先選現場要解決的問題，再選希望取得的輸出。')
start=s.index('      if (applyPocDraft({task:',s.index('    function fillPocExample()'))
end=s.index('\n    }',start)
s=s[:start]+'''      if (applyPocDraft({task:POC_CHOICES.task[2],output:POC_CHOICES.output[2],data:POC_CHOICES.data[1],model:'ad-patchcore',baseline:POC_CHOICES.baseline[0],contract:POC_CHOICES.contract[0],evidence:POC_CHOICES.evidence[0],hold:POC_CHOICES.hold[2],owner:POC_CHOICES.owner[0],_notes:{task:'晶圓 AOI：找出不像正常品的局部，交由人工確認。'}},'已帶入可調整的選項範例。')) render();'''+s[end:]
p.write_text(s,encoding='utf8')
p=C/'tools/build_interactive_learning_html.py';s=p.read_text(encoding='utf8')
s=s.replace('      if (event.target.dataset.poc && event.target.tagName !== "SELECT")', '      if (event.target.dataset.pocNote) { progress.poc._notes=validRecord(progress.poc._notes,{}); progress.poc._notes[event.target.dataset.pocNote]=event.target.value; saveProgress(); updatePocUI(); }\n      if (event.target.dataset.poc && event.target.tagName !== "SELECT")')
s=s.replace('      if (event.target.id === "family-filter")', '      if (event.target.dataset.pocChoice) { choosePocAnswer(event.target.dataset.pocChoice,event.target.value); return; }\n      if (event.target.id === "family-filter")')
p.write_text(s,encoding='utf8')
p=C/'_course_content/poc-workbench.css';p.write_text(p.read_text(encoding='utf8')+'\n    .poc-optional { margin-top:12px; }\n    .poc-optional summary { color:var(--blue);font-size:13px;cursor:pointer;padding:8px 0; }\n    .poc-optional label { margin-top:12px; }\n    .poc-choice-warning { color:var(--ink);border-left:3px solid #dc9829;padding-left:10px;font-size:14px; }\n    .poc-workbench select { width:100%;min-height:48px; }\n',encoding='utf8')
print('Implemented choice-first fields, dependent outputs, optional notes and legacy preservation.')
