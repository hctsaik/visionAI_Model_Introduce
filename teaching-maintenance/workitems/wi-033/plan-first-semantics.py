"""Versioned preflights; no automatic visual acceptance."""
from pathlib import Path
import json,runpy
W=Path(__file__).resolve().parent
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
def add(owner,n,title,takeaway,panels,detail,source,kind='C',rid=None):
 rid=rid or f'{owner}-engineering-{n}'
 if any(r['id']==rid for r in rows):return
 rows.append(dict(id=rid,owner=owner,index=n,version='r01',title=title,kind=kind,takeaway=takeaway,panels=[dict(title=a,graphic=b) for a,b in panels],steps=[],detail=detail,source=source,review='pending'))
add('siglip',0,'SigLIP：逐對學習，再比較候選','每對各算損失，部署仍須驗證候選排名。',[
 ('訓練：圖文身份決定正負','paired-training'),('逐對損失，共同更新參數','siglip-local'),('部署：編碼後比較候選','siglip-match')],
 '手機核心原圖細字過密。本圖以同一支架／齒輪展示配對身份、2×2正負配對與共享更新，再接部署候選排名；具體雙編碼器已在工程2展開。部署不提供訓練標籤，排名不是生成回答或定位。',
 'https://arxiv.org/abs/2303.15343',rid='siglip-core-mobile')
add('pose',2,'Pose：先框再找點，或先找點再分組','兩條替代路徑都交出有身份的 2D 點。',[
 ('共同輸入：兩個支架','pose-two'),('Top-down：先框後找點','pose-topdown'),('Bottom-up：先點後分組','pose-bottomup')],
 '兩種2D關鍵點方法是替代方案。Top-down先偵測每個物件，再於各ROI估點並映回原圖；Bottom-up先估全圖點，再歸到不同實例。兩者都須保留物件ID、點名與原圖座標。求3D姿態仍需已知3D對應、K與畸變，這裡的三點僅解釋分組，不聲稱足以唯一求PnP。',
 'https://mmpose.readthedocs.io/en/latest/guide_to_framework.html ; https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html',kind='D')
pose='https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html'
add('pose',1,'Pose：影像點必須對上實體點','先鎖定點名與相機設定，才能解讀姿態。',[
 ('影像中找得到同名點','pose-correspondence'),('已知 3D 點與相機設定','pose-calibration'),('PnP 求物體到相機的姿態','pose-transform')],
 '同一支架的點名應跨影像與CAD一致。三點圖解只教對應；實際點數、幾何形狀與PnP方法影響可解性。需固定K、畸變、座標系及CAD單位，輸出的R/t才有意義；不以關鍵點熱區直接當姿態。',pose)
add('pose',3,'Pose：姿態還要投回原图檢查','交付 R／t、座標單位與逐點誤差，再核對實體。',[
 ('保存姿態與座標契約','pose-transform'),('把 3D 點投回相機影像','pose-reproject'),('逐點誤差與站點交付','pose-delivery')],
 'R/t表示物體到相機的變換，t單位跟3D工件座標一致。重投影把已知3D點經R/t與相機模型映回原圖，逐點比較觀測與投影；若用去畸變影像須搭配相應相機設定。交付點ID、可見性、誤差、版本與失敗狀態，外部機器人座標另需外參。',pose)
add('pose',4,'Pose：對稱件的小誤差也可能騙人','遇到身份歧義，補可見證據並攔下不確定姿態。',[
 ('遮擋讓點身份變模糊','pose-ambiguous'),('候選都能貼近觀測點','pose-ambiguity-error'),('增加可辨認的觀測','pose-disambiguate')],
 '近對稱工件上缺口被擋，錯誤ID也可能有低重投影誤差。比較有標記與第二視角的選擇時，需核對表面限制、可見性、校正與節拍，不只挑分數略低的姿態。不能確認就輸出失敗狀態並覆核。',pose)
