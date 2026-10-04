# GitHub Idea 早報 · 2026-10-05（台北）

> 訊號：GitHub Trending（日／週）＋ Search（9/28 後新建高星／自然語言 e2e 測試／agent 做 CAD／agent 剪片廠／自架遠端 coding pod／跨 agent skill 管理／本機跑大模型／WP 開源視覺建站＋MCP／WP「提案→核准→執行」Claude 連接器）。非 WP 為主；今日焦點是「QA 改用一句話寫、硬體設計交給 agent、影片外包變成管線、agent 跑在自己的伺服器、skill 庫要有人管、敏感資料留在本機推論」，WP 側跟進「AI 可直接操作的開源建站器」與「客戶敢放手的核准式 AI 改站」。

---

## 非 WP

### 1. 一句話寫測試 → agent 跑一次、之後零模型重播 → 便宜的 AI e2e
- **來源**：[tester-army/e2e](https://github.com/tester-army/e2e)（★~3.0k，今日 Trending +344；Apache-2.0）— web／行動 App 的 e2e 測試框架：用自然語言描述目標（`agent.act('upgrade to Pro')`），agent 驅動 App，再用 locator／assertion 驗證；被驗證過的 agent 步驟會錄下動作，下次無模型呼叫直接重播，直到 App 改版；Playwright 三瀏覽器、iOS／Android 模擬器、GitHub PR 留言 reporter；自帶 key 或本機模型。
- **標籤**：非 WP
- **為什麼值得做**：接案團隊最常省掉的就是 e2e，因為寫和維護 selector 太貴；「第一次用 AI、之後免費重播」讓回歸測試變成可以按月收費的維運項目，而不是一次性成本。
- **構想**：「E2E 驗收包 TW」— 繁中測試情境模板（會員升級、結帳、表單、多語切換）、每次 PR 自動貼結果與截圖、月報給客戶看「上線前擋下幾次壞掉」；Pro：託管瀏覽器＋行動模擬器；加 WP：WooCommerce 結帳／會員流程的現成測試組。
- **難度**：中；切入：先替一個現有客戶站寫 5 條關鍵流程，比較維護一個月的時間與模型費用。

### 2. 用說的畫零件 → STEP／STL／工程圖 → 給 agent 的 CAD 技能包
- **來源**：[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)（★~16.8k，今日 Trending；MIT）— 一組 agent skill：用自然語言或圖片建立與修改 CAD 模型（主輸出 STEP，可匯 STL／3MF／GLB）、找現成 STEP 零件（螺絲、軸承、馬達、連接器）、產出含尺寸與孔標註的工程圖 PDF，另有切片、機器人描述檔與模擬流程；texttocad.dev。
- **標籤**：非 WP
- **為什麼值得做**：台灣有大量小型製造、打樣與 maker 需求，「先做一個能報價的 3D 初稿」常卡在畫圖人力；agent 能產出 STEP＋工程圖，就能變成詢價前的快速打樣服務。
- **構想**：「打樣 Agent TW」— 客戶上傳草圖或描述 → 產出 STEP、工程圖與 3D 預覽頁 → 一鍵轉給合作的 3D 列印／CNC 廠報價；Pro：零件庫對應台灣常見規格與供應商。
- **難度**：中高；切入：先挑一個窄品類（治具、外殼、支架）做 10 個真實案例，看初稿可用率。

### 3. 一段描述 → 研究、腳本、素材、剪輯、合成 → agent 剪片廠
- **來源**：[calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)（★~63k，今日 Trending +361；AGPL-3.0）— 號稱首個開源 agentic 影片製作系統：12 條製作管線、100+ 工具、700+ skill／製作知識檔；讓 coding agent 負責研究、寫腳本、生素材、剪接到最終合成（Remotion／Blender／FFmpeg），也能從免費素材庫取真實動態片段剪成片；範例 60 秒動畫短片成本約 $1.33；openmontage.video。
- **標籤**：非 WP
- **為什麼值得做**：中小企業每月都需要短影音，但外包一支幾千到上萬；把製作流程固化成管線，就能用訂閱價賣「每月 N 支」的穩定產能。注意 AGPL，做託管服務要開源修改或另談授權。
- **構想**：「每月短影音管線 TW」— 繁中口播稿模板、台灣常見產業（餐飲、診所、課程）分鏡範本、字幕與品牌片頭自動套用；Pro：審片流程與多帳號排程上架；加 WP：新文章發布自動產一支 60 秒摘要影片。
- **難度**：中；切入：先替自家內容做一個月、每週兩支，算每支實際成本與修改次數。

### 4. 自己的伺服器開 coding agent 沙盒 → 手機也能接手 → 自架 agent pod
- **來源**：[pi-pod/pipod](https://github.com/pi-pod/pipod)（★~131，10/1 新建；AGPL-3.0）— 讓 pi coding agent 的工作階段跑在遠端沙盒（pod）裡，可從終端機或手機接上；含 CLI、控制平面（REST API、session gateway、Postgres）、單容器多 pod 沙盒服務、iOS／Android App 與一鍵自架腳本；身分用 Zitadel（OIDC），伺服器不存密碼；8GB RAM 的 Linux 主機即可。
- **標籤**：非 WP
- **為什麼值得做**：團隊想讓 agent 長時間跑任務，又不想把客戶程式碼放到第三方雲；「自架、多人、手機可看」正好是代理商與中小企業 IT 會買單的組合。
- **構想**：「Agent Pod 託管 TW」— 幫客戶在自有 VPS／機房裝好 pod 平台、對接公司 SSO、每個專案一個隔離 pod；Pro：用量與費用儀表、任務完成通知到 LINE／Slack。
- **難度**：中；切入：先在內部 VPS 自架，讓兩個專案的長任務改跑 pod 一週，記錄中斷與接手體驗。

### 5. 找出每個 agent 讀得到哪些 skill → 一鍵補齊、統計用量 → skill 管理台
- **來源**：[flaviocopes/skillscout](https://github.com/flaviocopes/skillscout)（★~52，9/30 新建；MIT）— Mac App：掃出本機所有 coding agent skill，顯示 Cursor、Claude Code、Codex、Gemini CLI、OpenCode、Droid、Pi、Amp 各自看得到哪些，一鍵補到缺的 agent；讀聊天紀錄統計每個 skill 被載入幾次，並找出你一直重複輸入的請求，建議做成新 skill。
- **標籤**：非 WP
- **為什麼值得做**：skill 越裝越多後，最大問題是「不知道哪些有在用、哪些 agent 讀不到」；團隊版的 skill 盤點與分發，正是 agent 導入顧問可以加值的地方。
- **構想**：「團隊 Skill 盤點台」— 跨成員、跨機器彙整 skill 清單與使用率，標出沒人用的與重複的，提供核准後統一推送；Pro：從團隊對話中自動提案新 skill；加 WP：內建一組 WP 開發 skill 套件當示範。
- **難度**：低中；切入：先做 CLI 版，掃自家所有 bot 與成員的 skill 目錄，出一份盤點報告。

### 6. 在自己買得起的機器上跑頂級開源模型 → 敏感資料不出門
- **來源**：[antirez/ds4](https://github.com/antirez/ds4)（★~23.4k，今日 Trending +211；MIT）— Redis 作者的 DwarfStar：刻意窄化的原生推論引擎，主打 DeepSeek V4 Flash／V4.1 Flash／V4 PRO、GLM 5.x、Qwen3.8 Flash Next；主要支援 96GB 以上 Mac（Metal，小機器可 SSD 串流）、NVIDIA CUDA（DGX Spark 為主）、Strix Halo 的 ROCm；模型載入、tool call、KV 狀態、HTTP 伺服器與 coding agent 一起整合測試。
- **標籤**：非 WP
- **為什麼值得做**：法律、醫療、製造業客戶常因資料不能上雲而卡住 AI 導入；「一台機器＋整合好的本機模型與 agent」是可以報價的硬體加服務方案。
- **構想**：「地端 AI 主機方案 TW」— 選機建議（Mac Studio／DGX Spark／Strix Halo）、預裝 ds4 與內部文件問答、繁中使用手冊與年度維護；Pro：多人帳號與使用紀錄稽核。
- **難度**：中高（硬體門檻高）；切入：先用一台 Mac 跑內部文件問答，測速度與答案品質，做成示範影片給潛在客戶看。

---

## WP

### 7. 開源視覺建站器內建 MCP → AI 直接蓋頁面、頁首與文章類型
- **來源**：[dilukangelosl/brik](https://github.com/dilukangelosl/brik)（★~1，10/3 新建；GPL-2.0）— 主打 Divi／Elementor 的開源替代：shadcn/ui 風格元件與 token 設計系統、90+ 元素含 3D 動態區塊、佈景主題建構器、自訂文章類型與欄位、WooCommerce；頁面同時存成 JSON 與乾淨 HTML（關掉外掛內容仍可讀）；每頁只出用到的 CSS／JS；內建效能、無障礙、SEO 稽核；內建 MCP 伺服器，Claude／Cursor 可直接建頁面、選單與內容類型。
- **標籤**：WP
- **為什麼值得做**：客戶要「AI 幫我改站」，最卡的是頁面建構器格式封閉、AI 改不動；一個 AI 可讀寫、又不鎖定的建構器，是做「AI 建站方案」的好底座。星數還很低，屬早期觀察。
- **構想**：「AI 建站起手包 TW」— 在 Brik 上做繁中產業版型（餐廳、診所、課程、電商），配一組 MCP 指令範本讓 AI 依客戶資料一次生出整站；Pro：上線前自動跑效能與無障礙稽核報告。
- **難度**：中；切入：先在測試站用 MCP 讓 AI 從零生一個五頁形象站，評估品質與要手修的比例。

### 8. Claude 先提案、站長核准一次、再動手 → 敢交給客戶的 AI 改站
- **來源**：[fatihborasoftware-sudo/fb-claude-connector](https://github.com/fatihborasoftware-sudo/fb-claude-connector)（★~1，10/3 新建；GPL-2.0）— 把 WordPress 接成 Claude 的自訂連接器（遠端 MCP＋OAuth）：在聊天中先對齊樣稿，核准一份建站計畫後 Claude 才建頁面、文章、主題、選單；即時看 Claude 正在改哪頁；動工前先 WPvivid 備份、完工前檢查壞連結與缺圖；獨立 Editor 帳號、權限分級、核准佇列、每次修改留修訂版、活動紀錄與緊急停止開關。
- **標籤**：WP
- **為什麼值得做**：客戶不敢讓 AI 直接動正式站，痛點不是能力而是「誰核准、能不能復原」；核准佇列＋備份＋紀錄這套機制，本身就是代理商可以賣的「AI 維護方案」。
- **構想**：「核准式 AI 站務 TW」— 繁中介面、核准通知推到 LINE／Email、每月修改紀錄報表給客戶；Pro：多站管理與不同客戶的權限範本。
- **難度**：中；切入：先在一個維護中的客戶測試站試跑，讓客戶用核准流程改三次內容，收集回饋。

---

*本期未採用但掃過：garrytan/gstack（與先前 openrig／agent 團隊主題重疊）、alexknowshtml/claude-auto-handoff、cablate/ctx-handoff-mod、hamzafer/claude-code-mods、isoshimodo/ai-data-extractor、shinshin86/mesh-avatar-studio、Adolanium/hermes-gadget-sdk、ythx-101/live-panel-skill、kargulstudio/sales-crm（無說明的模板，星數異常）、SahibYar/open-agency-os、faidodaisen/sitessaver、deckerweb/brand-admin-schemes 等。*
