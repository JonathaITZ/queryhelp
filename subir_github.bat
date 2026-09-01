@echo off
chcp 65001 > nul
setlocal

set "PATH=C:\Users\dantas.jonatha\MinGit\cmd;%PATH%"

echo =======================================================
echo    🚀 QueryHelp - Sincronizador GitHub & Vercel
echo    Desenvolvido por: Jonatha Dantas
echo =======================================================
echo.

echo [1/3] Verificando status dos arquivos locais...
git status
echo.

echo [2/3] Adicionando arquivos alterados...
git add -A
echo.

set /p MSG="Digite a mensagem do commit (ou de Enter para padrao): "
if "%MSG%"=="" set MSG=sync: atualizacao do projeto QueryHelp - Jonatha Dantas

git commit -m "%MSG%"
echo.

echo [3/3] Enviando para o GitHub (origin main)...
git push origin main

echo.
if %ERRORLEVEL% equ 0 (
    echo [OK] Sucesso! Arquivos enviados ao GitHub e a Vercel iniciou o deploy!
) else (
    echo [AVISO] Se o push pedir autenticacao, faca o login com seu GitHub ou use seu Personal Access Token.
)

echo.
pause
