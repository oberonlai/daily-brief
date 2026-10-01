# GitHub Idea 早報 · 2026-10-02（台北）

> 訊號：GitHub Trending（日／週）＋ Search（9/25 後新建高星／agent 執行時沙箱／垂直熱點站框架／notch 代理人伴／CJK 推敲 skill／風格仿製影片／常駐 AI 同事模板／WP Changesets＋自架託管）。非 WP 為主；今日焦點是「給 agent 艦隊可形式驗證的政策沙箱、可換信源的行業熱點站、看得見權限請求的 notch 伴、可賣的繁中推敲 skill、可審核的風格仿影片流水線、可自架的常駐同事工作區」，WP 側跟進「先暫存再 Preview／Publish 的 agent 編輯」與「自架版 WP Engine 級託管」。

---

## 非 WP

### 1. 核心層強制政策 → 憑證只到核准端點 → Agent 艦隊可稽核沙箱
- **來源**：[NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)（★~14.0k，今日 Trending）— 自主 agent 的安全私有執行時：核心層限制檔案／系統呼叫／外連，政策變更先形式驗證再套用；agent 看不到真憑證，只在核准端點注入；支援 sandbox／gateway／K8s Helm、Python／TS／Go／Rust SDK、agent skills；Apache-2.0，docs.nvidia.com/openshell。
- **標籤**：非 WP
- **為什麼值得做**：企業敢給 agent 裝套件、打 API，前提是「碰不到祕密、外連可證明」；政策沙箱＋審批閘是託管／合規產品的硬需求。
- **構想**：「OpenShell Desk TW」— 繁中政策模板（只讀 repo／禁外連／允許特定 SaaS）、客戶隔離 gateway、花費與違規儀表；Pro：多租戶 Helm、與 Claude Code／Codex 一鍵安裝；加 WP：建站 agent 只能寫草稿目錄與核准外掛清單。
- **難度**：高；切入：先做「單 sandbox＋三種政策模板＋違規日誌 Email」示範，不碰自研 kernel。

### 2. 換信源＋KnowHow → 雙重打分聚簇 → 可賣的行業熱點站框架
- **來源**：[KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT)（★~4.6k，9/28 新建）— 自己找熱點、自己寫日報的網站框架：採集→預篩→兩次獨立打分→中文標題摘要→事件聚簇→熱度→成刊；提示詞與門檻可改；Docker／Postgres；示範 18 個海外 AI 信源；MIT，aihot.news。
- **標籤**：非 WP
- **為什麼值得做**：法律／HR／金融／電商代理都想要「自己產業的早報站」，但缺可換信源與精選標準的完整骨架；這正是訂閱＋白標交付。
- **構想**：「AIHOT Vertical TW」— 台灣產業模板（電商／法規／創業／WP 生態）、繁中信源包、LINE／Email 日報出口；Pro：多品牌白標、客戶自訂門檻；加 WP：精選稿一鍵進草稿＋MainWP 多站分發。
- **難度**：中；切入：先換一組台灣公開信源＋一頁熱點榜＋每日 Email。

### 3. Notch 裡的代理人伴 → 權限一鍵允／拒 → 不離開工作的 Agent 監督台
- **來源**：[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)（★~2.4k，9/27 新建）— 住在 macOS notch（Windows 頂邊）的小伴 Mochi：監看 Claude Code／Gemini CLI 等 session、權限 Allow／Deny、跳到對應終端、拖檔／拖窗當上下文、串 Stripe／n8n／GitHub／Vercel／Notion；無遙測；MIT。
- **標籤**：非 WP
- **為什麼值得做**：代理商與產品團隊同時跑多 agent 時，「誰在等核准」比再一個 dashboard 更痛；可愛＋即時核准是桌面訂閱楔子。
- **構想**：「Coucou Agency」— 團隊共享核准佇列、繁中狀態文案、多 agent 色標；Pro：稽核匯出、與 Discord／LINE 鏡像通知；加 WP：外掛安裝／寫入能力請求走同一 notch 閘。
- **難度**：中；切入：先穩「Claude Code 權限泡泡＋三種整合 pill」示範包。

