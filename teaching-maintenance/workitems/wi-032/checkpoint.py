from pathlib import Path
import json
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
msg='''WI-032最新checkpoint：Overall_Review.md已列第一部分6課、第二部分52課與學習；6課完整正文／自測草稿已保存lesson-content.json，15檔基準與14組主線brief已保存。ECC核心桌機手機、DINO核心、YOLO-World核心等候選已生成實看；ChArUco兩次生成角點失敗後改精確SVG，r05已產出待頁內核對。SIFT/LightGlue點位與ECC反例仍在修正，不把候選當完成。其餘反例／比較正在製作，工程4圖尚待重建；尚未整合教材，測試未跑，未發布，user approval pending。下一步完成主線候選與精確幾何修正，再重建工程層、整合和實頁驗收。產物在workitems/wi-032，詳細原生審查見prototype-review.md。'''
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:
 s=p.read_text(encoding='utf-8')
 s=s.replace('- 狀態：文件前置完成，未生成／整合／驗證；使用者成品核准pending。WI-031審查已完成，舊checkpoint保留歷史。','- '+msg)
 p.write_text(s,encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n'+msg+'\n')
p=R/'Overall_Review.md';s=p.read_text(encoding='utf-8').replace('待製作／WI-032進行中','候選製作中／尚未整合')
if '### 第一部分製作checkpoint' not in s:s+='\n### 第一部分製作checkpoint\n\n'+msg+'\n'
p.write_text(s,encoding='utf-8')
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf-8') as f:
 f.write('''\n### WI-032 原型階段校正\nChArUco兩版生成的同角點與棋盤格位不一致，已依G6改原生SVG幾何再輸出PNG，同一板座標決定所有A位置；保留失敗稿不啟用。SIFT／LightGlue點位跨圖漂移、ECC反例整件與局部不符亦重開修正。這些是WI-031既有身份不變量規則的實際執行，不新增審美偏好；prototype-review.md保留各版證據。完整六課尚未整合或驗收。\n''')
print('Checkpoint saved; production remains incomplete')
