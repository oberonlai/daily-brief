# GitHub Idea 早報 · 2026-09-24（台北）

> 訊號：GitHub Trending（日）＋ Search（新建高星／MCP／WP）。非 WP 為主；今日 WP 新建高星偏薄，安全可見性外掛＋核心 CVE 波剛好對齊。

---

## 非 WP

### 1. 程式碼知識圖譜 MCP → 代理商／多倉 Code Intelligence SaaS
- **來源**：[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)（★~44.5k，今日 trending）— 把 repo 建成持久知識圖譜的高速 MCP（162 語言、毫秒級查詢、本機單一二進位）。
- **標籤**：非 WP
- **為什麼值得做**：Agent 最大成本是反覆 grep／讀檔；「少 token、可追溯影響面」是可收費的基建，也適多客戶 WP／外掛維護。
- **構想**：「Repo Graph Cloud」— 一客戶一隔離索引，給 Cursor／Claude Code；WP 方案預建外掛／主題／mu-plugin 邊界與 REST 路由圖。
- **難度**：中高；切入：先做 PHP／JS 雙語索引＋「改動影響哪些短碼／區塊」報告。

### 2. AI 前端設計語言 → 落地頁／主題品質閘道
- **來源**：[pbakaus/impeccable](https://github.com/pbakaus/impeccable)（★~70k，今日 trending）— 給 AI coding agent 的設計技能：24 指令、61 條可判定偵測規則、瀏覽器迭代。
- **標籤**：非 WP
- **為什麼值得做**：AI 產出的 UI 同質化（Inter、紫藍漸層、卡片套卡片）；「設計護欄＋自動 audit」可賣給 SaaS 與 WP 建站代理。
- **構想**：「Theme QA Bot」— CI／PR 跑 impeccable 規則，對 Gutenberg／Elementor 匯出頁截圖＋可執行修復清單；月費含品牌 `PRODUCT.md` 模板。
- **難度**：中；切入：先包 10 條最高頻「AI slop」規則＋截圖 diff。

### 3. 任意軟體變 Agent-Native CLI → WP／SaaS 操作層產品
- **來源**：[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)（★~50k，今日 trending）— 讓既有軟體變成 agent 可呼叫的 CLI，含社群 CLI-Hub。
- **標籤**：非 WP
- **為什麼值得做**：Agent 不會點 GUI，但會跑 CLI；把 WP-CLI、Woo、託管面板、CRM 包成穩定 CLI＝平台型收費點。
- **構想**：「WP Agent CLI Pack」— 標準化 `wp-site content|woo|seo|backup` 指令集，給 Cursor／自架 agent；賣給主機商白牌。
- **難度**：中；切入：先做內容發布＋Woo 訂單查詢兩條 happy path。

### 4. 個人 Agent（瀏覽／終端／檔案）→ 垂直「繼續做事」SaaS
- **來源**：[CopilotKit/openmuse](https://github.com/CopilotKit/openmuse)（★~1.7k，9/15 新建）— 可自架的個人 agent：瀏覽器、終端、檔案，工作可延續；CopilotKit＋AG-UI。
- **標籤**：非 WP
- **為什麼值得做**：市場從聊天框轉成「交代結果、可接管瀏覽器」；開源模板＝可快速做成垂直產品。
- **構想**：「Site Ops Muse」— 代理商掛客戶站：夜間巡檢、競品截圖、草稿文章進 WP；行動／桌面同一條 thread。
- **難度**：中高；切入：先接 WP REST 發布＋瀏覽器截圖驗收。

### 5. 輸入框隨意圖變形 → 表單／報價／Onboarding UX SaaS
- **來源**：[anishfn/shapeshift](https://github.com/anishfn/shapeshift)（★~396，9/22 新建）— 一個文字框邊打邊變成活動卡、清單、分帳、投票等 UI；Jev 判意圖、其餘確定性解析。
- **標籤**：非 WP
- **為什麼值得做**：表單轉換率仍是 SaaS／電商瓶頸；「自然語言 → 正確控件」比多步驟 wizard 更可差異化。
- **構想**：「Intent Forms」— 嵌入落地頁／Woo checkout 輔助：一句話變預約、詢價、分票；匯出 React 元件或 Gutenberg 區塊。
- **難度**：中；切入：先做預約＋詢價兩種 schema。

### 6. SEO／GEO CLI＋MCP → 內容站技術 SEO 產品
- **來源**：[AkashPriyadarshii/jev-seo](https://github.com/AkashPriyadarshii/jev-seo)（★~42，9/18）— Rust SEO／GEO CLI＋MCP：數十條稽核、即時爬站、GEO 分數、排名漂移、CI gate。
- **標籤**：非 WP（強相關內容站／代理商）
- **為什麼值得做**：Semrush 級需求在「agent 可呼叫、可進 CI」；開源 CLI＝可做成託管儀表板與 WP 外掛橋。
- **構想**：「GEO Gate」— 每次發文／部署跑稽核，分數掉就擋合併；繁中 llms.txt／schema 模板＋WP webhook。
- **難度**：中低；切入：先做 on-page＋sitemap／robots 閘道 Web UI。

---

## WP

### 7. 本地安全可見性外掛 → 代理商資安加值（對齊核心 CVE 波）
- **來源**：[WPAuditor/WPAuditor](https://github.com/WPAuditor/WPAuditor)（★~4，9/21）— 本機活動紀錄、可疑請求、核心完整性、檔案鑑識／隔離、登入與 REST 強化；免帳號免雲端。
- **標籤**：WP
- **為什麼值得做**：今日 WP 新建高星稀少，但核心 LFI（CVE-2026-87902）PoC 同天湧現＝客戶會問「我有沒有中、有沒有留下痕跡」；無雲依賴的可見性層好賣給在意資料主權的站長。
- **構想**：「Agency Harden Desk」— 多站匯總儀表（仍可自架）、一鍵核心／外掛完整性報告、與 MainWP／自架監控串接；Free 引流、Pro 賣多站與告警。
- **難度**：低～中；切入：先做「核心檔 hash 巡檢＋可疑 REST 時間線」MVP，對齊本次 CVE 溝通包。

---

## 今日脈絡（一句）
Agent 基建（程式碼圖譜 MCP、設計護欄、CLI-Anything、個人 agent）與意圖型 UI／GEO SEO 同天熱；WP 側以「本地資安可見性」對齊核心 CVE 焦慮最務實。

## 備註
- 掃過未採用已記入 seen（含 Jev 周邊目錄、會議助理、盯盤、mac 清理 CLI、多個 CVE PoC 本體等）。
- 未把 CVE PoC 當產品構想來源；只當市場時機訊號。
