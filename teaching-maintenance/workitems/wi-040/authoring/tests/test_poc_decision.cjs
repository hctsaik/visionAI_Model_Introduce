const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(root, '_course_content/poc-decision.js'), 'utf8');
const context = vm.createContext({});
vm.runInContext(source + '\nthis.decision = POC_DECISION;', context);
// Normalize values from the sandbox for strict object comparisons.
const evaluate = a => JSON.parse(JSON.stringify(context.decision.evaluate(a)));
const questions = a => JSON.parse(JSON.stringify(context.decision.questions(a)));
const text = r => [r.title, ...r.steps, ...r.gaps, ...r.experiment].join('\n');
const fixtures = {
  anomaly:{task:'defect',defectKind:'novel',detail:'location',visibility:'clear',data:'normal'},
  count:{task:'count',placement:'fixed',visibility:'clear',data:'normal'},
  contours:{task:'contour',separation:'each',overlap:'touching',visibility:'clear',data:'masks'},
  measure:{task:'measure',unit:'mm',plane:'planar',calibration:'none',visibility:'clear',data:'few'},
  text:{task:'text',textGoal:'transcribe',visibility:'clear',data:'few'},
};

test('normal-only anomaly route asks for real independent anomalies, not promised detection rate', () => {
  const result = evaluate(fixtures.anomaly);
  assert.equal(result.ruleId, 'defect-novel');
  assert.match(result.title, /正常參考/);
  assert.match(text(result), /只有正常照片不能估計缺陷檢出率/);
  assert.equal(result.state, '先補必要條件');
  assert.match(text(result), /不等於缺陷種類、精密輪廓/);
});

test('fixed slots use a rule baseline; changing placement changes route and data requirements', () => {
  const fixed = evaluate(fixtures.count);
  const free = evaluate({...fixtures.count, placement:'free'});
  assert.equal(fixed.ruleId, 'count-fixed');
  assert.deepEqual(fixed.courses, []);
  assert.match(text(fixed), /固定區域/);
  assert.equal(free.ruleId, 'count-free');
  assert.match(text(free), /每件的位置與正確數量/);
  assert.notEqual(fixed.title, free.title);
});

test('touching instances remain different from whole-region segmentation', () => {
  const each = evaluate(fixtures.contours);
  const whole = evaluate({...fixtures.contours,separation:'whole'});
  assert.equal(each.ruleId, 'contour-each');
  assert.deepEqual(each.courses, ['yolo-seg']);
  assert.match(text(each), /整片前景區域不能當逐件輪廓/);
  assert.match(text(each), /相貼物件核對組/);
  assert.equal(whole.ruleId, 'contour-whole');
  assert.notDeepEqual(each.courses, whole.courses);
});

test('millimetres without calibration cannot be presented as ready measurement', () => {
  const result = evaluate(fixtures.measure);
  assert.equal(result.ruleId, 'measure-mm');
  assert.equal(result.state, '先補必要條件');
  assert.match(text(result), /目前不能宣稱得到可靠毫米尺寸/);
  assert.match(text(result), /未參與校正的已知尺寸/);
  const pixel = evaluate({...fixtures.measure,unit:'pixel'});
  assert.equal(pixel.ruleId, 'measure-pixel');
  assert.ok(!questions({...fixtures.measure,unit:'pixel'}).some(q=>q.id==='calibration'));
  assert.ok(!pixel.gaps.some(s=>s.includes('目前不能宣稱')));
});

test('transcription uses OCR even when no corresponding course exists', () => {
  const result = evaluate(fixtures.text);
  assert.equal(result.ruleId, 'text-ocr');
  assert.deepEqual(result.courses, []);
  assert.match(text(result), /本站暫無專門 OCR 課程/);
  assert.match(text(result), /不用合理的補字代替原字/);
  assert.equal(evaluate({...fixtures.text,textGoal:'question'}).ruleId, 'text-question');
});

test('poor visibility and occlusion take priority over model suggestions', () => {
  for (const visibility of ['poor','occluded']) {
    const result = evaluate({...fixtures.anomaly,visibility});
    assert.equal(result.ruleId, 'capture-first');
    assert.deepEqual(result.courses, []);
    assert.equal(result.state, '先補必要條件');
    assert.match(text(result), /先改善取像/);
  }
});

test('unknown visibility never counts as a usable image', () => {
  const result = evaluate({...fixtures.count,visibility:'unknown'});
  assert.equal(result.state,'先補必要條件');
  assert.match(result.gaps.join(' '),/看得清/);
});

test('missing photos produce a collection action without model cards', () => {
  const result = evaluate({...fixtures.count,placement:'free',data:'none'});
  assert.match(result.ruleId, /no-data$/);
  assert.match(result.title, /先收集現場影像/);
  assert.match(result.steps[0], /先拍攝/);
  assert.match(result.steps[1], /資料準備並核對後/);
  assert.deepEqual(result.courses, []);
  assert.equal(result.state, '先補必要條件');
});