### 4. 七原則統語轉換 → 去 AI 腔 → 可安裝的 CJK 推敲 Skill
- **來源**：[nanaism/yomiyasu](https://github.com/nanaism/yomiyasu)（★~911，9/30 新建）— 把 AI 生成日文推敲成自然、高資訊密度日文的 Agent Skill；七轉換原則（主謂還原、非生物主語拆除、比喩動詞技術化等）；對準技術文／規格／PR／報告；支援 Codex／Claude Code／Cursor；MIT。
- **標籤**：非 WP
- **為什麼值得做**：台灣交付物常死在「AI 腔繁中」；可重跑的推敲 skill＋客戶用語表，比再寫一則「請寫自然一點」提示好賣。
- **構想**：「Yomiyasu 繁中 Desk」— 繁中七原則＋台灣用語／產業詞庫、批次掃 PR 說明與說明文件；Pro：品牌語氣包、與 CI 綁「合併前推敲」；加 WP：文章／產品描述審核後寫入。
- **難度**：低～中；切入：先做「貼上一段 → 前後對照＋違規原則標註」網頁／skill。

### 5. 拆參考片節奏 → 多 agent 分鏡審核 → 風格仿製但不抄素材
- **來源**：[edenfunf/reelmimic](https://github.com/edenfunf/reelmimic)（★~685，9/28 新建）— 丟參考影片（檔案／手機錄／YouTube）＋一句 brief，拆剪輯節奏／鏡頭／轉場／色調，先出計劃再核准；最多 6 agent 平行製作、交叉審核、修正要前後截圖證明；本機 Claude Code／Codex；已有繁中介面；MIT。
- **標籤**：非 WP
- **為什麼值得做**：代理商要的是「像那支片、但是我們的產品」，不是再一個文生影片黑箱；可審核流水線＝專案報價與訂閱加值。
- **構想**：「ReelMimic Desk TW」— 電商／募資／課程三種風格模板、繁中審核台、客戶留言釘在時間軸；Pro：多租戶佇列、與 HyperFrames 渲染農場；加 WP／Woo：成片掛產品頁草稿。
- **難度**：中高；切入：先做「一支 30 秒參考 → 計劃 PDF＋三鏡風格幀」交付包。

### 6. 常駐 Specialist Dots → 各自電腦＋Spaces → 可自架的 AI 同事工作區
- **來源**：[CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots)（★~286，9/29 新建）— 開源常駐 AI 同事模板：文字／通話／Slack 移動；每個 Dot 有角色、工具權限與獨立電腦（瀏覽器／檔案／終端持久）；Spaces 文件庫與視覺編輯；自架、MIT、alpha；建於 CopilotKit／AG-UI。
- **標籤**：非 WP
- **為什麼值得做**：團隊要的是「研究員＋撰稿人各一台可接管的電腦」，不是單一 chat；模板＋產業 Dot 包可做成實作品 SaaS。
- **構想**：「OpenDots TW」— 預設研調／客服／內容三 Dot、繁中 Spaces、人工核准卡；Pro：多租戶、與 OpenShell 類沙箱串；加 WP：內容 Dot 只寫 Changesets 預覽鏈。
- **難度**：中高；切入：先部署單機模板＋一種「研調→草稿→核准」示範。

---

## WP

### 7. 暫存 Changeset → Preview URL → 核准後才 Publish 的 Agent 編輯
- **來源**：[Automattic/changesets](https://github.com/Automattic/changesets)（★~2，9/28 新建）— WordPress 外掛：agent 經 MCP 建立 Changeset，暫存內容／全域樣式／設定，給人 `?changeset=` 預覽，核准後 approve／publish；永不直接改線上；需 WP 6.9+ 與 MCP Adapter；GPL-2.0。
- **標籤**：WP
- **為什麼值得做**：全開 MCP 寫入沒人敢上正式站；「先預覽、可丟棄、媒體不上暫存」是代理商敢簽維護約的形狀。
- **構想**：「Changesets Agency」— 繁中核准流程、多站預覽彙總、每日待核准 Email／LINE；Pro：與 Safe MCP 政策互補、客戶自助核准頁。
- **難度**：中；切入：先穩「文章草稿 changeset＋預覽連結＋一鍵核准」Playground／示範站。

### 8. 一鍵 VPS → 站站隔離容器 → 自架版 Managed WP 託管
- **來源**：[parthh37/wpgenie](https://github.com/parthh37/wpgenie)（★~0，9/28 新建）— 開源自架 managed WordPress：每站硬化容器、自動 SSL、AI bot shield／PoW CAPTCHA、WAF、備份／staging、分析、面板角色與稽核；目標「自己 VPS 上的 WP Engine」；早期 v0.1。
- **標籤**：WP
- **為什麼值得做**：台灣中小託管仍靠共享主機拼湊；「可白標的隔離託管面板」是代理商升級 ARPU 的直接路徑（即使上游尚早期）。
- **構想**：「WPGenie TW」— 繁中面板、台灣金流／發票、預設嚴格 shield；Pro：多機 agent、經銷帳務；先當內部託管骨架再對外。
- **難度**：高；切入：先在單 VPS 跑通「建站→SSL→備份→staging」四步＋繁中儀表。

---

## 今日脈絡（一句）
產品化焦點從「再包一個 chatbot」轉向「可稽核的 agent 沙箱、可換信源的行業熱點站、可核准的 notch 監督、可賣的繁中推敲、可審核的風格仿影片、可自架的常駐同事」；WP 側可跟進 Changesets（暫存→預覽→發布）與自架 managed 託管骨架。

## 備註
- 掃過未採用已記入 seen（含 earendil-works/pi、cursor/plugins、tile-ai/tilelang、pablostanley/yoinks、HunxByts/GhostTrack、composio-community/open-dot、AFK-surf/Comma、openJiuwen-ai/iCode、AgentSystemLabs/agent-office、alpcanaydin/tusk、OpSafari/hypoarena、mwender/omawrite-wordpress、zeam-labs/pass、CVE／PoC／惡意與帳號檢查類等；並補記昨日已報但未入帳的 OpenKB／jeeves／Raven／claude-seo）。
- 未把 exploit／PoC／惡意軟體／帳號檢查器當產品構想來源。
