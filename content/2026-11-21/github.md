# GitHub 熱門 × WP／SaaS idea 早報｜2026-11-21

今日從 GitHub Trending、近 3／14 天新建高星 repo 與 WordPress 主題搜尋中，篩出 7 則新專案（皆為近 30 天內建立）。

## 1. 本機隱私會議紀要 → 企業合規版會議助理
- GitHub：https://github.com/FrigadeHQ/yogurt （建立日期：2026-11-10）
- 來源重點：開源、資料留在本機的 AI 會議筆記，定位為 Granola 免費替代品，跨 Mac／Windows／Linux，約 2.8k stars。
- 為什麼值得做：律所、診所、顧問業想用 AI 記會議但不能上雲；本機方案已被驗證有需求。
- 產品構想：以此為底，做「團隊版」：集中管理模板、客戶別紀要歸檔、匯出到 Notion／HubSpot、稽核紀錄，月訂閱按席次收費。
- 難度與切入點：中。先鎖定繁中會議（口音／中英夾雜）的轉寫與摘要模板，切台灣中小事務所。

## 2. 自架 Slack 替代品，人與 AI agent 同頻道
- GitHub：https://github.com/agentes-chat/agentes-chat （建立日期：2026-11-09）
- 來源重點：開源自架團隊聊天，agent 可用 Claude／ChatGPT／Gemini 等在頻道與私訊中協作。
- 為什麼值得做：「AI 員工」進入團隊溝通是趨勢，但多數公司不想把內部對話交給 SaaS。
- 產品構想：託管版 agent 聊天室＋垂直 agent 市集（客服週報、記帳提醒、請款追蹤），向小型工作室收費。
- 難度與切入點：中高。先做託管部署與 SSO，再賣垂直 agent 範本包。

## 3. 一站式自架影音庫（影集／電影／音樂）→ 託管 homelab 服務
- GitHub：https://github.com/HolyArrs/HolyArrs （建立日期：2026-11-09）
- 來源重點：用 Go 寫的單一自架應用，整合原本 *arr 系列多個工具，約 2.4k stars。
- 為什麼值得做：自架媒體堆疊安裝繁瑣，使用者願意為「一鍵」付費。
- 產品構想：提供一鍵部署的託管版／NAS 套件，加上備份與監控儀表板，按月收費。
- 難度與切入點：低至中。先做 Synology／Docker 安裝包與教學內容導流，再收託管費。注意內容版權合規，行銷避免導向盜版。

## 4. 長影片自動剪短影音 → 台灣社群行銷 SaaS
- GitHub：https://github.com/iamajmeena/neonclipping （建立日期：2026-11-19）
- 來源重點：貼連結即產出帶字幕 9:16 短片，音訊優先、YouTube 字幕、本機 LLM，免費開源，1 天破 1k stars。
- 為什麼值得做：Podcast／課程創作者需要大量短影音，但中文字幕與 IG／Shorts 發佈流程仍弱。
- 產品構想：雲端版剪輯 SaaS：繁中字幕校正、品牌字卡模板、排程發佈到 IG／YouTube Shorts／Threads，按剪輯分鐘收費。
- 難度與切入點：中。先做「Podcast 單集 → 5 支短片」的單一流程。

## 5. 讓 AI agent 操作實體手機（Android／iPhone）的 MCP
- GitHub：https://github.com/hridaya423/phonedriver （建立日期：2026-11-08）
- 來源重點：Rust 寫的 MCP server＋CLI，agent 以文字方式讀螢幕並操控手機，敏感操作會先詢問。
- 為什麼值得做：App 的 QA 與重複性手機作業（LINE／電商後台）缺少 API，agent 直控是出路。
- 產品構想：雲端真機農場＋agent 測試服務：用自然語言寫 E2E 測試、回報截圖與錄影，給中小 App 團隊月租。
- 難度與切入點：高（硬體與裝置管理）。先做自帶裝置的 CLI 工作流與測試報告 SaaS，再談雲端真機。

## 6. 讓網頁版 AI 聊天連本機檔案／終端機的橋接（MCP）
- GitHub：https://github.com/ysunyang4/Nexus （建立日期：2026-11-13）
- 來源重點：把 ChatGPT／Gemini 等網頁 AI 透過 MCP 連到本機檔案、終端機、Git，使用者控管權限；配套瀏覽器擴充 webagent。
- 為什麼值得做：許多人用網頁版訂閱，不想另買 API；權限管理是企業採用的關鍵。
- 產品構想：「AI 權限閘道」：團隊策略管理、操作稽核紀錄、一鍵撤銷，賣給想導入 AI 但需合規的 IT。
- 難度與切入點：中。先做權限與稽核層，作為既有 MCP server 的外掛式產品。

## 7.（WP）用對話擴充的 WordPress 替代品 → 給 WP 代理商的「AI 建站」賣點
- GitHub：https://github.com/mrwebtv/ultimapress （建立日期：2026-11-12）
- 來源重點：自稱「靠詢問 Claude 擴充、不需外掛」的 WordPress 替代品，內建頁面編輯器、部落格、SEO、表單，約 69 stars。
- 為什麼值得做：反映「外掛疲勞」與「用 AI 取代外掛」的需求；WP 這邊的對應機會是 AI 生成輕量功能。
- 產品構想：WP 外掛「用說的加功能」：以自然語言產生並沙盒化小型 snippet（表單、WooCommerce 結帳欄位），含版本回滾與審核，賣年費授權給接案者。
- 難度與切入點：中。先限定 WooCommerce 結帳與表單兩類情境，並加入程式碼審核與安全掃描以降低風險。

---
備註：僅依 repo 描述與 stars 判斷，投入前請再讀 README 與授權條款。已略過含 exploit／PoC、遊戲外掛、疑似灌星的 repo。
