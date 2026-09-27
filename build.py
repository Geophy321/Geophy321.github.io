#!/usr/bin/env python3
"""Build the static site into dist/.

    pip install -r requirements.txt
    python build.py
    python -m http.server -d dist 8000     # preview at http://localhost:8000

Add a blog post: copy content/posts/_template.md to
content/posts/YYYY-MM-DD-my-post.md, fill it in, run `python build.py` again
(or just push — the GitHub Actions workflow does this for you, see README).
No other file needs to change; the post appears on the Blog page automatically.
"""
import re
import shutil
from pathlib import Path
import markdown

import theme
import data

ROOT = Path(__file__).parent
OUT = ROOT / "dist"
POSTS_DIR = ROOT / "content/posts"
NEWS_DIR = ROOT / "content/news"


def reading_time(body_html):
    text = re.sub(r"<[^>]+>", " ", body_html)
    words = len(text.split())
    minutes = max(1, round(words / 200))
    return f"{minutes} min read"


def load_posts():
    posts = []
    for f in sorted(POSTS_DIR.glob("*.md")):
        if f.name.startswith("_"):
            continue  # _template.md and similar are skipped
        md = markdown.Markdown(extensions=["meta", "extra"])
        body_html = md.convert(f.read_text(encoding="utf-8"))
        meta = md.Meta or {}
        posts.append({
            "slug": f.stem,
            "title": meta.get("title", [f.stem])[0],
            "date": meta.get("date", [""])[0],
            "summary": meta.get("summary", [""])[0],
            "cover": meta.get("cover", [""])[0],
            "body_html": body_html,
        })
        posts[-1]["reading_time"] = reading_time(body_html)
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def load_news():
    news = []
    if NEWS_DIR.exists():
        for f in sorted(NEWS_DIR.glob("*.md")):
            if f.name.startswith("_"):
                continue  # _template.md and similar are skipped
            md = markdown.Markdown(extensions=["meta", "extra"])
            body_html = md.convert(f.read_text(encoding="utf-8"))
            meta = md.Meta or {}
            news.append({
                "slug": f.stem,
                "title": meta.get("title", [f.stem])[0],
                "date": meta.get("date", [""])[0],
                "summary": meta.get("summary", [""])[0],
                "cover": meta.get("cover", [""])[0],
                "body_html": body_html,
            })
            news[-1]["reading_time"] = reading_time(body_html)
    news.sort(key=lambda n: n["date"], reverse=True)
    return news


def post_card(item, cover_prefix, href, index=0, animate=False):
    if item["cover"]:
        thumb = f'<div class="post-card-cover" style="background-image:url(\'{cover_prefix}{item["cover"]}\')"></div>'
    else:
        thumb = f'<div class="post-card-cover post-card-cover-empty">{theme.ICON_PEN}</div>'
    cls = "post-card"
    style = ""
    if animate:
        # Cycle through 4 entry directions so consecutive articles feel varied:
        # left, right, top, bottom.
        directions = [(-40, 0), (40, 0), (0, -30), (0, 30)]
        fx, fy = directions[index % 4]
        delay = min(index * 0.25, 1.5)
        cls += " news-fly"
        style = f' style="--d:{delay:.2f}s;--fx:{fx}px;--fy:{fy}px"'
    return f'''<a class="{cls}"{style} href="{href}">
  {thumb}
  <div class="post-card-body">
    <div class="post-date">{theme.esc(item["date"])} &middot; {theme.esc(item["reading_time"])}</div>
    <div class="post-title">{theme.esc(item["title"])}</div>
    <div class="post-summary">{theme.esc(item["summary"])}</div>
  </div>
</a>'''


def rotator_html(items, href_prefix, tag, limit=3):
    if not items:
        return ""
    slides = "".join(
        f'''<a class="news-slide{" active" if i == 0 else ""}" href="{href_prefix}{n["slug"]}/index.html">
  <span class="news-banner-tag">{tag}</span>
  <span class="news-banner-title">{theme.esc(n["title"])}</span>
  <span class="news-banner-date">{theme.esc(n["date"])}</span>
</a>'''
        for i, n in enumerate(items[:limit])
    )
    return f'<div class="news-highlights-rotator">{slides}</div>'


def recent_news_banner(news, limit=3):
    return rotator_html(news, "news/", "News", limit)


def recent_blog_banner(posts, limit=3):
    return rotator_html(posts, "blog/", "Blog", limit)