test('unknown data, stale model and invalid answers cannot silently choose a route', () => {
  assert.deepEqual(evaluate({task:'unknown',model:'ad-patchcore'}).courses, []);
  assert.equal(evaluate({task:'not-a-task'}).ruleId, 'task-unknown');
  const unknown = evaluate({...fixtures.count,data:'not-a-value'});
  assert.equal(unknown.state,'先補必要條件');
  assert.match(unknown.gaps.join(' '), /哪些現場資料/);
  assert.deepEqual(evaluate({...fixtures.count,model:'yolo-world'}),evaluate(fixtures.count));
});

test('generation for display does not ask irrelevant image visibility or training data', () => {
  const answers = {task:'generate',generationUse:'display'};
  assert.deepEqual(questions(answers).map(q=>q.id), ['task','generationUse']);
  const result = evaluate(answers);
  assert.equal(result.ruleId,'generate-display');
  assert.match(text(result), /不是現場檢測或量測的原始證據/);
  const decision = evaluate({...answers,generationUse:'decision'});
  assert.equal(decision.state,'先補必要條件');
  assert.deepEqual(decision.courses, []);
});

test('video tracking identifies pipeline dependencies rather than interchangeable models', () => {
  const result = evaluate({task:'video',videoGoal:'track',timing:'offline',data:'video'});
  assert.equal(result.ruleId,'video-track');
  assert.match(text(result),/追蹤器不能獨立取代偵測/);
  assert.match(text(result),/偵測與追蹤步驟/);
  const moving = evaluate({task:'video',videoGoal:'change',camera:'moving',data:'video'});
  assert.equal(moving.state,'先補必要條件');
  assert.match(moving.gaps.join(' '),/相機移動/);
  const live = evaluate({task:'video',videoGoal:'track',timing:'live',data:'video'});
  assert.equal(live.state,'先補必要條件');
  assert.match(live.gaps.join(' '),/可接受的反應時間/);
  assert.match(live.experiment.join(' '),/完整流程延遲/);
});

test('stale branch answers do not change results or remain active questions', () => {
  const current = {task:'video',videoGoal:'track',data:'video'};
  assert.deepEqual(evaluate(current),evaluate({...current,camera:'moving',calibration:'none',visibility:'poor'}));
  assert.ok(!questions(current).some(q=>q.id==='camera'));
});

test('all tasks offer unknown, produce a consistent result, and reference existing courses', () => {
  const topics = JSON.parse(fs.readFileSync(path.join(root,'_course_content/learner-briefs.json'),'utf8'));
  for (const [task] of questions({})[0].options) {
    const qs = questions({task});
    assert.equal(new Set(qs.map(q=>q.id)).size,qs.length);
    for (const q of qs) {
      assert.ok(q.options.some(([value])=>value==='unknown'));
      assert.equal(new Set(q.options.map(([value])=>value)).size,q.options.length);
    }
    const result = evaluate({task});
    assert.deepEqual(Object.keys(result),['ruleId','title','state','reasons','gaps','steps','experiment','courses']);
    assert.notEqual(result.state,'可開始規劃比較');
  }
  for (const fixture of Object.values(fixtures)) {
    for (const id of evaluate(fixture).courses)assert.ok(topics[id],id);
  }
});

test('questions and evaluations do not mutate caller answers or shared definitions', () => {
  const answers = Object.freeze({...fixtures.count});
  assert.doesNotThrow(()=>evaluate(answers));
  const list=context.decision.questions(answers);
  list[0].options[0][1]='mutated';
  list[0].label='mutated';
  assert.notEqual(questions(answers)[0].label,'mutated');
  assert.notEqual(questions(answers)[0].options[0][1],'mutated');
});

test('every reachable complete answer path references real courses and preserves unmet prerequisites', () => {
  const topics = JSON.parse(fs.readFileSync(path.join(root,'_course_content/learner-briefs.json'),'utf8'));
  let paths = 0;
  function visit(answers) {
    const next = questions(answers).find(q=>!Object.hasOwn(answers,q.id));
    if(next) {
      for(const [value] of next.options)visit({...answers,[next.id]:value});
      return;
    }
    paths++;
    const result=evaluate(answers);
    for(const id of result.courses)assert.ok(topics[id],`Unknown course ${id}`);
    assert.ok(result.steps.length>0,JSON.stringify(answers));
    assert.ok(result.experiment.length>0,JSON.stringify(answers));
    if(Object.values(answers).includes('unknown')||answers.data==='none') {
      assert.notEqual(result.state,'可開始規劃比較',JSON.stringify(answers));
    }
    if(answers.data==='none'||['poor','occluded'].includes(answers.visibility)) {
      assert.deepEqual(result.courses,[],JSON.stringify(answers));
    }
  }
  visit({});
  assert.ok(paths>1000,`Only exercised ${paths} paths`);
});
