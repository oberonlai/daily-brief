# GitHub Idea 早報 · 2026-09-30（台北）

> 訊號：GitHub Trending（日／週／TS／Python）＋ Search（9/23 後新建高星／agent 沙盒執行時／DB×MCP 客戶端／自架部署平台／Next 可攜執行時／垂直熱點站框架／ChatGPT MCP 原生擴充／WP Markdown for Agents／Jev 型別決策外掛）。非 WP 為主；今日焦點是「給 agent 可驗證的沙盒、把資料庫與部署變成 agent 可操作面、Next 解鎖部署、垂直產業日報可複製、ChatGPT 插件像原生功能」，WP 側跟進「內容給 agent 讀」與「型別決策寫進主題／外掛」。

---

## 非 WP

### 1. Kernel 政策沙盒 → 形式驗證改權限 → Agent 艦隊執行時
- **來源**：[NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)（★~10.5k，今日 Trending）— 給自主 agent 用的安全私有 runtime：每個 agent 在隔離 sandbox 裡跑，kernel 層限制檔案／系統呼叫／網路；政策變更先做形式驗證才放行；含 gateway、supervisor、CLI／PyPI、`openshell sandbox create`；支援 Linux／Apple Silicon／WSL2（實驗），Apache-2.0。
- **標籤**：非 WP
- **為什麼值得做**：代理商與企業不敢把「會裝套件、會打 API」的 agent 直接丟本機；「可稽核沙盒＋政策閘門」比再賣一個 coding agent 更好鎖 B2B。
- **構想**：「OpenShell Desk TW」— 預設政策檔（只讀專案／禁外網／允許指定 MCP）、中文稽核報表、多專案隔離；Pro：團隊政策模板、Spend／檔案存取匯出；加 WP：建站 agent 只准寫指定 `wp-content` 路徑。
- **難度**：中高；切入：先包一種「Claude Code／Codex 進 sandbox」安裝器＋兩份政策模板。

