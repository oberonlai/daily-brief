# Threads 社群熱門｜2026-10-06（二）

只收繁體中文貼文。英文、日文，以及清潔／除毛店徵短影音代操／工作室招租類「個人接案」、純服務廣告、wordpress.com 個人部落格轉貼都沒放；前幾天已收過的貼文不重複。優先近 48 小時，「一人公司」「個人接案」TOP 多為舊文或無關，改看 RECENT。

### AI Agent

裸搜「AI Agent」TOP 仍以英文、日文為主；繁體中文今天有三則可看。

### 1. @aiposthub｜agent 的下一步是「決策層」，不是更大的模型
作者認為 AI Agent 接下來的重點，是讓它知道現在該用哪個模型、某個工具該不該呼叫、某個動作風險太高要不要擋下來，也就是所謂的 Decision Layer。做 agent 產品時，路由和護欄可能比換模型更值得花力氣。
https://www.threads.com/@aiposthub/post/DeHWQrCgUKo

### 2. @aiposthub｜不重新訓練，只改工作流程，準確率 46% 變 62%
介紹一篇叫 MOSiB（Mixture of Self-Improving Branches）的研究：同一個模型不重新訓練，只把 agent 流程拆成幾條各自練成專長的分支，數學準確率就從 46% 提高到 62%。數字為貼文說法。
https://www.threads.com/@aiposthub/post/DeGMyriAVIk

### 3. @teamhouse.tw｜OpenAI 文字浮水印 textGrain 的限制
10/6 的 AI 晨報整理 OpenAI 公告：API 客戶可在部分模型選擇啟用文字浮水印（預設關閉），歐盟的 ChatGPT 與 Codex 文字輸出未來數週分階段加入。貼文引述的限制是，誤判率 1% 時約能辨識 80% 的 200-token 文字、95% 的 400-token 文字，同義詞替換 25% 後只剩 17%，而且偵測結果不能判定作者身分或內容真偽。數字為貼文說法。
https://www.threads.com/@teamhouse.tw/post/DeIXJ6hk6kP

### WordPress

裸搜 WordPress 今天沒有繁體中文正題，近 48 小時幾乎都是日文店家與 wordpress.com 轉貼。

### WordPress 外掛

### 4. @wpmax_tw｜10/6 免費外掛早報（WooCommerce 偏多）
今天五款：給活動、藝術家、店家用的媒體新聞包建構器（VEFpressKit）、商品頁「出價議價」按鈕（MOAW Price Negotiation）、訂單異常與排程錯誤的站內監控警報（StoreCanary Order Monitor）、WooCommerce Subscriptions 的取消挽留與問卷（Retention Core），以及深度整合區塊編輯器的表單（Streamery Forms）。訂單監控和取消挽留這兩類，都是台灣電商客戶會買單的題目。
https://www.threads.com/@wpmax_tw/post/DeIVs3UDKYu

### 5. @william0348｜Claude Code 全自動經營的 WordPress 旅遊站
作者說一個上線不到三個月、由 Claude Code 驅動的日本旅遊網站，自然流量呈指數成長。做法包括讓 Claude 自己寫 WordPress API 套件來建文章、分類、上傳圖片和填 SEO 欄位，直連 FTP 部署，後來改成 Headless 架在 Google Cloud Run；用內建搜尋做事實查核，串 Google Search Console API 每週依曝光和點擊重新優化文章，並讓模型自行在文章裡置入旅遊平台商品卡。流量成長為貼文說法。
https://www.threads.com/@william0348/post/DeFHk2Zk3iS

### 6. @gino0406｜自寫網站系統只吃 WordPress 五分之一資源
作者自己寫了一套網站系統，發現資源只需要 WordPress 的五分之一，也不必花太多時間顧安全；他點出 WordPress 裝外掛時會不知不覺多出一堆 Cron 排程。不過他也認同，要交接給別人時，WordPress 這種標準化還是重要，自用才適合只求自己熟。
https://www.threads.com/@gino0406/post/DeHSEVZEqf9

### WordPress 架站

這一題今天有三則在找人，可能是接案機會。

