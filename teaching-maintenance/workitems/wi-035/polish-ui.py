from pathlib import Path
C=Path(__file__).resolve().parents[2]
p=C/'_course_content/poc-workbench.js';s=p.read_text(encoding='utf8')
old='<button class="button primary" type="button" data-action="poc-preview">預覽完整草稿 →</button>'
new='${app.pocPreview ? `<button class="button primary" type="button" data-action="export-poc-markdown">下載 PoC Markdown</button><p><button class="button" type="button" data-action="poc-step" data-step="${progress.pocStep || 0}">← 繼續編輯</button></p>` : `<button class="button primary" type="button" data-action="poc-preview">預覽完整草稿 →</button>`}'
assert s.count(old)==1;s=s.replace(old,new);p.write_text(s,encoding='utf8')
