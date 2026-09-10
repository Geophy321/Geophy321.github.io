# Yawar Hussain — personal site

A small Python static-site generator, no framework. Same design as before
(craftzdog-homepage-inspired), now split into real pages so adding a blog
post is a one-file change.

## Adding a blog post

1. Copy `content/posts/_template.md` to `content/posts/YYYY-MM-DD-your-slug.md`.
2. Fill in `Title`, `Date`, `Summary`, and write the post body in Markdown below the blank line.
3. `python build.py` (or just `git push` — see Deploying below).

That's it — no other file changes, no registering the post anywhere. The
filename becomes the URL (`/blog/your-slug/`), and it's sorted onto the Blog
page automatically by date.

**Adding pictures to a post:** drop the image into `images/` (e.g.
`images/my-post-photo.jpg` — anything in there gets published as-is) and
reference it in the post's Markdown as:

```markdown
![Caption for the image](../../images/my-post-photo.jpg)
```

The `../../` is because a post page lives two folders deep
(`blog/<slug>/index.html`); it's the same for every post, regardless of
slug. Standard Markdown image syntax, so normal image sizes/formats (jpg,
png, gif, svg) all work.

## Editing everything else

- `data.py` — your CV content: employment, fieldwork, projects, editorial
  roles, education, conferences, publications. Plain Python lists/dicts.
- `theme.py` — colours, fonts, CSS, icons, the page shell (nav/footer). You
  shouldn't need to touch this for content changes.
- `build.py` — the page layouts themselves (what goes on Home/Works/Fieldwork/Publications).
- `images/profile.jpg` — your photo.

## Running it locally

```
pip install -r requirements.txt
python build.py
```

That's it — `dist/index.html` opens directly in a browser (double-click it,
or `open dist/index.html`), no server needed. Every link and asset in the
site is a relative path, so it works the same over `file://` as it does once
deployed. (A local server also works if you prefer one: `python -m
http.server -d dist 8000`.)

`build.py` writes everything into `dist/` (git-ignored — it's generated, not
source).

## Deploying on GitHub Pages

This repo includes `.github/workflows/deploy.yml`, which builds the site and
publishes it automatically on every push to `main`. One-time setup:

1. Push this repo to GitHub — either as `<your-username>.github.io` (a user
   site at the domain root) or as any other repo name (a project site at
   `<username>.github.io/reponame/`). Both work with no configuration: every
   link and asset path in the site is relative, not root-absolute, so it
   doesn't care which path it's served from.
2. Repo Settings → Pages → **Source: GitHub Actions**.
3. Push to `main`. The Action builds with `python build.py` and deploys
   `dist/` — no need to commit generated HTML, and no Ruby/Jekyll involved
   (there's a `.nojekyll` file in the output so GitHub Pages serves it as-is).

After that, writing a post is: add the Markdown file, commit, push — the
site rebuilds and redeploys on its own in ~30 seconds.

## On "Jekyll" vs Python options

GitHub Pages' *native*, zero-build option is Jekyll — but Jekyll is Ruby, not
Python, so it's not what you asked for. If you want a fuller Python blogging
engine instead of this hand-rolled one, **Pelican** is the closest
equivalent (Markdown/reST posts, Jinja2 themes, RSS/Atom feeds, tags and
categories built in, and a documented GitHub Pages deploy path via
`ghp-import` or the same Actions approach used here). It's more powerful but
also more machinery — a theme to install or write, a settings file, a
plugin system — for what's currently a five-page personal site.

This repo goes with the smaller option on purpose: ~250 lines of Python
total, one dependency (`Markdown`), and the exact design you already have.
If the blog grows into the main thing on the site and you want tags, feeds,
or pagination, migrating this content into Pelican later is a straightforward
step up — the Markdown posts themselves need no changes.
