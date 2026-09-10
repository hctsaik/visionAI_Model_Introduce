# WI-031 技術疑點與核對範圍

本輪以五份專案Markdown為審查準據；只對會改變審查結論的幾何疑點補查第一手文件，沒有把58課每個論文、實測、效能數字重新執行一遍。其餘方法描述是對現頁教學內容的判讀，並非全面論文復現認證。

- ChArUco：相機校正用多個視角的已知標靶點求相機參數；solvePnP在已知相機內參／畸變下由3D–2D對應求姿態。現頁並列兩種工作時應明示「已知／要估計」；不能用同一未分流方塊混過去。來源：[OpenCV ChArUco calibration](https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html)、[solvePnP](https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html)。
- SIFT：「只有4條線就約束不住整張圖」過於絕對。平面單應估計可用4組合適、非退化的正確點對；本案例應強調錯配、幾何分布與驗證不足，不能只憑4這個數字下結論。來源：[OpenCV findHomography文件（四點取樣、丟棄共線子集）](https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html)、[Homography tutorial](https://docs.opencv.org/4.13.0/d9/dab/tutorial_homography.html)。
- LightGlue：官方實作的自適應深度／寬度分別涉及提早停止與點修剪。應畫出候選或執行量真的改變，不能用一張相同匹配圖加上attention/pruning字樣取代機制。來源：[官方repository](https://github.com/cvg/LightGlue)、[官方matcher實作](https://github.com/cvg/LightGlue/blob/main/lightglue/lightglue.py)。

ECC現有數值及其餘課程標示的歷史模型實測本輪未重跑；可保留為有來源的既有教學證據，不能稱為本輪實測。AnomalyDINO深讀旋轉圖的問題來自實際圖中刻字方向不一致，不依赖模型輸出推測。
