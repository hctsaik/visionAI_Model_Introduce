# WI-032 ChArUco精確幾何原型r03
- lesson objective: 同一標靶角點跨視角有固定身份，才能由已知板上位置與影像位置估相機內參及畸變，再用重投影核對。
- page type: C — 已知目標、跨視角對應、參數與驗證。
- primary reading path: 已知標靶角點 → 同一點跨視角位置 → 多視角估計內參與畸變 → 用獨立視角核對重投影
- major visual nodes:
  1. 已知棋盤與固定角點A。
  2. 同一棋盤在三個示意視角，A由同座標轉換。
  3. 相機內參／畸變及重投影核對；單張姿態另題明示。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 沿用具體標靶與幾何證據、淡藍細框與大主體；不用照片填空。
- pale-yellow takeaway: #FFF4CC：已知角點跨視角對應，才能建立可核對的相機幾何。
- generation: 新建精確SVG→瀏覽器PNG；不是修改既有生成PNG。桌機1672×941，手機768×1850，actual PNG review pending，user approval pending。
- evidence: 棋盤與點位為受控幾何示意，無本機校正性能宣稱；視角使用同一板座標的仿射示意，不偽裝實際鏡頭實測。
- source: https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html

## 修正與不變量
本版補明確主區箭頭與手機32px最小標註，移除r03的重複局部與手機重疊。標記使用OpenCV 4×4字典生成唯一代碼，但整張教學圖仍不是可直接列印的標靶。r04相同brief的validator在render後才補跑，未冒稱先跑；r05先通過validator再render。
r01/r02生成棋盤發生角點與格位漂移，因此改精確座標。所有棋盤格、標記與A共用一個定義，A固定內部交點(1,1)，角點不是marker中心。主要講多視角校正，單張已知K求姿態移到工程圖另明說，避免擠入一張圖。校正輸出K／畸變，重投影殘差屬核對；圖中校正前後網格僅示意，不暗示獨立量測已通過。
