from pathlib import Path
import json
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
learning='''
## WI-032 第一部分重建學習（2026-09-11）

本輪先建立Overall_Review.md，將58課分成6課主線／工程重建與52課局部修正；只執行前6課。紀錄、製作、實頁驗證依序完成，不把計畫建立等同教材完成。

- 幾何圖的同一點／同一件必須有單一座標定義。ChArUco角點兩次生成身份不一致後改精確SVG；SIFT／LightGlue使用同一缺口與兩孔，ECC的外框和孔位用同一變換。不是只讓A/B標籤看起來相同。
- 手機直向畫布仍可能文字過小。偵測核心與反例改用少量大標註；SIFT工程標題被拆成m／atcher後改成完整中文短句。最後以360px頁面檢查，而不是以原生圖大尺寸判通過。
- 圖像角色要區分：校正內參與已知內參求姿態；SIFT特徵、LightGlue配對與幾何求解；DINO正負去噪只用於訓練；YOLO-World词彙快取與重參數化。對齊、找到物件與判定缺陷不能混成同一交付。
- 「部署模型」方框仍不夠。YOLO-World工程3的r04在最終審查被退回，r07按官方分類頭例畫出詞彙向量成為1×1分類頭參數，再由影像特徵產生類別分數；不靠正文替空方框加分。
- 新主線不能遮住舊工程內容的矛盾。來源、四張工程圖、展開交付、家族摘要和model.md一起核對；修掉SIFT warp等舊用語。工程圖使用獨立資產與手機來源，不重貼首讀PNG充數。
- 保存舊案例要重新核對證據等級。R06 SIFT與ECC原圖標示「教學示意，非實測」；120／104、46／4、32／12、217px保留原圖及SHA，但本輪沒有重跑原程序，不能稱新實測。ECC原工程4仍可連結查看。
- 檢查工具也可能錯。長圖元素截圖會混入sticky導覽列；另存排除固定介面的圖框截圖，正常viewport證據保留。SVG檢查器把內部小殘差框當整張節點背景造成誤報，核對實圖後修檢查器並保留失敗結果。HTTP相對URL測試錯誤亦有保留，不歸咎網站。
- 分數、互動、hash與使用者核准互不替代。76張新PNG有逐張分項與扣分，六課有整課評價；手機長捲動、簡筆幾何及未做現場模型比較仍列限制。沒有真人理解測試，沒有使用者成品核准，也未發布。

詳見 [WI-032 報告](teaching-images/vision-ai-model-selection/workitems/wi-032/REPORT.md)、[來源與界線](teaching-images/vision-ai-model-selection/workitems/wi-032/sources.md)及[Overall Review](Overall_Review.md)。量表仍用v1.0，沒有改配分與門檻。
'''
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf-8') as f:f.write('\n'+learning)
with (R/'IMAGE_STYLE_GUIDE.md').open('a',encoding='utf-8') as f:f.write('''

### WI-032 共用製圖學習（2026-09-11；沿用既有量表）

同物件／同角點的連續圖以單一幾何定义或可核對原圖控制；標籤相同不能取代位置一致。兩次同類生成錯誤後改變方法，必要時用新建原生幾何圖保留精確關係。示意圖裡的操作必須有可見狀態改變，例如詞彙向量整合進分類頭參數，而非換一個部署方框。

手機需獨立檢查句長、英文斷詞與頁內尺寸。原生圖清楚或畫布直向不等於360px可讀。正式工程圖有自己的學習責任和手機圖，不以首讀圖片重用充作四張工程圖。歷史數值依原圖證據標示保存，不因本輪引用變成新實測。案例與失敗版本见TEACHING_REVIEW_LOG.md WI-032及workitems/wi-032。
''')
with (R/'TEACHING_WEBPAGE_GUIDE.md').open('a',encoding='utf-8') as f:f.write('''

### WI-032 共用網頁學習（2026-09-11；沿用既有量表）

完整課程重建須核對首讀、展開工程圖、交付操作卡、家族摘要與可下載Markdown。可折疊不代表可以留互相矛盾的舊交付。工程手機圖採獨立來源時，同步驗證picture實際選圖、自然高寬比與放大後的捲動可達性；其餘課程保持原有顯示路徑並做回歸。

圖片、caption、alt、正文與測試輸出分別作證據。長圖元素截圖若混入sticky介面，保留一般viewport截圖，再另取不含固定介面的圖框證據；不要先認定素材被遮擋。檢查器須以真正節點框判範圍，誤把內嵌子圖當整卡時保留失敗記錄並修檢查器。示意、原圖、歷史數據及本輪實測狀態須清楚分開。詳見TEACHING_REVIEW_LOG.md WI-032。
''')
status='六課主線、工程4圖、手機版與交付已重建，76張新PNG已逐圖及整頁自評；14 tests／130 subtests、24主頁狀態／168放大與18補充390px及舊課回歸已通過。正在保存最終報告、資產重新核對與維護來源快照。第二部分52課未啟動，未發布，使用者成品核准pending。下一步：完成final-verification.json與維護快照一致性，將Overall／PLAN及本入口結案。'
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:
 s=p.read_text(encoding='utf-8');first=s.find('\n## ',1);p.write_text('## WI-032 最新接續狀態（取代下方舊checkpoint）\n'+status+'\n'+s[first:],encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n## 收尾checkpoint\n'+status+'\n64個啟用原生SVG畫布／大型節點文字邊界檢查通過；38份選定故事brief通過preflight。每圖完成度五項有理由，圖片分數不可借用頁面正文或測試成功。\n')
(W/'test-results.json').write_text(json.dumps({'pytest':{'tests':14,'subtests':130,'result':'passed','duration_seconds':76.47,'files':['test_github_pages_bundle.py','test_engineering_mobile_pages.py','test_collapsed_deep_dive.py','test_tall_mobile_artwork.py','test_deep_dive_mobile_steps.py','test_interactive_navigation.py']},'preflight':'38 passed','svg_layout':'64 checked; no final errors; initial false positive retained','inference':'not run','human_learning_test':'not run','user_approval':'pending'},ensure_ascii=False,indent=2),encoding='utf-8')
print('Learning saved to three authority Markdown files and resume entries')
