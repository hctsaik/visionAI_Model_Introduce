from pathlib import Path
import json,shutil,hashlib
W=Path(__file__).resolve().parent;C=W.parents[1]
p=W/'siglip-core-mobile-r02-mobile.png'
# Only run after native PNG inspection. Page review remains pending.
review=dict(id='siglip-core-mobile',image=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scores=[23,24,19,17,9],total=92,evidence=['支架齒輪身份与2×2配對一致','正負對角正確，共享更新与部署分开','候選排名接工作驗證，不生成回答','手機三段較原有四段密圖可讀，仍需長捲動','新SVG示意，未冒充模型實測'],completion={'aesthetics':[8,'藍頭與單一黃結論'],'completeness':[9,'配對、損失、部署三段俱全'],'professionalism':[9,'訓練標籤不送部署'],'density':[8,'刪去重複編碼器，詳圖另有工程2'],'hierarchy':[9,'同一縱向閱讀路徑']},veto=[],native_review='passed',page_review='pending',user_approval='pending')
(W/'siglip-core-assessment.json').write_text(json.dumps([review],ensure_ascii=False,indent=2),encoding='utf-8')
dest=C/'_course_content/generated-concepts/siglip/wi033-core-r02-mobile.png';shutil.copyfile(p,dest)
tp=C/'_course_content/topics/siglip.json';t=json.loads(tp.read_text(encoding='utf-8'));rv=t['beginner_path']['visuals'][0]['reading_views'][0]
rv.update(mobile_image=dest.relative_to(C).as_posix(),mobile_crop=[0,0,768,2304],mobile_intrinsic_width=768,mobile_intrinsic_height=2304,alt='SigLIP逐對學習与部署比較。桌機為既有生成示意，手機為新SVG示意；均非模型實測。')
tp.write_text(json.dumps(t,ensure_ascii=False,indent=2),encoding='utf-8')
