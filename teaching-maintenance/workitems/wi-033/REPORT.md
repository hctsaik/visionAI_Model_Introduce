# WI-033 第二部分交付報告

52／52課本機修正、逐圖審查與逐課驗證完成；使用者核准pending，尚未commit、push或發布。本輪沒有新增模型推論，原有實測資料依原來源保留。

入口：[課程](http://127.0.0.1:8000/interactive-learning.html)、[本機網站包](http://127.0.0.1:8000/docs/index.html)。第一部分六課的教材資料與本輪基準相同。

## 改動與證據

保留成立的首讀主線，完成52課共208組工程故事（桌機／手機416張PNG）、指定主反例／比較與深讀手機修正。全部本輪啟用新PNG共460張，逐圖自評91–93，無否決項，五項完成度均至少8；這是作者自評，不是真人學習成效或使用者核准。逐圖來源、版本及hash見[final-selected-assets.json](final-selected-assets.json)。

指定深讀：AnomalyDINO旋轉反例、EfficientAD雙分支與1/2/3/4/5/7/8章、ResNet 2/4/8章、SegFormer 1/3/4/5章、PatchCore 2章均已完成，保留有效桌機來源與實測數值。證據見batch2、batch3及batch5的deep-page-review／validation-summary。

## 實際驗證

- 最終來源HTML與docs SHA256：`17a716a585d9c10b490a46ba86757e4ac216f15c39261c22e11a75dbf282e89a`；1,370個引用資產一致。
- 全52課現行HTTP核對1506個檔案通過；[verification-all52.json](verification-all52.json)保存實際URL及hash。包含圖檔、model.md與manifest。
- 各批累計208個主頁狀態、1,472次放大、208次答案及導覽檢查；最後44狀態在此HTML版本重新擷取。其餘已審版本以既有HTTP hash重核後引用，沒有宣稱208狀態全部在最後一次重拍。
- 指定深讀累計160個章節狀態（64+64+32）通過，逐頁實看另存各批證據。
- 最終必要回歸24 tests、130 subtests通過：工程手機、bundle、導航、長圖、深讀、收合入口及放大邊界；58課178個手機圖說間距通過。未宣稱跑過所有歷史版型測試。
- `git diff --check`通過；只出現Git既有LF/CRLF轉換提示。

## 學習與限制

共用學習已回寫根IMAGE_STYLE_GUIDE.md、TEACHING_WEBPAGE_GUIDE.md與TEACHING_REVIEW_LOG.md：同件同位置、梯度更新對象、差異量與成本單位、條件與結果逐區核對、候選與真實觀測分開、圖片解碼與截圖診斷、分批證據版本追溯。

幾何圖為教學簡化，部分專有名詞仍需正文支援；手機需縱向捲動。生成、復原與超解析候選不能替代獨立實測。使用者成品核准及外部發布仍未發生。

維護副本已保存並核對於`teaching-maintenance/workitems/wi-033/`；權威入口為[PLAN.md](PLAN.md)及根WORKITEMS.md。舊失敗／未完成紀錄保留作歷史，現行狀態以本報告與最終驗證為準。inventory內初始whole_course_compliant等欄位來自WI-031基準，現行完成狀態看status與evidence_wi033。

## 逐課證據

| 課程 | 現行狀態 | 頁面及驗證紀錄 |
| --- | --- | --- |
| ResNet | 本機完成；使用者審閱pending | [batch3-page-assessment.json](batch3-page-assessment.json)、[batch3-validation-summary.json](batch3-validation-summary.json) |
| ConvNeXt | 本機完成；使用者審閱pending | [batch3-page-assessment.json](batch3-page-assessment.json)、[batch3-validation-summary.json](batch3-validation-summary.json) |
| ViT | 本機完成；使用者審閱pending | [batch3-page-assessment.json](batch3-page-assessment.json)、[batch3-validation-summary.json](batch3-validation-summary.json) |
| U-Net | 本機完成；使用者審閱pending | [batch3-page-assessment.json](batch3-page-assessment.json)、[batch3-validation-summary.json](batch3-validation-summary.json) |
| SegFormer | 本機完成；使用者審閱pending | [batch3-page-assessment.json](batch3-page-assessment.json)、[batch3-validation-summary.json](batch3-validation-summary.json) |
| YOLO-Seg | 本機完成；使用者審閱pending | [batch3-page-assessment.json](batch3-page-assessment.json)、[batch3-validation-summary.json](batch3-validation-summary.json) |
| Keypoint R-CNN | 本機完成；使用者審閱pending | [batch3-page-assessment.json](batch3-page-assessment.json)、[batch3-validation-summary.json](batch3-validation-summary.json) |
| Pose Pipeline | 本機完成；使用者審閱pending | [pose-page-assessment.json](pose-page-assessment.json)、[verification-pose.json](verification-pose.json) |
| YOLO dense detector | 本機完成；使用者審閱pending | [batch4-page-assessment.json](batch4-page-assessment.json)、[batch4-validation-summary.json](batch4-validation-summary.json) |
| RT-DETR | 本機完成；使用者審閱pending | [batch4-page-assessment.json](batch4-page-assessment.json)、[batch4-validation-summary.json](batch4-validation-summary.json) |
| Grounding DINO | 本機完成；使用者審閱pending | [batch4-page-assessment.json](batch4-page-assessment.json)、[batch4-validation-summary.json](batch4-validation-summary.json) |
| YOLOE | 本機完成；使用者審閱pending | [batch4-page-assessment.json](batch4-page-assessment.json)、[batch4-validation-summary.json](batch4-validation-summary.json) |
| PatchCore | 本機完成；使用者審閱pending | [batch5-page-assessment.json](batch5-page-assessment.json)、[batch5-validation-summary.json](batch5-validation-summary.json) |
| PaDiM | 本機完成；使用者審閱pending | [batch5-page-assessment.json](batch5-page-assessment.json)、[batch5-validation-summary.json](batch5-validation-summary.json) |
| AnomalyDINO | 本機完成；使用者審閱pending | [batch2-page-assessment.json](batch2-page-assessment.json)、[batch2-deep-report.json](batch2-deep-report.json)、[deep-detail-report.json](deep-detail-report.json) |
| SubspaceAD | 本機完成；使用者審閱pending | [batch5-page-assessment.json](batch5-page-assessment.json)、[batch5-validation-summary.json](batch5-validation-summary.json) |
| STFPM | 本機完成；使用者審閱pending | [batch5-page-assessment.json](batch5-page-assessment.json)、[batch5-validation-summary.json](batch5-validation-summary.json) |
| RD4AD | 本機完成；使用者審閱pending | [batch5-page-assessment.json](batch5-page-assessment.json)、[batch5-validation-summary.json](batch5-validation-summary.json) |
| EfficientAD | 本機完成；使用者審閱pending | [batch2-page-assessment.json](batch2-page-assessment.json)、[batch2-deep-report.json](batch2-deep-report.json)、[deep-detail-report.json](deep-detail-report.json) |
| Autoencoder (AE) | 本機完成；使用者審閱pending | [batch5-page-assessment.json](batch5-page-assessment.json)、[batch5-validation-summary.json](batch5-validation-summary.json) |
| DRAEM | 本機完成；使用者審閱pending | [batch5-page-assessment.json](batch5-page-assessment.json)、[batch5-validation-summary.json](batch5-validation-summary.json) |
| UniAD | 本機完成；使用者審閱pending | [batch5-page-assessment.json](batch5-page-assessment.json)、[batch5-validation-summary.json](batch5-validation-summary.json) |
| Dinomaly | 本機完成；使用者審閱pending | [batch6-page-assessment.json](batch6-page-assessment.json)、[batch6-validation-summary.json](batch6-validation-summary.json) |
| InvAD | 本機完成；使用者審閱pending | [batch6-page-assessment.json](batch6-page-assessment.json)、[batch6-validation-summary.json](batch6-validation-summary.json) |
| DiffusionAD | 本機完成；使用者審閱pending | [first-rest-page-assessment.json](first-rest-page-assessment.json)、[verification-dinov3-ad-diffad-ad-anomalygpt.json](verification-dinov3-ad-diffad-ad-anomalygpt.json) |
| DDAD | 本機完成；使用者審閱pending | [batch6-page-assessment.json](batch6-page-assessment.json)、[batch6-validation-summary.json](batch6-validation-summary.json) |
| WinCLIP | 本機完成；使用者審閱pending | [batch6-page-assessment.json](batch6-page-assessment.json)、[batch6-validation-summary.json](batch6-validation-summary.json) |
| AnomalyCLIP | 本機完成；使用者審閱pending | [batch6-page-assessment.json](batch6-page-assessment.json)、[batch6-validation-summary.json](batch6-validation-summary.json) |
| AnomalyGPT | 本機完成；使用者審閱pending | [first-rest-page-assessment.json](first-rest-page-assessment.json)、[verification-dinov3-ad-diffad-ad-anomalygpt.json](verification-dinov3-ad-diffad-ad-anomalygpt.json) |
| Frame Difference | 本機完成；使用者審閱pending | [batch6-page-assessment.json](batch6-page-assessment.json)、[batch6-validation-summary.json](batch6-validation-summary.json) |
| Background Subtraction | 本機完成；使用者審閱pending | [batch6-page-assessment.json](batch6-page-assessment.json)、[batch6-validation-summary.json](batch6-validation-summary.json) |
| Lucas–Kanade | 本機完成；使用者審閱pending | [batch2-page-assessment.json](batch2-page-assessment.json)、[batch2-deep-report.json](batch2-deep-report.json)、[deep-detail-report.json](deep-detail-report.json) |
| RAFT | 本機完成；使用者審閱pending | [batch2-page-assessment.json](batch2-page-assessment.json)、[batch2-deep-report.json](batch2-deep-report.json)、[deep-detail-report.json](deep-detail-report.json) |
| ByteTrack | 本機完成；使用者審閱pending | [batch6-page-assessment.json](batch6-page-assessment.json)、[batch6-validation-summary.json](batch6-validation-summary.json) |
| ConvLSTM | 本機完成；使用者審閱pending | [batch7-page-assessment.json](batch7-page-assessment.json)、[batch7-validation-summary.json](batch7-validation-summary.json) |
| VideoMAE | 本機完成；使用者審閱pending | [batch7-page-assessment.json](batch7-page-assessment.json)、[batch7-validation-summary.json](batch7-validation-summary.json) |
| V-JEPA | 本機完成；使用者審閱pending | [batch7-page-assessment.json](batch7-page-assessment.json)、[batch7-validation-summary.json](batch7-validation-summary.json) |
| DINOv2 | 本機完成；使用者審閱pending | [batch4-page-assessment.json](batch4-page-assessment.json)、[batch4-validation-summary.json](batch4-validation-summary.json) |
| DINOv3 | 本機完成；使用者審閱pending | [first-rest-page-assessment.json](first-rest-page-assessment.json)、[verification-dinov3-ad-diffad-ad-anomalygpt.json](verification-dinov3-ad-diffad-ad-anomalygpt.json) |
| CLIP | 本機完成；使用者審閱pending | [alignment-page-assessment.json](alignment-page-assessment.json)、[verification-clip-siglip.json](verification-clip-siglip.json) |
| SigLIP | 本機完成；使用者審閱pending | [alignment-page-assessment.json](alignment-page-assessment.json)、[verification-clip-siglip.json](verification-clip-siglip.json) |
| LLaVA | 本機完成；使用者審閱pending | [batch4-page-assessment.json](batch4-page-assessment.json)、[batch4-validation-summary.json](batch4-validation-summary.json) |
| Qwen-VL | 本機完成；使用者審閱pending | [batch4-page-assessment.json](batch4-page-assessment.json)、[batch4-validation-summary.json](batch4-validation-summary.json) |
| Gemini Vision | 本機完成；使用者審閱pending | [batch4-page-assessment.json](batch4-page-assessment.json)、[batch4-validation-summary.json](batch4-validation-summary.json) |
| DefectFill | 本機完成；使用者審閱pending | [batch7-page-assessment.json](batch7-page-assessment.json)、[batch7-validation-summary.json](batch7-validation-summary.json) |
| AnomalyDiffusion | 本機完成；使用者審閱pending | [batch7-page-assessment.json](batch7-page-assessment.json)、[batch7-validation-summary.json](batch7-validation-summary.json) |
| TF-IDG | 本機完成；使用者審閱pending | [batch7-page-assessment.json](batch7-page-assessment.json)、[batch7-validation-summary.json](batch7-validation-summary.json) |
| ControlNet | 本機完成；使用者審閱pending | [batch7-page-assessment.json](batch7-page-assessment.json)、[batch7-validation-summary.json](batch7-validation-summary.json) |
| Inpainting | 本機完成；使用者審閱pending | [batch7-page-assessment.json](batch7-page-assessment.json)、[batch7-validation-summary.json](batch7-validation-summary.json) |
| Diffusion Restoration | 本機完成；使用者審閱pending | [batch7-page-assessment.json](batch7-page-assessment.json)、[batch7-validation-summary.json](batch7-validation-summary.json) |
| Deblur | 本機完成；使用者審閱pending | [batch7-page-assessment.json](batch7-page-assessment.json)、[batch7-validation-summary.json](batch7-validation-summary.json) |
| Super-resolution | 本機完成；使用者審閱pending | [batch7-page-assessment.json](batch7-page-assessment.json)、[batch7-validation-summary.json](batch7-validation-summary.json) |

最終交付核對：[final-verification.json](final-verification.json)；維護副本：[maintenance-verification.json](maintenance-verification.json)。
