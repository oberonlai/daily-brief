# GitHub Idea 早報 · 2026-10-04（台北）

> 訊號：GitHub Trending（日／週）＋ Search（9/27 後新建高星／agent 跨場次記憶壓縮／公司級 Cloudflare Agent OS／用一頁 HTML 回答難題／System 1 決策小模型／把 AI UI 設計推到極限／十一步複刻任意 App／自架 Claude／Codex 瀏覽器工作區／一站式 WP 資安／上傳自動 WebP）。非 WP 為主；今日焦點是「agent 記得昨天、公司敢給 agent 跑、顧問交付變成可讀網頁、決策不用再燒大模型、設計 skill 可裝進代理商管線、競品複刻可報價」，WP 側跟進「可託管的一站式資安」與「媒體庫自動 WebP」。

---

## 非 WP

### 1. 跨場次壓縮記憶 → 下次開機還認得專案 → Agent 不再失憶
- **來源**：[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)（★~95.5k，今日 Trending；Apache-2.0）— 為 Claude Code（亦支援 Codex／Gemini／Hermes／Copilot／OpenCode 等）做的持久記憶壓縮：捕捉場次內行為、AI 壓縮後注入未來場次；有繁中 README；claude-mem.ai；Vercel OSS Program。
- **標籤**：非 WP
- **為什麼值得做**：代理商多客戶、多 repo 時，「昨天講過的架構決策」每天重講＝帳單與信任成本；可安裝的跨場次記憶＝可賣的座位／專案記憶訂閱。
- **構想**：「Claude-Mem Desk TW」— 繁中記憶儀表、依客戶／專案隔離租戶、忘記／匯出／稽核；Pro：與公司 gateway 共用記憶策略；加 WP：內容站「已核准品牌語調／外掛清單」進記憶，避免 agent 每次重學。
- **難度**：中；切入：先對內兩專案裝一週，對照「有無記憶」的重複提問次數與 token。

### 2. 公司知識＋沙盒小工具＋Gatekeepers → 自製「自家 OS」
- **來源**：[cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os)（★~10.5k，今日 Trending；Apache-2.0）— Cloudflare 內部大量員工在用的 AI 生產力環境開源版：帶公司脈絡的 agent 聊天、沙盒裡做「gadget」小 app 並安全分享、Gatekeepers 對 agent／app 設護欄；設計意圖是 fork 成「Your Company OS」；os.cloudflare.app；早期開放。
- **標籤**：非 WP
- **為什麼值得做**：企業要的不是再一個 chatbot，而是「業務／業務開發也能亂玩、資安能睡覺」的公司 OS；台灣代理商可當導入＋客製＋託管方案（簡報／Issue 儀表／文件改錯等藍圖已內建）。
- **構想**：「Codotx Company OS」— 繁中政策模板、台灣常見整合（Google／GitHub／Notion）、部門 gadget 目錄；Pro：多租戶、與 Tuskira 類閘道串接；加 WP：外掛／媒體 MCP 只走核准 Gatekeeper。
- **難度**：高；切入：先 `pnpm run-local` 示範「做一頁客戶簡報＋一個只讀 GitHub gadget」給內部試用。

### 3. 難題 → 短 Markdown → 50ms 變成可讀一頁 HTML
- **來源**：[QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)（★~292，10/2 新建；MIT）— agent skill：複雜問題不回文字牆，改產出可讀單頁 HTML；模型只寫內容、CLI 組版，宣稱輸出 token 約砍到 1/7；適用 Claude Code／Codex／Cursor／OpenCode。
- **標籤**：非 WP
- **為什麼值得做**：顧問／售前最痛的是「答案在聊天裡、客戶看不懂」；可下載／可轉寄的一頁說明＝可報價的交付物格式（架構圖、技術選型、模組關係）。
- **構想**：「Answer HTML TW」— 繁中版型（架構／比較／流程三模板）、客戶品牌色、一鍵匯 PDF；Pro：與 Notion／客戶入口同步；加 WP：說明頁可當草稿貼進 Gutenberg。
- **難度**：低；切入：先對三個真實售前問題產出對照（純文字 vs HTML 頁）給業務看。

