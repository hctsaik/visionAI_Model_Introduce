# WI-032 來源、版本與示意界線

本輪以第一手論文、官方文件及既有教材核對機制。沒有新模型推論、相機校正或真人學習測試。幾何精確圖是新SVG經瀏覽器繪製；其餘主線圖使用內建imagegen，prompt意圖、失敗稿及修正版保存在同工作項目。

| 課程 | 核對來源 | 版本／主張範圍 |
| --- | --- | --- |
| charuco | [來源1](https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html)；[來源2](https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html) | OpenCV 4.13.0；板角點身份、多視角校正與已知內參求姿態分開。 |
| ecc | [來源1](https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html) | OpenCV 4.13.0 findTransformECC；函式回傳相關與warp。採樣方向以xI=W(xT)定義，常見warp用WARP_INVERSE_MAP。 |
| sift | [來源1](https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html)；[來源2](https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html) | OpenCV SIFT；尺度／方向、4×4×8描述與ratio test，幾何估計另接。 |
| lightglue | [來源1](https://github.com/cvg/LightGlue)；[來源2](https://arxiv.org/abs/2306.13643) | 官方預訓練matcher與相容extractor；自注意力、交互注意力、提前停止與點修剪。 |
| det-dino-detector | [來源1](https://arxiv.org/abs/2203.03605)；[來源2](https://github.com/IDEA-Research/DINO) | DINO偵測論文（2203.03605），不是DINOv2；mixed query位置／內容、訓練專用對比去噪。 |
| yolo-world | [來源1](https://arxiv.org/abs/2401.17270)；[來源2](https://github.com/AILab-CVC/YOLO-World/blob/master/docs/reparameterize.md)；[來源3](https://arxiv.org/html/2401.17270v3) | YOLO-World論文2401.17270 v3第3.3節：文字引導max＋sigmoid權重，以及ImagePooling Attention；快取與官方支援的重參數化分開，版本差異需查部署實作。 |

## 既有證據保留

ECC工程4原圖仍由工程4段落連結；R06的SIFT 120／104、模糊46／4及ECC 32／12、遠起點217px案例依原圖的「教學示意，非實測」界線保留，未另行確認原始演算程序。複製檔與原檔SHA256相同，見retained-evidence.json。

## 本輪可驗證範圍

SVG座標能核對同一板角點／同一工件及幾何變換；4像素40、80、120、160中心的雙線性插值示例為100。相似度格、描述條、候選框、曲線、速度流程都是機制示意，不提供準確率或FPS。原生圖自評、實頁檢查、自動測試與使用者核准各自紀錄。
