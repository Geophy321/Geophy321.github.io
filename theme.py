"""Look & feel: icons, CSS, the page shell (nav + footer), and small render
helpers shared by every page. Content lives in data.py and content/posts/ —
you shouldn't need to touch this file to update the site."""
import html as _html


def esc(s):
    return _html.escape(str(s), quote=False)


# ---------------------------------------------------------------- icons ----
ICON_DROP = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="footprint"><path d="M12 2.2c-.3.4-6.6 8.06-6.6 12.4a6.6 6.6 0 0 0 13.2 0c0-4.34-6.3-12-6.6-12.4Zm3.55 13.5a4.6 4.6 0 0 1-3.8 2.28.85.85 0 0 1 0-1.7 2.9 2.9 0 0 0 2.42-1.46.85.85 0 0 1 1.38.88Z"/></svg>'
ICON_MOON = '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M21 12.79A9 9 0 1 1 11.21 3a7 7 0 0 0 9.79 9.79Z"/></svg>'
ICON_SUN = '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><circle cx="12" cy="12" r="4.2"/><g stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 2v2.2M12 19.8V22M4.2 4.2l1.55 1.55M18.25 18.25l1.55 1.55M2 12h2.2M19.8 12H22M4.2 19.8l1.55-1.55M18.25 5.75l1.55-1.55"/></g></svg>'
ICON_MENU = '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M3 6h18v2H3V6Zm0 5h18v2H3v-2Zm0 5h18v2H3v-2Z"/></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6 8.5 7 8.5-7"/></svg>'
ICON_CHEVRON = '<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M9 6l6 6-6 6"/></svg>'
ICON_DOC = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/></svg>'
ICON_PEN = '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25ZM20.71 7.04a1 1 0 0 0 0-1.41l-2.34-2.34a1 1 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83Z"/></svg>'
TILE_ICONS = {
    "flask": '<svg viewBox="0 0 24 24" width="26" height="26" fill="currentColor"><path d="M9 2v2h1v5.2L4.7 18a2 2 0 0 0 1.7 3h11.2a2 2 0 0 0 1.7-3L14 9.2V4h1V2H9Zm3 7.6 2 3.4H10l2-3.4ZM8.1 17l1.2-2h5.4l1.2 2H8.1Z"/></svg>',
    "trophy": '<svg viewBox="0 0 24 24" width="26" height="26" fill="currentColor"><path d="M6 3h12v2h3v3a4 4 0 0 1-4 4h-.35A6 6 0 0 1 13 15.9V18h3v2H8v-2h3v-2.1A6 6 0 0 1 7.35 12H7a4 4 0 0 1-4-4V5h3V3Zm0 4H5v1a2 2 0 0 0 2 2V7Zm12 0v3a2 2 0 0 0 2-2V7h-2Z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" width="26" height="26" fill="currentColor"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/></svg>',
    "briefcase": '<svg viewBox="0 0 24 24" width="26" height="26" fill="currentColor"><path d="M9 3h6a1 1 0 0 1 1 1v2h4a2 2 0 0 1 2 2v3H2V8a2 2 0 0 1 2-2h4V4a1 1 0 0 1 1-1Zm1 3h4V5h-4v1ZM2 12h20v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-6Z"/></svg>',
}

NAV_LINKS = [("", "About"), ("works/", "Works"), ("fieldwork/", "Fieldwork"),
             ("blog/", "Blog"), ("publications/", "Publications")]


# ------------------------------------------------------------------ nav ----
def nav_html(active, base):
    def link(href, label):
        cls = "nav-link active" if href == active else "nav-link"
        target = href + "index.html"  # href="" -> "index.html", "works/" -> "works/index.html"
        return f'<a class="{cls}" href="{base}{target}">{label}</a>'
    links = "\n".join(link(h, t) for h, t in NAV_LINKS)
    mobile = "\n".join(link(h, t) for h, t in NAV_LINKS)
    return f'''
<nav id="navbar">
  <div class="nav-inner">
    <a class="logo" href="{base}index.html">{ICON_DROP}<span>Yawar Hussain</span></a>
    <div class="nav-links">
      {links}
      <a class="nav-link nav-contact" href="mailto:yawar.pgn@gmail.com">{ICON_MAIL} Contact</a>
    </div>
    <div class="nav-right">
      <button id="theme-btn" class="icon-btn" aria-label="Toggle theme"></button>
      <button id="menu-btn" class="icon-btn menu-only" aria-label="Menu">{ICON_MENU}</button>
    </div>
  </div>
  <div id="mobile-menu" hidden>
    {mobile}
    <a class="menu-item" href="mailto:yawar.pgn@gmail.com">Contact</a>
  </div>
</nav>
'''


