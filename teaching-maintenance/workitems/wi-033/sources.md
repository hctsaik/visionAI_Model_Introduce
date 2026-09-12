# WI-033 第一批來源與教學推論

核對日期：2026-09-12。本輪未執行模型推論；工件、配對和流程皆為教學示意。

- [CLIP 原論文](https://arxiv.org/abs/2103.00020)及[官方程式](https://github.com/openai/CLIP)：影像和文字各自編碼，以正規化表示比較；訓練批次對比與部署候選排名分開。
- [原始 SigLIP](https://arxiv.org/abs/2303.15343)：逐對 sigmoid 損失，與 CLIP 批次 softmax 目標不同。兩種損失名稱不能直接決定域內選型優劣。
- [MMPose](https://mmpose.readthedocs.io/en/latest/guide_to_framework.html)：top-down 與 bottom-up 是不同處理路徑；資料在原圖、模型輸入與輸出尺度間轉換。[OpenCV PnP](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html)另處理已知 3D／2D 對應及相機參數。三個示意點只教身份與分組，不宣稱唯一姿態。
- [DINOv3 §4.2](https://arxiv.org/html/2508.10104v1)：Gram anchoring 約束同圖 patch 兩兩相似關係，對齊較早教師的 Gram 目標；屬訓練機制，不能畫成每次部署都串接的模組。
- [DiffusionAD 官方程式說明](https://github.com/HuiZhang0812/DiffusionAD)：恢復網路與分割網路分工，分割接原圖及恢復圖。恢復時去掉異常不是最後漏檢的充分判準；應檢查分割是否利用差異定位。
- [AnomalyGPT 官方程式說明](https://github.com/CASIA-LMC-Lab/AnomalyGPT)：視覺文字特徵匹配的 image decoder 產生定位，再由 prompt learner 傳細粒度語意給 LLM。不能把定位來源改畫成任意外接 specialist map。

本輪教學推論：使用同一件工件，分清影像、表示、訓練監督及部署輸出；替代路徑不以因果箭頭串接。以上規則用於圖解，不代表已比較這些模型的實際準確率。

手機比較核對：WinCLIP https://arxiv.org/abs/2303.14814 的狀態文字/視窗聚合及WinCLIP+正常參考；AnomalyCLIP https://arxiv.org/abs/2310.18961 的輔助資料與物件無關提示。已讀原論文摘要，沒有使用paper數值替本課評分。
