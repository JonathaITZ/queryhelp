import os
import re

scratch_dir = r"C:\Users\dantas.jonatha\.gemini\antigravity\scratch"
patterns = {
    "Supabase Secret Key": r"sb_secret_[A-Za-z0-9_-]+",
    "Supabase Password": r"Tk8#mQ2\$vL9!xR4_wP7\*zY5N",
    "PostgreSQL Connection DSN": r"postgresql://[^:\s]+:[^@\s]+@",
    "Google Gemini API Key": r"AIzaSy[A-Za-z0-9_-]{33}",
    "JWT Token / Anon Key": r"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+"
}

findings = []
for root, dirs, files in os.walk(scratch_dir):
    if "python" in root or ".git" in root or "__pycache__" in root or "audit_security.py" in root:
        continue
    for f in files:
        if f.endswith((".py", ".js", ".html", ".sql", ".json", ".bat", ".ps1", ".md", ".env", ".txt")):
            path = os.path.join(root, f)
            rel_path = os.path.relpath(path, scratch_dir)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as fp:
                    content = fp.read()
                    for name, pat in patterns.items():
                        matches = re.findall(pat, content)
                        if matches:
                            findings.append({
                                "file": rel_path,
                                "secret_type": name,
                                "count": len(matches),
                                "sample": matches[0][:15] + "..." if len(matches[0]) > 15 else matches[0]
                            })
            except Exception:
                pass

print("=== RELATORIO DO SCANNER DE ARQUIVOS LOCAIS ===")
for item in findings:
    print(f"[{item['secret_type']}] no arquivo: {item['file']} ({item['count']} ocorrencias)")
