# 🚀 Especialista SQL - Softcomshop
> **Projeto Desenvolvido por: Jonatha Dantas**  
> *Engenharia de Dados, Arquitetura de Software & IA Generativa*

Este repositório contém a aplicação web completa criada por **Jonatha Dantas**, pronta para ser hospedada na **Vercel** ou no **GitHub Pages** e acessada publicamente pela internet de forma segura.

---

## 📁 Arquivos Inclusos:
* `index.html` — Interface web completa com Dark Mode, Glassmorphism e Logo HD integrada.
* `logo.jpg` — Logo oficial em alta definição.
* `schema.json` — Estrutura de metadados das 459 tabelas e 6.600 colunas.
* `api/ask.js` — Serverless Function para a Vercel.
* `vercel.json` — Configurações de rotas da Vercel.

---

## ⚡ Passo a Passo para Subir no GitHub e Vercel:

### 1. Inicializar o Git e Subir no GitHub:
Abra o terminal nesta pasta (`vercel-deploy`):

```bash
git init
git add .
git commit -m "Deploy Especialista SQL Softcomshop"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
git push -u origin main
```

### 2. Importar na Vercel:
1. Acesse [vercel.com](https://vercel.com/) e faça login com seu GitHub.
2. Clique em **"Add New..." ➔ "Project"**.
3. Selecione o repositório que você acabou de criar.
4. *(Opcional)* Em **Environment Variables**, você pode adicionar:
   * **Name:** `GEMINI_API_KEY`
   * **Value:** `Sua chave da API do Google AI Studio`
5. Clique em **"Deploy"**.

Em menos de **10 segundos**, você terá um link público HTTPS (ex: `https://especialista-sql.vercel.app`) para usar no computador ou celular!
