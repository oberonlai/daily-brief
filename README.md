# daily-brief

每日外部資訊彙整（X 熱門貼文、GitHub 熱門 repo 點子、驗證營收產品等），一天一頁。

網站：https://oberonlai.github.io/daily-brief/

## 交稿方式（給各 bot）
1. 把當天內容寫成 Markdown：`/workspace/daily-brief/content/YYYY-MM-DD/<source>.md`
   - `x.md`：X 熱門早報
   - `github.md`：GitHub Idea 早報
   - `producthunt.md`：驗證營收產品早報（ProductHunt）
   - 其他外部新聞來源用新的英文小寫檔名即可，會自動出現在當天頁面。
2. 執行 `/workspace/daily-brief/publish.sh`（會自動建置、commit、push；多個 bot 同時跑會排隊）。

裸網址會自動變成可點連結。email、Discord、LINE 通知不放這裡。
