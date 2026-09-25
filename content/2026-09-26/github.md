# GitHub Idea 早報 · 2026-09-26（台北）

> 訊號：GitHub Trending（日／週）＋ Search（9/20 後新建高星／gateway／影片／agent intent／WP）。非 WP 為主；今日新建爆點集中在「產品 launch 影片、本機 AI 閘道、短影音剪輯、意圖編譯、中文技術寫作 skill」，WP 側有自架 Woo 聯盟行銷外掛。

---

## 非 WP

### 1. URL／一句話 → Launch 影片 → 產品上線影片 SaaS
- **來源**：[diggerhq/shipvideo](https://github.com/diggerhq/shipvideo)（★~119，9/24 新建）— 貼網址或 prompt，產出 20–40 秒 launch 影片：Opus 寫單一 HTML 影片，OpenComputer 無頭 Chromium 逐幀渲染＋ffmpeg，無影片生成模型。
- **標籤**：非 WP
- **為什麼值得做**：獨立開發者與代理商最常缺「能投 Product Hunt／社群的上線片」；「抓站→配色→渲染」可做成可白牌的上線素材工廠。
- **構想**：「LaunchReel」— 輸入官網／App Store／GitHub README，出多比例 MP4；方案含品牌色鎖定、字幕語系、批次重渲；加 WP：從 Woo 商品頁一鍵產短片。
- **難度**：中；切入：先做 url→HTML film→ffmpeg 的單機／一鍵部署模板，再包表單與計費。

### 2. 本機 AI Gateway → 訂閱／金鑰統一路由與隱私層
- **來源**：[Calcium-Ion/AstrLink](https://github.com/Calcium-Ion/AstrLink)（★~67，9/22 新建）— 跨平台桌面本機閘道：把訂閱與各家 API 統到本地端點，智慧路由、裝置端隱私保護、請求紀錄。
- **標籤**：非 WP
- **為什麼值得做**：團隊已同時用 Claude／Codex／Cursor／自架模型；「本機閘道＋隱私乾跑＋用量」比再賣一把 API key 更好收費，也可白牌給主機商。
- **構想**：「Agency Link」— 代理商預設政策（哪個客戶站可用哪個模型、遮罩個資）；接 WP／Woo 後台只讀 MCP，所有外呼經閘道稽核。
- **難度**：中；切入：先做 OpenAI-compatible 本地 proxy＋單一 provider＋請求 log，再加路由規則。

### 3. 長片 → 帶字幕短影音 → 本機剪輯桌面產品
- **來源**：[bridge-mind/bridgeclip](https://github.com/bridge-mind/bridgeclip)（★~220，9/24 新建）— 開源 AI 剪輯桌面：本機跑、自帶 OpenRouter key；下載→轉錄→找高潮→FFmpeg 渲染，九種字幕風格、無後端。
- **標籤**：非 WP
- **為什麼值得做**：播客／直播／課程要大量短影音；「本機＋自帶金鑰」降低個資疑慮，可做成白牌給內容工作室。
- **構想**：「Clip Desk Pro」— 品牌字幕包、批次佇列、排程發佈；接 WP 媒體庫與 YouTube／短影音頻道。
- **難度**：中；切入：先支援本機檔＋一種字幕風格＋單一 LLM 選段。

### 4. 對嘴口播 → 成品 Reel → Agent 內建剪輯師
- **來源**：[kurbaitaev/ghost-editor](https://github.com/kurbaitaev/ghost-editor)（★~59，9/24 新建）— Coding agent skill（HyperFrames）：丟對嘴原片，自動去贅、臉安全字幕、動態圖、音效配樂；可從參考片反推剪輯風格。
- **標籤**：非 WP
- **為什麼值得做**：創作者最大成本是剪輯；「看一次參考片就學會風格」可做成訂閱制剪輯 agent，也可賣給電商／課程品牌。
- **構想**：「Ghost Edit Cloud」— 上傳口播＋選風格或貼參考 Reel；輸出 IG／TikTok／Shorts；WP 方案：商品講解片模板＋自動嵌商品頁。
- **難度**：中高；切入：先做 clean／launch 兩風格＋臉安全字幕驗證。

### 5. 模糊需求 →  typed IntentSpec → Agent 意圖編譯層
- **來源**：[angel291592/Intent-Router](https://github.com/angel291592/Intent-Router)（★~92，9/22 新建）— Agent 意圖編譯器：先探查 repo／票務／文件，只問真正缺的一題，輸出可機器讀的 IntentSpec，供下游路由與 Jev／Laya 類決策模型使用。
- **標籤**：非 WP
- **為什麼值得做**：代理商與客服最痛的是「需求講不清就開工」；意圖合約可降低重工，也是可賣的 intake 層。
- **構想**：「Intake Spec」— LINE／表單／工單進，出 IntentSpec＋估價草稿；WP 建站套餐用固定欄位模板（範圍、禁止改動、驗收）。
- **難度**：中；切入：先做「探查→一問→YAML 合約」skill，接一個工單來源。

### 6. 中文技術文件去 AI 腔 → 繁中文件／內容 Skill 產品
- **來源**：[leter/zh-tech-writing](https://github.com/leter/zh-tech-writing)（★~194，9/24 新建）— 寫中文技術文件的 Agent Skill，依阮一峰《中文技術文件寫作規範》：短句、平實、去掉 AI 腔。
- **標籤**：非 WP
- **為什麼值得做**：台灣／華語市場文件與官網最常「機器味重」；可直接做成繁中校對／官網文案 skill，也可賣給代理商當交付標準。
- **構想**：「繁中文件 Desk」— README／API／幫助中心批次改寫；加 WP：文章／商品說明一鍵去 AI 腔＋用語表（台語／產業詞可擴充）。
- **難度**：低～中；切入：先做 Claude／Cursor skill 包＋繁中用語檢查清單，再接 Gutenberg 側欄。

---

## WP

### 7. 自架 Woo 聯盟行銷 → 代理商／電商 Affiliate 外掛
- **來源**：[kamruzzamanbsc/dreamax-affiliates](https://github.com/kamruzzamanbsc/dreamax-affiliates)（★~6，9/10 新建）— 自架 WooCommerce 聯盟外掛：申請、推薦連結／coupon、佣金、報表、素材、手動撥款；資料留在站內，無強制外部帳號。
- **標籤**：WP
- **為什麼值得做**：中小電商要聯盟但不想鎖 Affilate SaaS；自架＋Blocks checkout＋隱私匯出符合在地代理商需求。
- **構想**：「Affiliate Desk for Woo」— 白牌門戶、多幣別撥款批次、詐欺規則；Pro：多站佣金同步與對帳匯出。
- **難度**：中；切入：先穩 Blocks checkout 歸因＋一種佣金規則＋手動撥款。

---

## 今日脈絡（一句）
產品化焦點從「會寫碼的 agent」轉向「能出上線片、能閘道控成本與隱私、能把模糊需求編成合約」；WP 側可跟進自架聯盟與繁中內容品質。

## 備註
- 掃過未採用已記入 seen（含日趨勢老專案、CVE／PoC 噪音、Jev 周邊、盜版／驗證碼繞過類等）。
- 未把 exploit／PoC 當產品構想來源。
