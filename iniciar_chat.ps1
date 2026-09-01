Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  Iniciando Chat Especialista em Estrutura SQL & Regras de Negócio" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Abrindo navegador em http://localhost:8080 ..." -ForegroundColor Green
Start-Process "http://localhost:8080"
& "C:\Users\dantas.jonatha\.gemini\antigravity\scratch\python\python.exe" "C:\Users\dantas.jonatha\.gemini\antigravity\scratch\app_chat_sql.py" 8080
