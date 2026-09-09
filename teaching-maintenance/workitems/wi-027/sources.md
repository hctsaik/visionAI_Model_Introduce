# WI-027 來源與版本界線

核對日期：2026-09-10。以下為第一手來源；本課影像、特徵色塊、排序及回答均為教學示意，非模型推論或效能實測。

| 主題 | 核對來源 | 採用範圍 |
|---|---|---|
| DINOv2 | https://arxiv.org/abs/2304.07193 ; https://github.com/facebookresearch/dinov2 | 原始自監督視覺骨幹，整圖與局部特徵；不把後續 dino.txt 擴充說成原模型必備 |
| DINOv3 | https://arxiv.org/html/2508.10104v1 | ViT 範例，§4.2 Gram 比較局部特徵兩兩內積；訓練目標不是部署時異常頭 |
| CLIP | https://arxiv.org/abs/2103.00020 ; https://github.com/openai/CLIP | 原始雙編碼、共同表示與批次對比；候選排序不是文字生成 |
| SigLIP | https://arxiv.org/abs/2303.15343 | 原始逐對 sigmoid 損失，含不配對組合；不混入 SigLIP 2 |
| LLaVA | https://llava-vl.github.io/ ; https://arxiv.org/abs/2304.08485 | 原始 projection／CLIP vision／LLM 與兩段對齊和指令學習；不稱所有版本都相同 |
| Qwen-VL | https://qwenlm.github.io/blog/qwen2-vl/ ; https://arxiv.org/abs/2409.12191 | Qwen2-VL 動態解析度與 M-ROPE 範例；舊 Qwen2-VL GitHub URL 已重導 Qwen3-VL，不以重導頁冒充舊版本 |
| Gemini Vision | https://ai.google.dev/gemini-api/docs/image-understanding ; https://ai.google.dev/gemini-api/docs/structured-output | API 影像輸入／回答與格式和內容驗證分離；不推定內部模型架構，不聲稱固定服務版本或最新性能 |

比較為資料準備、訓練機制、輸出責任與部署工作，不以跨論文分數排名。現場選用仍需固定實際權重或model ID，以同資料及任務測量。僅做教材，不進行付費API或GPU訓練。