add('dinov3',2,'DINOv3：訓練時守住局部關係','Gram 約束局部關係；部署不再跑這個訓練分支。',[
 ('同一影像，對照兩個模型','dino-gram-input'),('比較 patch 之間的關係','dino-gram-matrix'),('用關係差異更新學生','dino-gram-update')],
 'Gram矩陣記錄同圖patch特徵的兩兩內積；以較早教師的關係當目標，約束目前學生，並保留原有自監督訓練目標。這不是把特徵逐點鎖成相同數值，也不是推論時要額外跑的模組。本圖數字為二維單位向量算例。',
 'https://arxiv.org/html/2508.10104v1')
dino='https://arxiv.org/html/2508.10104v1'
add('dinov3',1,'DINOv3：一張圖保留多個局部表示','骨幹交出特徵，局部位置與下游工作仍要對齊。',[
 ('輸入一個墊圈影像','dino-washer'),('每個區塊各有特徵','dino-patchfeatures'),('下游才解讀相似或不同','dino-nearest')],
 '以ViT骨幹為例，影像轉成patch token並與其他位置交換資訊，輸出局部及全局表示。局部表示保留對應位置，但每個向量包含上下文，不等於該格像素值。異常判斷、分類或匹配要接下游方法；特徵色圖不是現成缺陷分數。',dino)
add('dinov3',3,'DINOv3：換骨幹也要重建相容參考','保存權重與前處理，同條件重建庫並量完整成本。',[
 ('固定取像與骨幹版本','dino-version'),('建立相容的參考表示','dino-library'),('核對下游結果與成本','dino-evaluate')],
 '部署不跑Gram教師；用固定權重與前處理抽取表示，再建相容特徵庫或訓練下游頭。不能把DINOv2庫直接當DINOv3庫查詢。以同一留出集核對命中／漏檢、抽特徵和查庫時間、記憶體與重建成本，不能只比較色圖漂亮程度。',dino)
add('dinov3',4,'DINOv3：縮圖後的缺口可能變弱','先讓工作細節可見，再驗證特徵與下游判斷。',[
 ('同一墊圈，缺口在右側','dino-notch'),('縮小取樣讓缺口變弱','dino-resolution'),('補取像，重新驗下游','dino-retake')],
 '同一墊圈的右側缺口在粗取樣中可能被平均而減弱；本圖固定件形與方向，不把後段換成別種工件。提高輸入可見性只改善證據條件，不保證DINOv3或下游一定找出異常；仍要測漏檢及正常品誤報。',dino)
add('dinov3',0,'局部特徵也救不回看不清的缺口','同一缺口先看輸入，再看特徵與下游漏檢。',[
 ('原圖：右側缺口可見','dino-notch'),('粗取樣：細節變弱','dino-resolution'),('重新取像後再驗證','dino-retake')],
 '替換DINOv3原反例工件切換及手机小字。三段使用同一右側有缺口墊圈；取樣格為分析式SVG示意，不冒充真實模型輸出。保留原桌機核心與方法比較。',dino,rid='dinov3-main-failure')
diff='https://github.com/HuiZhang0812/DiffusionAD'
add('ad-diffad',2,'DiffusionAD：恢復與定位分兩個工作','原圖與恢復圖一起進分割，最後才交出異常位置。',[
 ('同一原圖走兩個噪聲尺度','diff-noise-branches'),('高噪聲估計引導低噪聲恢復','diff-guidance'),('原圖＋恢復圖 → 分割位置','diff-segment')],
 '同一原圖A加入高低噪聲；高噪聲正常估計N引導低噪聲恢復R。各尺度用單步估計，不是整套只呼叫一次網路；A和R一起進學習的分割網路，不是直接拿R當最終檢測答案。',diff)
gpt='https://github.com/CASIA-LMC-Lab/AnomalyGPT'
add('ad-anomalygpt',2,'AnomalyGPT：定位由內建支路產生','內建位置圖先轉提示，再連同影像與問題產生回答。',[
 ('同一影像產生全局與局部表示','gpt-features'),('內建解碼與圖文匹配定位','gpt-localize'),('位置轉提示後接入 LLM','gpt-prompt')],
 '影像編碼器提供全局與局部表示。局部表示經影像解碼器，與正常／異常文字特徵匹配得位置圖，再由prompt learner轉為提示；LLM另接全局影像表示與使用者問題。此圖是原模型內建支路，不把任意外部檢測器當必要輸入。',gpt)
(W/'engineering-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
runpy.run_path(str(W/'plan-alignment.py'))
