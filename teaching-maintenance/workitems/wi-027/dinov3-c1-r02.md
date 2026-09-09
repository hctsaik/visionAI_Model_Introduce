# WI027 DINOv3 核心 r02
- lesson objective: 看懂訓練中局部兩兩關係的對齊，且關係矩陣保持對稱。
- page type: C — 來源、關係、訓練及部署用途。
- primary reading path: 接頭A/B/C局部 → 早期關係目標 → Student對齊關係 → 下游使用特徵。
- major visual nodes:
  1. 黑色接頭與A/B銀色插針、C外殼。
  2. 早期模型3×3對稱關係。
  3. Student的3×3對稱關係，對齊提示。
  4. 部署單骨幹及下游。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看。
- pale-yellow takeaway: #FFF4CC Gram anchoring 穩住局部關係，實際用途仍由下游決定。
- correction: r01參考矩陣A-B與B-A藍色色深不同。採離散二色：較相近均同藍，不相近均同灰；兩矩陣同色圖例，不暗示未測的連續值。
- evidence: 質性教學關係，非實測；actual review pending；user approval pending。
