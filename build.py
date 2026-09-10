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
import shutil
from pathlib import Path
import markdown

import theme
import data

ROOT = Path(__file__).parent
OUT = ROOT / "dist"
POSTS_DIR = ROOT / "content/posts"


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
            "body_html": body_html,
        })
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def recent_post_teaser(posts):
    if not posts:
        return ""
    p = posts[0]
    return f'''<div class="grid-card" style="text-align:left;margin-bottom:20px">
  <div class="post-date">{theme.esc(p["date"])}</div>
  <div class="post-title"><a href="blog/{p["slug"]}/index.html">{theme.esc(p["title"])}</a></div>
  <div class="post-summary">{theme.esc(p["summary"])}</div>
</div>'''


def home_page(posts):
    bio_rows = "\n".join(
        f'<div class="bio-row"><span class="bio-year">{theme.esc(y)}</span>{theme.esc(t)}</div>'
        for y, t in data.BIO_ROWS
    )
    cards = "".join([
        theme.link_card("fieldwork/index.html", theme.TILE_ICONS["pin"], "Fieldwork", "DAS/DTS installs, seismic surveys, geohazard site work"),
        theme.link_card("works/index.html", theme.ICON_PEN, "Editorial Roles", "Handling Editor, Seismica; Associate Editor, IJEEG"),
        theme.link_card("publications/index.html", theme.ICON_DOC, "Publications", "35+ peer-reviewed papers on Scopus"),
    ])
    return f'''
<div class="intro-box">Hi, I&apos;m a geophysicist working on fibre-optic sensing and geohazard monitoring, based in Stockholm!</div>

<div class="hero-row">
  <div class="hero-text">
    <h2 class="page-title">Yawar Hussain</h2>
    <p class="subtitle">Geophysicist ( Fibre-Optic Sensing / Seismology / Geohazards )</p>
  </div>
  <div class="avatar"><img src="images/profile.jpg" alt="Yawar Hussain" width="100" height="100" /></div>
</div>

<section class="fade" style="--d:0.1s">
  <h3 class="section-title">Work</h3>
  <p class="para">Yawar is a geophysicist based in Stockholm with a background spanning near-surface
  geophysics, seismic monitoring and geohazard characterisation, built over postdoctoral appointments in
  Brazil, Belgium, Italy and the United States. He currently works as a Specialist in Infrastructure Hazard
  Monitoring at HydroResearch Solutions AB, supporting fibre-optic monitoring (DTS, DSS, DAS) of dams and
  embankments from field deployment through to interpretation. Over 35 peer-reviewed publications, an
  H-index of 19 and 1284 citations (Scopus).</p>
  <div class="center-cta"><a class="btn" href="publications/index.html">My publications {theme.ICON_CHEVRON}</a></div>
</section>

<section class="fade" style="--d:0.2s">
  <h3 class="section-title">Bio</h3>
  {bio_rows}
</section>

<section class="fade" style="--d:0.3s">
  <h3 class="section-title">Interests</h3>
  <p class="para">{data.INTERESTS}</p>
</section>

<section class="fade" style="--d:0.3s">
  <h3 class="section-title">On the web</h3>
  <ul class="link-list">
    <li><a class="ghost-btn" href="mailto:yawar.pgn@gmail.com">{theme.ICON_MAIL} yawar.pgn@gmail.com</a></li>
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
    editorial_items = "".join(f'<li><b>{theme.esc(role)}</b> — {theme.esc(org)}</li>' for role, org in data.EDITORIAL)
    education_items = "".join(
        f'<li><span class="bio-year">{theme.esc(y)}</span>{theme.esc(deg)} — {theme.esc(place)}</li>'
        for y, deg, place in data.EDUCATION
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
        items = "".join(f'''<div class="post-list-item">
  <div class="post-date">{theme.esc(p["date"])}</div>
  <div class="post-title"><a href="{p["slug"]}/index.html">{theme.esc(p["title"])}</a></div>
  <div class="post-summary">{theme.esc(p["summary"])}</div>
</div>''' for p in posts)
        body = items
    return f'''
<h3 class="page-heading">Blog</h3>
{body}
'''


def post_page(p):
    return f'''
<article>
  <h3 class="page-heading">{theme.esc(p["title"])}</h3>
  <p class="post-date">{theme.esc(p["date"])}</p>
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

    (OUT / "assets/css/main.css").write_text(theme.CSS)
    (OUT / "assets/js/main.js").write_text(theme.SCRIPT)
    shutil.copytree(ROOT / "images", OUT / "images")  # profile photo + any blog-post images
    (OUT / ".nojekyll").write_text("")  # tell GitHub Pages this isn't a Jekyll site

    posts = load_posts()

    (OUT / "index.html").write_text(theme.layout("Yawar Hussain", "", home_page(posts), base=""))
    (OUT / "works/index.html").write_text(theme.layout("Works", "works/", works_page(), base="../"))
    (OUT / "fieldwork/index.html").write_text(theme.layout("Fieldwork", "fieldwork/", fieldwork_page(), base="../"))
    (OUT / "publications/index.html").write_text(theme.layout("Publications", "publications/", publications_page(), base="../"))
    (OUT / "blog/index.html").write_text(theme.layout("Blog", "blog/", blog_index_page(posts), base="../"))

    for p in posts:
        page_dir = OUT / "blog" / p["slug"]
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / "index.html").write_text(
            theme.layout(p["title"], "blog/", post_page(p), base="../../", description=p["summary"] or None)
        )

    print(f"built {len(posts)} post(s) -> {OUT}")


if __name__ == "__main__":
    build()
