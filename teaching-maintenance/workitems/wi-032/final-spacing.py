from pathlib import Path
import subprocess,sys
W=Path(__file__).resolve().parent;C=W.parents[1]
id='yolo-world-engineering-2';p=W/(id+'-r05.md');p.write_text((W/(id+'-r04.md')).read_text(encoding='utf-8')+'\n## r05\n文字引導綠箭頭繞右邊，避免穿過max/sigmoid標註。原生／頁內待核對。\n',encoding='utf-8')
subprocess.run([sys.executable,'-X','utf8',str(C/'tools/validate_teaching_preflight.py'),str(p)],check=True,stdout=subprocess.DEVNULL)
p=W/'render-engineering.py';s=p.read_text(encoding='utf-8').replace("+'-r04-'+mode","+'-r05-'+mode");p.write_text(s,encoding='utf-8')
subprocess.run([sys.executable,'-X','utf8',str(p),id],check=True)
# Inject evidence links beside the existing explanations without replacing them.
p=C/'tools/build_interactive_learning_html.py';s=p.read_text(encoding='utf-8')
old='${plain}${technical}${takeaways}${next ?'
new='${plain}${(slide.evidenceLinks || []).map(link => `<p class="retained-evidence"><a href="${escapeHTML(link.image)}" target="_blank" rel="noopener">${escapeHTML(link.title)} ↗</a></p>`).join("")}${technical}${takeaways}${next ?'
assert old in s;s=s.replace(old,new,1);p.write_text(s,encoding='utf-8')
