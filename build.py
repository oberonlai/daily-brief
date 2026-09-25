#!/usr/bin/env python3
"""Render content/YYYY-MM-DD/<source>.md into a static site under docs/."""
import html, json, os, re, sys
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parent
CONTENT, DOCS = ROOT / "content", ROOT / "docs"
SITE_TITLE = "每日外部資訊"
# Known sources, in display order. Any other <source>.md is shown after these.
SOURCES = [
    ("x", "X 熱門貼文"),
    ("github", "GitHub 熱門 × 產品點子"),
    ("producthunt", "驗證營收產品"),
]
LABELS = dict(SOURCES)
ORDER = [s for s, _ in SOURCES]
WEEKDAY = "一二三四五六日"
URL_RE = re.compile(r'(?<![\(<"\'=\]])(https?://[^\s<>）」」、，。]+)')

CSS = """
:root{--bg:#fff;--fg:#1f2328;--muted:#656d76;--line:#d0d7de;--card:#f6f8fa;--link:#0969da}
@media (prefers-color-scheme:dark){:root{--bg:#0d1117;--fg:#e6edf3;--muted:#8d96a0;--line:#30363d;--card:#161b22;--link:#4493f8}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.75 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang TC","Noto Sans TC","Microsoft JhengHei",sans-serif}
main{max-width:820px;margin:0 auto;padding:24px 18px 80px}a{color:var(--link);word-break:break-all}
header.site{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:10px;margin-bottom:18px}
header.site a{color:var(--fg);text-decoration:none;font-weight:700}nav.days a{margin-left:12px;font-weight:400;color:var(--link)}
.toc{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px}.toc a{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:2px 12px;text-decoration:none;font-size:14px}
section.src{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:6px 20px 14px;margin:0 0 22px}
section.src>h2.src-title{font-size:13px;letter-spacing:.05em;color:var(--muted);margin:10px 0 0;font-weight:600}
h1{font-size:1.5em;line-height:1.35}h2{font-size:1.25em;margin-top:1.4em}h3{font-size:1.08em;margin-top:1.3em}
blockquote{margin:0;padding:0 14px;border-left:3px solid var(--line);color:var(--muted)}hr{border:0;border-top:1px solid var(--line);margin:1.4em 0}
ul.days{list-style:none;padding:0}ul.days li{border-bottom:1px solid var(--line);padding:10px 0}ul.days .meta{color:var(--muted);font-size:14px;margin-left:8px}
code{background:var(--card);padding:1px 5px;border-radius:4px;font-size:.9em}footer{color:var(--muted);font-size:13px;margin-top:40px}
"""

def autolink(text):
    out = []
    in_code = False
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            in_code = not in_code
        out.append(line if in_code else URL_RE.sub(lambda m: f"<{m.group(1)}>", line))
    return "\n".join(out)

def render_md(text):
    return markdown.markdown(autolink(text), extensions=["extra", "nl2br", "sane_lists"])

def page(title, body, rel=""):
    return f"""<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title>
<link rel="stylesheet" href="{rel}style.css"></head><body><main>{body}
<footer>由 Grok Bot 每日自動彙整外部資訊。時間皆為台北時間。</footer></main></body></html>"""

def day_label(d):
    import datetime as dt
    wd = WEEKDAY[dt.date.fromisoformat(d).weekday()]
    return f"{d}（{wd}）"

def sources_for(day_dir):
    files = [p for p in day_dir.glob("*.md") if p.stat().st_size > 0]
    return sorted(files, key=lambda p: (ORDER.index(p.stem) if p.stem in ORDER else 99, p.stem))

def main():
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("")
    (DOCS / "style.css").write_text(CSS)
    days = sorted([p for p in CONTENT.iterdir() if p.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.name)], reverse=True)
    days = [d for d in days if sources_for(d)]
    index_rows = []
    for i, d in enumerate(days):
        name = d.name
        files = sources_for(d)
        newer = days[i - 1].name if i > 0 else None
        older = days[i + 1].name if i + 1 < len(days) else None
        nav = "".join([
            f'<a href="{older}.html">← {older}</a>' if older else "",
            f'<a href="{newer}.html">{newer} →</a>' if newer else "",
            '<a href="index.html">全部日期</a>',
        ])
        toc, secs = [], []
        for f in files:
            label = LABELS.get(f.stem, f.stem)
            toc.append(f'<a href="#{f.stem}">{html.escape(label)}</a>')
            secs.append(f'<section class="src" id="{f.stem}"><h2 class="src-title">{html.escape(label)}</h2>{render_md(f.read_text())}</section>')
        body = (f'<header class="site"><a href="index.html">{SITE_TITLE}｜{day_label(name)}</a><nav class="days">{nav}</nav></header>'
                f'<div class="toc">{"".join(toc)}</div>{"".join(secs)}')
        (DOCS / f"{name}.html").write_text(page(f"{SITE_TITLE} {name}", body))
        labels = "、".join(LABELS.get(f.stem, f.stem) for f in files)
        index_rows.append(f'<li><a href="{name}.html">{day_label(name)}</a><span class="meta">{html.escape(labels)}</span></li>')
    latest = f'<p>最新一期：<a href="{days[0].name}.html">{day_label(days[0].name)}</a></p>' if days else "<p>還沒有內容。</p>"
    body = f'<header class="site"><a href="index.html">{SITE_TITLE}</a></header>{latest}<ul class="days">{"".join(index_rows)}</ul>'
    (DOCS / "index.html").write_text(page(SITE_TITLE, body))
    print(f"built {len(days)} day(s)")

if __name__ == "__main__":
    main()
