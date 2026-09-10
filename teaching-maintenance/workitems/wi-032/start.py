from pathlib import Path
import json,shutil,hashlib
W=Path(__file__).resolve().parent; C=W.parents[1]; R=C.parents[1]
rows=json.loads((C/'workitems/wi-031/results.json').read_text(encoding='utf-8'))
first=[r for r in rows if r['classification']=='需要重建']; second=[r for r in rows if r['classification']=='局部修正']
assert len(first)==6 and len(second)==52
p=R/'Overall_Review.md'
assert not p.exists(),'Do not overwrite existing plan'
s='''# Overall Review：58課重建與修正總計畫

建立日期：2026-09-11。依據[WI-031完整審查](teaching-images/vision-ai-model-selection/workitems/wi-031/REPORT.md)。

本輪授權：先保存本計畫與學習，再執行第一部分六課重建。第二部分52課先記錄待辦，未開始製作。本機實作、圖像生成、頁面整合及必要驗證屬第一部分；發布狀態與使用者成品核准分開紀錄。

狀態：計畫已建立，第一部分進行中。具體製作與驗證checklist唯一入口：[WI-032 PLAN](teaching-images/vision-ai-model-selection/workitems/wi-032/PLAN.md)。

## 第一部分：6課主線重建（本輪執行）

重建核心圖、反例、比較、文字、自測、操作交付與桌機／手機閱讀；一併處理這六課已審出的工程圖缺口，使首讀與展開層不互相矛盾。保留有來源且有效的既有實測，例如ECC工程4案例。新圖不冒充模型實測。

| 課程 | 保留證據 | 重建範圍 | 狀態 |
| --- | --- | --- | --- |
'''
for r in first:s+=f"| {r['model']} | {r['keep']} | {r['fix']} | 待製作／WI-032進行中 |\n"
s+='''
完成條件：每課啟用來源及course/docs引用更新；逐圖實看、固定v1.0量表分項與實質缺口驗收；桌機手機可讀，放大、自測、導覽與文件連結通過；必要回歸與資產一致驗證；實作、自評、測試、使用者核准分開。

## 第二部分：52課局部修正（已記錄，尚未執行）

保留已成立的主線，逐課修正舊工程图、語意錯接、指定深讀圖與手機排版。先處理會教錯的內容，再處理機制不明與閱讀負擔；不是把52課全部推倒。

| 課程 | 保留主線 | 待修範圍 | 狀態 |
| --- | --- | --- | --- |
'''
for r in second:s+=f"| {r['model']} | {r['keep']} | {r['fix']} | 待執行 |\n"
s+='''
第二部分優先項：CLIP／SigLIP並行編碼器、Pose替代方法分支、DINOv3訓練／推論、DiffusionAD恢復與檢測、AnomalyGPT內建定位、LK／RAFT同條件比較、AnomalyDINO深讀旋轉圖與EfficientAD深讀輸出關係。其餘依家族重畫受影響工程圖、修公式缺字及手機小字／橫滑。

## 這輪學習與下一輪驗證

| 審查學習 | 已保存位置 | 本輪如何落實 |
| --- | --- | --- |
| 首讀完成不代表展開層全課符合 | TEACHING_WEBPAGE_GUIDE.md WI-031 | 六課連工程層一起檢查；依實際啟用圖判定 |
| 換標籤和同款熱點不能解釋不同模型 | IMAGE_STYLE_GUIDE.md WI-031 | 用匹配點、位移／殘差、框、參數等各自正確輸出 |
| 箭頭代表真實資料關係，替代方案不能串接 | IMAGE_STYLE_GUIDE.md WI-030／031 | 逐線查來源／目的，比較採同輸入分支 |
| 同案例與同條件才支持比較 | IMAGE_STYLE_GUIDE.md WI-031 | 工件身份、方向與缺陷位置固定；反例只變宣告條件 |
| 小圖大留白不能靠加大畫布修復 | IMAGE_STYLE_GUIDE.md WI-031 | 放大有效機制區，360px重新排版並實看 |
| 截圖異常先重查，不把時序當網站故障 | TEACHING_WEBPAGE_GUIDE.md WI-031 | SVG等待繪製、排除sticky遮蓋；疑似圖說遮字量測字形 |
| 缺口分類不等於逐張數字評分或使用者批准 | TEACHING_REVIEW_LOG.md WI-031 | 新成圖逐項附證據，保留失敗稿與pending核准 |

審查原始證據與誤判撤回保存在WI-031/observations.md；共用學習已回寫三份權威Markdown，本次製作前再記錄觀察→變更→驗證到共用log。後續每個可驗證步驟更新WI-032 checkpoint，再同步本總計畫的課程狀態；未通過的項目不打勾。
'''
p.write_text(s,encoding='utf-8')
plan='''# WI-032 第一部分：六課重建

- 目標：執行Overall_Review.md第一部分，重建ChArUco／ECC／SIFT／LightGlue／DINO detector／YOLO-World主線及其受影響工程圖。
- 授權：使用者明確要求先記錄兩部分與本輪學習，再執行第一部分。第二部分52課待辦不啟動。完成本機生成、整合與驗證；使用者成品核准pending。
- 規格：五份權威Markdown、量表v1.0與teaching-review-cycle G0–G6；保留有效實測，不把新示意當真實推論。
- 基準：WI-031 baseline與本工作item/baseline；開始製作前核對當前來源。
- 下一步：讀完適用權威與實看認可參考，為6課建立versioned preflight，先做一張代表核心原型再擴展。

## Checklist
- [x] 建立根Overall_Review.md，列6課及52課全部範圍。
- [x] 保存本輪審查學習與下次驗證方式。
- [ ] 保存6課來源基準、核對權威與第一手技術來源。
- [ ] 逐圖brief／preflight通過，完成代表原型實圖審查。
- [ ] ChArUco圖文、自測、工程層重建及實圖檢查。
- [ ] ECC圖文、自測、工程層重建及實圖檢查。
- [ ] SIFT圖文、自測、工程層重建及實圖檢查。
- [ ] LightGlue圖文、自測、工程層重建及實圖檢查。
- [ ] DINO detector圖文、自測、工程層重建及實圖檢查。
- [ ] YOLO-World圖文、自測、工程層重建及實圖檢查。
- [ ] course/docs整合、6課桌機手機、放大／自測／導覽／文件連結與相關回歸。
- [ ] 各圖及整頁分項證據、hash核對、學習回寫與總計畫狀態更新。

## Checkpoint
2026-09-11：計畫與學習已落盤，正在讀製作規則及準備原型；未生成，未整合，測試未跑。成品自評未評、使用者核准pending。無已知阻礙。
'''
(W/'PLAN.md').write_text(plan,encoding='utf-8')
checkpoint='''## WI-032 進行中：Overall Review第一部分六課重建
- 總計畫：根Overall_Review.md已建立，兩部分共58課與學習已記錄。
- 授權：製作第一部分6課主線及受影響工程圖；第二部分52課維持待辦。
- 接續：teaching-images/vision-ai-model-selection/workitems/wi-032/PLAN.md為唯一細項。下一步保存基準、實看參考、製作preflight與單圖原型。
- 狀態：文件前置完成，未生成／整合／驗證；使用者成品核准pending。WI-031審查已完成，舊checkpoint保留歷史。

'''
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:
    p.write_text(checkpoint+p.read_text(encoding='utf-8'),encoding='utf-8')
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf-8') as f:
    f.write('''\n## WI-032 製作前學習轉換（2026-09-11）
使用者要求建立Overall_Review.md分兩部分，完成紀錄後製作第一部分。已列6課主線重建與52課局部修正。沿用WI-031學習，未重複另建規則：觀察是核心只換字／工程輸出通用化；本輪變更是同物件上顯示幾何、候選與框的實際變化；驗證是逐張遮長說明看能否追因果、同輸入比較、360px實看。圖片指南WI-031、網頁指南WI-031為共用位置，逐課細節見總計畫與WI-032/PLAN.md。第一部分包含六課已知工程圖缺口，保留ECC工程4有效案例，避免再次以首讀代替全課。尚未生成或給分；使用者核准pending。\n''')
print('Overall_Review.md: 6 + 52 courses; WI-032 recorded')
