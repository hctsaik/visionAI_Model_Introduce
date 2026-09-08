# visionAI 專案接續資訊

僅在這個工作區使用；路徑是定位提示，使用前核對現況，不盲目套用到其他專案。

- Workspace：`C:/code/claude/visionAI`
- Course：`teaching-images/vision-ai-model-selection`
- 四份共用 Markdown 在 workspace 根目錄；不要在 course 或主題下另建 review log。
- `IMAGE_STYLE_GUIDE.md` 包含優先順序、撤銷的舊稿與11.11後續偏好，須分辨有效條文；實看指定PPTX／認可參考，不能只讀白底藍框等片段。根目錄產圖規則 RULE-012 連結本技能 `image-production-cycle.md` 的 G0–G6。
- AnomalyDINO A04已撤回v02圖片91–94的高估評分，現為60–84、需重製；以共用log最新紀錄為準。不得再用A03高分結案。原型优先處理比較與最近鄰的可見差異，模型特定內容留在專案，不寫成通用限制。
- 必讀／更新：course 的 `BEGINNER_VISUAL_TODO.md`、`BEGINNER_VISUAL_STATUS.md`。依本地 AGENTS.md 記錄生成模式、設計意圖、資產與使用者審閱狀態。
- 最新來源以 `_course_content/topics/<topic>.json` 的啟用資產為準；歷史 HTML、vXX 資產與 log 的高分不代表目前品質或使用者核准。
- EfficientAD 的 v11 生成器是 `tools/render_efficientad_mechanism.py`，會匯入 `render_efficientad_workplace.py`。執行前核對新修改，避免用舊腳本蓋掉使用者內容。其他主題另找相應生成入口。第 6 章有選用 `mobile_steps` 裁切／文字欄位，變更時驗證 test_deep_dive_mobile_steps.py 與手機實圖，保留完整圖入口。
- 構建：course 下 `python tools/build_interactive_learning_html.py`；本機 bundle `python tools/build_github_pages_site.py`（不需要破壞性 clean）。使用者說還是小圖／沒更新時，跑 `tools/audit_lesson_visual_slots.py <slug>`（會截 course 與 docs，量 CSS 寬）；權威說明 `TEACHING_VISUAL_SLOT_AUDIT.md`。
- 驗證入口：`tools/verify_interactive_learning_html.py`；`tests/test_interactive_navigation.py`、`tests/test_github_pages_bundle.py`；改 zoom 時加 `tests/test_concept_zoom_edges.py`。依改動選必要檢查，不宣稱跑過完整套件。
- 既有 QA 範例：workspace 的 `tmp/efficientad-redesign-20260905/capture_review.py`、`check_mechanism.py`。它們有主題、版本、連接埠等特定假設；調整後才能用於下一版，不能把舊截圖標成新證據。
- 網頁入口曾為 `http://127.0.0.1:8000/interactive-learning.html`，雜湊例 `#view=lesson&lesson=ad-efficientad&slide=3`。確認服務仍在運行並驗證頁面版本，不把 localhost 當外部發布網址。
- Browser 工具或替代工具的可用性與授權以當前環境及會話為準，不把歷史工具故障當永久限制。
