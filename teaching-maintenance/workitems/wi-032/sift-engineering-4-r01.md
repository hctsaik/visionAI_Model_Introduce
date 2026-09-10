# WI-032 sift-engineering-4 r01
- lesson objective: 匹配失敗與幾何模型不適用，要分開診斷。
- page type: D
- primary reading path: 同場景不同深度 → 點對可能仍正確 → 改選幾何假設 → 工作核對與接手
- major visual nodes:
  1. 同場景不同深度
  2. 點對可能仍正確
  3. 改選幾何假設
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：匹配失敗與幾何模型不適用，要分開診斷。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html
- evidence: SIFT可提供局部對應，但場景有非平面視差時，單一單應未必能同時對齊全部深度。不能把此時的殘差全部解釋成特徵錯配，需检查模型适用范围。