### 4. 選項／量表決策 → 比 LLM 快、帶校準信心 → 工作流 System 1
- **來源**：[strands-labs/strands-decider](https://github.com/strands-labs/strands-decider)（★~290，9/29 新建；Apache-2.0）— 「決策模型／System 1」：在選項間挑選或在量表打分，比 LLM 快、不必像傳統分類器那樣重訓；每決策附校準信心（高信心約 95% 正確）；接 Strands Agents SDK；strandsagents.com。
- **標籤**：非 WP
- **為什麼值得做**：agent 裡大量「要不要重試／這則是不是垃圾／走哪條工具」不該每步燒 frontier 模型；可嵌入的決策小模型＝延遲與帳單雙降，也補昨日 caveman「省輸出」之外的「省決策」。
- **構想**：「Decider Gate TW」— 繁中決策模板庫（審稿／路由／風險）、低信心自動升級大模型或人工；Pro：多租戶儀表；加 WP：留言／表單先走 Decider，高毒才打大模型。
- **難度**：中；切入：先在一條 agent 路由上 A/B「純 LLM vs Decider＋升級」延遲與費用。

### 5. 先認品類再定調性 → 可安裝設計 Skill → AI UI 不再「高級簡潔」空話
- **來源**：[oil-oil/oil-ui](https://github.com/oil-oil/oil-ui)（★~305，9/30 新建；MIT）— 把 AI UI 設計能力推到極限的方法論 skill：認品類、拆競品、五刻度調性、首屏給誰、方向差異性檢查、留一處記憶點；`npx skills add`；畫廊 ui.oiloil.org；Pro 另售交互／特效。
- **標籤**：非 WP
- **為什麼值得做**：台灣代理商接「vibe coding 出站」時，設計一致性比再多一個 component 庫更值錢；可安裝的設計方法＝可複製的設計工時產品。
- **構想**：「Oil UI Agency TW」— 繁中品牌問卷、產業模板（電商／SaaS／課程）、客戶並排揀選會；Pro：與 Remotion／成片 skill 共用調性；加 WP：主題／區塊變數對齊同一套刻度。
- **難度**：低～中；切入：先對一個真實客戶 brief 產出三方向小樣對照頁。

### 6. 十一個 Skill → 偵察／重建／測 bug／讀差評改進 → 可賣的複刻流水線
- **來源**：[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill)（★~90，10/3 新建；MIT）— 十一個免費 Claude skill：逆向理解目標 App、重建功能與設計系統、測 bug、Entrepreneur 讀用戶抱怨並改進；強調 clean-room（不抄 code／logo／文案）；opusjake.ai。
- **標籤**：非 WP
- **為什麼值得做**：客戶常說「想要像某某＋但修好痛點」；有紀律的複刻流水線＝售前拆解報告＋MVP 報價包（注意智財邊界，skill 本身也強調不碰對方資產）。
- **構想**：「Replica Desk TW」— 繁中法律檢查清單、台灣熱門垂直模板、交付「差異評分＋改進清單」；Pro：多專案佇列；加 WP／Woo：複刻競品結帳／會員流程時對照 Gutenberg／Woo 區塊。
- **難度**：中；切入：先選一個公開產品做偵察＋差異報告示範（不公開對方資產）。

---

## WP

### 7. 防火牆＋掃毒＋完整性＋2FA＋備份＋稽核 → 一站式可託管資安
- **來源**：[loyal-security/loyal-security](https://github.com/loyal-security/loyal-security)（★~2，10/2 新建；GPL-2.0-or-later 宣稱）— 一站式 WordPress 資安外掛：雙模式 WAF、惡意／完整性掃描、強化、2FA／通行密鑰、備份還原、稽核與即時流量；規則在站上跑、免 Node 建置；免費完整功能，Pro 另售代理商自動化；loyalsecuritywp.com。
- **標籤**：WP
- **為什麼值得做**：台灣維護約最常賣「幫你顧安全」；開源可審的一站式外掛＋Pro 代理商工具＝可標準化的資安加價包（星低但產品完整，值得跟進）。
- **構想**：「Loyal TW Care」— 繁中預設政策、月報 PDF／LINE、多站 MainWP 彙總；Pro：虛擬修補與代操工單。
- **難度**：中；切入：先在兩台示範站跑完整掃描＋一頁「紅燈清單」給維護客戶看。

### 8. 上傳 JPEG／PNG → 自動 WebP（可還原）→ 媒體庫變輕
- **來源**：[donnma777/wp-webp-upload](https://github.com/donnma777/wp-webp-upload)（★~1，10/3 新建；GPL-2.0）— 上傳時自動轉 WebP（含縮圖）；可比原檔更大就跳過；可保留原圖並一鍵／批次還原、改寫文章內 URL；管理介面日文；Imagick／GD 會選真的能寫 WebP 的編輯器。
- **標籤**：WP
- **為什麼值得做**：電商／內容站首屏重量仍是維護痛點；「可逆的自動 WebP」比再塞一個全能優化外掛好講、也好做繁中代理商預設包。
- **構想**：「WebP Care TW」— 繁中設定頁、與 CDN／圖片 CDN 並存策略、批次舊庫轉換報告；Pro：多站政策同步。
- **難度**：低；切入：先 fork 繁中介面＋在一站對照前後 LCP／傳輸量。

---

## 今日脈絡（一句）
產品化焦點從「再包一個 chatbot」轉向「跨場次還認得的 agent 記憶、可 fork 的公司 Agent OS、可轉寄的 HTML 交付頁、可嵌入的 System 1 決策、可安裝的 UI 設計方法、有纪律的競品複刻流水線」；WP 側可跟進一站式可託管資安與可逆自動 WebP。

## 備註
- 掃過未採用已記入 seen（含 devilcoolyue/agentbox、telepath-computer/television、emdash-cms/emdash-build、callstackincubator/codex-mobile-dev-plugin、FidelisMM/shipstores、jarrodwatts/claude-image-view、blendi-remade/agentcraft、pingdotgg/t3code、OpenCut-app/OpenCut、DietrichGebert/ponytail 已見、pbakaus/impeccable 已見、affaan-m/ECC 已見、CVE／PoC／惡意／破解／帳號繞過／star 噪聲等）。
- 未把 exploit／PoC／惡意軟體／帳號檢查器／破解軟體當產品構想來源。
