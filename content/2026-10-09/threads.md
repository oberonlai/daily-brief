# Threads 社群熱門｜2026-10-09（五）

今早排程失敗，這份是補產的（改用 Po Once 關鍵字搜尋，不靠瀏覽器）。

只收繁體中文貼文。英文、日文、西班牙文、簡體中文（例如用 Hermes AI agent 串公司系統那則），以及美容床位分租、美業空間頂讓、居家清潔、短影音代操、剪輯師徵才這類「個人接案」純服務廣告、wordpress.com 個人部落格轉貼都沒放；前幾天已收過的貼文不重複。只看近 48 小時。各題 RECENT 結果偏少、TOP 幾乎都是舊文，所以另外補搜了「AI 架站」「網站架設」「獨立開發」「Codex」，挑出跟主題相關的放進對應分類。

### AI Agent

### 1. @danieltsai04｜讓 AI Agent 改正式資料庫，先想清楚「改錯能不能退」
作者的重點是：Agent 寫錯程式，revert 一個 commit 就能回來；但改錯資料庫 schema，資料可能就回不來。他舉 PlanetScale 的做法，讓資料庫變更像 Git 一樣可以開分支、審查、退回，認為這正是 agent 能安全上手的條件。用 AI 幫客戶改 WordPress 站時也一樣，資料庫備份和測試站要先準備好。
https://www.threads.com/@danieltsai04/post/DePY9IDnzix

### 2. @ivansoig｜8 個 App 的 AdMob 設定，交給 Claude 的 Chrome 控制功能
作者做完 8 款 iOS App，要在 AdMob 逐一新增 App、核實 App Store 連結、建立廣告單元、複製 ID，手動估計要 2～3 小時。他改成跟 Claude 的 Chrome 控制功能說明要做什麼，讓它自己在瀏覽器點擊、填寫，最後整理出各個 ID，他只負責檢查結果。他的結論是：步驟固定、重複、不需要創意的網頁雜務最適合交給 AI 代理，這套思路也能套到外掛後台設定這類重複操作。
https://www.threads.com/@ivansoig/post/DeQBoHYE8dX

### 3. @11.6_d_m_b_｜idea-to-launch：把模糊想法推到上線計畫的開源 skill
介紹一組開源的 AI prompt（skill），重點不是叫 AI「給我一個賺錢點子」，而是把好幾個想法擺在一起，用「可行、原創、好行銷」三個標準篩一輪，選一個再往下規劃到上線。作者說適合手上一堆靈感卻不知從哪下手的獨立開發者、小工作室和副業族。
https://www.threads.com/@11.6_d_m_b_/post/DeQLAhinzf_

### 4. @learn.invest｜被 Codex 氣到，改回 Claude 20x 方案
作者抱怨最近用 Codex 不管選哪個模型都不順：簡單工作拆成很多段還做不完、來回授權溝通幾小時，核心問題還是沒解決。他說同一份指令丟給 Opus 5.5，一小時就跑完，所以把 Claude 恢復成每月 200 美元的 20x 方案、下個月要把 Codex 降級（以上都是貼文說法）。屬於個人使用心得，可以當作挑 coding agent 時的一個參考聲音。
https://www.threads.com/@learn.invest/post/DeP-QwXiPBH

### WordPress 外掛

### 5. @wpmax_tw｜10/9 免費外掛早報
今天五款：PHP 升級前的相容性診斷工具（CompatNav）、處理留言、WooCommerce 評價、Pingback 和 Contact Form 7 垃圾訊息的防護外掛（SpamLens）、管理外掛更新排程與安全的自動化工具（Orchestrator）、WooCommerce 的歐盟 GPSR 產品安全法規合規外掛（Lodestone），以及 WooCommerce 盤點維護模式（Stock Take Mode）。幫客戶升 PHP 前跑一次 CompatNav 這類檢查，可以少很多升級後才爆的狀況。
https://www.threads.com/@wpmax_tw/post/DeQEFMIDICt

### 6. @wpmax_tw｜Return Refund and Exchange：WooCommerce 退換貨管理
單則外掛介紹，主打把售後服務自動化，幫 WooCommerce 商店建立退換貨管理流程。貼文只有一句介紹，功能細節要看外掛頁面。
https://www.threads.com/@wpmax_tw/post/DeOWSDTGUMi

### WordPress 架站

### 7. @piecesofme.cc｜想做網站以為要用 WordPress，朋友說「不用」
作者的需求是沒有購物、沒有金流、放很多文字和照片的個人網誌，問了有 SEO 和架站經驗的朋友，對方建議不用 WordPress，直接用「資料夾」方式部署。她先試 Wix，覺得字型、顏色、細節綁手綁腳，最後還是自己走上 GitHub、Cloudflare、Python 的自建路線。這類「純內容網站不一定需要 WordPress」的討論越來越多，教學時把選型理由講清楚會更有說服力。
https://www.threads.com/@piecesofme.cc/post/DeO-WQ9jmRt

