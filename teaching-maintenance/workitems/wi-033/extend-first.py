from pathlib import Path
import json,runpy
W=Path(__file__).resolve().parent
ns=runpy.run_path(str(W/'plan-first-semantics.py'));rows=ns['rows'];add=ns['add']
for r in rows:
 if r['id']=='dinov3-engineering-4':
  r.update(version='r02',kind='D',title='DINOv3：以工作結果決定是否換骨幹',takeaway='同題比較效果與重建代價，保留基準也合理。',panels=[dict(title='同一批正常與缺口件',graphic='dino-comparison-data'),dict(title='既有骨幹：保留相容基準',graphic='dino-compare-v2'),dict(title='新骨幹：重建後再比較',graphic='dino-compare-v3')],detail='工程4不重複主反例。固定同一批正常與缺口墊圈及取像，各自使用相容骨幹與參考表示；記錄下游漏檢/誤報、抽特徵/查庫時間與重建負擔。新骨幹訓練機制不同，不代表每項域內指標一定進步。')
diff=ns['diff'];gpt=ns['gpt']
add('ad-diffad',1,'DiffusionAD：去噪與定位要分別學','正常資料教恢復，合成異常和遮罩教定位。',[
 ('正常影像加噪聲練恢復','diff-normal-training'),('合成異常有已知位置','diff-synthetic'),('兩個網路各有訓練責任','diff-training-targets')],
 '正常圖用於學習噪聲估計及恢復；合成異常與已知遮罩提供分割監督。兩個網路不能只用一張異常熱圖概括。合成資料仍需覆盖任務變化，最後以未見正常與真缺陷驗證。',diff)
add('ad-diffad',3,'DiffusionAD：要交付最後的位置結果','保存 A／R／位置圖，連同完整耗時一起驗收。',[
 ('把恢復前後成對保存','diff-save-pair'),('位置圖映回原圖覆核','diff-output'),('計入兩尺度與分割時間','diff-time')],
 '保存原圖A、恢復R與分割位置圖能追查恢復或定位失敗。位置圖須映回原始影像座標，配合域內門檻及覆核；延遲包含兩尺度估計、分割和前後處理，不能由單步估計直接宣稱整套最快。',diff)
add('ad-diffad',4,'DiffusionAD：恢復變乾淨不等於漏檢','檢查最後位置圖，分清恢復成功與定位失敗。',[
 ('共同原圖：支架有刮痕','diff-defect-input'),('恢復乾淨，分割仍可定位','diff-clean-detected'),('恢復保留刮痕，另查漏檢','diff-retained-missed')],
 '固定同一刮痕影像，比較恢復是否去除異常及最後分割是否找到位置。去掉異常本來就是恢復子任務的方向，不直接等於漏檢；缺陷留在R也不必然漏，但會改變可用線索。兩條示意結果需以真實留出集驗證。',diff,kind='D')
add('ad-anomalygpt',1,'AnomalyGPT：用成對資料學定位與回答','合成影像、遮罩與文字要描述同一處异常。',[
 ('影像異常與遮罩對齊','diff-synthetic'),('文字描述同一位置與外觀','gpt-training-text'),('更新解碼器與提示學習器','gpt-training-targets')],
 '用合成異常影像、位置遮罩及文字配對訓練；預訓練影像編碼器和LLM保持固定，更新影像解碼器及提示學習器。遮罩和描述須對上同一異常，否則不同監督互相矛盾；真實未見缺陷仍需獨立驗證。',gpt)
add('ad-anomalygpt',3,'AnomalyGPT：文字與位置一起交付','回答、位置和原圖一起覆核，對不上就保留疑問。',[
 ('保留同一影像的定位','gpt-localize'),('問題與位置提示參與回答','gpt-prompt'),('核對文字是否有原圖證據','gpt-review')],
 '交付原圖、內建定位與對話記錄，逐項核對文字描述的部位和異常類型。對話可協助判讀但不能替代定位驗證；若回答與圖不一致，保留失敗狀態並回原圖。額外外部檢測器是應用整合選擇，不是原模型必需支路。',gpt)
add('ad-anomalygpt',4,'AnomalyGPT：會回答不代表會判對','同圖比較定位與文字證據，再量覆核成本。',[
 ('共同原圖：刮痕在中部','diff-defect-input'),('位置在中部，文字卻說孔邊','gpt-mismatch'),('帶對話是否真能減少工時','gpt-work-comparison')],
 '同一支架若位置圖指中部，回答卻描述孔邊，不能因語句流暢就放行。以同一批真缺陷與正常圖比較只看位置或加問答的錯誤、延遲和人工覆核时间；沒有收益時保留簡單流程也合理。',gpt,kind='D')
(W/'engineering-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n## 第一批其餘四課 checkpoint\n\nPose四工程已原生實看與記分後整合；首次建置被每圖需兩個名詞的來源契約攔下，補入R/t及重投影定義後重建。舊HTML未被失敗的來源建置覆寫；新增build.py讓來源建置失敗時不再繼續bundle。DINOv3主反例与工程4曾重複，工程4改同題換骨幹取捨；DiffusionAD/AnomalyGPT r02核心原型原生實看通過，將延伸各自其他三工程。尚未宣稱這四課完成；第二部分仍2/52。\n')
runpy.run_path(str(W/'plan-first-semantics.py'))
