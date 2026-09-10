from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
entries={
R/'IMAGE_STYLE_GUIDE.md':'''

### WI-030 箭頭與手機重排補充（2026-09-11）
- 分支圖按「來源節點→產物節點」逐線核對，不能只查標籤：共享特徵各產生原型與係數，兩者再加權；殘差x同時接直通與F(x)；PnP輸出R,t，內參不是R,t的產生器。重排後重新逐線查，桌機正確不代表手機正確。
- 對稱案例需實際核對旋轉後的點名排列。左右互換可能是鏡射；保留工件幾何、孔洞與物理點身份。人工回查框與模型輸出分色，空孔不能被遮罩填滿。
- 複雜分支連續兩版仍生成錯誤時，改一件代表的完整計算，其他件標示同法處理；不要複製多組基底增加歧義。簡化後仍保留資料來源與人的判讀。
''',
R/'TEACHING_REVIEW_LOG.md':'''

### WI-030 本輪學習與驗證追蹤（2026-09-11）
逐圖證據：teaching-images/vision-ai-model-selection/workitems/wi-030/prototype-review.md。旋轉與鏡射、分支來源逐線核對、手機重排後核對計算責任已併入IMAGE_STYLE_GUIDE.md。下輪逐線問「誰產生誰」，依像素核對，不以正文補足。
建置發現：build_github_pages_site.py只打包既有HTML，不能代表教材重建。先build_interactive_learning_html.py，再打包及查入口。collapsed UI初次失敗揭露舊HTML，後兩次是測試selector選到多個合法入口，已用工程jump-step容器與首個章節按鈕精確定位；collapsed＋tall 3 tests/4 subtests、舊deep mobile＋navigation 6 tests/6 subtests通過。全十二課頁面QA尚未完成，不宣稱發布或使用者核准。
''',
C/'BEGINNER_VISUAL_STATUS.md':'''

WI-030測試checkpoint：先重建interactive-learning.html後，collapsed＋tall 3 passed/4 subtests；既有deep mobile與navigation回歸6 passed/6 subtests。首次失敗是舊HTML，兩次strict selector失敗已修定位，沒有放寬行為斷言。仍待全十二課整合與QA，未發布。
'''
}
for p,s in entries.items():
 if s.strip() not in p.read_text(encoding='utf-8'):
  with p.open('a',encoding='utf-8') as f:f.write(s)
print('Learning and actual test evidence saved')
