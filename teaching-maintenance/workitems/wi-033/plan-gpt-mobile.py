from pathlib import Path
import json,runpy
W=Path(__file__).resolve().parent
ns=runpy.run_path(str(W/'plan-first-semantics.py'));rows=ns['rows'];add=ns['add'];src=ns['gpt']
add('ad-anomalygpt',0,'AnomalyGPT：先定位，再接看圖對話','內建位置提供線索，回答仍回原圖核對。',[
 ('訓練：合成影像與位置對齊','gpt-mobile-training'),('測試：同圖內建定位','gpt-mobile-location'),('位置轉提示，連同圖文回答','gpt-mobile-answer')],
 '手機核心原四段密圖減為三段。保留原金屬板兩孔對角佈局、右側細痕，改以新SVG重建同一類幾何示意；訓練、內建定位與提示/影像/問題接LLM分清。原桌機主線保留，沒有修改既有bitmap。',src,rid='anomalygpt-mobile-core')
add('ad-anomalygpt',0,'AnomalyGPT：回答肯定仍要查證','位置、觀察和推測分開核對，不能由流暢度放行。',[
 ('同一原圖：p 細痕、q 孔邊','gpt-mobile-evidence'),('錯誤假設：位置與根因無據','gpt-mobile-wrong'),('分開記錄，再補需要的證據','gpt-mobile-review')],
 '保留原反例p/q身份與原圖兩孔幾何，不用工程4的另一種錯答替換。錯誤熱區指q，文字宣稱裂縫和夾具根因；學習者須分觀察、推測、未知，回原圖補證據。',src,rid='anomalygpt-mobile-failure')
add('ad-anomalygpt',0,'三種圖文方法：先選工作結果','先驗定位，再驗對話能否減少覆核成本。',[
 ('WinCLIP：人工狀態與視窗','gpt-mobile-winclip'),('AnomalyCLIP：學到的提示','gpt-mobile-anomalyclip'),('AnomalyGPT：定位加對話','gpt-mobile-gpt')],
 '同一工件与取像比較三種工作輸出：WinCLIP人工狀態提示/視窗与可選正常參考；AnomalyCLIP輔助資料學提示；AnomalyGPT合成資料對齊後內建定位/對話。圖中位置皆為機制示意，不宣稱同精度。成本與驗收在正文固定正常/真缺陷、硬體、解析度与漏檢要求。',src+' ; https://arxiv.org/abs/2303.14814 ; https://arxiv.org/abs/2310.18961',kind='D',rid='anomalygpt-mobile-comparison')
for r in rows:
 if r['id'].startswith('anomalygpt-mobile-'):r['mobile_height']=2304
(W/'engineering-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\nAnomalyGPT首讀三張手機原圖已實看：核心四段密集、反例四段多餘人物與細節、比較四段；即將以三組2304高手機SVG減量，保留原p/q與兩孔板身份，工程4另有教學責任。三課頁面驗證先跑目前工程版，之後僅補驗改動範圍。\n')
runpy.run_path(str(W/'plan-first-semantics.py'))
