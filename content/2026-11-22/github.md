# GitHub 熱門 × WP／SaaS idea 早報 2026-11-22

今天從 GitHub Trending、近 3／14 天新建高星 repo 與 Show HN 中篩選。搜尋結果混有大量遊戲外掛／破解類垃圾 repo，已全部排除。

## 一、SaaS／開發者工具

### 1. TamServe：多路攝影機即時物件追蹤服務
- GitHub：https://github.com/aryamandarda/tamserve （建立：2026-11-11）
- 來源重點：Show HN 123 分；以 SAM3／SAM 2／EdgeTAM 在單張或多張 GPU 上服務多路即時影像追蹤，Apache-2.0，約 269 星。
- 為什麼值得做：零售、工廠、停車場需要「看得懂畫面」，但中小企業沒有 ML 團隊自架。
- 產品構想：託管式「攝影機 → 追蹤事件 webhook」SaaS，按攝影機路數月費，提供人流熱區、停留時間、區域入侵告警儀表板。
- 難度與切入點：中高（GPU 成本）。先鎖定台灣連鎖店人流統計，用 RTSP 接入。

### 2. TrnRT：AWS Trainium 的 LLM 推論引擎
- GitHub：https://github.com/RunanywhereAI/trnrt （建立：2026-10-30）
- 來源重點：Show HN；約 1,650 星；NKI megakernel、100 萬 token context、OpenAI 相容 API。
- 為什麼值得做：Trainium 比 GPU 便宜，但缺好用推論層，成本敏感團隊有誘因。
- 產品構想：「推論成本比價與遷移」服務：貼上現有 OpenAI 呼叫，自動基準測試並產出遷移到 Trainium 的成本報告與部署模板。
- 難度與切入點：高。先做成本估算器（輕量工具）導流，再賣託管。

### 3. Open Artifact：本機檔案化、與模型無關的 AI 產物編輯器
- GitHub：https://github.com/JimLiu/open-artifact （建立：2026-11-17）
- 來源重點：Trending 候選；約 142 星；簡報、UI 設計、白板等 AI 產物存成純檔案，可編輯、留言、匯出。
- 為什麼值得做：AI 生成的簡報／頁面常「生成完就卡住」，缺少審閱與協作流程。
- 產品構想：面向代理商的「AI 產物審閱平台」：客戶直接在 AI 產出的提案、網站稿上留言，版本與匯出集中管理。
- 難度與切入點：中。先做分享連結＋留言＋版本比較。

### 4. agy-fast：Antigravity 的 MCP 加速外掛
- GitHub：https://github.com/INK-Q/agy-fast （建立：2026-11-19）
- 來源重點：約 251 星，MIT；宣稱降低 LLM 回合數 34%、token 配額 31%、上傳流量 40%（作者自述，需自行驗證）。
- 為什麼值得做：Coding agent 的 token 成本是團隊痛點，優化有直接金額可衡量。
- 產品構想：「Agent 成本儀表板」：收集各 coding agent 的 token／回合紀錄，找出浪費模式並建議 MCP／設定調整。
- 難度與切入點：中。先做 CLI 本機分析日誌，產出週報。

### 5. MR Office：開源文件／試算表／簡報／PDF 編輯器
- GitHub：https://github.com/XinaTian/MROffice （建立：2026-11-10）
- 來源重點：約 1,411 星，AGPL-3.0；網頁版全套辦公編輯器，含手寫與程式碼編輯。
- 為什麼值得做：企業想要可私有部署的辦公套件，台灣中小企業與政府標案常有資料不出境需求。
- 產品構想：在地化部署服務：繁中字型、台灣公文／發票範本、SSO 整合，按席位收年費維運。
- 難度與切入點：中。注意 AGPL 授權，商業做法以「託管＋服務」為主，需先法務確認。

### 6. PiBot：本機優先的 AI 代理團隊桌面應用
- GitHub：https://github.com/w01fb0ss/PiBot （建立：2026-11-21）
- 來源重點：約 167 星，Apache-2.0；多代理群組聊天、電腦操作、瀏覽器、MCP、排程與核准機制。剛建立一天，需觀察穩定度。
- 為什麼值得做：「排程＋核准」是代理落地到小公司的關鍵，與同類產品相比強調本機隱私。
- 產品構想：垂直化代理團隊範本包（電商客服、行銷週報、財務對帳），以訂閱販售流程範本與核准規則。
- 難度與切入點：低到中。先賣範本與設定服務，不自己做底層。

## 二、WordPress

### 7. AI Connect（TensorPass）：網站用 AI 對話／答案式搜尋 SDK
- GitHub：https://github.com/tensorpass/aiconnect （建立：2026-11-12）
- 來源重點：約 31 星（早期），Apache-2.0；為網站加入 AI 聊天、能回答問題的搜尋列，由訪客自己的 AI 額度驅動。
- 為什麼值得做：「訪客自帶額度」讓站長免付 token 成本，是 WP 站點導入 AI 搜尋的最大門檻之一。
- 產品構想：WordPress／WooCommerce 外掛：把站內文章、商品索引後，提供答案式搜尋與商品推薦，不需站長負擔 API 費用。
- 難度與切入點：低到中。先做 WooCommerce 商品搜尋區塊（Gutenberg block），再擴到客服。專案很新，需評估 SDK 穩定度。
