# GitHub Idea 早報 · 2026-10-01（台北）

> 訊號：GitHub Trending（日／週／Python／TS）＋ Search（9/24 後新建高星／agent 瀏覽器／程式碼知識圖／Jev 推理決策／多 agent harness／無向量知識庫／SEO skill／WP 權限化 MCP／WP 執行期安全）。非 WP 為主；今日焦點是「給 coding agent 可外科手術的本機圖索引、不被擋的瀏覽器執行時、可累積的 wiki 知識層、會先思考再決策的 Jev、可編排多 harness 的宿主、可賣的 SEO agent 技能包」，WP 側跟進「能力開關＋Undo＋稽核的 MCP」與「追到外掛檔案行號的執行期監控」。

---

## 非 WP

### 1. 程式碼預建圖 → 跨檔語意索引 → Agent 少 token 外科手術
- **來源**：[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)（★~72.6k，今日 Trending）— 本機預索引程式碼知識圖，檔案變更自動同步；給 Claude Code／Codex／Cursor／Gemini／Hermes 等用，減少 token 與 tool call；Rust kernel、MCP tools、框架路由感知；平台產品（PR 影響面／測什麼）在 waitlist（getcodegraph.com）；MIT。
- **標籤**：非 WP
- **為什麼值得做**：代理商與產品團隊不是缺另一個 chat，而是缺「改這支 PR 會炸哪條路徑」；圖索引＋影響報告是清楚的 B2B／託管楔子。
- **構想**：「CodeGraph Desk TW」— 一鍵索引客戶 monorepo、繁中影響報告、PR 風險徽章；Pro：多客戶隔離、與 CI 串「必測清單」；加 WP：外掛／主題目錄圖＋`wpdb`／hook 依賴面。
- **難度**：中；切入：先做「上傳／連 repo → PDF／Notion 影響報告」＋一種 Claude Code 安裝包。

