# X 熱門早報｜2026-10-02（週五）

François Chollet 把「現代 LRM」與舊版 LLM 的差異講清楚（從猜答案變成猜程式）；Cloudflare 開源決策模型 Clef 與 multi-harness RL 指南同時刷版。SEO 圈則在推品牌 AI instructions 頁、看 AI Overviews 訴訟被駁回，以及「agent 怎麼用網站」的研究。WordPress 側 WPVibe 破 5 萬安裝、Woo 官方區塊主題 Purple 進 beta；穿戴裝置也開始用 WebMCP 定義 agent 可控介面。

### 1. François Chollet（@fchollet）｜AI coding agents
他主張：2024 年前的 base LLM 與現代 LRM 的關鍵差異，不是會不會用符號工具，而是從「直接直覺出答案」（transductive）切到「直覺出能產出答案的程式／指令」（inductive）。這正好對上 agent／coding harness 為什麼突然變好用。
https://x.com/fchollet/status/2105729206273634696

### 2. Peter Steinberger（@steipete）｜AI coding agents
他轉發並感嘆 Cloudflare 釋出兩款自家訓練的決策模型 Clef 與 Clef-flash——「從沒見過一個想法傳這麼快」。小型專用決策模型進基礎設施層，是 agent 堆疊下一波值得盯的產品訊號。
https://x.com/steipete/status/2105778011635400949

### 3. Adithya S K（@adithya_s_k）｜AI coding agents
發布「multi-harness RL」終極指南：同一模型在不同 agent harness 行為不同，因此用開放方式在 Claude Code、Codex、OpenCode 等真實 harness 裡對任意任務集做 RL，不必綁死單一環境。實務訓練與評測開始對齊「人實際在用的殼」。
https://x.com/adithya_s_k/status/2105684965891703141

### 4. Chris Long（@chris_nectiv）｜SEO
再次強調：立刻做 AI instructions 頁——它能大幅影響品牌搜尋上出現的 AI Overviews。收藏與轉發都很高，顯示搜尋圈把「給模型看的品牌說明」當成可操作的 GEO／AIO 動作，而不只是理論。
https://x.com/chris_nectiv/status/2105655128162468334

### 5. Barry Schwartz（@rustybrick）｜SEO
針對 Google AI Overviews、以及未以流量或其他方式補償出版商的訴訟已被駁回。短期內「用搜尋摘要換授權金」的司法路線受挫，出版商與 SEO 仍得多靠產品與協議談判，而不是法庭。
https://x.com/rustybrick/status/2105682486453739896

### 6. Aleyda Solís（@aleyda）｜SEO
推薦 MERJ／@giacomozecchini 的研究《How AI Agents Use Websites, Where They Fail, and What to Fix》：100 個目的導向測試、多模型跑過，拆解 agent 怎麼逛站、卡在哪、站方該修什麼。對要讓站點被 agent「用」而不只是被爬的人是必讀。
https://x.com/aleyda/status/2105688103541256697

### 7. Lily Ray（@lilyraynyc）｜SEO × AI
提問：大家有沒有注意到 GSC 裡 Generative AI impressions 佔整體比例意外地低？討論把「AIO／生成式曝光」從行銷幻燈片拉回 Search Console 可驗證的數字，對評估品牌 AI 能見度很實際。
https://x.com/lilyraynyc/status/2105654001458897065

### 8. Syed Balkhi（@syedbalkhi）｜WordPress
WPVibe 突破 5 萬次安裝（兩週前還約 3 萬）。外掛讓 WordPress 站接上 ChatGPT、Claude、Cursor 等——WP 生態把「站點當 agent 工具後端」產品化的速度在加快。
https://x.com/syedbalkhi/status/2105672681961984394

### 9. WordPress.com（@wordpressdotcom）｜WordPress
WooCommerce 第一款官方區塊主題 Purple 已進 beta，歡迎商店當測試廚房並回饋給 Woo 團隊。區塊主題路線從內容站延伸到電商前台，值得店家與主題開發者跟著試。
https://x.com/wordpressdotcom/status/2105663159730135101

### 10. Oscar Falmer（@OscarFalmer）｜WebMCP
Meta Ray-Ban Display 的 Web Apps 更新提到 WebMCP：在 app 裡定義 Meta AI 能控制什麼，讓使用者用口語把事情做完。WebMCP 從瀏覽器／桌面 agent 實驗，開始出現在穿戴裝置產品敘事裡。
https://x.com/OscarFalmer/status/2105719397293928488