### 7. @andywang2190｜品牌徵求網站設計與架站長期夥伴
已有品牌素材、商品圖和文案，想找人從版面規劃、視覺、首頁／商品頁設計、後台設定、RWD 到正式上線一路做完；平台可用既有的，也可由夥伴規劃自架。要求附作品集、熟悉的平台、時程、完整報價，以及後續修改次數與維護方式。
https://www.threads.com/@andywang2190/post/DeG0vzgow2V

### 8. @lebleu0315｜用了 10 年的 Weebly 官網跟著下架
作者說 Weebly 平台下架台灣，用了十年的官網也一起消失，正在問有沒有好用的免費架站平台。Weebly 退出台灣是貼文說法；如果屬實，會有一批小店家需要搬站。
https://www.threads.com/@lebleu0315/post/DeF1r-_AQtz

### 9. @eiji.hsp01｜自己架的站，對防駭沒信心
想找能長期配合的工程師處理網站基礎建設，因為對自己架站的資安沒信心，也不信任 AI 說它能檢查。「架站後維運與資安」是一個明確的付費需求。
https://www.threads.com/@eiji.hsp01/post/DeFN76ljwfX

### 10. @dev_classroom｜同樣是網站，價錢為什麼差十倍（粵語）
香港帳號用粵語寫：租平台（模板、Wix、Shopify）每月付費、改動受限、搬走麻煩；買現成系統再改（WordPress）程式碼是你的，但要養外掛、主題和更新；請人自建則是一次寫好、之後改自己的東西。三種買的根本不是同一件事，所以拿報價時別只問多少錢。可當跟客戶解釋報價的素材。
https://www.threads.com/@dev_classroom/post/DeGhrX-kYVw

### 架站

### 11. @iwant.seo｜品牌舊網域到期，被撿去掛娛樂城
作者追查發現，多個台灣品牌（含牙醫、肉圓店、眼鏡行、嬰兒用品，以及費雪牌台灣網站）的舊網址因為沒續約被人重新註冊，拿來掛娛樂城內容，借用舊站累積的外部連結和 Google 信任度。他查到這批網域都是今年才在同一家國外註冊商被註冊，6 到 7 月一個月就被撿走 7 個，最快 9 天就被收錄。品牌名單與數字為貼文說法。幫客戶搬站時，提醒保留舊網域並設好轉址，是很實際的一句話。
https://www.threads.com/@iwant.seo/post/DeHmGc3iXUb

### 12. @ting_z.001｜把整套寄信系統搬回自己主機的開源專案
作者說 10/4 Product Hunt 日榜第五名有個開源郵件系統，能自架 REST API、SMTP、模板、群發與自動化，不按封計費，從 Resend 遷過來只要改兩行程式碼；他建議接案者可以拿來省掉「郵件服務另計」。貼文沒寫出專案名稱，排名與遷移難度都是貼文說法；文末是作者自己的訂閱服務宣傳。
https://www.threads.com/@ting_z.001/post/DeGZZDNDvOM

### 個人接案

搜「個人接案」近 48 小時幾乎都是清潔、除毛店徵代操、工作室出租、工程備標服務廣告，沒有軟體或架站的正題。從「架站」搜到一則相關的：

### 13. @nisssss_zz｜接案一年，終於要做工作室官網
做文字、企劃、設計接案滿一年，準備做工作室官網，問同業做了官網之後有什麼改變。底下回覆是了解接案者為什麼要官網、在意什麼的好樣本。
https://www.threads.com/@nisssss_zz/post/DeGngC2E2dU

### 一人公司

近 48 小時沒有繁體中文正題，只有畫作貼文和 AI 工具廣告。補一則稍早（10/2）的：

### 14. @stonez56｜不找代辦，21 天自己把公司設起來
作者從公司名稱預查、籌備戶與驗資、設立登記、刻大小章、健保投保單位、稅籍統編、工商憑證，一路做到籌備戶轉正式戶和電子發票申請，全程自己辦，每一步都在 Threads 寫成 DAY1 到 DAY21 的紀錄。適合想開一人公司的讀者照著走。
https://www.threads.com/@stonez56/post/Dd-dgduGIUO
