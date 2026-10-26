from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "index.html",
    "consultorio.html",
    "prontuario.html",
    "agenda.html",
    "financeiro.html",
    "servidor-favmed.ps1",
    "INICIAR-SERVIDOR-FAVMED.bat",
    "INSTRUCOES-REDE-LOCAL.txt",
    "README.md",
]
missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
if missing:
    print("Arquivos obrigatórios ausentes: " + ", ".join(missing), file=sys.stderr)
    sys.exit(1)

node = subprocess.run(["node", "--version"], capture_output=True, text=True)
if node.returncode:
    print("Node.js não está disponível para validar JavaScript.", file=sys.stderr)
    sys.exit(1)

script_pattern = re.compile(r"<script\b[^>]*>(.*?)</script\s*>", re.I | re.S)
for name in ("index.html", "consultorio.html", "prontuario.html", "agenda.html", "financeiro.html"):
    source = (ROOT / name).read_text(encoding="utf-8")
    scripts = script_pattern.findall(source)
    if not scripts:
        print(f"Nenhum script inline encontrado em {name}", file=sys.stderr)
        sys.exit(1)
    for number, script in enumerate(scripts, start=1):
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as temp:
            temp.write(script)
            temp_path = Path(temp.name)
        try:
            result = subprocess.run(["node", "--check", str(temp_path)], capture_output=True, text=True)
            if result.returncode:
                print(f"Erro de sintaxe JavaScript em {name}, bloco {number}:")
                print(result.stdout + result.stderr, file=sys.stderr)
                sys.exit(result.returncode)
        finally:
            temp_path.unlink(missing_ok=True)
    print(f"OK: {name} — {len(scripts)} bloco(s) JavaScript verificado(s)")

print("OK: arquivos obrigatórios presentes.")