### 2. 25MB 跨平台 DB 客戶端 → 內建 AI＋MCP → 資料庫操作台
- **來源**：[t8y2/dbx](https://github.com/t8y2/dbx)（★~21.9k，今日 Trending）— 約 25MB 輕量資料庫客戶端，支援 MySQL／PostgreSQL／SQLite／Redis／MongoDB／DuckDB／達夢等 100+；桌面／Docker／CLI、內建 AI 助手與 **MCP Server**；Apache-2.0，產品站 dbxio.com。
- **標籤**：非 WP
- **為什麼值得做**：中小團隊與電商仍用 GUI 管庫，卻缺「給 coding agent 受控查庫」的標準入口；MCP＋白名單查詢是清楚的訂閱／託管楔子。
- **構想**：「DBX Agency」— 連線加密保管、唯讀／寫入角色、查詢稽核、繁中 schema 註解；Pro：多租戶、與 Woo／自架 ERP 一鍵連；加 WP：本機／staging 的 `wpdb` 唯讀 MCP 給建站 agent。
- **難度**：中；切入：先做 MySQL／Postgres 兩種＋「唯讀 MCP 設定精靈」。

### 3. 指到 repo → 建置／路由／TLS → 自架部署平台
- **來源**：[oblien/openship](https://github.com/oblien/openship)（★~13.8k，今日 TS Trending）— 開源可自架部署平台：對準 repo 後負責 build、ship、路由與 TLS；桌面／Web dashboard／CLI／npm；Apache-2.0，openship.io。
- **標籤**：非 WP
- **為什麼值得做**：台灣代理商與 indie 想離開大廠 PaaS 帳單，又不要自己拼 GitHub Actions＋Caddy；「agent 可驅動的自架 PaaS」剛好接上昨日 golive 類 skill。
- **構想**：「OpenShip TW Node」— 一鍵裝到台灣 VPS、預設 WordPress／Next／靜態三種 pipeline、中文儀表；Pro：多客戶隔離、用量計費、與 OpenShell 沙盒串部署前驗收。
- **難度**：中；切入：先穩「靜態＋Node」兩條流水線＋一種台灣雲主機安裝腳本。

### 4. Vite 重實作 Next API → 一鍵遷離鎖定 → 隨處部署
- **來源**：[cloudflare/vinext](https://github.com/cloudflare/vinext)（★~9.0k，今日 TS Trending）— Vite plugin 重實作 Next.js API surface，目標「寫 Next、部署任意處」；`create-vinext-app`／`vinext init`／`vinext check`，並附 AI coding agent skill；MIT，vinext.dev。
- **標籤**：非 WP
- **為什麼值得做**：大量 SaaS／行銷站卡在 Vercel／特定 runtime；「相容檢查＋遷移 skill」本身就能做成顧問產品或託管遷移服務。
- **構想**：「ViNext Move」— 掃描現有 Next app → 相容報告 → 自動 PR；Pro：Cloudflare／自架雙目標、回歸測試包；加 WP：headless WP＋Next 前端的遷移模板。
- **難度**：中；切入：先做 `vinext check` 報告 SaaS（上傳 repo → PDF／Notion 報告）。

### 5. 換信源＋精選 KnowHow → 垂直產業熱點站 → 自動日報
- **來源**：[KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT)（★~3.0k，9/28 新建）— 自架熱點／日報網站框架：採集→預篩→雙重打分→中文標題摘要→事件聚簇→熱度→成刊；提示詞與門檻都在 repo，Docker Compose＋Postgres；示範站 aihot.news，MIT。
- **標籤**：非 WP
- **為什麼值得做**：法律／HR／金融／電商都想要「自己的 AI 早報」，但不懂管線；這正是可白標的垂直媒體 SaaS，也與本機 daily-brief 路線同源。
- **構想**：「Industry Hot Desk」— 產業信源包（台灣電商／WP 生態／SaaS）、繁中精選門檻、LINE／Email 晨報；Pro：多品牌白標、客戶自訂 KnowHow、MCP 把精選事件餵給研究 agent。
- **難度**：低～中；切入：先做「台灣電商／WP」一套信源＋門檻＋晨報輸出。

### 6. MCP 擴充 → 側欄／檔案檢視／@提及／表單 → ChatGPT 原生感插件
- **來源**：[openai/mcp-extensions](https://github.com/openai/mcp-extensions)（★~169，9/29 新建）— 為 MCP 加上 ChatGPT 專屬能力：側欄 entrypoint、檔案副檔名自訂檢視、composer @mention、擴充表單（含縮圖選擇）；TS／Python SDK，Apache-2.0；示範 Bits & Bolts。
- **標籤**：非 WP
- **為什麼值得做**：MCP 工具很多，但在 ChatGPT 裡仍像「外掛聊天」；「像原生產品面」才賣得動目錄位與顧問案。
- **構想**：「Native MCP Studio」— 幫電商／CAD／文件庫做側欄＋檔案檢視器；Pro：設計系統模板、審核上架檢查清單；加 WP：文章／媒體庫在 ChatGPT 側欄可搜可插。
- **難度**：中；切入：先做一種「產品目錄／零件庫」側欄＋@mention 範本。

---

## WP

### 7. 文章／頁面 → `/markdown` 與 `?markdown=true` → Agent 可讀內容層
- **來源**：[Automattic/content-for-agents](https://github.com/Automattic/content-for-agents)（★~2，9/10 新建，VIP beta）— WordPress VIP 外掛：在 `{permalink}/markdown` 與 `markdown=true` 提供帶 YAML frontmatter 的 Markdown；區塊／經典編輯器都轉可讀 Markdown，並在 HTML 頁宣告 alternate；衍生自 Pew Research Center 的 PRC Markdown for Agents；需 WP 7.0+／PHP 8.2+／VIP runtime（beta，勿直接上正式站）。
- **標籤**：WP
- **為什麼值得做**：AEO／llms.txt 時代缺的是「機器穩定讀正文」，不是再一個聊天框；代理商可把「給 agent 的內容層」做成加值服務。
- **構想**：「Agent Readable WP」— 非 VIP 相容版、`llms.txt`／sitemap 對接、欄位白名單、快取失效；Pro：多站 MainWP、與 MaskDesk 脫敏後再給雲端 agent。
- **難度**：中；切入：先做自架相容的 `/markdown`＋一種 frontmatter 約定＋Playground 示範。

### 8. 主題／外掛 → 問 Jev 得機率／選項／分數 → 可分支的型別決策
- **來源**：[juanlentino/jev-connector](https://github.com/juanlentino/jev-connector)（★~2，9/18 新建）— WordPress 連接 TypeSafe Jev System One：用 PHP API 對內容提問，回傳可分支的機率（noul）／具名選項／分數＋信心值；範例可直接 `wp_spam_comment`；WP 7.0+，GPL-2.0，目錄審核中。
- **標籤**：WP
- **為什麼值得做**：評論垃圾、客服分流、內容分級若再靠「解析 LLM 散文」一定碎；「型別決策 API」是代理商敢寫進生產邏輯的形狀。
- **構想**：「Jev Gate for WP」— 預設問題包（垃圾留言／退貨風險／SEO 意圖）、後台信心閾值、稽核日誌；Pro：A／B 閾值、與 Woo 訂單風險串接。
- **難度**：低～中；切入：先做留言垃圾一條規則＋後台閾值 UI。

---

## 今日脈絡（一句）
產品化焦點從「再包一個 chatbot」轉向「可驗證的 agent 執行時、DB／部署的 MCP 操作面、Next 可攜、垂直產業日報可複製、ChatGPT 原生插件面」；WP 側可跟進 Markdown-for-agents 內容層與 Jev 型別決策寫回。

## 備註
- 掃過未採用已記入 seen（含 PageIndex／VoltAgent／InferenceX／BeefTV／iCode／ouroboros 等延後、下載器／星刷 API gateway、CVE／PoC、預設主題 Ipsum 弱 SaaS 楔子等）。
- 未把 exploit／PoC 當產品構想來源。
