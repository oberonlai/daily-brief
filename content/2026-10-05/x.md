# X 熱門早報｜2026-10-05（一）

Chollet 用「石頭也由原子組成」反駁「AI 有意識」論，DAIR 連推兩篇 agent 論文：NVIDIA 證明終端 agent 該把預算花在驗證器，Meta 的 RankEvolve 防止自動研究 agent 被隱藏 bug 拖垮。SEO 圈普遍嗅到 Google 大更新將至，Glenn Gabe 帶回 Search Central Live 的爬取預算細節；WordPress 側 Joost 喊「快出 API」，WordPress.org 支援信箱改用自架 FreeScout。

### 1. François Chollet（@fchollet）｜AI
他說「意識來自運算基質，AI 也是運算，所以 AI 可能有意識」這種論證，就跟「生物由原子組成，石頭也是原子，所以石頭可能是活的」一樣沒有意義。延續昨天的 AI 意識辯論，這則互動量破兩千讚、三百多則回覆。
https://x.com/fchollet/status/2106547436244304232

### 2. DAIR.AI（@dair_ai）｜MCP／Agent
摘要 NVIDIA 一篇終端 agent 測試時運算論文：先取樣多個候選 shell 指令、執行前先驗證再挑一個跑，而且預算該多花在驗證器上，而不是多取樣。做 CLI／DevOps agent 的人可以直接拿來改 harness 設計。
https://x.com/dair_ai/status/2106700907106943107

### 3. DAIR.AI（@dair_ai）｜MCP／Agent
Meta 的 RankEvolve 論文：讓 coding agent 自動跑 ML 實驗時，一個評估資料外洩或梯度斷線的隱藏 bug，就可能讓好幾小時的訓練和後續迭代全部作廢。RankEvolve 強制每個研究階段都要過關檢查，讓自動研究 agent 更可靠。
https://x.com/dair_ai/status/2106529236676976773

### 4. Claude Code Changelog（@ClaudeCodeLog）｜AI／開發工具
Claude Code 2.1.289 上線，共 27 項 CLI 變更：隊友可以用 agent.spawn 產生共用 agent、agent ID 統一並釐清 idle／waiting 狀態，也修掉使用者外掛會改寫組織管理的 MCP server 登入說明的問題。
https://x.com/ClaudeCodeLog/status/2106525277618635228

### 5. Mario Nawfal（@RoundtableSpace）｜開源
貼文指出 HeyGen 開源了內部用 AI agent 做影片的工具 HyperFrames：agent 寫 HTML，就能算圖成真正的 MP4，支援 GSAP、Three.js、Lottie，附 21 個 Claude Code skills，算圖不另收費。
https://x.com/RoundtableSpace/status/2106666885928657018

### 6. Lily Ray（@lilyraynyc）｜SEO
她在 Substack 新文中整理：從 Google 近期的公開說法和文件修改來看，各種跡象都指向一次重大 Google 更新即將到來。內容站與電商站最好先盤點品質與主要內容。
https://x.com/lilyraynyc/status/2106854591623000282

### 7. Glenn Gabe（@glenngabe）｜SEO
轉述 Google Search Central Live 巴塞隆納場的爬取預算說明：Google 不清楚某個網址的品質或熱門程度時，會用它上層路徑的整體表現來推估，再往上一層層類推。網站目錄結構和同路徑下的內容品質，會直接影響新頁面被爬的需求。
https://x.com/glenngabe/status/2106743953194090822

### 8. Cyrus Shepard（@CyrusShepard）｜SEO
他酸 Google 一直強烈暗示別大量產 AI 內容，除非你是大品牌，或者就是 Google 自己。這則兩百多讚，反映 SEO 圈對 Google AI 內容政策雙重標準的不滿。
https://x.com/CyrusShepard/status/2106634277677109253

### 9. Joost de Valk（@jdevalk）｜WordPress／SaaS
Yoast 創辦人說：你不出 API，客戶就會照你網頁的 HTML 自己做一個。他遇過一個 web app 底層明明就是 JSON API，只是不給客戶 key，結果他直接用 headless browser 自動化它的介面。結論是「Ship the API」，在 agent 時代更是如此。
https://x.com/jdevalk/status/2106692264370057484

### 10. WordPress（@WordPress）｜WordPress
WordPress.org 的支援信箱接下來幾週要從 HelpScout 搬到自架的 FreeScout。已有 HelpScout 帳號的人會透過 WordPress.org 帳號直接取得權限，不需要另外註冊，官方也公布了分階段計畫。
https://x.com/WordPress/status/2106761422260597186
