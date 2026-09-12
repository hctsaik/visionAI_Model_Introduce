from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent
notes={
'dinov3-engineering-1':([23,23,19,18,9],['同墊圈ABC局部位置與不同表示','區塊表示与下游比較分工，非像素熱點','回原圖核對查詢位置，固定前處理','B標籤箭頭已分開；雙墊圈較小','位置身份保持，示意特徵不當推論']),
'dinov3-engineering-2':([23,24,18,18,9],['同圖patch與兩模型對應','對稱Gram由向量角度算出，訓練約束与部署分開','只更新學生，部署另頁','算例一位小數；手機需跨區讀','教師關係為目標，並非固定特徵數值']),
'dinov3-engineering-3':([23,23,19,18,9],['同墊圈与正常缺口留出集','不同權重需重建相容表示，無Gram推論分支','工作/運算/維護三成本明示','長句已限制，手機仍捲動','不捏造命中或時間數字']),
'dinov3-engineering-4':([24,23,19,18,9],['兩路用同正常缺口資料','相容庫和不同骨幹表示分開','保留基準或重建，以工作結果取捨','替代路徑不串接，內容簡短','無新骨幹必勝宣稱']),
'dinov3-main-failure':([24,23,19,18,9],['同件右側缺口贯穿三段','粗格由同幾何每格100樣本平均','取像條件与下游再驗證','手機三段短句，格值不塞主圖','解析式取樣，非模型實測；形狀未換件']),
'ad-diffad-engineering-1':([23,24,19,18,9],['正常加噪已去除誤加刮痕，合成異常另列','恢復与定位各有監督目標','正常和真缺陷獨立驗證','分支目標對齊，手機名稱仍長','不把合成當真缺陷結果']),
'ad-diffad-engineering-2':([24,24,18,18,9],['同支架A、高低噪聲与恢復R','N引導實際接恢復，A/R共同進分割','交出位置圖，單步不等於單次','末句和位置圖不再重疊','示意區域位置不變，噪聲為圖解']),
'ad-diffad-engineering-3':([23,23,19,18,9],['A/R及映回位置可追','恢復、分割、前後處理均計成本','原圖与位置交給覆核，門檻另驗','工件大，時間長條只解釋構成','時間條明示非實測']),
'ad-diffad-engineering-4':([24,24,18,18,9],['共同刮痕，恢復兩結果保持件形','兩支皆A/R進分割，恢復乾淨不等於漏檢','最終圖另驗真缺陷；非必然關係','两路比較不串接，手機需上下比','假設結果標明，未捏造模型效能']),
'ad-anomalygpt-engineering-1':([23,23,19,18,9],['異常、遮罩与文字指同處','固定骨幹/LLM，更新解碼与提示器','配對資料要對齊，真缺陷獨立驗證','三段避免微小拓樸','合成監督不當已測結果']),
'ad-anomalygpt-engineering-2':([24,24,18,18,9],['同支架局部表示指中部異常','內建匹配得位置再轉提示，影像/問題另接LLM','回答和位置可交付；工程3另教覆核','完整三分工，手機較長','無任意外部specialist map輸入']),
'ad-anomalygpt-engineering-3':([23,23,19,18,9],['同圖位置/文字回查原痕跡','位置轉提示与模型輸出可追','文字与原圖三者核對','前兩段重申關鍵支路，第三段補工作','示意回答不當實際推論']),
'ad-anomalygpt-engineering-4':([24,23,19,18,9],['相同支架中部圖与孔邊錯答','定位正確也可能文字無據','同題比定位/對話的錯誤、延遲和工時','錯答橘框明确，不把假設當真','沒有替兩種流程捏造結果'])}
out=[]
for row in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')):
 if row['id'] not in notes:continue
 ss,why=notes[row['id']]
 for mode in ['desktop','mobile']:
  p=W/f"{row['id']}-{row['version']}-{mode}.png";sc=list(ss)
  if mode=='mobile':sc[3]-=1
  assert sum(sc)>90
  out.append(dict(id=row['id'],image=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scores=sc,total=sum(sc),evidence=why,completion={'aesthetics':[8,'藍頭黃結論與簡化工件'],'completeness':[9,row['takeaway']],'professionalism':[9,why[1]],'density':[8,'只保留本圖責任，仍有留白'],'hierarchy':[9,why[3]]},veto=[],native_review='passed',page_review='pending',user_approval='pending'))
(W/'first-rest-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