def layout(title, active, body, base="", description=None):
    """Wrap `body` HTML in the full page shell. `active` is the NAV_LINKS href
    of the current page (e.g. '' for home, 'works/' for Works). `base` is the
    RELATIVE path back to the site root — "" at the root, "../" one level
    down (works/, fieldwork/, publications/, blog/), "../../" two levels down
    (blog/<slug>/) — so the whole site opens by double-clicking index.html,
    no server required, and it hosts correctly at any GitHub Pages path."""
    description = description or "Yawar Hussain — geophysicist working on fibre-optic sensing and geohazard monitoring"
    page_title = "Yawar Hussain" if title == "Yawar Hussain" else f"{title} — Yawar Hussain"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>{esc(page_title)}</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="description" content="{esc(description)}" />
<link rel="stylesheet" href="{base}assets/css/main.css" />
</head>
<body>
{nav_html(active, base)}
<main class="container">
{body}
</main>
<footer>
  &copy; 2026 Yawar Hussain. All Rights Reserved.<br/>
  Design based on <a href="https://www.craftz.dog/" target="_blank" rel="noopener">Takuya Matsuyama&apos;s homepage</a> (MIT-licensed source, 3D model excluded per its CC BY-NC-ND terms).
</footer>
<script src="{base}assets/js/main.js"></script>
</body>
</html>
'''


# --------------------------------------------------------- render helpers --
def role_title(bold_part):
    return bold_part.rstrip(":,").strip()


def grid(cards_html):
    return f'<div class="grid2">\n{cards_html}\n</div>'


def static_card(icon, title, desc):
    title_html = f'<div class="grid-title">{esc(title)}</div>' if title else ""
    return f'''<div class="grid-card static">
  <div class="grid-thumb">{TILE_ICONS[icon]}</div>
  {title_html}
  <div class="grid-desc">{esc(desc)}</div>
</div>'''


def link_card(href, icon_svg, title, desc):
    return f'''<a class="grid-card" href="{href}">
  <div class="grid-thumb">{icon_svg}</div>
  <div class="grid-title">{esc(title)}</div>
  <div class="grid-desc">{esc(desc)}</div>
</a>'''


def plain_list(items):
    return f'<ul class="plain-list">{"".join(items)}</ul>'


def pubs_accordion(pubs):
    blocks = []
    for cat, items in pubs.items():
        lis = []
        for text, url in items:
            if url:
                lis.append(f'<li>{esc(text)} <a href="{esc(url)}" target="_blank" rel="noopener">↗</a></li>')
            else:
                lis.append(f'<li>{esc(text)}</li>')
        blocks.append(f'''<details class="pub-cat">
  <summary>{esc(cat)} <span class="count">{len(items)}</span></summary>
  <ul class="pub-list">{"".join(lis)}</ul>
</details>''')
    return "\n".join(blocks)


CSS = '''
@import url('https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@300;400;700&display=swap');

:root{
  --bg:#f0e7db; --fg:#1a202c; --fg-soft:#4a5568; --link:#3d7aed; --accent:#88ccca;
  --underline:#525252; --navbg:rgba(255,255,255,0.55); --card-bg:rgba(255,255,255,0.6);
  --card-border:rgba(0,0,0,0.08); --btn-fg:#1f7a72; --btn-bg:rgba(56,178,172,0.12); --btn-bg-hover:rgba(56,178,172,0.22);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#202023; --fg:#f7fafc; --fg-soft:#cbd5e0; --link:#ff63c3; --accent:#88ccca;
    --navbg:rgba(32,32,35,0.55); --card-bg:rgba(255,255,255,0.06); --card-border:rgba(255,255,255,0.12);
    --btn-fg:#7fe0d8; --btn-bg:rgba(127,224,216,0.12); --btn-bg-hover:rgba(127,224,216,0.22);
  }
}
:root[data-theme="dark"]{
  --bg:#202023; --fg:#f7fafc; --fg-soft:#cbd5e0; --link:#ff63c3; --accent:#88ccca;
  --navbg:rgba(32,32,35,0.55); --card-bg:rgba(255,255,255,0.06); --card-border:rgba(255,255,255,0.12);
  --btn-fg:#7fe0d8; --btn-bg:rgba(127,224,216,0.12); --btn-bg-hover:rgba(127,224,216,0.22);
}

