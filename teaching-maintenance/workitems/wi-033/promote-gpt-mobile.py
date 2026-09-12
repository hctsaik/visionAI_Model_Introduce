from pathlib import Path
import json,hashlib,shutil
W=Path(__file__).resolve().parent;C=W.parents[1]
plan=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
tp=C/'_course_content/topics/ad-anomalygpt.json';t=json.loads(tp.read_text(encoding='utf-8'));reviews=[]
notes=[['同板兩孔和右側痕跡身份保持','訓練、內建定位、位置轉提示三責任完整','影像與問題另接LLM，回原圖核對','手機三段字量減少，仍需捲動','原生SVG示意，無模型實測宣稱'],['p細痕與q正常孔邊在三段一致','錯定位和無據根因分清','觀察、推測、未知各有下一步','錯誤框與原圖並列，不需找小人物','假設錯答明示，非真實推論'],['三方法固定同件與位置問題','人工視窗、學提示、定位對話三種機制分清','先驗位置再驗對話成本，正文固定條件','三段各只留一種方法，標頭與黃結論清楚','位置圖為示意，不把相同色塊當同精度']]
for i,kind in enumerate(['core','failure','comparison']):
 r=next(r for r in plan if r['id']==f'anomalygpt-mobile-{kind}');src=W/f"{r['id']}-{r['version']}-mobile.png"
 dest=C/f"_course_content/generated-concepts/ad-anomalygpt/wi033-{kind}-{r['version']}-mobile.png";dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
 rv=t['beginner_path']['visuals'][i]['reading_views'][0];rv.update(mobile_image=dest.relative_to(C).as_posix(),mobile_crop=[0,0,768,2304],mobile_intrinsic_width=768,mobile_intrinsic_height=2304,alt=r['title']+'。'+r['takeaway']+' 手機為原生SVG教學示意，非模型實測。')
 scores=[23,24,19,18,9]
 reviews.append(dict(id=r['id'],image=src.name,active_path=dest.relative_to(C).as_posix(),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),scores=scores,total=sum(scores),evidence=notes[i],completion={'aesthetics':[8,'既有桌機與新手機風格不同'],'completeness':[9,'三段完整承接正文'],'professionalism':[9,notes[i][1]],'density':[8,'字量下降，三段長捲動'],'hierarchy':[9,'藍標頭與單一黃結論']},veto=[],native_review='passed',page_review='pending',user_approval='pending'))
 brief=W/f"{r['id']}-{r['version']}.md";s=brief.read_text(encoding='utf-8').replace('金屬支架／齒輪／軸承','對角兩孔金屬板、同位置細痕').replace('手機768×2400','手機768×2304');brief.write_text(s,encoding='utf-8')
t['comparison']=[dict(model='AnomalyGPT',normality='合成影像、遮罩與文字訓練；局部解碼與狀態文字匹配，位置再轉提示',candidate='內建異常位置與對話回答，兩者均回原圖核對'),dict(model='AnomalyCLIP',normality='輔助資料學習物件無關的正常／異常提示，與CLIP表示匹配',candidate='異常分數與位置圖；目標產品另驗適用範圍'),dict(model='WinCLIP',normality='人工狀態文字與視窗／patch／整圖聚合；WinCLIP+可加正常參考',candidate='異常分數與位置圖；同條件比較漏檢、誤報與成本')]
tp.write_text(json.dumps(t,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'gpt-mobile-image-assessment.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2),encoding='utf-8')
mp=C/'roadmap-model-selection/anomaly-detection/ad-anomalygpt/model.md';s=mp.read_text(encoding='utf-8');a=s.index('## Model identity');b=s.index('## Sources',a)
s=s[:a]+'''## Model identity

AnomalyGPT is the industrial anomaly localization and dialogue model in the 2023 paper / AAAI 2024 publication. The image encoder and LLM are frozen; synthetic anomaly images, masks and paired text train the image decoder and prompt learner. Anomaly localization is an internal model capability, not a required external specialist input.

## Architecture path

### Build

Align synthetic anomaly pixels, masks and location descriptions. Train the lightweight image decoder and prompt learner with localization and text supervision while keeping the image encoder and LLM fixed. Keep independent normal and real-defect validation examples. Version image preprocessing, frozen checkpoints, decoder and prompt weights, training data and generation settings.

### Inference

The test image encoder provides global and local representations. The image decoder maps local features for matching with normal/anomalous text representations, producing the internal location map. The prompt learner converts location information into prompts; the LLM receives those prompts together with the image representation and user question to generate a response. The few-shot extension may additionally use normal reference feature matching.

Save the original image, location map, question and response together. Review location and language against the original. Measure preprocessing, encoding, localization, prompt processing and text generation when reporting latency. External retrieval, SOP lookup or a separate specialist model are optional application extensions and must not be presented as the paper's mandatory inference path.

## Representation and score

- Local representation: decoded image features matched with normal/anomalous text features.
- Output: an anomaly location map and natural-language answer. A structured evidence/uncertainty record may be added by the application; it is not a guaranteed native output schema.
- Validation: measure localization and normal/defect errors separately from unsupported language, region-text disagreement, latency and human review time.

## Failure boundary

- Synthetic training patterns may not cover real defects. Validate on unseen real anomalies and acceptable normal variation.
- Tiny defects may disappear during acquisition or preprocessing. Inspect the original and effective input resolution.
- Location and text can disagree. A confident root-cause statement does not establish depth, mechanism or acceptability.
- Updated weights, prompts, token generation settings or normal references require renewed checks of affected outputs.

## Selection gate

Compare WinCLIP, AnomalyCLIP and AnomalyGPT on the same images, image resolution, required defect sensitivity and hardware. First compare localization errors; then determine whether dialogue reduces review time enough to justify language errors and generation cost. WinCLIP and AnomalyCLIP do not natively provide the same dialogue output. Do not describe all three as external-evidence assistants.

## Visual primitives

- `training_pairs`: synthetic image, same-location mask and text; frozen backbone/LLM versus trained decoder/prompt learner.
- `internal_localization`: image -> local features -> image decoder -> normal/anomaly text matching -> location map.
- `location_guided_dialogue`: map -> prompt learner -> LLM, with image representation and question entering separately.
- `evidence_review`: same original image, proposed location and answer; observed versus inferred versus unknown.
- `selection`: common localization task first, additional dialogue benefit and cost second.

'''+s[b:];mp.write_text(s,encoding='utf-8')
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('\nAnomalyGPT手機三圖r01已逐張原生實看：三段核心、同p/q反例與共同工件比較，無字形/箭頭重疊；各93，頁內待驗。同步修正raw comparison與model.md舊工程契約：外部specialist、retrieval與structured schema只能是可選應用擴充，不能覆蓋內建定位→提示→回答的機制。\n')
with (W/'sources.md').open('a',encoding='utf-8') as f:f.write('\n手機比較核對：WinCLIP https://arxiv.org/abs/2303.14814 的狀態文字/視窗聚合及WinCLIP+正常參考；AnomalyCLIP https://arxiv.org/abs/2310.18961 的輔助資料與物件無關提示。已讀原論文摘要，沒有使用paper數值替本課評分。\n')
