# GitHub Idea 早報 · 2026-09-27（台北）

> 訊號：GitHub Trending（日／週）＋ Search（9/21 後新建高星／Slack 記憶／決策模型／MCP 稽核／創意 code／WP ORM）。非 WP 為主；今日新建爆點集中在「Slack 公司大腦開源、程式繪製品牌動效、本機決策模型 runtime、AI coding 桌面管家、ChatGPT↔本機 MCP、MCP 資安稽核」，WP 側有 Prisma 風格 ORM 與一頁一語系輕量多語。

---

## 非 WP

### 1. Slack 對話 → 公司記憶 → 可自架的團隊大腦 SaaS
- **來源**：[supermemoryai/company-brain](https://github.com/supermemoryai/company-brain)（★~481，9/25 新建）— 原付費產品整包開源：掛在 Slack，記住團隊說過什麼，能開 issue／讀 PR／挖 repo，並在相關對話主動插嘴；跑在自有 Cloudflare Workers。
- **標籤**：非 WP
- **為什麼值得做**：代理商與遠端團隊知識散落在 Slack；「自架＋權限＋可做事」比再賣一個 chatbot 更好收費，也可白牌給主機商／顧問公司。
- **構想**：「Agency Brain」— 接 Slack／Discord／LINE，出專案記憶＋工單草稿；方案含客戶隔離租戶、敏感詞遮罩、只讀 MCP；加 WP：從工單一鍵產估價頁／報價區塊。
- **難度**：中高；切入：先做 Slack 匯入＋問答＋一類動作（開 GitHub issue），再加多租戶與計費。

### 2. Prompt → 可重繪插畫／動效 → 品牌視覺 Code 工廠
- **來源**：[alexgreensh/anidoodle](https://github.com/alexgreensh/anidoodle)（★~469，9/22 新建）— 手繪感藝術寫成程式：31 種風格、插畫／延時繪製片／互動網頁藝術；每筆畫與音符皆為函式，同原始碼在任何機器、任何尺寸重渲一致。
- **標籤**：非 WP
- **為什麼值得做**：品牌要「同一隻手」的圖與宣傳片，卻怕 AI 每次長不一樣；可重現的 code art 可賣成訂閱制品牌素材工廠。
- **構想**：「Brand Doodle Desk」— 選風格＋主題，出 SVG／MP4／互動頁；代理商方案：鎖定品牌色與筆觸；加 WP：區塊／媒體庫一鍵嵌入繪製過程短片。
- **難度**：中；切入：先做 3 風格＋靜態圖＋一種繪製延時片模板。

### 3. 客服／工單狀態 → 校準機率 → 本機決策模型 Runtime
- **來源**：[ollaya-dev/ollaya](https://github.com/ollaya-dev/ollaya)（★~395，9/23 新建）— 「決策模型版 Ollama」：本機 pull／serve Laya、decider、NLI、GLiClass；吃狀態＋ typed 問題，一次 forward 回校準機率，不產文字；相容 TypeSafe `/v1/systemone`。
- **標籤**：非 WP
- **為什麼值得做**：客服分流、退款、風險打分不需要長文 LLM；毫秒級本機決策可降成本與個資外流，適合代理商／電商後台。
- **構想**：「Triage Local」— 工單／表單進，出 intent／急迫／流失風險；接 Woo／客服 inbox；Pro：規則覆寫＋稽核 log。
- **難度**：中；切入：先包一種 triage preset＋OpenAI-compatible 端點＋單一來源 ingest。

### 4. 多把 AI coding CLI → 一鍵安裝／修復 → 桌面管家產品
- **來源**：[OnlistTeam/ai-manager](https://github.com/OnlistTeam/ai-manager)（★~311，9/21 新建）— Tauri 桌面：安裝、更新、設定、修復 Claude Code／Codex 等 AI coding CLI；不碰手改 shell profile／PATH；本機優先、AGPL。
- **標籤**：非 WP
- **為什麼值得做**：代理商與團隊同時養多把 agent，環境壞掉最耗支援；「艦隊健康儀表板」可做成 B2B 桌面＋遠端診斷訂閱。
- **構想**：「Agent Fleet Desk」— 偵測已裝工具、端點、金鑰健康；團隊方案：標準設定檔下發；加 WP 建站套件：交付前環境檢查清單。
- **難度**：中；切入：先支援 2–3 款 CLI 的偵測／安裝／健康檢查。

### 5. ChatGPT 對話 → 本機工具／MCP → 官方隧道 Agent 平台
- **來源**：[XiaoPuOuO/openchatx-mcp](https://github.com/XiaoPuOuO/openchatx-mcp)（★~129，9/23 新建）— 本機 MCP 平台：檔案／shell／電腦控制／Skills／Subagents；經 OpenAI 官方 Secure MCP Tunnel 接一般 ChatGPT Chat（非逆向、不吃 Work／Codex agent 額度）；有繁中 README。
- **標籤**：非 WP
- **為什麼值得做**：很多團隊已付 ChatGPT、卻缺本機工具鏈；「官方 MCP＋本機能力」可做成白牌桌面／託管閘道，尤其華語市場。
- **構想**：「ChatX Local」— 一鍵裝本機 MCP＋預設 Toolbox（檔案、瀏覽、WP CLI）；企業方案：群組權限與稽核；加 WP：站內編輯／外掛健康檢查 skill。
- **難度**：中高；切入：先做 macOS／Windows 安裝器＋檔案／shell 兩類工具＋文件化權限警告。

### 6. MCP 設定檔 → 靜態掃毒 → Agent 供應鏈稽核 SaaS
- **來源**：[graygnatconsole/mcp-audit-tool](https://github.com/graygnatconsole/mcp-audit-tool)（★~69，9/26 新建）— 純 Python MCP 資安稽核 CLI：掃 tool poisoning、rug pull、硬編碼密鑰、指令注入、供應鏈風險；SARIF＋CI 就緒，不需 LLM key。
- **標籤**：非 WP
- **為什麼值得做**：MCP 爆炸後設定檔成新攻擊面；「安裝前掃一次」是可賣的合規／DevSecOps 切入，也適合代理商交付檢查。
- **構想**：「MCP Guard」— 掃 Cursor／Claude Desktop／VS Code 設定，出等級報告＋修復建議；Pro：CI gate、允許清單、組織政策；加 WP：外掛／MCP 橋設定一併稽核。
- **難度**：低～中；切入：先支援常見 mcp.json 格式＋密鑰／未釘版本／filesystem 根目錄三類規則。

---

## WP

### 7. Prisma 風格查詢 → WordPress ORM → 外掛／頭less 資料層產品
- **來源**：[nlproduction/plasma](https://github.com/nlproduction/plasma)（★~3，9/25 新建）— MapSVG 團隊開源：PHP／WP 的 Prisma 風 ORM；內建 WP core schema、wpdb／PDO adapter、關聯 include、交易；用可讀陣列查詢，少寫 SQL 字串。
- **標籤**：WP
- **為什麼值得做**：客製外掛最痛 `$wpdb` 字串與 N+1；schema 感知 ORM 可加速交付，也可賣給頭less／多站代理商當標準資料層。
- **構想**：「Plasma Desk for WP」— 視覺查詢建構器＋自訂表 schema 匯入；Pro：REST／MCP 只讀投影、多站 schema 同步。
- **難度**：中；切入：先穩 posts／meta／taxonomy 三模型＋一種外掛範本。

### 8. 一頁一語系 → 輕量 hreflang → 無 WPML 的多語外掛
- **來源**：[ivanusto/just-lang](https://github.com/ivanusto/just-lang)（★~2，9/24 新建）— 給「每種語言各做一頁」的站：html lang、hreflang、og:locale、語言切換區塊／短碼、快取友善自動偵測；不改寫 URL；繁中說明齊全。
- **標籤**：WP
- **為什麼值得做**：台灣中小站常只要中英兩頁，卻被 WPML 級複雜度嚇跑；輕量多語＋SEO 標記是代理商高頻交付項。
- **構想**：「Just Lang Pro」— 語系頁對應精靈、Sitemap 語系、與 Rank Math／Yoast 欄位同步；加 Woo：商品頁語系對照表。
- **難度**：低～中；切入：先做兩語系對應＋hreflang／切換器＋與一種 SEO 外掛相容。

---

## 今日脈絡（一句）
產品化焦點從「會寫碼的 agent」轉向「記得公司、能本機決策、能管 MCP／CLI 艦隊、能產出可重現品牌動效」；WP 側可跟進 ORM 資料層與輕量多語。

## 備註
- 掃過未採用已記入 seen（含日／週趨勢老專案、CVE／PoC／Comment2Shell 噪音、驗證碼繞過、盜版 CapCut、逆向／rootkit、Jev 周邊重複訊號等）。
- 未把 exploit／PoC 當產品構想來源。
