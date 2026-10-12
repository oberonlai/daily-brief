# GitHub 熱門 × SaaS idea 早報｜2026-10-13

今天挑 7 則新上榜 repo（5 則非 WP、2 則 WP）；另排除偽裝成破解軟體的垃圾 repo、繞過帳號／指紋偵測的工具，以及逆向工程、滲透測試類。今天有一波「麥當勞中國官方 MCP」程式設計師節參賽作品洗版，合併成一則看趨勢。

## 1. zhuyansen/new-term-radar — 搶在關鍵字工具之前抓到 AI 新名詞
https://github.com/zhuyansen/new-term-radar
- 來源重點：每天從 X、Hugging Face 熱門、GitHub 爆紅 repo、競品 sitemap 與新註冊網域抓出剛冒出的模型／產品名稱，Google Trends 只拿來回頭驗證，約 510 星。
- 為什麼值得做：新詞從出現到進關鍵字工具要好幾天到幾週，做內容站和電子報的人最需要搶這段時間差。
- 產品構想：繁中版「AI 新詞雷達」訂閱服務，每天早上推一份新詞清單＋建議標題，可直接接 OpenSEO 與 Search Console 看自己站有沒有吃到曝光。
- 難度／切入點：中；先只做 X＋GitHub＋HF 三個來源，輸出成每日 email／頁面，再加 sitemap 監控。

## 2. onehumanbeing/esp32-iphone-agent — 用 7 美元 ESP32 讓 AI 操作真的 iPhone
https://github.com/onehumanbeing/esp32-iphone-agent
- 來源重點：AirPlay 當眼睛、USB HID 當手，接任何 OpenAI 相容視覺模型，不需要 Mac、開發者帳號或越獄，約 510 星。
- 為什麼值得做：手機 App 的自動化與測試一直被 iOS 封閉卡住，硬體外接繞開了這層限制。
- 產品構想：「真機 App 巡檢」服務，每天用 AI 跑一遍客戶 App 的註冊、下單流程並截圖回報，適合沒有 QA 團隊的小公司。
- 難度／切入點：中到高；先做單一 App 的固定腳本巡檢＋失敗截圖通知，硬體用現成套件出貨。

## 3. chekusu/yobiru — 讓不同電腦上的 agent 互相傳訊、交檔、叫醒彼此
https://github.com/chekusu/yobiru
- 來源重點：走 Tailscale 連接個人 agent，用 `host/agent` 定址傳文字、JSON 和檔案，接收端可設誰能叫醒誰、安靜時段與頻率限制，README 直接舉 Grok Bot 當例子，約 110 星。
- 為什麼值得做：一人公司常同時跑好幾個 bot，彼此交接全靠人工複製貼上。
- 產品構想：託管版「agent 訊息匯流排」，給多 bot 用戶一個收件匣看所有 bot 之間的交接紀錄與待決事項。
- 難度／切入點：中；先做唯讀的交接紀錄看板，權限與叫醒規則照它的設計。

## 4. shaongitbd/doory — 開源、可自架的 Canva 替代品
https://github.com/shaongitbd/doory
- 來源重點：React 19＋Django 5 的瀏覽器設計編輯器，海報、社群圖、簡報、名片都能做，可匯出 PNG／PDF／MP4／GIF，Docker 三行自架，約 775 星；授權是 Attribution Assurance，商用要保留署名。
- 為什麼值得做：小商家天天要做社群圖卡，Canva 團隊方案越來越貴，自架又沒有好選擇。
- 產品構想：在它上面做「品牌圖卡工廠」，預載客戶品牌色與字型，搭配 AI 一鍵把文章或商品轉成 IG／LINE 圖卡。
- 難度／切入點：中；先做繁中字型與 5 套台灣常用模板，再接 WordPress 文章自動出封面圖。

## 5. zhutoumeme/mcd-git — 麥當勞官方 MCP 參賽潮（用 git 指令點餐）
https://github.com/zhutoumeme/mcd-git
- 來源重點：`add` 放購物車、`rebase` 湊最省、`push` 確認才下單，約 74 星；同一週還有數十個基於麥當勞中國官方 MCP 的程式設計師節參賽 repo（比價、熱量、優惠券、碳足跡）。
- 為什麼值得做：品牌開官方 MCP＋辦開發者比賽，幾天內就換來幾十個免費產品原型和大量曝光，這套打法台灣還沒人做。
- 產品構想：幫台灣連鎖品牌或電商「代建官方 MCP＋辦黑客松」的顧問服務，從 WooCommerce／POS 資料直接生出唯讀 MCP。
- 難度／切入點：中；先用 WooCommerce 店做示範 MCP（菜單、價格、優惠券唯讀），拿去提案。

## 6. erayusta/kinetik — 專為土耳其在地化的 WooCommerce 佈景主題（WP）
https://github.com/erayusta/kinetik
- 來源重點：輕量經典 PHP 主題加四個獨立外掛，內建省／區／里三層地址、法定遠距買賣契約、銀行轉帳流程與當地貨幣格式，手機 390px 逐頁測過，約 4 星。
- 為什麼值得做：各國 WooCommerce 店家都卡在同樣的在地問題，台灣是超商取貨、電子發票、縣市區地址與 ATM 轉帳。
- 產品構想：「台灣 WooCommerce 在地套件」，地址三層選單＋超商取貨＋光貿電子發票＋轉帳對帳拆成可單獨買的外掛，主題當免費引流。
- 難度／切入點：中；先做縣市區地址＋電子發票兩個外掛，你手上已經有光貿串接經驗。

## 7. phuryn/work-humanizer — 去 AI 味但不改原意的潤稿 skill（WP 切入）
https://github.com/phuryn/work-humanizer
- 來源重點：Agent Skill 形式的工作文件去 AI 腔工具，附盲測評審、人工逐條檢查意思有沒有被改、Pangram 偵測分數當證據，約 104 星。
- 為什麼值得做：「去 AI 味」大家都在做，但很少有人證明改完沒有偷改承諾和事實，這正是企業敢用的關鍵。
- 產品構想：把它的「意思不變」檢查流程搬進你正在做的 WP 人味潤稿外掛，潤稿後並排顯示改動處與意思是否變動。
- 難度／切入點：低到中；先借它的規則清單與評測方法，在 Gutenberg 側欄加「改動對照」面板。