*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;transition:background .25s ease,color .25s ease}
h1,h2,h3,h4{font-family:'M PLUS Rounded 1c',sans-serif;font-weight:700;margin:0}
a{color:var(--link);text-decoration:none;text-underline-offset:3px}
a:hover{text-decoration:underline}
.container{max-width:768px;margin:0 auto;padding:0 16px}

#navbar{position:fixed;top:0;left:0;right:0;z-index:20;background:var(--navbg);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.nav-inner{max-width:768px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:8px 16px;flex-wrap:wrap}
.logo{display:inline-flex;align-items:center;gap:10px;font-family:'M PLUS Rounded 1c',sans-serif;font-weight:700;font-size:18px;color:var(--fg);padding:6px 4px}
.logo:hover{text-decoration:none}
.logo .footprint{transition:transform .2s ease}
.logo:hover .footprint{transform:rotate(20deg)}
.nav-links{display:flex;align-items:center;gap:4px}
.nav-link{padding:8px;border-radius:6px;color:var(--fg)}
.nav-link:hover{text-decoration:none;background:var(--card-bg)}
.nav-link.active{background:var(--accent);color:#20202b}
.nav-contact{display:inline-flex;align-items:center;gap:5px}
.nav-right{display:flex;align-items:center;gap:6px}
.icon-btn{border:none;background:var(--card-bg);color:var(--fg);width:34px;height:34px;border-radius:8px;display:inline-flex;align-items:center;justify-content:center;cursor:pointer}
.icon-btn:hover{background:var(--btn-bg-hover)}
.menu-only{display:none}
#mobile-menu{display:none;flex-direction:column;padding:8px 16px 14px;gap:2px}
#mobile-menu a{padding:10px 8px;border-radius:6px;color:var(--fg)}
#mobile-menu a:hover{background:var(--card-bg);text-decoration:none}

@media (max-width:680px){
  .nav-links{display:none}
  .menu-only{display:inline-flex}
  #mobile-menu:not([hidden]){display:flex}
}

main.container{padding-top:70px;padding-bottom:48px}

.intro-box{border-radius:12px;margin-bottom:24px;padding:12px;text-align:center;background:var(--card-bg);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border:1px solid var(--card-border)}
.hero-row{display:flex;align-items:center;gap:24px;margin-bottom:24px;flex-wrap:wrap}
.hero-text{flex:1;min-width:200px}
.page-title{font-size:28px}
.subtitle{margin:6px 0 0;color:var(--fg-soft)}
.avatar{flex-shrink:0}
.avatar img{width:100px;height:100px;border-radius:999px;object-fit:cover;border:2px solid var(--card-border)}

.fade{margin-bottom:24px;animation:fadeIn .6s ease both;animation-delay:var(--d,0s)}
@keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}

.section-title{text-decoration:underline;font-size:20px;text-underline-offset:6px;text-decoration-color:var(--underline);text-decoration-thickness:4px;margin-top:12px;margin-bottom:16px}
.page-heading{font-size:22px;margin-bottom:16px}
.sub-heading{font-size:18px;margin:0 0 12px}
.para{text-align:justify;text-indent:1em;hyphens:auto;line-height:1.6}
.bio-row{padding-left:3.4em;text-indent:-3.4em;margin-bottom:6px}
.bio-year{font-weight:bold;margin-right:1em}

.center-cta{text-align:center;margin:16px 0}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 16px;border-radius:8px;background:var(--btn-bg);color:var(--btn-fg);font-weight:600}
.btn:hover{background:var(--btn-bg-hover);text-decoration:none}

.link-list{list-style:none;padding:0;margin:0 0 16px}
.link-list li{margin-bottom:6px}
.ghost-btn{display:inline-flex;align-items:center;gap:8px;padding:8px 12px;border-radius:8px;color:var(--btn-fg)}
.ghost-btn:hover{background:var(--btn-bg-hover);text-decoration:none}

