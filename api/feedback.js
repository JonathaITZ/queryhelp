const https = require("https");
const fs = require("fs");
const path = require("path");

const GITHUB_USER = "JonathaITZ";
const REPO_NAME = "queryhelp";
const GITHUB_TOKEN = process.env.GITHUB_TOKEN || "";

// Cache em memória para requisições rápidas no serverless
let memoryFeedbacks = [];

function getGitHubFile(filePath) {
  return new Promise((resolve) => {
    const options = {
      hostname: "api.github.com",
      path: `/repos/${GITHUB_USER}/${REPO_NAME}/contents/${filePath}`,
      method: "GET",
      headers: {
        "User-Agent": "QueryHelp-Feedback-API",
        "Authorization": `Bearer ${GITHUB_TOKEN}`,
        "Accept": "application/vnd.github.v3+json"
      }
    };

    const req = https.request(options, (res) => {
      let data = "";
      res.on("data", (chunk) => { data += chunk; });
      res.on("end", () => {
        try {
          if (res.statusCode === 200) {
            const json = JSON.parse(data);
            const content = Buffer.from(json.content, "base64").toString("utf-8");
            return resolve({ sha: json.sha, data: JSON.parse(content) });
          }
          resolve({ sha: null, data: [] });
        } catch (e) {
          resolve({ sha: null, data: [] });
        }
      });
    });

    req.on("error", () => resolve({ sha: null, data: [] }));
    req.end();
  });
}

function updateGitHubFile(filePath, contentObj, sha) {
  return new Promise((resolve) => {
    const rawContent = JSON.stringify(contentObj, null, 2);
    const b64 = Buffer.from(rawContent, "utf-8").toString("base64");

    const payload = JSON.stringify({
      message: "feat(feedback): new user query error report",
      content: b64,
      branch: "main",
      ...(sha ? { sha } : {})
    });

    const options = {
      hostname: "api.github.com",
      path: `/repos/${GITHUB_USER}/${REPO_NAME}/contents/${filePath}`,
      method: "PUT",
      headers: {
        "User-Agent": "QueryHelp-Feedback-API",
        "Authorization": `Bearer ${GITHUB_TOKEN}`,
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json",
        "Content-Length": Buffer.byteLength(payload)
      }
    };

    const req = https.request(options, (res) => {
      let resp = "";
      res.on("data", (chunk) => { resp += chunk; });
      res.on("end", () => {
        resolve(res.statusCode === 200 || res.statusCode === 201);
      });
    });

    req.on("error", () => resolve(false));
    req.write(payload);
    req.end();
  });
}

module.exports = async function handler(req, res) {
  // CORS Headers
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");

  if (req.method === "OPTIONS") {
    return res.status(204).end();
  }

  // GET: Listar todos os feedbacks salvos no banco / repositório
  if (req.method === "GET") {
    try {
      // Tenta ler local primeiro se existir
      const localPath = path.join(process.cwd(), "data", "feedbacks.json");
      if (fs.existsSync(localPath)) {
        try {
          const fileData = JSON.parse(fs.readFileSync(localPath, "utf-8"));
          if (Array.isArray(fileData) && fileData.length > 0) {
            return res.status(200).json({ success: true, count: fileData.length, feedbacks: fileData });
          }
        } catch (_) {}
      }

      // Se não, busca do repositório remoto permanente
      const gh = await getGitHubFile("data/feedbacks.json");
      const list = gh.data && Array.isArray(gh.data) ? gh.data : memoryFeedbacks;
      return res.status(200).json({ success: true, count: list.length, feedbacks: list });
    } catch (err) {
      return res.status(200).json({ success: true, count: memoryFeedbacks.length, feedbacks: memoryFeedbacks });
    }
  }

  // POST: Registrar novo feedback de erro
  if (req.method === "POST") {
    let body = req.body;
    if (typeof body === "string") {
      try { body = JSON.parse(body); } catch (e) { body = {}; }
    } else if (!body) {
      body = {};
    }

    const system = (body.system === "softshop") ? "softshop" : "softcomshop";
    const user_prompt = String(body.user_prompt || body.prompt || "").trim();
    const generated_sql = String(body.generated_sql || body.sql || "").trim();
    const error_type = String(body.error_type || "Incorreto").trim();
    const feedback_notes = String(body.feedback_notes || body.notes || "").trim();

    if (!feedback_notes && !error_type) {
      return res.status(400).json({ error: "Informe os detalhes do erro para enviar o feedback." });
    }

    const newFeedback = {
      id: "fb-" + Date.now() + "-" + Math.random().toString(36).substring(2, 6),
      created_at: new Date().toISOString(),
      system: system,
      system_name: (system === "softshop") ? "Softshop Desktop (SQL Server)" : "Softcomshop Web (MySQL)",
      user_prompt: user_prompt,
      generated_sql: generated_sql,
      error_type: error_type,
      feedback_notes: feedback_notes,
      status: "PENDENTE"
    };

    // 1. Grava no cache de memória imediato
    memoryFeedbacks.unshift(newFeedback);

    // 2. Grava no arquivo local se o diretório permitir
    try {
      const dataDir = path.join(process.cwd(), "data");
      if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });
      const localPath = path.join(dataDir, "feedbacks.json");
      let current = [];
      if (fs.existsSync(localPath)) {
        try { current = JSON.parse(fs.readFileSync(localPath, "utf-8")); } catch (_) {}
      }
      current.unshift(newFeedback);
      fs.writeFileSync(localPath, JSON.stringify(current, null, 2), "utf-8");
    } catch (_) {}

    // 3. Grava no repositório GitHub permanente via API assíncrona
    try {
      const gh = await getGitHubFile("data/feedbacks.json");
      const currentList = Array.isArray(gh.data) ? gh.data : [];
      currentList.unshift(newFeedback);
      await updateGitHubFile("data/feedbacks.json", currentList, gh.sha);
    } catch (err) {
      console.error("Erro ao persistir feedback no GitHub:", err);
    }

    return res.status(200).json({
      success: true,
      message: "Feedback registrado no banco com sucesso! Obrigado pelo reporte.",
      feedback: newFeedback
    });
  }

  return res.status(405).json({ error: "Método não permitido." });
};
