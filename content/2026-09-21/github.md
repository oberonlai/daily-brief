# GitHub Idea 早報 · 2026-09-21（台北）

> 訊號：GitHub Trending（日／週）＋ Search（新建高星／MCP）。非 WP 為主；今日新建 WP 高星偏薄。

---

## 非 WP

### 1. Agent-native 應用框架 → 垂直 Agent SaaS 底座
- **來源**：[BuilderIO/agent-native](https://github.com/BuilderIO/agent-native)（★~5.2k，今日 trending）— 用來打造 agentic apps 的框架（React／TypeScript）。
- **標籤**：非 WP
- **為什麼值得做**：市場從「聊天框」轉成「可操作的 agent 產品」；有明確 SDK＝可做成託管 runtime／模板市集。
- **構想**：「Agency Agent Studio」— 給代理商拖拉式組裝「客服／SEO／報價」agent，接 WP REST／Woo，按客戶站點月費。
- **難度**：中高；切入：先做 1 個垂直模板（Woo 客服）＋託管 sandbox。

### 2. Generative UI（JSON → 畫面）→ 儀表板／表單 SaaS
- **來源**：[vercel-labs/json-render](https://github.com/vercel-labs/json-render)（★~17k，今日 trending）— Generative UI framework：模型輸出結構化 JSON 直接渲染 UI。
- **標籤**：非 WP
- **為什麼值得做**：AI 產品最大摩擦是「文字回覆不夠可操作」；JSON UI 可賣給內部工具、客製後台、WP 外掛設定精靈。
- **構想**：「FormForge」— 用自然語言生成多步驟表單／報價器，匯出 React 或 Gutenberg 區塊；給 SaaS onboarding 與 WP 落地頁。
- **難度**：中；切入：鎖定「報價／問卷／onboarding」三類 schema。

### 3. 跨 OS Computer-use 車隊 → 自動化 RPA／評測平台
- **來源**：[trycua/cua](https://github.com/trycua/cua)（★~25k，今日 +1k 星）— Computer-use 2.0：開源驅動、跨 OS fleets、訓練／評測／資料產生。
- **標籤**：非 WP
- **為什麼值得做**：瀏覽器 MCP 之外，桌面與多機編排是下一個瓶頸；可對代理商賣「夜間批次改站／截圖驗收」。
- **構想**：「Night Shift Fleet」— 客戶提交「驗收腳本」，雲端／自架 agent 在乾淨環境跑完回傳影片＋差異報告；WP 版預載 wp-env。
- **難度**：高；切入：先做單一 Linux 容器＋截圖 diff MVP。

### 4. 平行 AI agent 的 Git worktree CLI → 開發者工具
- **來源**：[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)（★~8.2k，本週 trending）— 專為平行 AI agent 工作流設計的 Git worktree CLI。
- **標籤**：非 WP
- **為什麼值得做**：一人多 agent 已成常態；「分支／目錄／環境隔離」是可收費的 DX 層，也適多客戶 WP 維護。
- **構想**：「Repo Lane」— 桌面／CLI：一 issue 一 worktree，綁 Claude／Codex，合併前自動跑測試；代理商方案支援多客戶遠端 repo。
- **難度**：中；切入：包裝 worktrunk＋預設測試 hook＋簡單 UI。

### 5. MCP → OpenAPI 閘道 → 平台／整合中介
- **來源**：[TiancongLx/open-mcp-gateway](https://github.com/TiancongLx/open-mcp-gateway)（★~51，9/20 新建）— 高效能 MCP-to-OpenAPI 3.1 閘道，對齊 Open WebUI 生態。
- **標籤**：非 WP
- **為什麼值得做**：企業要的是 OpenAPI／現有 API 閘道，不是再學一套 MCP；「雙向翻譯＋配額／稽核」是經典中介收費點。
- **構想**：「MCP Bridge Cloud」— 把公司內部 REST／WP REST 一鍵曝成 MCP，或反過來讓 MCP 工具進 API gateway；含用量計費與 allowlist。
- **難度**：中；切入：先支援 WP REST＋一組常用 MCP server。

### 6. YouTube 頻道全流程 Agent Skills → 內容成長 SaaS
- **來源**：[Jakeschincariol/youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill)（★~44，9/16）— 11 個 Claude skills：腳本／hook 評分、標題縮圖配對、EDL、留存分析、Shorts、病毒引擎。
- **標籤**：非 WP
- **為什麼值得做**：創作者與課程／外掛行銷都缺「可重複的發布流水線」；skills 開源＝可做成託管工作台。
- **構想**：「Channel OS」— 連 YouTube＋WP 部落格：一題材同時產出長片腳本、Shorts、文章與社群文；訂閱制＋繁中模板。
- **難度**：中低；切入：先做 hook／標題／縮圖評分 Web UI。

---

## WP

### 7. 技術堆疊線索資料集 → 代理商開發／電商名單
- **來源**：[leadita/tech-stack-datasets](https://github.com/leadita/tech-stack-datasets)（★~78）— 依技術（含 Shopify、Stripe、**WooCommerce**、HubSpot 等）分組的公司／網站開放資料（CSV／JSON）。
- **標籤**：WP（電商／代理商開發向）
- **為什麼值得做**：WP／Woo 代理最貴的是找對客戶；可查「誰在用 Woo／競品」直接變成名單產品。
- **構想**：「Stack Radar TW」— 台灣／華語站過濾＋週更 Woo／Elementor／特定外掛訊號，CRM 一鍵匯出；Freemius 作者可買「競品用戶名單」。
- **難度**：低～中；切入：先包 WooCommerce 分片＋ enrichment（Whois／流量粗標）。

### 8. 進階分類排除外掛 → 內容／會員站控制
- **來源**：[ArchitectOfRuin/advanced-category-excluder](https://github.com/ArchitectOfRuin/advanced-category-excluder)（★~4，9/19 新建）— 從文章、feed、搜尋等查詢排除分類的 WP 外掛（PHP 7.4+）。
- **標籤**：WP
- **為什麼值得做**：今日新建 WP 高星稀少；分類可見性仍是會員、課程、多品牌站的剛需，可做成規則引擎升級版。
- **構想**：「Audience Gates」— 依角色／方案／UTM 動態排除分類與區塊；給會員外掛／EDD 互補，含可視化規則。
- **難度**：低；切入：REST＋區塊編輯器條件 UI。

---

## 今日脈絡（一句）
Agent 應用層（native apps、generative UI、平行 worktree、MCP 閘道）與 computer-use 基建同天熱；WP 新建高星偏薄，技術堆疊名單與查詢控制仍是務實切入。

## 備註
- 掃過未採用已記入 seen（含金融／GPU 編排老專案、Jev 周邊實驗、明顯 SEO 灌水 EDD 文、PoC／逆向等）。
- 未收錄：`hirotomasato/yowes`（偽造證件向，不適合作產品靈感）。
