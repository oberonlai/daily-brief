# GitHub Idea 早報 · 2026-09-25（台北）

> 訊號：GitHub Trending（日／週）＋ Search（9/20 後新建高星／MCP／WP）。非 WP 為主；今日新建爆點集中在「agent 上線／模型路由／記憶／MCP 閘道」，WP 側有 PHP agent 引擎與 AI 主題前端編輯。

---

## 非 WP

### 1. Agent 一鍵上線 → 「自有帳號」上線 SaaS／Skill 產品
- **來源**：[mikehasa/golive-skill](https://github.com/mikehasa/golive-skill)（★~847，9/23 新建）— Agent Skill＋零依賴 Node CLI：偵測 → 計畫 → 核准 → 套用 → 驗證；託管、資料庫、網域、郵件、金流走你自己的帳號，無 GoLive 後端／遙測。
- **標籤**：非 WP
- **為什麼值得做**：vibe coding 卡在「做得出來、上不了線」；開源 skill 把 DevOps 變成可核准步驟＝可做成代理商／獨立開發者的上線工作台。
- **構想**：「GoLive Desk」— 預設 Vercel／Cloudflare／Neon／Stripe／Resend 腳本；賣「核准閘道＋稽核紀錄」給代理商；加 WP 方案：外掛 zip 建置 → 暫存站 → 正式站切換。
- **難度**：中；切入：先做 detect→plan→approve 三步 Web UI，只接一個託管＋一個 DB。

### 2. 多 Agent 共用模型選單 → 模型路由／成本控管 SaaS
- **來源**：[yetone/magpie](https://github.com/yetone/magpie)（★~597，9/23 新建）— 選單列統一管理每個 coding agent 的模型：Codex 跑 DeepSeek、Claude Code 跑 Kimi 等。
- **標籤**：非 WP
- **為什麼值得做**：團隊已同時開 Codex／Claude／Cursor；模型切換與預算是剛需，也是可白牌給主機商／顧問的切入點。
- **構想**：「Model Switchboard」— 團隊政策（誰可用哪個模型、每日額度）、用量儀表；接公司 OpenRouter／自架 gateway。
- **難度**：中；切入：先做本機選單列＋單一 API key 輪替，再加團隊政策。

### 3. 會學習的 Agent Memory → 長期記憶／交接 SaaS
- **來源**：[vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)（★~27.7k，今日 trending 約 +1.6k）— Agent Memory That Learns：記憶會隨互動進化，不只是向量堆。
- **標籤**：非 WP
- **為什麼值得做**：多日／多工具 agent 最大痛是失憶與交接；「可學習記憶」比單純 RAG 更可收費。
- **構想**：「Agency Memory Cloud」— 客戶專案記憶隔離；WP 代理商把站況、外掛決策、客訴承諾寫進記憶，換人或換 agent 可接續。
- **難度**：中高；切入：先做 SQLite／單租戶 MCP memory，驗證「換 session 仍記得承諾」。

### 4. 聊天承諾／關係記憶 → 客服／業務「首席幕僚」產品
- **來源**：[georgeding/Relate](https://github.com/georgeding/Relate)（★~97，9/23 新建）— 自架 AI 聊天首席幕僚：記得對方說過什麼、你答應過什麼。
- **標籤**：非 WP
- **為什麼值得做**：客服與業務最貴的是漏承諾；開源「關係記憶」可垂直成電商／顧問 CRM 加值。
- **構想**：「Promise Desk」— 接 LINE／Discord／郵件摘要，抽出承諾與到期；WP／Woo 訂單備註自動回寫。
- **難度**：中；切入：先做「承諾抽取＋到期提醒」單頻道 MVP。

### 5. Agent↔MCP 零信任閘道 → 企業 Agent 安全層
- **來源**：[Matthew0822/MCPBastion](https://github.com/Matthew0822/MCPBastion)（★~20，9/22 新建）— Agent 與 MCP 之間的零信任閘道：能力範圍、遮罩、速率／成本上限、可驗證 session log。
- **標籤**：非 WP
- **為什麼值得做**：企業敢接 MCP 的前提是可控；「政策＋稽核」比再多一個 MCP server 更好賣。
- **構想**：「MCP Policy Hub」— 代理商／SaaS 給客戶站掛白名單工具（只讀 WP REST、禁刪庫）；月費含審計匯出。
- **難度**：中；切入：先代理 3 個常見 MCP（filesystem／browser／db）＋ deny-by-default。

### 6. Prompt→透明循環 3D 圖示 → 品牌資產／區塊素材產品
- **來源**：[samyost1/3dicon](https://github.com/samyost1/3dicon)（★~380，9/23 新建）— Claude Code skill：一句 prompt 產出可循環動畫、真透明背景的 3D icon。
- **標籤**：非 WP
- **為什麼值得做**：落地頁／App icon／社群素材需求大；「可批次、可品牌化」可比純圖庫訂閱。
- **構想**：「Icon Loop Studio」— 品牌色板＋風格鎖定，批次出 WebM／APNG；輸出 Gutenberg 媒體庫與 Elementor widget。
- **難度**：低～中；切入：先做 CLI／skill 包＋品牌色參數，再接 WP 媒體上傳。

---

## WP

### 7. PHP 通用 AI Agent 引擎 → WP／Woo 站內 Agent 外掛
- **來源**：[phpclaw-php/phpclaw-monorepo](https://github.com/phpclaw-php/phpclaw-monorepo)（★~9，9/23 新建）— PHP 通用 AI agent 引擎：tools、memory、guards、ReAct；支援 Laravel／Symfony／WordPress 等，核心零框架依賴。
- **標籤**：WP
- **為什麼值得做**：多數 WP 站仍是 PHP 運行時；「站內可跑、可護欄」的 agent 比外掛一堆 AI 聊天框更可產品化。
- **構想**：「WP Claw」— 外掛包裝：內容草稿、Woo 訂單查詢、安全巡檢 tools；Pro 賣多站政策與稽核。
- **難度**：中；切入：先接 WP REST 讀寫＋一個 guard（禁直接 SQL）。

### 8. AI 主題前端就地編輯 → 「生成後可改」體驗產品
- **來源**：[rinothecoder/pencil-by-rino](https://github.com/rinothecoder/pencil-by-rino)（★~5，9/24 新建）— 給 AI 建好的 WordPress 主題做前端內容編輯。
- **標籤**：WP
- **為什麼值得做**：AI 建站最大摩擦是「生成完客戶改不動」；就地編輯是轉換與續約關鍵。
- **構想**：「Pencil for Agency」— 與 block theme／Elementor 生成流程串接：客戶只改文案與圖，結構鎖定；賣白牌給建站服務。
- **難度**：低～中；切入：先支援標題／段落／圖三類 inline edit。

---

## 今日脈絡（一句）
Agent 從「會寫碼」轉向「能上線、能記、能控成本與權限」；WP 側可跟進 PHP 原生 agent 引擎與 AI 主題可編輯體驗。

## 備註
- 掃過未採用已記入 seen（含日趨勢老專案、Jev 周邊、多帳號沙盒、CVE toolkit 本體等）。
- 未把 exploit／PoC 當產品構想來源。
