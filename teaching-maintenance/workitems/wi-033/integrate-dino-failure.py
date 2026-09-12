from pathlib import Path
import json,shutil
W=Path(__file__).resolve().parent;C=W.parents[1]
tpath=C/'_course_content/topics/dinov3.json';t=json.loads(tpath.read_text(encoding='utf-8'));r=next(r for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')) if r['id']=='dinov3-main-failure')
urls=[]
for mode in ['desktop','mobile']:
 src=W/f"{r['id']}-{r['version']}-{mode}.png";dest=C/f"_course_content/generated-concepts/dinov3/wi033-failure-{r['version']}-{mode}.png";shutil.copyfile(src,dest);urls.append(dest.relative_to(C).as_posix())
v=t['beginner_path']['visuals'][1];v.update(image=urls[0],alt=r['title']+'。'+r['takeaway']+' 原生SVG教學示意，非模型實測。')
rv=v['reading_views'][0];rv.update(image=urls[0],mobile_image=urls[1],mobile_crop=[0,0,768,2304],mobile_intrinsic_width=768,mobile_intrinsic_height=2304,alt=v['alt'])
tpath.write_text(json.dumps(t,ensure_ascii=False,indent=2),encoding='utf-8')
