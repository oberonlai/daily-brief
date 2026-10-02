# GitHub Idea 早報 · 2026-10-03（台北）

> 訊號：GitHub Trending（日／週）＋ Search（9/26 後新建高星／token 省錢 proxy／agent 原生 Remotion 剪輯／MCP＋LLM 閘道／agent 工時時間軸／Claude harness 組裝圖／iPhone 協作本機 27B／Wix→WP 解放／Jev 非同步留言審）。非 WP 為主；今日焦點是「把 agent 帳單砍半、把成片當可改程式、把 MCP 呼叫變成可稽核閘、把多 agent 一天變成可報帳時間軸、把 CLAUDE.md 混沌畫成圖、把閒置 iPhone 當本機加速卡」，WP 側跟進「封閉建站器一鍵搬進 WP」與「留言提交不堵、背景再判垃圾」。

---

## 非 WP

### 1. 洞穴人口語 → 輸出少寫 65% → Coding Agent 帳單立砍
- **來源**：[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)（★~109k，今日 Trending；Apache-2.0）— skill＋proxy：逼 agent 用短句說話，程式／路徑／錯誤訊息不壓縮；宣稱輸出 token 可砍約 65%；`npx skills add`、中介層可塞進自有 app；Adobe／JetBrains 有公開測量與文件 docs.caveman.so。
- **標籤**：非 WP
- **為什麼值得做**：台灣代理商與產品隊同時開 Claude Code／Cursor 時，帳單痛感比「再一個 prompt 包」更硬；可計量省錢＝可賣的座位訂閱。
- **構想**：「Caveman Desk TW」— 繁中／英文雙模式、專案級省 token 儀表、與公司 LLM gateway 串接；Pro：多租戶配額、部門報表；加 WP：建站 agent 預設 caveman，長文稿才切回全文。
- **難度**：低～中；切入：先對內三專案 A/B（有無 caveman）一週帳單對照＋一頁安裝手冊。

