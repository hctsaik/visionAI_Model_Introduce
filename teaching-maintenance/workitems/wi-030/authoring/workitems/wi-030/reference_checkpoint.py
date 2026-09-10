from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
s='''
### WI-030 發布文件缺漏修正
最後查操作卡時發現本機docs缺少model.md／slide-manifest.md，原因是bundle只選圖與concept_path，未收modelPath／manifestPath。HTML雖有連結，但發布目標不存在；不是瀏覽器快取。已補builder依現有課程連結打包文件，會使其餘課程既有文件也可到達，不改其教材JSON。即將重建docs、測全部文件的來源／打包位元一致及十二課24個HTTP連結；原1231資產數屬修正前歷史，新總數待實際建置確認。公開部署尚未執行。
'''
for p in [W/'PLAN.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md',R/'WORKITEMS.md']:
 with p.open('a',encoding='utf-8') as f:f.write('\n'+s)
for p in [R/'TEACHING_WEBPAGE_GUIDE.md',R/'TEACHING_REVIEW_LOG.md']:
 with p.open('a',encoding='utf-8') as f:f.write('\n'+s+'\n文件連結也是交付內容：除了圖片HTTP，需檢查操作卡引用的Markdown是否隨發布包存在，來源與發布版本一致。\n')