.grid2{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:8px 0 20px}
@media (max-width:560px){.grid2{grid-template-columns:1fr}}
.grid-auto{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:16px;margin:8px 0 20px}
.empty-state{text-align:center;padding:32px 20px;border:1px dashed var(--card-border);border-radius:12px;color:var(--fg-soft)}
.grid-card{display:block;background:var(--card-bg);border:1px solid var(--card-border);border-radius:12px;padding:16px;text-align:center;color:var(--fg)}
a.grid-card:hover{text-decoration:none;background:var(--btn-bg-hover)}
.grid-card.static{text-align:left}
.grid-thumb{width:44px;height:44px;border-radius:10px;display:flex;align-items:center;justify-content:center;background:var(--btn-bg);color:var(--btn-fg);margin:0 auto 10px}
.grid-card.static .grid-thumb{margin:0 0 10px}
.grid-title{font-weight:700;margin-bottom:4px}
.grid-desc{font-size:14px;color:var(--fg-soft)}

.divider{border:none;border-top:1px solid var(--card-border);margin:24px 0}

.plain-list{padding-left:1.2em;margin:0 0 8px;line-height:1.7}
.plain-list li{margin-bottom:4px}

.pub-cat{border:1px solid var(--card-border);border-radius:10px;padding:10px 14px;margin-bottom:10px;background:var(--card-bg)}
.pub-cat summary{cursor:pointer;font-weight:700;list-style:none}
.pub-cat summary::-webkit-details-marker{display:none}
.pub-cat summary:before{content:'▸';display:inline-block;margin-right:8px;transition:transform .15s ease}
.pub-cat[open] summary:before{transform:rotate(90deg)}
.count{font-weight:400;color:var(--fg-soft);font-size:13px}
.pub-list{padding-left:1.4em;margin:10px 0 2px;line-height:1.6}
.pub-list li{margin-bottom:8px;font-size:15px}

.post-list-item{padding:16px 0;border-top:1px solid var(--card-border)}
.post-list-item:first-child{border-top:0}
.post-date{color:var(--fg-soft);font-size:13px}
.post-title{font-size:19px;margin:2px 0 4px}
.post-summary{color:var(--fg-soft)}

.post-body{line-height:1.7}
.post-body h1,.post-body h2,.post-body h3{margin:1.4em 0 .5em}
.post-body p{margin:0 0 1em}
.post-body img{max-width:100%;border-radius:8px}
.post-body pre{background:var(--card-bg);border:1px solid var(--card-border);border-radius:8px;padding:12px;overflow-x:auto}
.post-body code{background:var(--card-bg);border-radius:4px;padding:.1em .35em;font-size:.9em}
.post-body pre code{background:none;padding:0}
.post-body blockquote{border-left:3px solid var(--card-border);margin:0 0 1em;padding:.2em 1em;color:var(--fg-soft)}
.post-body ul,.post-body ol{padding-left:1.4em;margin:0 0 1em}

footer{max-width:768px;margin:32px auto 0;padding:0 16px;text-align:center;opacity:.55;font-size:13px;line-height:1.6}
'''

SCRIPT = '''
(function(){
  var root = document.documentElement;
  function setTheme(t){
    if (t) root.setAttribute('data-theme', t); else root.removeAttribute('data-theme');
    try { localStorage.setItem('theme', t || ''); } catch(e){}
    renderThemeBtn();
  }
  function currentIsDark(){
    var explicit = root.getAttribute('data-theme');
    if (explicit) return explicit === 'dark';
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  var ICON_MOON = '__ICON_MOON__';
  var ICON_SUN = '__ICON_SUN__';
  function renderThemeBtn(){
    var btn = document.getElementById('theme-btn');
    btn.innerHTML = currentIsDark() ? ICON_SUN : ICON_MOON;
  }
  try {
    var saved = localStorage.getItem('theme');
    if (saved) root.setAttribute('data-theme', saved);
  } catch(e){}
  renderThemeBtn();
  document.getElementById('theme-btn').addEventListener('click', function(){
    setTheme(currentIsDark() ? 'light' : 'dark');
  });

  var menuBtn = document.getElementById('menu-btn');
  var mobileMenu = document.getElementById('mobile-menu');
  menuBtn.addEventListener('click', function(){ mobileMenu.hidden = !mobileMenu.hidden; });
})();
'''
SCRIPT = SCRIPT.replace('__ICON_MOON__', ICON_MOON.replace("'", "\\'")).replace('__ICON_SUN__', ICON_SUN.replace("'", "\\'"))
