# anant's site

A static blog + portfolio. No build framework, no JavaScript, no
database — just markdown files turned into HTML by `build.py`.

## Adding content (this is the only workflow you need)

**New blog post**
```
cp content/posts/2026-01-14-autograd-from-scratch.md content/posts/my-new-post.md
```
Edit `my-new-post.md`: change the `title`, `date`, `summary`, `tags` at the
top, then write your post in markdown below the `---`.

**New project**
```
cp content/projects/cortex.md content/projects/my-project.md
```

**New paper note**
```
cp content/papers/attention-is-all-you-need.md content/papers/my-paper.md
```

Then rebuild:
```
python3 build.py
```

That regenerates every HTML page from the markdown files. You never edit
HTML directly.

## Preview locally before pushing
```
python3 -m http.server 8000
```
Then open http://localhost:8000 in a browser.

## Deploying

See `DEPLOY.md` for the full one-time setup and the day-to-day push
workflow.

## Editing your bio / links / nav

Open `build.py` and edit the block near the top marked
`EDIT THESE — your site's identity` (your name, tagline, bio, links,
GitHub username). Re-run `python3 build.py` after changing it.

## Changing the look

All visual styling lives in one file: `static/css/style.css`. Colors are
defined as CSS variables at the very top of that file if you ever want to
change the palette.
