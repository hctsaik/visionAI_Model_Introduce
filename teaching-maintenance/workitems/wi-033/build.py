"""Sequential build with fail-fast behavior; never bundle a failed source build."""
from pathlib import Path
import subprocess,sys
C=Path(__file__).resolve().parents[2]
for name in ['build_interactive_learning_html.py','build_github_pages_site.py']:
 subprocess.run([sys.executable,str(C/'tools'/name)],cwd=C,check=True)
