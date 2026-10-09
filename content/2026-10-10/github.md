# GitHub 熱門 × SaaS idea 早報｜2026-10-10

今天新上榜的高星 repo 不多（趨勢榜大多已報過，另有大量偽裝成破解工具的垃圾 repo 已排除），挑 5 則；WordPress 相關今天沒有值得報的新 repo。

## 1. HelixDB/helix-foundry — 本機優先的公司資料本體庫
https://github.com/HelixDB/helix-foundry
- 來源重點：把公司各處資料串成一個 ontology，跑在自己電腦上，約 500 星。
- 為什麼值得做：小團隊想要 Palantir 式「資料全連起來」但不想上雲。
- 產品構想：給台灣中小企業的「本機知識圖譜」：接 Google Drive、Notion、WooCommerce 訂單，讓 AI agent 查詢。
- 難度／切入點：中高；先做 2–3 個資料源 connector＋MCP 介面。

## 2. franzenzenhofer/big-arrow-on-the-screen — 讓 AI agent 在螢幕上畫箭頭
https://github.com/franzenzenhofer/big-arrow-on-the-screen
- 來源重點：一個 CLI，讓 agent 在 Mac 螢幕上畫箭頭、框和文字，可點穿、自動消失，約 420 星。
- 為什麼值得做：agent 操作電腦時，人類需要看懂「它要點哪裡」。
- 產品構想：教學／客服用的「AI 螢幕指引」：遠端教客戶操作 WP 後台時直接標示位置。
- 難度／切入點：低中；包成 MCP server＋跨平台版本。

## 3. scarletkc/Hatoba — 內建 AI 的開源 SSH 客戶端
https://github.com/scarletkc/Hatoba
- 來源重點：桌面 SSH client，附 AI 助手，透過自己的 Cloudflare 做端對端加密同步。
- 為什麼值得做：維運多台主機（如 Kinsta、InstaWP）的人需要 AI 幫忙下指令又不想交出金鑰。
- 產品構想：專給 WordPress 主機維運的 SSH＋WP-CLI AI 助手，內建常用救站指令。
- 難度／切入點：中；從 WP-CLI 指令建議＋操作紀錄做起。

## 4. BinceQu/RoboHarness — 給 LLM agent 的機器人視覺控制面板
https://github.com/BinceQu/RoboHarness
- 來源重點：用視覺幾何控制面板讓 LLM 直接理解並操控機器人，約 220 星。
- 為什麼值得做：「agent harness」從軟體延伸到實體設備，是新興方向。
- 產品構想：借它的 harness 概念，做「把任何 GUI 轉成 agent 可操作面板」的 SDK。
- 難度／切入點：高；先觀察，適合作為技術趨勢追蹤。

## 5. zhouwei713/luobo-ppt ＋ robbin/android-adb-control — Agent Skill 生態持續長
https://github.com/zhouwei713/luobo-ppt
https://github.com/robbin/android-adb-control
- 來源重點：一個是生成可編輯原生 PPT 的 Agent Skill，一個是用 ADB 控制 Android 手機的 Skill（支援 Codex、Claude Code 等）。
- 為什麼值得做：Skill 正變成可販售的小型產品單位。
- 產品構想：做繁中市場的 Skill 市集或付費 Skill 包（簡報、電商上架、手機 App 測試）。
- 難度／切入點：低；先自己寫 3–5 個繁中 Skill 上架測水溫。
