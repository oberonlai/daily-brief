# GitHub Idea 早報 · 2026-09-28（台北）

> 訊號：GitHub Trending（日／週）＋ Search（9/24 後新建高星／TS→原生編譯／多 agent 編排／本機 coding 工作區／本機歌曲工作室／豎版宣傳片／分類器蒸餾／Lemon×Elementor／Woo 可購買短影音）。非 WP 為主；今日新建／新趨勢集中在「把 TS 編成原生 CLI、把多把 coding agent 編成小隊、本機決策＋桌面工作區、本機 GPU 出歌、便宜模型出片、小模型取代分類 API」，WP 側有無 Woo 數位商品目錄與可購買 Reel。

---

## 非 WP

### 1. TypeScript → 原生執行檔／WASM → 無 Node CLI 分發平台
- **來源**：[vercel-labs/scriptc](https://github.com/vercel-labs/scriptc)（★~5.3k，Vercel Labs 實驗、今日 Trending）— 用 TypeScript 編譯器做解析與型別檢查，輸出 typed IR、可讀 C、LLVM IR、組合語言／物件檔、原生執行檔與 WASM；靜態編譯產物不需 Node；`--dynamic` 可嵌 quickjs-ng。
- **標籤**：非 WP
- **為什麼值得做**：代理商與 SaaS 常要交付「一支可執行 CLI／安裝器」，卻被 Node 執行時綁架；「TS 寫、原生發」可做成內部工具鏈或白牌打包服務。
- **構想**：「Native Pack Desk」— 上傳 TS CLI，一鍵出 macOS／Linux／Windows／WASI 產物＋簽名檢查；Pro：私有 runtime 策略、CI 模板；加 WP：外掛健康檢查 CLI 或 WP-CLI 擴充打包。
- **難度**：中高；切入：先包一種 CLI 範本＋兩平台 build＋失敗診斷報告。

### 2. YAML 定義 agent 小隊 → Claude＋Codex 同場 → Agent Fleet 編排器
- **來源**：[mvschwarz/openrig](https://github.com/mvschwarz/openrig)（★~908，今日 Trending）— 「harness 包模型，rig 包 harness」：用 YAML 定義 agent 團隊，一指令開機；Claude Code 與 Codex 同場，tmux／TUI 儀表板，佇列、座位、權限與共享 dashboard。
- **標籤**：非 WP
- **為什麼值得做**：團隊已同時養多把 coding agent，缺的是「可重播的小隊編制＋審核座位」；編排層比再賣一個 chatbot 更好收費。
- **構想**：「Rig Desk」— 預設 owner／checker／docs 三種座位模板；團隊方案：專案隔離、權限政策、Spend 上限；加 WP：交付站驗收 checklist 座位。
- **難度**：中高；切入：先支援 2 種 harness＋一種「實作→審核」佇列模板。

### 3. 本機決策路由 → macOS coding 工作區 → 桌面 Agent IDE
- **來源**：[codejunkie99/keel](https://github.com/codejunkie99/keel)（★~291，9/22 新建）— Rust／GPUI 本機優先 macOS 工作區：接 Claude Code／Codex／Cursor／Grok／Hermes／pi（ACP）；本機 Laya 或可選 Jev 為「新任務」選路，主機驗證後才套用，並留下可匯出的決策收據。
- **標籤**：非 WP
- **為什麼值得做**：代理商要「多 provider 一窗＋可稽核路由」，不是再一個聊天框；決策收據可賣合規／成本分析加值。
- **構想**：「Keel Agency」— 團隊標準路由政策、決策報表、客戶專案隔離；加 WP：建站任務預設路由到便宜模型、風險變更才升 Claude。
- **難度**：中高；切入：先做 macOS 安裝包＋2 provider＋決策 export／report。

### 4. 歌詞＋風格 → 可編輯樂譜＋本機演唱 → 本機音樂工作室
- **來源**：[timoncool/YuE2-Studio](https://github.com/timoncool/YuE2-Studio)（★~237，9/22 新建）— 本機 YuE2 歌曲工作室：先出可編輯 ABC 樂譜再演唱；Cover、精準重渲、Windows 安裝器；內建 MCP（`127.0.0.1:8791`）給 coding agent 驅動；6GB+ NVIDIA 可跑。
- **標籤**：非 WP
- **為什麼值得做**：品牌／ Podcast／短影音要「可改旋律再重唱」的本機音樂，不是黑盒一次生成；MCP 讓代理商可把出歌嵌進內容流水線。
- **構想**：「Score Studio」— 品牌音效包訂閱（風格鎖定＋樂譜庫）；Pro：批次 cover／多語歌詞；加 WP：媒體庫一鍵嵌歌曲＋樂譜預覽區塊。
- **難度**：中；切入：先做 MCP 驅動「風格＋歌詞→試聽」＋一種品牌 preset。

### 5. 產品簡報 → 便宜模型填分鏡 → 豎版宣傳片工廠
- **來源**：[Finderchangchang/brewreel](https://github.com/Finderchangchang/brewreel)（★~66，9/26 新建）— 「精釀 BrewReel」：強模型先調好配方與元件，便宜模型只填 `storyboard.json`；cards／quiz／journey 三種風格、六行業、廣告法極限詞校驗、一命令出 9:16 片；Apache-2.0、中英字幕。
- **標籤**：非 WP
- **為什麼值得做**：台灣中小與代理商要大量短影音，卻付不起每支都用頂級模型；「配方兜底＋合規校驗」是可賣的訂閱工廠。
- **構想**：「BrewReel Desk」— 上傳產品簡報出豎片；代理商白牌、行業模板包；加 WP／Woo：商品頁欄位一鍵產片並回寫媒體庫。
- **難度**：低～中；切入：先做 1 行業＋1 配方的 SaaS 包裝與中文簡報表單。

### 6. 大模型標籤 → 17M 分類器蒸餾 → 低成本意圖分類 SaaS
- **來源**：[MaximeRivest/tiny-classifiers](https://github.com/MaximeRivest/tiny-classifiers)（★~37，9/27 新建）— 用大模型標 2k 筆再 fine-tune 17M encoder；約一分鐘 GPU（筆電／手機也可）；銀行訊息 77 類可逼近 Opus，推論約 5ms、成本近零；含配方、教學、損益平衡計算。
- **標籤**：非 WP
- **為什麼值得做**：客服分流、表單意圖、工單標籤若長期打 API，量一上來就燒錢；「先評估、再蒸餾」是清楚的 B2B 切入。
- **構想**：「Distill Label」— 上傳歷史訊息→教師標註→出本機／邊緣分類器；Pro：週更蒸餾、A／B 與漂移監控；加 Woo／表單：退款／詢價／抱怨三分類預設包。
- **難度**：中；切入：先做單一意圖包＋評估集精靈＋OpenAI-compatible 推論端點。

---

## WP

### 7. Lemon Squeezy → Elementor 數位商品頁 → 無 Woo 目錄外掛
- **來源**：[BerkayKaraduman/lemon-catalog-sync-for-elementor](https://github.com/BerkayKaraduman/lemon-catalog-sync-for-elementor)（★~1，9/26 新建）— 把 Lemon Squeezy 商品同步成 WP `lcs_product`，用 Elementor／Theme Builder／Loop Grid 做目錄與單頁；結帳走 Lemon（hosted／overlay）；API key 建議放 `wp-config.php`。
- **標籤**：WP
- **為什麼值得做**：數位下載／課程／授權常不想扛 Woo 複雜度，卻仍要漂亮落地頁；「Lemon 管金流、WP 管內容」是代理商高頻需求。
- **構想**：「Lemon Desk for WP」— 同步精靈、比價／徽章欄位、方案比較表模板；Pro：多店、優惠碼區塊、會員下載門檻。
- **難度**：低～中；切入：先穩同步＋單頁模板＋一種 Elementor Loop。

### 8. YouTube Reel → Woo 可購買短影音 → 社群電商外掛
- **來源**：[developersazzad/Shopable-Reel-Wp-Plugin](https://github.com/developersazzad/Shopable-Reel-Wp-Plugin)（★~1，9/26 新建）— 每商品貼一支 YouTube：輪播、全螢幕沉浸、商品頁可拖曳浮動影片；原生 Elementor widget、零依賴、對標 Shopify ReelUp。
- **標籤**：WP
- **為什麼值得做**：社群已訓練用戶「滑影片再買」；Woo 站缺免訂閱、可自架的 shoppable reel，代理商可當電商改版加值。
- **構想**：「Shopable Reel Pro」— 批次匯入、CTA／加購、分析（完看率→加購）；加 UGC 審核佇列。
- **難度**：低～中；切入：先做短碼＋Elementor＋單商品浮動影片三件套。

---

## 今日脈絡（一句）
產品化焦點從「單一 coding agent」轉向「原生分發、多 agent 編排、本機決策工作區、本機音樂／便宜模型出片、小模型取代分類 API」；WP 側可跟進無 Woo 數位目錄與可購買短影音。

## 備註
- 掃過未採用已記入 seen（含日／週趨勢老專案、Opus 影片 awesome 清單、3D office 娛樂向、RAW 修圖、layout engine、LinkedIn 爬取合規風險、CVE／PoC／注入、盜版／破解噪音等）。
- 未把 exploit／PoC 當產品構想來源。