def news_index_page(news):
    if not news:
        body = f'''<div class="empty-state">
  <div class="grid-thumb" style="margin:0 auto 12px">{theme.ICON_PEN}</div>
  <p>No news yet — updates on new publications, project milestones and other announcements
  will show up here.</p>
</div>'''
    else:
        cards = "".join(post_card(n, "../", f'{n["slug"]}/index.html', i, animate=True) for i, n in enumerate(news))
        body = f'<div class="grid-auto post-grid">{cards}</div>'
    return f'''
<h3 class="page-heading">News</h3>
{body}
'''


def news_item_page(n):
    cover_html = f'<img class="post-cover" src="../../{n["cover"]}" alt="" />' if n["cover"] else ""
    return f'''
<article>
  {cover_html}
  <h3 class="page-heading">{theme.esc(n["title"])}</h3>
  <p class="post-date">{theme.esc(n["date"])} &middot; {theme.esc(n["reading_time"])}</p>
  <div class="post-body">{n["body_html"]}</div>
  <p><a href="../index.html">&larr; Back to News</a></p>
</article>
'''


def recent_post_teaser(posts):
    if not posts:
        return ""
    p = posts[0]
    return post_card(p, "", f'blog/{p["slug"]}/index.html')


def home_page(posts, news):
    cards = "".join([
        theme.link_card("fieldwork/index.html", theme.TILE_ICONS["pin"], "Fieldwork", "DAS/DTS installs, seismic surveys, geohazard site work"),
        theme.link_card("works/index.html", theme.ICON_PEN, "Editorial Roles", "Handling Editor, Seismica; Associate Editor, IJEEG"),
        theme.link_card("publications/index.html", theme.ICON_DOC, "Publications", "35+ peer-reviewed papers on Scopus"),
    ])
    return f'''
<div class="hero-row">
  <div class="news-highlights">
{recent_news_banner(news)}
{recent_blog_banner(posts)}
  </div>
  <div class="hero-photo"><img src="images/IMG_1002.jpeg" alt="Yawar Hussain" width="130" height="130" /></div>
</div>

<section>
  <h3 class="section-title">Work</h3>
  <p class="para">Yawar is a geophysicist based in Stockholm with a background spanning near-surface
  geophysics, seismic monitoring and geohazard characterisation, built over postdoctoral appointments in
  Brazil, Belgium, Italy and the United States. He currently works as a Specialist in Infrastructure Hazard
  Monitoring at HydroResearch Solutions AB, supporting fibre-optic monitoring (DTS, DSS, DAS) of dams and
  embankments from field deployment through to interpretation. Over 35 peer-reviewed publications, an
  H-index of 19 and 1284 citations (Scopus).</p>
  <div class="center-cta"><a class="btn" href="files/cv.pdf" target="_blank" rel="noopener">CV {theme.ICON_CHEVRON}</a></div>
</section>

<section>
  <h3 class="section-title">Interests</h3>
  <p class="para">{data.INTERESTS}</p>
</section>

<section>
  <h3 class="section-title">On the web</h3>
  <ul class="link-list">
    <li><a class="ghost-btn" href="mailto:yawar.pgn@gmail.com">{theme.ICON_MAIL} Contact</a></li>
  </ul>

  <div class="grid-auto">{cards}</div>

  {recent_post_teaser(posts)}

  <h3 class="section-title">Get in touch</h3>
  <p>Happy to talk fibre-optic monitoring, near-surface geophysics, or postdoc/industry opportunities.</p>
  <div class="center-cta"><a class="btn" href="mailto:yawar.pgn@gmail.com">{theme.ICON_MAIL} Email me</a></div>
</section>
'''


def works_page():
    employment_cards = "".join(
        theme.static_card("briefcase", theme.role_title(bold), desc)
        for bold, desc in data.EMPLOYMENT
    )
    project_cards = "".join(
        theme.static_card(icon, title, desc) for icon, title, desc in data.PROJECTS
    )
    def editorial_line(role, org, url):
        org_html = theme.esc(org)
        if url:
            org_html = f'<a href="{theme.esc(url)}" target="_blank" rel="noopener">{org_html}</a>'
        return f'<li><b>{theme.esc(role)}</b> — {org_html}</li>'
    editorial_items = "".join(editorial_line(role, org, url) for role, org, url in data.EDITORIAL)
    education_items = "".join(
        f'<li>{theme.esc(deg)} — {theme.esc(place)}</li>'
        for deg, place in data.EDUCATION
    )
    conferences_items = "".join(f'<li>{theme.esc(c)}</li>' for c in data.CONFERENCES)
    return f'''
<h3 class="page-heading">Works</h3>

<h4 class="sub-heading">Employment</h4>
{theme.grid(employment_cards)}

<hr class="divider" />
<h4 class="sub-heading">Projects &amp; Grants</h4>
{theme.grid(project_cards)}

<hr class="divider" />
<h4 class="sub-heading">Editorial Contributions</h4>
{theme.plain_list(editorial_items)}

<hr class="divider" />
<h4 class="sub-heading">Education</h4>
{theme.plain_list(education_items)}

<hr class="divider" />
<h4 class="sub-heading">Selected Conferences</h4>
{theme.plain_list(conferences_items)}
'''


