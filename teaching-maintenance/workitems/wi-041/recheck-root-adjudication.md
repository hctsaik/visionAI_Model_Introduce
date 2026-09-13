# 主 Agent 反證與裁決 checkpoint

2026-09-13。公開版本 2c4cb738606a79bc919d523c7e24a1636ad27b5a，HTML SHA-256 43c3557afba4300ad67425bdaba432e0a3582a14e227af0144711db1c0e75e28。產品未改、未發布、使用者核准 pending。

## 已確認

- 公開 HTML、course HTML、docs HTML 一致。公開桌面 1440／手機 390 從首頁到需求助手、方法及計畫成功；錯誤 JSON 不跳取代確認且不更動原稿。`recheck-public-verification.json`。
- 1370 個引用資產來源/docs內容 hash 相同，公開 HTTP 全可達；包含 SVG 引用依賴及 Markdown 操作文件。`recheck-asset-audit.json`。
- 初始135個來源字串不全是 URL；14個拼接／備註字串不能當死鏈。抽出134個個別 URL 後，GET122成功、11 OpenCV403及1 ECVA TLS限制；剩12項用 web工具成功讀取。`recheck-source-links.json`、`recheck-source-fallback.md`。尚需實際渲染 href 清單補核對，不把源字串誤算成連結。
- navigation/bundle 5 tests＋116 subtests通過，`recheck-navigation-bundle.txt`。
- 舊通用 verifier 本輪實跑失敗：`Missing expected learning UI text/hooks: ['帶入晶圓 AOI 範例']`；`recheck-legacy-verifier.txt`。它仍鎖定舊介面，這次在舊 ChArUco schema 檢查之前停止，不得抄歷史原因當本次結果。不宣稱全套測試全綠；建議同步維護驗證入口，不能靠刪斷言假通過。
- 公開 DiffusionAD 展開第2步確有「一次 forward」；預設主線沒有此誤述。主 Agent 實看 `recheck-finding-ad-diffad.png` 並核對官方 DDPM.py：高／低噪聲各 calc_loss，內呼叫 model。C1成立，定版前修正單步與整套呼叫次數的限定。
- 公開 U-Net 展開第1步標題講像素標註，段落講下採樣。主 Agent 實看 `recheck-finding-u-net.png`；C2首項成立。其餘四課錯位由全58課 default/expanded文字證據核對。

## 追加反證

- 六課均已由主 Agent在公開站實際展開並查看 `recheck-finding-*.png`，U-Net、YOLO-Seg、EfficientAD、ConvLSTM、VideoMAE的六处標題／正文錯位全部成立；不是僅依子Agent主張。
- 58課實際DOM的35個外部href全部包含在134個已測試URL中，無拼接異常。
- 全58課×1440/390共116筆磁碟瀏覽器圖片解碼，1228次img檢查、零失敗；與原8000傳輸故障分開。主Agent亦實看8014穩定HTTP PatchCore圖片，完整可讀。磁碟解碼的測試啟用file-access旗標，只用於排除檔案損壞，不用它宣稱一般瀏覽器的所有file://安全政策相容。

## 收尾狀態

全部審查完成。代表圖像報告已收齊，公開390px額外交互亦通過，證據recheck-public-mobile-ui.json及兩張公開截圖由主Agent實看。最終裁決見PLAN.md及REVIEW.md；已確認文字問題可用有限修正解決，不支持全站重畫或新增大量章節。完整圖像逐張盲評、真人理解與現場模型測試不在本輪完成聲明內。六課修正尚未實作、產品未改、使用者核准pending。