### 2. 真 Firefox 指紋 → 一人一 seed → 不被擋的瀏覽器 Agent
- **來源**：[feder-cr/dots](https://github.com/feder-cr/dots)（★~1.9k，9/29 新建）— 開源 web agent：模型可換，瀏覽器才是網站看到的身分；C++ 修過的 Firefox、一致指紋、可信指標事件、profile 記憶登入；可經 MCP（invisible_playwright_mcp）接到 Claude／Codex；MIT。
- **標籤**：非 WP
- **為什麼值得做**：競品監控、電商比價、政府／航空查詢常死在「被擋」；「可稽核的反偵測瀏覽器艦隊」比再包一個 scraper 好賣。
- **構想**：「Dots Fleet TW」— 台灣代理／出口 IP、任務佇列、錄影稽核、失敗重試；Pro：多租戶、合規白名單網域；加 WP：競品主題／價格巡檢寫回 Woo 草稿。
- **難度**：中高；切入：先做「單一種子＋一種台灣電商巡檢模板」＋稽核影片匯出。

### 3. 長文編譯成 Wiki → 無向量檢索 → 可累積的公司知識層
- **來源**：[VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB)（★~4.7k，Python Trending）— 把 PDF／Office／URL 等編成互相連結的 wiki 知識庫（PageIndex 無向量推理檢索）；支援多模態、實體頁、OKF、Obsidian、Skill Factory、Web UI；Apache-2.0，openkb.ai。
- **標籤**：非 WP
- **為什麼值得做**：中小團隊 RAG 一問一忘；「先編譯再問、知識會複利」正好做成垂直知識台與顧問交付物。
- **構想**：「OpenKB Agency」— 產業模板（電商／法規／客服 SOP）、繁中編譯門檻、LINE／Notion 出口；Pro：多品牌白標、Skill Factory 產出客戶專屬 agent skill；加 WP：把說明文件／FAQ 編成 wiki 再餵建站 agent。
- **難度**：中；切入：先做「上傳 20 份 PDF → Obsidian 相容 wiki＋一頁查詢 UI」。

### 4. 先推理再決策 → Jev 相容 API → 可上線的型別決策層
- **來源**：[PostHog/jeeves](https://github.com/PostHog/jeeves)（★~336，9/29 新建）— 會先思考再決策的 Jev 風格分類器（Qwen3.5-9B＋diffusion drafter）；支援 noul／choice／score；JevBench 公開集優於 Jev；MIT，權重在 Hugging Face。
- **標籤**：非 WP
- **為什麼值得做**：客服分流、審核、風控若再解析 LLM 散文一定碎；「可校準機率＋同 API」是代理商敢寫進生產的形狀（延續昨日 Jev Gate）。
- **構想**：「Jeeves Gate Cloud」— 託管／自架雙路徑、繁中問題包、信心閾值與 A／B；Pro：與 PostHog／自有事件串、稽核匯出；加 WP：留言／退貨／SEO 意圖走同一決策 API。
- **難度**：中高；切入：先包 Docker 推論＋三種問題模板＋簡單儀表。

### 5. 宿主編排多 Agent → DAG／專責角色 → 可驗證的 Harness 艦隊
- **來源**：[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)（★~5.0k）—「harness of harnesses」：把內建（Research／Code／Design／Oncall）與第三方 agent 編成 DAG；支援 RSI 自我改進、EverOS 長期記憶；預 alpha，Apache-2.0，raven.evermind.ai。
- **標籤**：非 WP
- **為什麼值得做**：企業要的是「一任務多專長、可監督」，不是再一個全能 bot；編排＋驗收閘門可做成專案制 SaaS。
- **構想**：「Raven Desk TW」— 預設產業 DAG（研調→設計→實作→驗收）、中文監督台、花費上限；Pro：客戶沙盒、與 OpenShell 類執行時串接；加 WP：建站流水線固定節點（內容／版型／上線檢查）。
- **難度**：高；切入：先做一種「四節點 DAG 模板＋人工核准閘」示範，不碰 RSI 本體。

### 6. 26 子技能＋19 子代理 → GEO／AEO／報表 → 可賣的 SEO Agent 作業系統
- **來源**：[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)（★~18.0k，Python Trending）— Claude Code 通用 SEO skill：技術 SEO、E-E-A-T、schema、GEO／AEO、agent readiness（Lighthouse Agentic、WebMCP、llms.txt）、在地／電商／國際、PDF／Excel 報告；可接 DataForSEO／Firecrawl／Ahrefs／Matomo；MIT，claude-seo.md。
- **標籤**：非 WP
- **為什麼值得做**：台灣代理商 SEO 交付仍靠人肉檢查表；「可重跑的技能包＋客戶報告」是訂閱與專案加值的直接入口。
- **構想**：「SEO Skill Desk」— 繁中檢查清單、台灣在地／電商預設、月報白標；Pro：多站 MainWP 巡檢、與 Trends／爬蟲信源串；加 WP：Yoast／Rank Math 欄位一鍵套用（審核後寫入）。
- **難度**：低～中；切入：先做「單站技術＋AEO 掃描 → 繁中 PDF」一條流水線。

---

## WP

### 7. 能力預設關閉 → 唯讀／Undo／稽核 → 敢交給 Agent 的 WP MCP
- **來源**：[the-anup-das/att-mcp-abilities](https://github.com/the-anup-das/att-mcp-abilities)（★~0，9/28 新建）— WordPress 外掛：經 MCP 讓 agent 讀／建／改站；逐能力開關、唯讀模式、寫入速率、Undo 快照、稽核日誌；涵蓋內容／設計／Elementor／GeneratePress／Rank Math 等；需 WP 6.9+ 與 MCP Adapter；GPL-2.0。
- **標籤**：WP
- **為什麼值得做**：全開 MCP 沒人敢上正式站；「預設關、可還原、可追查」才是代理商的上架條件與維護合約。
- **構想**：「Safe MCP for WP」— 繁中政策模板（只讀內容／允許草稿／禁裝外掛）、每日摘要 Email、多站同步政策；Pro：與 MainWP／託管面板串、客戶核准佇列。
- **難度**：中；切入：先穩「唯讀＋文章草稿＋Undo」三條能力＋Playground 示範。

### 8. 外連／假回應／新管理員／檔案變更 → 追到外掛行號 → 執行期安全哨兵
- **來源**：[muzychenko-dev/nightward](https://github.com/muzychenko-dev/nightward)（★~1，9/28 新建）— WordPress 執行期安全監控：追蹤 outbound、偽造 HTTP 回應、新管理員、檔案變更，並標到外掛檔案與行號；每日 Email 與即時警報。
- **標籤**：WP
- **為什麼值得做**：CVE 掃完仍怕「活著的惡意外掛」；「誰在打外網、哪一行改了檔」是維護合約與加值監控的核心 KPI。
- **構想**：「Nightward Desk」— 多站匯總、繁中風險等級、可疑外連白／黑名單；Pro：與 WPAuditor 類稽核互補、自動開工單；搭配 CVE 熱點季提供「加固巡檢」專案。
- **難度**：低～中；切入：先做單站安裝＋每日摘要 LINE／Email＋三種高風險規則。

---

## 今日脈絡（一句）
產品化焦點從「再包一個 chatbot」轉向「本機程式碼圖、不被擋的瀏覽器、可累積 wiki 知識、會推理的型別決策、多 harness 編排、可賣的 SEO skill」；WP 側可跟進權限化 MCP（開關／Undo／稽核）與追到行號的執行期哨兵。

## 備註
- 掃過未採用已記入 seen（含 openclaw／nanobot／GenericAgent／Trends-MCP／aws agent-toolkit／Composio awesome-skills／wp-godmode／tqk-wp-seo／pencil／plasma／CVE／PoC／星刷與破解軟體等）。
- 未把 exploit／PoC／惡意軟體當產品構想來源。
