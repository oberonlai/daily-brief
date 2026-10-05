# GitHub Idea 早報 · 2026-10-06（台北）

> 訊號：GitHub Trending（日／週）＋ Search（9/28 後新建高星／agent 終端機收件匣／agent 大資料記憶索引／AI 寫的程式碼稽核／檢查 agent 有沒有真的跑過測試／agent 角色庫／本機聊天剪片／WP 本機開發 MCP／WP SEO agent）。非 WP 為主；今日焦點是「一個畫面管所有 agent、讓 agent 便宜地查大量紀錄、替 vibe coding 的成果做體檢、驗證 agent 說的『完成』、把 agent 角色變成可賣的服務包、剪真實素材而不是生成假影片」，WP 側跟進「本機 WP 站一鍵接上 AI」與「會看轉換數據的 SEO 寫稿 agent」。

---

## 非 WP

### 1. 一個終端機視窗管所有 coding agent → 誰卡住、誰要核准，一個收件匣看完
- **來源**：[Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios)（★~4.8k，本週 Trending +708；MIT）— Go 寫的終端機多工器／視窗管理器（BSP 平鋪、工作區、可跨重開機存活的工作階段、tmux 相容層）；每個跑 agent 的窗格顯示 working／needs_input／idle／done／errored，Inbox 把所有工作階段、所有機器上等你的核准、問題、錯誤、完成的回合集中一處；agent 之間可以互相傳訊，讀到的內容一律當資料隔離，只有人能回答核准；另有 hooks、JSON 控制協定與 MCP。
- **標籤**：非 WP
- **為什麼值得做**：同時開三、五個 agent 後，最大的浪費是「有一個在等我核准，我卻十分鐘後才發現」；把所有 agent 的狀態收斂成一個收件匣，是團隊導入多 agent 時第一個會付錢的痛點。
- **構想**：「Agent 收件匣 TW」— 以 tuios 的狀態協定為底，做團隊版網頁儀表：每位成員、每台機器的 agent 狀態一覽，needs_input 推播到 LINE／Slack，手機上直接核准或回答；Pro：每週報表（各 agent 等人時間、失敗率）。
- **難度**：中；切入：先在自己的開發機用 tuios 跑一週多 agent，再寫一個讀 Inbox 狀態、推 LINE 通知的小服務。