def fieldwork_page():
    cards = "".join(theme.static_card("pin", "", item) for item in data.FIELDWORK)
    return f'''
<h3 class="page-heading">Fieldwork</h3>
<p class="para">Field deployments spanning dam and mine monitoring, seismic surveys and geohazard site
investigations across Sweden, Italy, Belgium, Spain, Brazil and the United States.</p>
{theme.grid(cards)}
'''


def publications_page():
    return f'''
<h3 class="page-heading">Publications</h3>
<p class="para">35+ peer-reviewed papers (Scopus H-index 19, 1284 citations), grouped by topic.</p>
{theme.pubs_accordion(data.PUBLICATIONS)}
'''


def blog_index_page(posts):
    if not posts:
        body = f'''<div class="empty-state">
  <div class="grid-thumb" style="margin:0 auto 12px">{theme.ICON_PEN}</div>
  <p>No posts yet — this space is reserved for write-ups on fibre-optic sensing, near-surface geophysics
  and fieldwork notes. Check back soon, or get in touch if you&apos;d like to be notified.</p>
  <div class="center-cta"><a class="btn" href="mailto:yawar.pgn@gmail.com">{theme.ICON_MAIL} Notify me</a></div>
</div>'''
    else:
        cards = "".join(post_card(p, "../", f'{p["slug"]}/index.html', i) for i, p in enumerate(posts))
        body = f'<div class="grid-auto post-grid">{cards}</div>'
    return f'''
<h3 class="page-heading">Blog</h3>
{body}
'''


def post_page(p):
    cover_html = f'<img class="post-cover" src="../../{p["cover"]}" alt="" />' if p["cover"] else ""
    return f'''
<article>
  {cover_html}
  <h3 class="page-heading">{theme.esc(p["title"])}</h3>
  <p class="post-date">{theme.esc(p["date"])} &middot; {theme.esc(p["reading_time"])}</p>
  <div class="post-body">{p["body_html"]}</div>
  <p><a href="../index.html">&larr; Back to Blog</a></p>
</article>
'''


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets/css").mkdir(parents=True)
    (OUT / "assets/js").mkdir(parents=True)
    (OUT / "works").mkdir(parents=True)
    (OUT / "fieldwork").mkdir(parents=True)
    (OUT / "publications").mkdir(parents=True)
    (OUT / "blog").mkdir(parents=True)
    (OUT / "news").mkdir(parents=True)

    (OUT / "assets/css/main.css").write_text(theme.CSS)
    (OUT / "assets/js/main.js").write_text(theme.SCRIPT)
    shutil.copytree(ROOT / "images", OUT / "images")  # profile photo + any blog-post images
    if (ROOT / "files").exists():
        shutil.copytree(ROOT / "files", OUT / "files")  # CV and other downloadable documents
    (OUT / ".nojekyll").write_text("")  # tell GitHub Pages this isn't a Jekyll site

    posts = load_posts()
    news = load_news()

    (OUT / "index.html").write_text(theme.layout("Yawar Hussain", "", home_page(posts, news), base=""))
    (OUT / "works/index.html").write_text(theme.layout("Works", "works/", works_page(), base="../"))
    (OUT / "fieldwork/index.html").write_text(theme.layout("Fieldwork", "fieldwork/", fieldwork_page(), base="../"))
    (OUT / "publications/index.html").write_text(theme.layout("Publications", "publications/", publications_page(), base="../"))
    (OUT / "blog/index.html").write_text(theme.layout("Blog", "blog/", blog_index_page(posts), base="../"))
    (OUT / "news/index.html").write_text(theme.layout("News", "news/", news_index_page(news), base="../"))

    for n in news:
        page_dir = OUT / "news" / n["slug"]
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / "index.html").write_text(
            theme.layout(n["title"], "news/", news_item_page(n), base="../../", description=n["summary"] or None)
        )

    for p in posts:
        page_dir = OUT / "blog" / p["slug"]
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / "index.html").write_text(
            theme.layout(p["title"], "blog/", post_page(p), base="../../", description=p["summary"] or None)
        )

    print(f"built {len(posts)} post(s) -> {OUT}")


if __name__ == "__main__":
    build()
