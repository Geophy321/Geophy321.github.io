# Yawar Hussain — personal website

## Folder structure

```
index.html              the page itself (About / Works / Publications, one file,
                         JS shows/hides the right section — no page reloads)
assets/css/main.css     all styling, incl. the light/dark theme toggle
assets/js/main.js       page behaviour: theme toggle, mobile menu, section routing
images/profile.jpg      your photo (About section)
```

## Editing content

Open `index.html` and search for the section you want:
- `id="page-home"` — About page (intro line, bio timeline, interests, links)
- `id="page-works"` — Works page (employment, projects, editorial, education, conferences)
- `id="page-fieldwork"` — Fieldwork page (field deployments, grid of entries)
- `id="page-blog"` — Blog page (empty state for now — add post cards here later)
- `id="page-pubs"` — Publications page (grouped, collapsible by topic)

## Swapping the photo

Overwrite `images/profile.jpg` with a similar-ish aspect ratio image (it's
cropped into a circle, so a centred headshot works best) — no HTML changes
needed.
## Deploying on GitHub Pages

Plain HTML/CSS/JS, no build step, no framework. Design based on Takuya
Matsuyama's [craftzdog-homepage](https://github.com/craftzdog/craftzdog-homepage)

1. Create a repo named `<your-username>.github.io`.
2. Push this whole folder's contents to the repo root (so `index.html` sits
   at the top level, not inside a subfolder).
3. Settings → Pages → should already serve from `main` / root for this repo
   name. Wait a minute, then visit `https://<your-username>.github.io`.