### 2. 一句 brief → Agent 寫 Remotion → 可擁有的成片專案
- **來源**：[Remocn/remocn-studio](https://github.com/Remocn/remocn-studio)（★~94，10/1 新建；MIT）— macOS app：自備 coding agent 把影片做成真 Remotion 專案（磁碟上的 code，不是租來的像素）；現場預覽、點畫面下指令改鏡；導出 mp4；remocn.studio。
- **標籤**：非 WP
- **為什麼值得做**：代理商要的是「可改字、可換品牌色、可進 CI」的發布片，不是再生成一支黑箱；可擁有的 Remotion 專案＝專案報價與維護約。
- **構想**：「Remocn Agency TW」— 電商開賣／募資／課程三模板、繁中導演指令、客戶審片留言釘在時間碼；Pro：多專案佇列、與 HyperFrames 渲染農場；加 WP／Woo：成片掛產品頁草稿。
- **難度**：中；切入：先交一支 20 秒開賣片＋可下載 Remotion zip 示範包。

### 3. 單一閘道 → MCP／LLM 鑑權與範圍 → Agent 艦隊可觀測
- **來源**：[Tuskira/ai-agent-gateway](https://github.com/Tuskira/ai-agent-gateway)（★~47，10/1 新建；Apache-2.0）— 開源 AI Agent Gateway：擋在 MCP tool server 與 Claude／Bedrock／OpenAI／Gemini 前面；每請求鑑權、注入憑證、依 agent profile 限工具、紀錄每次呼叫；Docker Compose＋控制台；tuskira.ai。
- **標籤**：非 WP
- **為什麼值得做**：企業敢給 agent 接生產 MCP，前提是「誰調了什麼、祕密不進模型」可證明；閘道＋稽核是託管／資安加值的標準形狀（補 OpenShell 類執行時之外的流量面）。
- **構想**：「Tuskira TW Gate」— 繁中政策模板（只讀／禁外連／允許清單）、客戶隔離 tenant、違規與花費儀表；Pro：與 ClickHouse 分析包、LINE／Email 告警；加 WP：外掛／媒體 MCP 只走核准 profile。
- **難度**：中高；切入：先 Docker 示範「兩 agent profile＋一個假 MCP＋存取日誌頁」。

### 4. Agent 自己記一行 → 日／週時間軸 → 可報帳的工廠日誌
- **來源**：[flaviocopes/factorylog](https://github.com/flaviocopes/factorylog)（★~50，10/1 新建；MIT）— macOS app：Codex／Cursor／Claude Code 等做完有變更的工作就 `factorylog` 一行；日與週時間軸、依專案看時間去向；不讀 code／diff／終端；本機純文字日誌。
- **標籤**：非 WP
- **為什麼值得做**：多 agent 一天跨五個客戶時，「晚上說不清做了什麼」比缺 IDE 外掛更痛；可匯出的工廠日誌＝報帳、回顧與管理報表楔子。
- **構想**：「Factory Log Agency」— 繁中狀態文案、客戶／專案標籤、週報 PDF／CSV；Pro：團隊共享、與 Notion／Linear 鏡像；加 WP：外掛安裝與內容發布事件同一時間軸。
- **難度**：低～中；切入：先穩「Claude Code＋Cursor 雙整合＋一週匯出」給內部兩人試用。

### 5. 讀 CLAUDE.md／MCP／權限／鉤子 → 一張組裝圖 → Harness 健診
- **來源**：[Dominic-DK/harness-map](https://github.com/Dominic-DK/harness-map)（★~52，10/2 新建；MIT）— 把 Claude Code harness（指示檔、記憶、MCP／skill、權限、hook）依啟動資料夾與 spawn 方式畫成組裝圖；成熟度 1–5 六邊形自評；只讀、不寫設定、不落 token。
- **標籤**：非 WP
- **為什麼值得做**：顧問／代理商接客戶 Claude Code 環境時，「到底繼承了什麼規則」是隱形債；可視化健診＝可報價的半天工作坊產品。
- **構想**：「Harness Map TW」— 繁中報告模板、風險清單（權限過寬／MCP 幽靈／規則互撞）、修復 playbook；Pro：多 repo 批量掃描 SaaS；加 WP：內容 agent 的 Changesets／MCP Adapter 一併入圖。
- **難度**：低；切入：先對自家兩專案出圖＋一頁「紅燈三條」檢查表。

### 6. USB-C 接 iPhone → 分層加速本機 27B → 隱私向 Local Agent
- **來源**：[StayLameBro/backburner](https://github.com/StayLameBro/backburner)（★~69，10/1 新建；MIT）— iPhone 幫 Mac 跑 Qwen3.8-27B：分層管線加速 prefill、把舊 context 放手機以拉長上下文（測到 128k）；答案與單機 greedy 一致；llama.cpp fork＋代理快取。
- **標籤**：非 WP
- **為什麼值得做**：法規／金流／醫療客戶常要「資料不出公司」；把閒置 iPhone 當加速卡，比再買一張 GPU 好講故事，也適合工作室級本機 agent 方案。
- **構想**：「Backburner Desk TW」— 繁中安裝精靈、推薦機型表、與 omp／Claude Code 本機後端一鍵；Pro：多機排程、花費對照雲端 API；加 WP：草稿生成走本機，發布仍經 Changesets。
- **難度**：高；切入：先驗證 M 系列＋一隻 iPhone 的「讀檔等待秒數」對照影片，不碰自研 kernel。

---

## WP

### 7. 貼上網址 → 瀏覽器擷取重建 → 封閉建站器搬進可下載的 WP
- **來源**：[Automattic/liberate.sh](https://github.com/Automattic/liberate.sh)（★~3，10/2 新建；GPL-2.0）— 貼上 Wix／Squarespace／Shopify／Webflow／GoDaddy 等站址，經 WordPress.com 靜態匯入重建成可下載的 WordPress（頁面＋媒體＋外觀主題）；可開 Studio 再推 WP.com／Pressable；liberate.sh；早期但官方。
- **標籤**：WP
- **為什麼值得做**：台灣大量中小還鎖在封閉建站器；「可帶走的 WP zip」是代理商搶遷移案的標準入口（即使還原度有落差，有站勝過沒站）。
- **構想**：「Liberate TW」— 繁中導引、遷移前後對照報告、金流／表單落差清單、接 Studio→自架／Pressable；Pro：批量代操、與維護約綁定。
- **難度**：中；切入：先跑三個真實 Wix／Webflow 案例＋落差表，當銷售一頁。

### 8. 送出先暫存 → 背景 Jev 打分 → 不堵表單的留言審
- **來源**：[soderlind/jev-comment-triage](https://github.com/soderlind/jev-comment-triage)（★~3，9/18 新建）— WordPress 外掛：留言提交當下只先 pending（不打 API），背景用 TypeSafe Jev 評 spam／scam／toxicity 再路由；不超越站台本身審核政策；需 AI Provider for Jev；WP 6.8+／PHP 8.3+。
- **標籤**：WP
- **為什麼值得做**：Akismet 以外，代理商要的是「表單不慢、可調門檻、可稽核分數」；非同步分流＝可賣的內容站／社群站加值。
- **構想**：「Jev Triage TW」— 繁中門檻預設、審核欄位與每日摘要 Email／LINE；Pro：多站 MainWP 彙總、與 jev-connector 決策鏈共用。
- **難度**：中；切入：先在示範站對照「同步打模型 vs 背景 drain」的提交延遲。

---

## 今日脈絡（一句）
產品化焦點從「再包一個 chatbot」轉向「可計量的 token 省錢、可擁有的 agent 成片專案、可稽核的 MCP 閘、可報帳的 agent 時間軸、可交付的 harness 健診、可講故事的本機加速」；WP 側可跟進 liberate.sh（封閉建站器→可下載 WP）與 Jev 非同步留言審。

## 備註
- 掃過未採用已記入 seen（含 google/skills、nykooi1/vibe-wise、youcci/playport、jarrodwatts/intermission、CAPCOM-TD-OSS/REDox、Effect-TS/effect、getsentry/sentry、IuCC123/CLIProxyAPI-Rust、Soulringen/aegis-claude、Kutuyyy/Leaked-System-Prompt-AI、CVE／PoC／惡意／帳號繞過／破解類等）。
- 未把 exploit／PoC／惡意軟體／帳號檢查器當產品構想來源。
