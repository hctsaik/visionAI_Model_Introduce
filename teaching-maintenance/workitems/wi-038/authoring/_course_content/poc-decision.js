    // WI-037: explicit teaching rules, not measured model rankings. Topic IDs refer
    // to learner-briefs.json; workflow stages must not be read as alternatives.
    const POC_DECISION = (() => {
      const unknown = ['unknown', '還不確定'];
      const q = (id, label, hint, options) => ({id, label, hint, options:[...options, unknown]});
      const task = q('task', '你希望電腦幫你完成什麼？', '選現場工作就好，不需要知道模型名稱。', [
        ['count','檢查有沒有漏裝、數量對不對'], ['defect','找出表面有問題的位置'],
        ['classify','分辨這是哪一種產品'], ['contour','沿著邊緣圈出物件'],
        ['measure','確認位置或量實際尺寸'], ['video','看影片中的移動、事件或變化'],
        ['text','讀取照片上的文字或整理內容'], ['generate','改善或產生影像作其他用途']
      ]);
      const visibility = q('visibility','原始照片上的目標或細節，看得清楚嗎？','以人能否核對需要的線索為準；不要用修復後的細節代替原始證據。',[
        ['clear','看得清楚，可以人工核對'], ['poor','反光或模糊，人工也難以判讀'], ['occluded','目標被其他物件擋住']
      ]);
      const definitions = {
        placement:q('placement','要檢查的零件放在哪裡？','位置是否固定，會影響先核對格位還是先找每一件。',[
          ['fixed','放在固定格位或裝配位置'],['free','位置不固定，需要先找出每一件']]),
        defectKind:q('defectKind','想找的是哪種問題？','已知缺陷與從未見過的異常，需要不同資料與核對方式。',[
          ['known','已知幾種缺陷，想分辨是哪一種'],['novel','新的異常也要找，不一定知道名稱']]),
        detail:q('detail','找到問題後，需要看得多細？','指出可疑位置，不等於沿缺陷邊緣精確圈出。',[
          ['location','先指出值得回看的可疑位置'],['boundary','需要沿缺陷邊緣圈清楚']]),
        classes:q('classes','要分辨的產品種類固定嗎？','種類經常改變時，要重新核對參考品與類別定義。',[
          ['fixed','種類固定，名稱與範例已定義'],['changing','經常增加新品或改變搜尋對象']]),
        multiplicity:q('multiplicity','每張照片要分辨幾件？','整張照片的類別，不會自動指出每件在哪裡。',[
          ['single','每張只看一件，或已切成單件照片'],['multiple','同一張有多件，需要分別辨認']]),
        separation:q('separation','圈出的區域需要每件分開嗎？','全部前景連成一區，與逐件分離是不同交付。',[
          ['whole','只要全部物件或缺陷的區域'],['each','需要每一件各自的輪廓']]),
        overlap:q('overlap','物件之間會相貼或重疊嗎？','相貼邊界與被遮住的部分，需要分開核對。',[
          ['separate','彼此分開'],['touching','會相貼，但要分開的邊界看得見'],['overlapping','有重疊，部分輪廓看不見']]),
        unit:q('unit','最後需要哪一種位置或尺寸？','照片上的距離與實際毫米，需要不同的核對條件。',[
          ['pixel','只要照片中的位置、對齊或像素距離'],['mm','需要實際毫米尺寸或孔距']]),
        plane:q('plane','要比較的位置都在同一個平面上嗎？','不同高度不能直接共用一個平面換算。',[
          ['planar','都在同一個平面'],['spatial','有不同高度，或需要立體位置']]),
        calibration:q('calibration','有尺寸基準或相機校正資料嗎？','有資料仍須用獨立已知尺寸檢查整套流程。',[
          ['ready','有已知長度、校正資料與取像條件'],['none','還沒有尺寸基準或校正資料']]),
        videoGoal:q('videoGoal','看影片主要想知道什麼？','畫面變化、逐件追蹤與整段動作，不能互相代替。',[
          ['change','畫面有沒有變化或物件進出'],['track','每件移到哪裡、跨線或停留多久'],['action','辨認整段操作或動作階段']]),
        camera:q('camera','拍影片時，相機會移動嗎？','相機移動本身也會造成畫面變化。',[
          ['fixed','相機固定'],['moving','相機會移動或晃動']]),
        timing:q('timing','影片結果需要多快交出？','已錄影片與現場提醒，接受的反應時間不同。',[
          ['offline','處理已錄好的影片'],['live','現場需要即時提醒']]),
        textGoal:q('textGoal','照片中的文字要怎麼使用？','逐字抄錄與自由回答問題，要採不同核對方法。',[
          ['transcribe','照原字抄錄，不能漏字或改字'],['fields','整理型號、批次等固定欄位'],['question','針對照片自由提問或描述內容']]),
        generationUse:q('generationUse','改善或產生的影像，要用在哪裡？','用途會決定需保留哪些原始證據，以及如何驗證。',[
          ['display','展示或製作示意圖片'],['reading','幫助人工閱讀現有照片'],['training','補充訓練資料'],['decision','用來判斷缺陷或量實際尺寸']])
      };
      function dataQuestion(t) {
        let choices;
        if(t==='count'||t==='defect') choices=[['normal','正常照片很多，問題照片很少'],['labeled','已有正常與問題照片，並整理每張正確答案'],['boxes','已在圖上圈出各物件或缺陷的位置'],['masks','已沿邊緣描出正確區域']];
        else if(t==='classify') choices=[['labeled','每類都有照片，並整理正確類別'],['boxes','已在圖上圈出每件，並記錄類別']];
        else if(t==='contour') choices=[['masks','已沿邊緣描出正確區域'],['boxes','只有方框位置，還沒描邊']];
        else if(t==='video') choices=[['video','已有原始影片與人工事件紀錄'],['clips','只有影片，還沒整理正確事件']];
        else choices=[['labeled','已有原始照片及人工核對的答案']];
        return q('data','目前準備了哪些現場資料？','參考或訓練用的資料，要與最後核對的測試資料分開。',[
          ...choices,['few','只有少量範例，還沒整理'],['none','還沒有可用的現場影像']]);
      }
      function valid(def, value) { return def.options.some(option=>option[0]===value); }
      function questions(answers={}) {
        const a=answers&&typeof answers==='object'?answers:{};
        const list=[task], t=valid(task,a.task)?a.task:'unknown';
        const add=(...ids)=>ids.forEach(id=>list.push(definitions[id]));
        if(t==='count') add('placement');
        if(t==='defect') add('defectKind','detail');
        if(t==='classify') add('classes','multiplicity');
        if(t==='contour') add('separation','overlap');
        if(t==='measure') {add('unit','plane');if(a.unit==='mm')add('calibration');}
        if(t==='video') {add('videoGoal');if(a.videoGoal==='change')add('camera');add('timing');}
        if(t==='text') add('textGoal');
        if(t==='generate') add('generationUse');
        if(['count','defect','classify','contour','measure','text'].includes(t))list.push(visibility);
        if(t!=='unknown'&&t!=='generate')list.push(dataQuestion(t));
        // Give callers fresh arrays so UI code cannot mutate future evaluations.
        return list.map(item=>({...item,options:item.options.map(option=>[...option])}));
      }
      function evaluate(answers={}) {
        const qs=questions(answers), a={};
        for(const item of qs)a[item.id]=valid(item,answers?.[item.id])?answers[item.id]:'unknown';
        const r={ruleId:'task-unknown',title:'先用一個現場例子確認工作目的',state:'仍有不同路徑',reasons:[],gaps:[],steps:[],experiment:[],courses:[]};
        const set=(id,title,steps,courses=[])=>{r.ruleId=id;r.title=title;r.steps=steps;r.courses=courses;};
        const gap=text=>{if(!r.gaps.includes(text))r.gaps.push(text);};
        r.reasons=qs.filter(item=>a[item.id]!=='unknown').map(item=>`${item.label}：${item.options.find(option=>option[0]===a[item.id])[1]}。`);
        for(const item of qs)if(a[item.id]==='unknown')gap(`待確認：${item.label} 可先拿一張現場照片，與實際覆核人員核對。`);
        r.experiment=['準備具代表性的現場資料，人工記錄正確答案，將參考與測試資料分開。','用同一批測試資料比較目前做法，記錄漏掉的問題、誤報與人工覆核量。'];
        if(a.task==='unknown') {
          r.steps=['例如：固定格位缺一件、表面有刮痕、抄錄銘牌，先選最像的工作。','先說清楚人工最後要核對什麼，再決定需要的資料與方法。'];
          r.experiment=['拿一個實際案例，請操作員說明目前如何判斷，以及最常花時間的步驟。'];
          return r;
        }
        if(a.task==='count') {
          if(a.placement==='fixed') set('count-fixed','先試對齊固定位置，再逐格檢查有無',[
            '固定取像與各格應有數量，先比較固定區域的有無核對規則；本站暫無專門的格位規則課程。','若格位有偏移，先對齊再檢查；規則不足時再與學習式方法比較。']);
          else if(a.placement==='free') set('count-free','先找出每一件，再核對數量',[
            '定義要找的產品與正確數量，先整理每件位置。','比較固定類別物件偵測，再核對漏件、重複框與計數規則。','下列偵測課程是同類輸出的工具例子，沒有依效能排名。'],['det-yolo-dense','det-rtdetr','det-dino-detector']);
          else set('count-unknown','先區分逐格核對與找每件再計數',['若位置固定，先試固定區域規則；若任意擺放，需先定位每件。']);
        }
        if(a.task==='defect') {
          if(a.detail==='boundary') {
            set('defect-boundary','先準備缺陷邊界，再比較分割流程',['沿真實缺陷邊緣整理核對資料；方框或整張正常／異常答案不能代替邊界。','比較區域分割與人工邊界；若要實際尺寸，另接校正與量測驗證。'],['u-net','segformer']);
            if(a.data!=='masks')gap('需要描出真實缺陷邊界，並另留獨立核對的缺陷樣本。');
            if(a.defectKind==='novel')gap('全新缺陷不一定被既有分割辨認；可另設異常篩查供人工回看，不把熱圖當精密輪廓。');
          } else if(a.defectKind==='novel'&&a.detail==='location') {
            set('defect-novel','先試正常參考的異常篩查',['整理正常品的允收變化，以正常參考找出值得回看的位置。','回到原圖核對可疑位置；異常分數不等於缺陷種類、精密輪廓或允收結論。'],['ad-patchcore','ad-padim']);
            gap('另留真實異常與正常變化的獨立測試資料；只有正常照片不能估計缺陷檢出率。');
          } else if(a.defectKind==='known'&&a.detail==='location') {
            set('defect-known','先定義已知缺陷，再比較定位流程',['整理各類缺陷與位置，分開訓練資料和獨立測試資料。','比較受監督缺陷定位；若只有整張答案，先補位置，不能直接假定能定位。'],['det-yolo-dense','det-rtdetr']);
            if(!['boxes','masks'].includes(a.data))gap('需要已知缺陷的位置核對資料；每張的正常／異常答案不足以直接訓練定位。');
          } else set('defect-unknown','先區分異常篩查與已知缺陷定位',['若要找新的可疑變化，探索正常參考異常篩查。','若要辨認已知缺陷，整理類別與位置；若要精密邊界，需另準備描邊資料。']);
        }
        if(a.task==='classify') {
          if(a.classes==='changing') set('classify-changing','先建立可更新的參考與候選搜尋',[
            '整理新品範例或搜尋詞，定義找到對象的人工核對方式。',a.multiplicity==='multiple'?'同圖有多件時，先找候選位置再核對類別。':'單件影像可先比對參考庫或文字候選；分數不是已驗證的產品判定。',
            '固定一組提示與參考資料比較；新品加入後重新核對，不宣稱零樣本就免資料。'],a.multiplicity==='multiple'?['det-grounding-dino-interface','yolo-world']:a.multiplicity==='single'?['clip','dinov2']:[]);
          else if(a.classes==='fixed'&&a.multiplicity==='single') set('classify-single','先建立固定類別的單件分類基準',['整理每類的不同背景與批次照片，另外定義未知產品如何交回人工。','比較整張單件影像的類別；分類不提供每件輪廓或立體姿態。'],['resnet','convnext']);
          else if(a.classes==='fixed'&&a.multiplicity==='multiple') set('classify-multiple','先定位每件，再辨認固定類別',['準備各件的位置與類別，可比較物件偵測或定位後分類的整套流程。','分別核對找不到物件與類別認錯，不能只看整張分類正確率。'],['det-yolo-dense','det-rtdetr']);
          else set('classify-unknown','先確認類別與單件／多件的判斷方式',['種類固定可建立分類基準；經常新增則另比較參考或文字搜尋。','單張多件需要先定位，不把整張分類當逐件結果。']);
          if(a.classes==='fixed'&&a.multiplicity==='single'&&!['labeled','boxes'].includes(a.data))gap('先整理每類正確答案與未知品案例，不能只憑模型名稱完成分類。');
        }
        if(a.task==='contour') {
          if(a.separation==='each') set('contour-each','先做每件分離，再核對逐件輪廓',['每件分別描出答案；整片前景區域不能當逐件輪廓。','比較實例分割，分別核對漏件、黏成一件及輪廓偏差。'],['yolo-seg']);
          else if(a.separation==='whole') set('contour-whole','先比較整體區域分割',['沿目標區域描出答案，再比較區域分割。','結果只表示區域類別，不保證同類物件能逐件分開。'],['u-net','segformer']);
          else set('contour-unknown','先確認要整體區域，還是每件獨立輪廓',['請人工圈一次預期結果；是否要分開每件，會改變資料與方法。']);
          if(a.data!=='masks')gap('需要與預期結果一致的描邊資料；只有方框不能直接當正確輪廓。');
          if(a.overlap==='touching')r.steps.push('另留相貼物件核對組，檢查是否合併成一件。');
          if(a.overlap==='overlapping')gap('被擋住的輪廓沒有直接影像證據；先確認只交可見輪廓，或改善取像。');
        }
        if(a.task==='measure') {
          if(a.unit==='mm') {
            set('measure-mm','先建立尺寸基準與校正，再驗證量測流程',['保留原圖，取得要量的位置；定位或分割只是取得位置的一個步驟。','核對尺寸基準、鏡頭與工作平面條件，再進行座標換算。','用未參與校正的已知尺寸重拍驗證，記錄誤差；像素不能直接當毫米。'],a.plane==='planar'?['charuco']:[]);
            if(a.calibration!=='ready')gap('先準備已知尺寸與相機校正資料；目前不能宣稱得到可靠毫米尺寸。');
            if(a.plane==='spatial')gap('不同高度需另外的幾何、深度或多視角方案，不能直接共用平面換算。');
          } else if(a.unit==='pixel') set('measure-pixel','先取得照片中的位置與對齊證據',['選清楚且可重複核對的特徵位置，保存原圖與獨立地標。','局部特徵、配對、幾何估計與細對位是可能的前後步驟，不是互斥排行榜。','只交像素位置或對齊結果；實際尺寸需要另走校正流程。'],['sift','lightglue','ecc']);
          else set('measure-unknown','先確認要影像位置，還是實際毫米尺寸',['像素定位與毫米量測的前提不同，請用一個要交付的數字或位置例子確認。']);
          r.experiment=['使用獨立地標或已知尺寸，測不同工作位置、重拍與重裝後的誤差。','保存原圖、校正或變換設定，以及取得位置到最終數字的完整流程。'];
        }
        if(a.task==='video') {
          if(a.videoGoal==='change') {
            set('video-change','先比較畫面變化的簡單基準',['先試影格差異或背景前景分離，核對真正事件與光照變化。','變化區域不提供產品類別、永久身分或完整動作理解。'],['frame-difference','background-subtraction']);
            if(a.camera==='moving')gap('相機移動也會產生差異；先固定相機或驗證穩定對齊，不能直接當物件事件。');
          } else if(a.videoGoal==='track') set('video-track','串接找物件、追蹤與事件規則',['先逐影格找出每件，再關聯相鄰影格的物件位置。','追蹤之後另設定跨線、停留或去重規則；追蹤器不能獨立取代偵測。','以下課程分別是偵測與追蹤步驟；編號不是永久實體身分。'],['det-yolo-dense','bytetrack']);
          else if(a.videoGoal==='action') set('video-action','先定義影片事件，再比較動作分析',['整理動作階段、時間範圍與正確答案，保留正常停頓等對照。','影片表示需接相應任務頭與驗證，不直接等於事件真值。'],['videomae','convlstm']);
          else set('video-unknown','先區分畫面變化、逐件追蹤或整段動作',['拿一段影片，標出希望系統提醒的時刻，以及需要附上的證據。']);
          if(a.data==='clips')gap('先人工記錄事件與時間，僅有影片還不足以判斷事件是否找對。');
          if(a.timing==='live')gap('先與現場確認可接受的反應時間與超時接手方式，再量完整流程，不能只憑模型名稱保證即時。');
          r.experiment=['另留完整影片，核對漏事件、誤事件、身分切換與反應時間。','固定影格取樣、時間窗與狀態重設方式，量完整流程延遲。'];
        }
        if(a.task==='text') {
          if(['transcribe','fields'].includes(a.textGoal))set('text-ocr','先建立文字辨識與逐字核對基準',['先找文字區域，再用 OCR 辨識原字；本站暫無專門 OCR 課程。',a.textGoal==='fields'?'將辨識文字對應固定欄位，逐欄比對原圖；格式正確不代表字值正確。':'逐字核對漏字、錯字與符號，不用合理的補字代替原字。','無法辨讀的文字標記待人工核對，保留原圖。']);
          else if(a.textGoal==='question')set('text-question','先限定影像問答範圍，再核對回答',['列出實際需要問的問題，對每題保存原圖證據與人工答案。','影像問答是候選回答，不等於逐字抄錄、精密定位或缺陷真值。'],['qwen-vl','llava','gemini-vision']);
          else set('text-unknown','先區分逐字抄錄與自由影像問答',['若每個字都要正確，先建立 OCR／欄位核對基準；若要描述內容，再比較影像問答。']);
          r.experiment=['準備不同反光、字體、角度與批次的原始照片，人工整理逐字或逐欄答案。','比較字元／欄位錯誤、漏讀與覆核工時，另外測試無法辨讀時能否正確交回人工。'];
        }
        if(a.task==='generate') {
          if(a.generationUse==='display')set('generate-display','先做展示用影像，核對內容與布局',['定義要展示的內容與條件，產出後人工核對。','生成圖是新內容，不是現場檢測或量測的原始證據。'],['controlnet','inpainting']);
          else if(a.generationUse==='reading')set('generate-reading','先保留原圖，再比較輔助閱讀效果',['先核對能否改善取像；復原或放大影像只能作輔助閱讀估計。','將處理圖與原圖並排，不把補出的細節當現場事實。'],['deblur','super-resolution']);
          else if(a.generationUse==='training')set('generate-training','先建立真實測試組，再試合成資料增補',['保存真實影像、合成設定與預定遮罩，人工核對合成內容。','比較加入合成資料前後，在同一真實獨立測試組的下游效果。'],['defectfill','anomalydiffusion']);
          else if(a.generationUse==='decision') {
            set('generate-decision','先保留原始證據，釐清檢測或量測需求',['請改從缺陷檢查或尺寸量測任務確認前提。','復原影像可能補出原圖沒有證據的細節，不能直接當成缺陷或尺寸真值。']);
            gap('需要可核對的原始現場影像與獨立真值；不能只用生成或復原結果驗收。');
          } else set('generate-unknown','先確認影像是展示、閱讀、補資料還是判定用途',['展示、輔助閱讀與檢測量測的證據要求不同，先確認使用方式。']);
          r.experiment=['保存原始資料與生成／處理設定，逐張核對內容及區域外變化。','若供下游工作使用，另用真實獨立資料比較效益，不以生成品質代替現場驗證。'];
          if(a.generationUse==='training')gap('先準備真實獨立測試資料，確認合成內容是否與現場問題一致。');
        }
        if(a.data==='none') {
          gap('還沒有可用的現場影像：先拍攝代表性資料，與覆核人員整理正確答案。');
          r.steps=['先拍攝代表性現場影像，請覆核人員整理正確答案，並分開參考與測試資料。',...r.steps.map(step=>`資料準備並核對後，再確認此方向：${step}`)];
          r.title='先收集現場影像，再確認方法';r.ruleId+='-no-data';r.courses=[];
        }
        if(a.visibility==='poor'||a.visibility==='occluded') {
          const reason=a.visibility==='poor'?'原圖反光或模糊，人工也難以判讀。':'目標被遮住，缺少直接可見的證據。';
          set('capture-first','先改善取像，再比較檢查方法',[
            '調整光線、焦距、角度或物件擺放，保留調整前後的同一目標照片。','請人工確認需要的邊緣、文字或物件確實可見，再重新走選型。','不要靠更大模型、零樣本或影像復原宣稱找回原本不可見的真值。']);
          gap(reason);r.experiment=['拍攝調整前後的對照照片，請實際覆核人員判讀同一目標。','保留仍不可見的案例，明定改拍或交回人工的流程。'];
        }
        if(a.visibility==='unknown')gap('先請人工確認原圖上的目標線索是否看得清；目前方法仍是有條件方向。');
        if(a.task==='count'&&a.placement==='free'&&!['boxes','masks'].includes(a.data))gap('先整理每件的位置與正確數量，才能核對偵測與計數流程。');
        if(a.task==='classify'&&a.multiplicity==='multiple'&&a.classes==='fixed'&&a.data!=='boxes')gap('先準備每件位置與類別；整張類別答案不足以驗證逐件辨認。');
        const rationale={
          'count-fixed':'位置已知，可以直接核對每格有無；先驗證簡單規則是否足夠。',
          'count-free':'位置不固定，必須先把每件找出來，才能檢查漏件或重複計數。',
          'defect-novel':'新的問題沒有完整類別可學，先用正常變化作參考篩查可疑處，再交人工核對。',
          'defect-known':'已知缺陷可整理類別與位置答案，因此能比較受監督的定位方法。',
          'defect-boundary':'精密邊界需要邊界答案來驗證；異常分數或方框都不能代替描邊。',
          'classify-single':'每張只看一件且種類固定，可以先直接比較單件分類。',
          'classify-multiple':'同圖有多件，整張類別無法說明每件是什麼，因此需要定位步驟。',
          'classify-changing':'新品持續加入，參考與搜尋條件也必須可更新，不能只沿用固定類別答案。',
          'contour-each':'每件都要獨立輪廓，必須區分個體；同類前景合成一區不符合需求。',
          'contour-whole':'只需整體區域時，可先驗證區域分割，不必額外推導每件身分。',
          'measure-mm':'實際尺寸依賴尺度與幾何條件，影像中的位置本身不包含毫米換算。',
          'measure-pixel':'交付是照片中的位置，因此先驗證定位與對齊誤差。',
          'text-ocr':'要求保留原字或固定欄位，需要逐字核對；自由描述無法代替抄錄正確性。',
          'video-track':'軌跡與事件需要跨影格關聯，單張偵測還不足以知道是否同一件。',
          'capture-first':'原圖缺少可核對線索時，模型結果也缺少可靠的現場驗證依據。'
        };
        if(rationale[r.ruleId])r.reasons.unshift(rationale[r.ruleId]);
        r.state=r.gaps.length?'先補必要條件':'可開始規劃比較';
        if(r.ruleId.endsWith('-unknown')||r.ruleId==='task-unknown')r.state='仍有不同路徑';
        return r;
      }
      return {questions,evaluate};
    })();