### 2. 百萬筆紀錄建一次索引 → agent 每題只花幾百 token → 客服與維運的「深記憶」
- **來源**：[elstongun/leviathan](https://github.com/elstongun/leviathan)（★~216，10/5 新建；Apache-2.0）— 單一 Rust 執行檔，把 JSONL／JSON／CSV／SQLite 或任何資料庫 CLI 的輸出建成排序全文索引；agent 用白話提問，拿回帶出處的精簡結果卡；作者的 100 萬筆（678MB）合成維修紀錄測試中，每題中位數約 436 token（grep 策略約 10.7 萬）、前五名命中 99%、中位延遲 33ms；可依客戶分組、篩欄位與時間，找不到明確分組就列候選而不亂猜。
- **標籤**：非 WP
- **為什麼值得做**：企業最想讓 AI 回答「這個客戶以前發生過什麼」，但把整包工單或 log 丟給模型又貴又不準；一個便宜、可引用出處的檢索層，是做客服 copilot 或維運助理的關鍵零件。
- **構想**：「工單記憶 Agent TW」— 從客服系統／Email／LINE 匯出歷史對話建索引，客服回覆前 agent 先查同客戶與相似案例並附來源；Pro：每日自動增量更新、多租戶權限隔離；加 WP：WooCommerce 訂單與售後紀錄一鍵匯入。
- **難度**：低中；切入：先拿自家半年的客服或錯誤紀錄建索引，測 20 個真實問題的命中率與 token 花費。

### 3. AI 寫完 → 用 SI 驗收的標準體檢 → 產出「貼給 AI 就能修」的修正指令
- **來源**：[JinHo-von-Choi/iron-laws](https://github.com/JinHo-von-Choi/iron-laws)（★~107，10/4 新建；MIT）— 韓國開發者依大企業與公部門 SI 驗收經驗做的原始碼檢查 CLI：抓寫死的金鑰與路徑、吞掉的例外、散落的重複函式、用 any／type: ignore 蓋掉的型別、沒驗證的 API 等 AI 常見毛病；用白話解釋風險；`fix-prompt` 依嚴重度產出可直接貼給 coding agent 的修正指令；可輸出 SARIF 接 GitHub Code Scanning，並對照韓國行政安全部 49 項安全檢查出報告（作者註明非官方認證工具）。
- **標籤**：非 WP
- **為什麼值得做**：越來越多非工程背景的人用 AI 做出可上線的服務，但沒人幫他們看「會不會被打穿、能不能維護」；「體檢＋讓 AI 自己修」這個迴圈很適合包成平價的上線前檢查服務。
- **構想**：「上線前 AI 程式體檢 TW」— 規則對照台灣資安法規與常見政府標案資安要求，繁中白話報告＋修正指令包，GitHub PR 自動留言；Pro：顧問人工複核與月度追蹤；加 WP：外掛與佈景主題專用規則（nonce、權限檢查、SQL 準備語句）。
- **難度**：中；切入：先拿三個 vibe coding 做出來的專案跑 iron-laws，整理最常見的 10 類問題，做成繁中規則與報告範本。

### 4. agent 說「完成了」→ 讀實際測試輸出驗證 → 抓出偷改測試的假通過
- **來源**：[Rikinshah787/dotpals](https://github.com/Rikinshah787/dotpals)（★~32，9/30 新建；MIT）— 桌面浮動小幫手，監看 Claude Code、Codex 或其他 agent：改了哪些檔、跑了哪些指令、測試是否真的通過（讀實際輸出，不聽 agent 自述）；測試失敗時把 Claude 擋回去修，抓出「刪斷言、加 skip、改預期值」造成的假綠燈；提醒「測試通過後又改了 2 個檔」；兩個 agent 先後改同一檔會先問你；提供 MCP（`check_my_work`、`ready_to_merge`）與每日成果 Markdown。
- **標籤**：非 WP
- **為什麼值得做**：agent 最危險的不是做錯，而是自信地說做好了；能拿出證據證明「真的測過」，是把 agent 產出交給客戶或併入主線前最需要的一道關。
- **構想**：「Agent 驗收閘門 TW」— 把 dotpals 的檢查搬到 CI：每個 agent 開的 PR 附上「改了什麼、跑了哪些測試、有沒有動到測試本身」的證據卡；Pro：團隊儀表統計各 agent 假通過與返工率。
- **難度**：低中；切入：先在自己的專案裝 dotpals 跑一週，記錄它攔下幾次假完成，當成產品說服力的素材。

### 5. 上百個專業 agent 角色 → 一鍵裝進各家 coding 工具 → 「AI 代理商團隊」服務包
- **來源**：[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)（★~157k，今日 Trending +687、本週 +1.9k；MIT）— 從 Reddit 討論長出來的 agent 角色庫：前端、後端、社群經營、品質把關等各有身分、工作流程、交付物範例與成功指標；有 macOS／Linux／Windows 桌面 App 一鍵安裝到 Claude Code、Cursor、Codex、Gemini 等，也有腳本轉成十多種工具的格式。
- **標籤**：非 WP
- **為什麼值得做**：中小企業想要「一支 AI 團隊」，但不知道每個角色該怎麼寫；在地化、經過實戰調校的角色包，加上導入教學，是很好賣的顧問產品。
- **構想**：「台灣 AI 代理商角色包」— 繁中改寫並加入在地情境（LINE 官方帳號經營、台灣電商法規、統一發票、蝦皮／momo 上架）的角色組，按產業打包；Pro：月度更新與導入工作坊；加 WP：WP 外掛開發、WooCommerce 營運角色。
- **難度**：低；切入：先挑 5 個最常用角色做繁中在地版，在自家專案實際使用一個月後再對外販售。

### 6. 丟進原始素材、用聊天下剪輯指令 → 真實時間軸即時更新 → 本機 AI 剪片
- **來源**：[rakesh0x/OpenCardboard](https://github.com/rakesh0x/OpenCardboard)（★~47，10/4 新建；MIT）— Electron＋React＋ffmpeg 的本機優先剪輯器：只剪你匯入的真實素材、不生成影片；whisper.cpp 逐字稿、場景偵測、節拍偵測都在本機跑；能自動剪掉停頓與重複鏡頭、依「說到什麼就切到哪」剪輯、從字級時間碼產生字幕、依音樂節拍重剪；每次 agent 修改都是可驗證的操作紀錄，可完整復原；內建聊天與任何 MCP 客戶端共用 30+ 個工具。
- **標籤**：非 WP
- **為什麼值得做**：講師、診所、店家拍了很多口播素材卻沒時間剪；「素材不上雲、AI 幫剪粗剪＋字幕」正好避開隱私顧慮，又比外包便宜。星數仍低，屬早期觀察。
- **構想**：「口播粗剪工作站 TW」— 繁中語音辨識調校、台灣常用字幕樣式、一鍵輸出 Reels／Shorts 直式版本；Pro：多支影片批次處理與品牌片頭片尾範本。
- **難度**：中；切入：先拿自己的 5 支口播素材測粗剪品質，計算比手動剪省下多少時間。

---

## WP

### 7. 在 Local 按一下「啟用」→ AI 工具立刻能跑 WP-CLI、讀錯誤紀錄 → 本機 WP 開發接上 agent
- **來源**：[10up/localwp-agent-tools](https://github.com/10up/localwp-agent-tools)（★~49；GPL-2.0；10up 出品，10/5 仍在更新）— Local（WP 本機開發工具）的外掛：在 Local 主程序內跑一個 MCP HTTP 伺服器，讓 Claude Code、Cursor、Windsurf、VS Code Copilot 能操作 WP-CLI、讀錯誤紀錄與設定、管理站台；自動寫好各家工具的 MCP 設定檔與 CLAUDE.md／.cursorrules（含 PHP／MySQL 版本、啟用外掛、佈景主題、檔案結構）；Bearer token 驗證、只回應 localhost；全域端點可建立新站、啟停站台、開預覽。
- **標籤**：WP
- **為什麼值得做**：WP 接案者開始用 AI 寫外掛和佈景主題，但每個專案都要手動設 MCP 與專案說明；大廠 10up 把它做成一鍵，代表這會成為標準流程，周邊的 skill 與範本就有市場。
- **構想**：「WP Agent 開發起手包 TW」— 搭配 localwp-agent-tools 的繁中 skill 組（WooCommerce 金流物流、綠界／藍新串接、繁中翻譯檔）、專案說明範本與測試流程；Pro：團隊共用的設定與規範同步。
- **難度**：低中；切入：先在一個現有外掛專案啟用它，讓 AI 完成一個小功能，記下還缺哪些在地知識，整理成 skill。

### 8. 寫文 → 查證 → 發布到 WP → 讀 PostHog 看哪篇帶來註冊 → 多寫贏家
- **來源**：[kevinbadi/seo-agent-kit](https://github.com/kevinbadi/seo-agent-kit)（★~5，10/1 新建；MIT）— Claude Code 用的自我改進 SEO agent：撰寫能被 Google 收錄、也被 ChatGPT／Claude／Perplexity 引用的文章，查證後透過 Creator OS API 發布到 WordPress；每日兩次從 PostHog 拉流量、註冊漏斗與來源（含 AI 搜尋來源分類）存進自家 Postgres，再搭配 Google Search Console，讓 agent 依「哪些文章真的帶來註冊」調整下一篇；附 React 儀表卡片。
- **標籤**：WP
- **為什麼值得做**：多數 AI 寫稿工具只管產量，不管轉換；「用轉換數據回饋選題」是 SEO 外包最缺的一環，也能讓報價從「一篇多少錢」變成「每月成長方案」。星數很低，屬早期觀察；目前發布要經作者的 Creator OS 服務。
- **構想**：「轉換導向 SEO Agent TW」— 改成直接用 WP REST API 或 MCP 發布、接 GA4 與 Search Console、繁中關鍵字研究與在地查證規則；Pro：每月報表列出 AI 寫的文章帶來多少詢問或訂單；加 WooCommerce：依商品銷售數據挑選題材。
- **難度**：中；切入：先替一個客戶站跑一個月，每週兩篇，比較 AI 文章與舊文章的註冊轉換。

---

*本期未採用但掃過：michael-denyer/pstack-claude（agent 工作流技能包，與先前 skill／agent 團隊主題重疊）、DuarteSantos8/openGym（自架健身紀錄，偏個人應用）、storytold/filmcraft 系列（Rust 重寫 Adobe 軟體，同日大量建立、星數待觀察）、VoltAgent/official-mcp-servers、TannerMidd/pi-pocket、Asigers/pi-knock、AgentMemoryRepo/agentmemoryrepo、try2love/codex-mobile-bridge、omlahore/RemoveMacAI、joeseesun/qiaomu-clipper、spenmcke/compress、M-Abozaid/esp32-c3-adblock 等；另有一批 10/5 新建、星數一致為 392 的「破解軟體」repo 疑似惡意，已排除；WP 側 CVE PoC 類不列入構想。*