### 8. @shinyan.woo｜AI 能做出 60 分的網站，剩下的才是專業
作者說現在做網站不難：跟 AI 工具講清楚你是誰、服務什麼、對象是誰，再丟現有素材，就能產出 60 分的網站，但從 60 分到 100 分還要再加油。貼文接著說有某些需求的話還是建議找她架站，不過抓到的內容沒有列出是哪些需求。對接案者來說，這也是現在常見的定位方式：AI 負責起步，人負責補完那 40 分。
https://www.threads.com/@shinyan.woo/post/DeO7z0KFArX

### 架站

### 9. @seo.lighting｜AI 架的電商站很漂亮，要串 LINE Pay 才發現沒後台
作者的朋友照著「30 秒用 AI 生成網站」的教學架了電商站，視覺很好，直到想串 LINE Pay 才發現沒有後台選項，想連動庫存系統平台也不提供 API。作者用買車比喻：作品集或形象官網用 AI 很夠，要經營事業就該找專業公司或用正規方式自學架站。跟昨天幾則「AI 架站交付品質」的討論是同一個方向，也是 WooCommerce 方案好切入的說法。
https://www.threads.com/@seo.lighting/post/DeOZM6pkhe1

### 10. @frankchiu.mkt｜秒站支援 ChatGPT Ads 追蹤代碼
秒站的「數位行銷代碼安裝」功能新增支援 ChatGPT Ads tagging，讓網站主更容易設定行銷追蹤代碼。貼文只有這段公告。ChatGPT 廣告的追蹤代碼開始被台灣架站平台支援，WordPress 站之後大概也會遇到客戶問怎麼裝。
https://www.threads.com/@frankchiu.mkt/post/DeO6wmZFBLI

### 11. @somehowworks.dev｜接手爛攤子案子，第一步不是開編輯器
作者說接手案子時會先列四件事：誰每天在用、哪個部分絕對不能停、哪個數字最不可信、改壞了怎麼退回。他的觀點是善後不是比誰改得快，先把不能碰的地方圈起來才知道哪裡能動；新網站架設也一樣，先列誰要用、一定要有什麼、什麼時候上線。文末是自家服務宣傳，但這份清單很適合接手別人做壞的 WordPress 站時直接拿來用。
https://www.threads.com/@somehowworks.dev/post/DeOVFeLFv6H

### 個人接案

### 12. @leon._.01_.21｜開發公司說：大型客製案別找個人工作室
布谷數位的宣傳文，主張大型系統、客製化 Web／App 專案應該避開個人接案工作室：雖然便宜，但卡關或工程師跑路時容易變爛尾樓，還說他們有些客戶原本就是先找個人工作室（貼文說法）。他們主打 7 年經驗、每案配 PM、前後端工程師和 UI/UX 設計師 4 人小組。這是公司端對個人接案者的典型攻擊點，個人接案者可以想想自己怎麼回應「穩定性」的疑慮。
https://www.threads.com/@leon._.01_.21/post/DeOfwo9kxIT

### 13. @bell_studio1006｜從皮膚管理跨到網站架設接案
作者原本做皮膚管理和個人色彩，經營自己的品牌後發現技術好不代表別人看得見，品牌定位、視覺、社群和網站都要摸索。她認為品牌跟個人色彩一樣，不該套同一個模板，所以最近也開始接網站架設與規劃。從別的專業跨進架站接案的人變多，也是 WordPress 課程的潛在學員。
https://www.threads.com/@bell_studio1006/post/DeNvAjYH5zL

### 一人公司

### 14. @yangmicky｜一人公司、沒融資，Claude Startups 申請通過
作者前天在 X 看到 Claude Startups 計畫擴大招生，當天申請，10/9 早上 07:29 收到「You're in」的通過信，條件是一人公司、bootstrapped、沒拿過融資。他列出拿到的福利：1,000 美元 Claude API credits（6 個月內用完）、Claude Team 免費 1 年 5 個 Premium 席位、最高 4.5 萬美元的 Startup Stack 兌換碼（含 ElevenLabs、Granola、Linear 等），以及每兩週一次 Anthropic 團隊的 office hours（都是貼文說法）。他說有整理完整申請攻略，正在用 Claude 做產品的一人公司值得看。
https://www.threads.com/@yangmicky/post/DeQS-G6k3mJ

### 15. @bendyyip｜一人網頁工作室：你 WhatsApp 的那個人就是做事的人
香港的網頁設計師（粵語貼文）說很多客戶來找他之前都有一間「前任」網頁公司，抱怨都是不回訊息、做事沒交代。他認為大公司回覆慢多半是結構問題：客戶問業務、業務問 PM、PM 再問工程師，一層層轉。他做了 15 年一人工作室，主打客戶直接聯絡到做事的人。這正好可以回應上一則「個人工作室不穩」的說法，是一人接案者很好用的差異化話術。
https://www.threads.com/@bendyyip/post/DeQVc14GarO
