# GitHub 熱門 × SaaS idea 早報｜2026-10-12

今天挑 6 則新上榜 repo（5 則非 WP、1 則 WP）；另排除大量偽裝成破解軟體的垃圾 repo 與逆向工程、漏洞賞金類。

## 1. aindeev/agent-chrome-relay — 讓 AI agent 用你已登入的 Chrome
https://github.com/aindeev/agent-chrome-relay
- 來源重點：Go 寫的中繼，讓 agent 在背景分頁以你的登入身分操作 Chrome，約 250 星。
- 為什麼值得做：agent 卡關最多的就是登入與驗證，直接借用真實瀏覽器 session 省掉大量麻煩。
- 產品構想：做成給小團隊的「agent 瀏覽器代理」託管服務，附權限白名單與操作紀錄。
- 難度／切入點：中；安全與稽核是賣點，先做網域白名單＋每步截圖紀錄。

## 2. Atoll92/agent-standup — 把 Claude Code 工作過程變成動畫視訊會議
https://github.com/Atoll92/agent-standup
- 來源重點：VS Code 擴充／本機 node server，把 agent session 演成即時團隊通話，約 130 星。
- 為什麼值得做：多個 agent 同時跑時，人很難一眼看出誰在做什麼。
- 產品構想：多 bot 狀態儀表板，把每個 bot 的進度做成「站會」畫面，可分享給客戶看。
- 難度／切入點：低到中；先接 Claude Code／Cursor 的 log 做唯讀看板。

## 3. fayazara/robot-heads — 顯示 agent 狀態的 3D 機器人頭像
https://github.com/fayazara/robot-heads
- 來源重點：React 元件，LED 臉表情反映 agent 正在思考、執行或完成，約 240 星。
- 為什麼值得做：AI 產品越來越需要有個性的狀態回饋，而不是只有 loading 轉圈。
- 產品構想：做成 WordPress／網站客服聊天框的頭像外掛，依回覆狀態變表情。
- 難度／切入點：低；包成 Web Component 就能嵌進任何站。

## 4. liyupi/ai-promo-video-maker — 一句話讓 AI 做產品宣傳片
https://github.com/liyupi/ai-promo-video-maker
- 來源重點：給 Cursor／Claude Code 用的流程，自動調研產品、截 4K 頁面、卡點剪輯，約 140 星。
- 為什麼值得做：獨立開發者都需要上架影片，但不會剪片。
- 產品構想：繁中版「SaaS／外掛上架影片」服務，輸入網址就出 30 秒影片，適合 Product Hunt 與 WP 外掛頁。
- 難度／切入點：中；先固定 2–3 種模板，渲染用 Remotion。

## 5. lawrencewzen/wx-bot — 把微信接到你的 AI agent
https://github.com/lawrencewzen/wx-bot
- 來源重點：透過官方 iLink 把微信接到 Grok／Claude 等 agent，約 110 星。
- 為什麼值得做：通訊軟體是 agent 最自然的入口。
- 產品構想：對應台灣市場做 LINE 版「個人 AI 助理橋接」，多 agent 路由＋待辦整理。
- 難度／切入點：中；LINE Messaging API 現成，難在記憶與權限設計。

## 6. Automattic/liberate.sh — 把任何網站轉成 WordPress（WP）
https://github.com/Automattic/liberate.sh
- 來源重點：Automattic 官方新工具，把任意網站轉成可下載、可自架的 WordPress 站，約 13 星。
- 為什麼值得做：從 Wix／Squarespace 搬家到 WP 一直是痛點，官方出手代表需求確定。
- 產品構想：在它之上做「搬家代辦＋SEO 轉址檢查」服務，搬完自動比對舊站網址與 meta。
- 難度／切入點：低到中；先做搬家後的 301 與 SEO 差異報告。
