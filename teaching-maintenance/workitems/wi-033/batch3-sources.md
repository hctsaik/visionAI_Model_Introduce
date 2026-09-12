# 第三批來源核對與待製作範圍

狀態：已核對原論文／官方程式，尚未製作或啟用第三批。範圍仍為ResNet、ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN各四工程圖，另補ResNet手機深讀2/4/8與SegFormer手機深讀1/3/4/5。

- ResNet：[原論文](https://arxiv.org/abs/1512.03385)。相容特徵x與F(x)相加；分類讀出不冒充定位熱點。
- ConvNeXt：[官方Block](https://raw.githubusercontent.com/facebookresearch/ConvNeXt/main/models/convnext.py)。depthwise空間混合、LayerNorm、通道Linear擴展/GELU/收回、layer scale與殘差；本輪限定2022原始ConvNeXt，不混入v2 GRN。
- ViT：[原論文](https://arxiv.org/html/2010.11929v2)。patch projection與位置嵌入、self-attention交換、MLP與殘差、CLS分類讀出；注意力不當缺陷定位或因果證明。
- U-Net：[原論文](https://arxiv.org/html/1505.04597v1)。encoder/context與decoder定位，同尺度skip串接特徵；原始valid convolution需crop對齊，不能畫成ResNet逐元素加法。
- SegFormer：[原論文§3](https://arxiv.org/html/2105.15203v3)。MiT產生H/4、H/8、H/16、H/32四尺度，Linear統一通道、對齊1/4後concat、融合與分類，再回映輸出。其重疊patch embedding與Mix-FFN不等同基本ViT位置表。
- YOLO-Seg：[官方process_mask](https://raw.githubusercontent.com/ultralytics/ultralytics/main/ultralytics/utils/ops.py)。每實例係數與共享prototype矩陣乘法、依框裁切／尺度映回。main分支的upsample/crop順序已改；教學採YOLOv8式機制，不把某一次main當所有版本。必須另鎖版本再舉逐步順序。
- Keypoint R-CNN：[官方heatmaps_to_keypoints](https://raw.githubusercontent.com/pytorch/vision/main/torchvision/models/detection/roi_heads.py)。每ROI每點熱圖，resize到ROI尺寸、argmax、半像素校正與ROI offset。Torchvision這個函式的輸出v固定1，另交peak scores；不能把這個v當模型估計的可見性。訓練的可見性標註、推論峰值與應用有效性須分開。

案例連續性：分類三課沿用十字／內六角螺絲及背景捷徑；語意分割沿用細焊縫；YOLO-Seg用同兩墊圈、每件獨立遮罩；Keypoint R-CNN用具方向線索的同四孔板A/B/C/D。仍需原生實看既有參考與建立版本preflight，不能把來源閱讀當成圖或課程完成。
