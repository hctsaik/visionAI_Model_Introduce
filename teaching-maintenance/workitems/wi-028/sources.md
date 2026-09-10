# WI-028 第一手來源與教學範圍

核對日期：2026-09-10。下列工業案例均為教學改編，PNG是AI生成示意，非作者輸出、現場推論或模型性能比較。

| 題目／版本 | 原始來源 | 本課採用與界線 |
|---|---|---|
| Frame Difference | [OpenCV absdiff](https://docs.opencv.org/4.x/d2/de8/group__core__array.html) | 同座標絕對亮度差；門檻與事件整合由應用定義，不稱為學習模型。 |
| Background Subtraction／MOG2例 | [OpenCV背景模型教學](https://docs.opencv.org/4.13.0/d1/dc5/tutorial_background_subtraction.html) | 初始化、更新、前景遮罩；不是固定一張背景照片。MOG2陰影可有獨立值，二值顯示需說明處理。 |
| Lucas–Kanade／金字塔稀疏追點例 | [OpenCV光流教學](https://docs.opencv.org/4.x/d4/dee/tutorial_optical_flow.html) | 鄰域相似位移、亮度近似不變、小位移及金字塔；只追選定點，點座標不等於物件身分。 |
| RAFT／ECCV2020原始架構 | [論文](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123470392.pdf)、[作者程式](https://github.com/princeton-vl/RAFT) | 特徵、全配對相關性、多尺度查詢與反覆更新稠密光流；遮擋區為估計，沒有直接觀測對應。 |
| ByteTrack／ECCV2022原始方法 | [論文](https://arxiv.org/abs/2110.06864)、[作者程式](https://github.com/FoundationVision/ByteTrack) | 先高分關聯，再以低分框補未匹配轨跡；不把所有低分框當新物件，偵測器另有訓練責任。 |
| ConvLSTM／2015原始單元 | [論文](https://arxiv.org/abs/1506.04214) | 空間卷積的狀態更新；原文降雨預測，工件狀態範例為改編，需另訓練任務頭。 |
| VideoMAE／2022原版 | [論文](https://arxiv.org/abs/2203.12602)、[作者程式](https://github.com/MCG-NJU/VideoMAE) | 時空tube遮蔽後重建像素的自監督預訓練；部署分類需下游訓練，並非天生缺陷模型。 |
| V-JEPA／2024原版 | [論文](https://arxiv.org/abs/2404.08471)、[作者程式](https://github.com/facebookresearch/jepa) | 遮蔽影片部分、由可見內容預測目標編碼器特徵；不是重建影片、不混入V-JEPA2／2.1動作條件或控制能力。 |

比較固定影片、相機、取樣時間与工作輸出，再記錄各方法資料／標註、完整延遲、記憶體及維護代價。無共同實測，不引用跨資料集數字排名。
