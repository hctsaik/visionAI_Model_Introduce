# WI-029 第一手來源與適用界線

已於製作前讀取。產線流程是本輪教學案例設計，圖像為AI生成示意。

## foundations

- [PatchCore 原論文：正常局部特徵參考](https://arxiv.org/abs/2106.08265)：正常參考路線的具體例子；圖中墊圈和輸出為教學示意。

- [scikit-learn：前處理與資料洩漏](https://scikit-learn.org/stable/common_pitfalls.html)：先分資料，再建立前處理／模型；測試資料不參與選擇。

- [OpenCV：相機校正](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)：校正與幾何關係的工程背景；不構成本文工件已校正的證據。

## production

- [scikit-learn：分組與時間相依資料的驗證](https://scikit-learn.org/stable/modules/cross_validation.html)：相依樣本不能用一般隨機切分推定泛化；依任務分組。

- [scikit-learn：資料洩漏](https://scikit-learn.org/stable/common_pitfalls.html)：測試集不參與前處理學習或模型選擇。

- [Google：Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml)：簡單基準、監控與訓練／服務差異；本頁旁觀及回退為案例流程設計。
