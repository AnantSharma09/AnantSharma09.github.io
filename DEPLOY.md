# Deploying to GitHub Pages (one-time setup)

This gets your site live at `https://YOUR-USERNAME.github.io`.

## 0. Prerequisites
- A GitHub account.
- Git installed on your machine (`git --version` to check; if missing,
  install from git-scm.com).

## 1. Create the repository on GitHub

Go to github.com → click **+** (top right) → **New repository**.

- Repository name: **exactly** `YOUR-USERNAME.github.io`
  (replace YOUR-USERNAME with your actual GitHub username — this exact
  naming is what makes GitHub serve it as a website automatically)
- Keep it **Public**
- Do NOT check "Add a README" — leave it empty
- Click **Create repository**

## 2. Point the site at your username

Open `build.py`, find this line near the top:
```python
GITHUB_USER = "your-github-username"
```
Replace `your-github-username` with your real GitHub username, then rebuild:
```
python3 build.py
```

## 3. Push your code (run these in the terminal, inside this `site/` folder)

```bash
git init
git add .
git commit -m "initial site"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-USERNAME.github.io.git
git push -u origin main
```

If this is the first time you've used git on this machine, it may ask
you to set an identity first — run these two lines once, then repeat
the commands above:
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

If `git push` asks for a username/password: GitHub no longer accepts
your account password here. Instead:
1. Go to GitHub → Settings → Developer settings → Personal access tokens
   → Tokens (classic) → Generate new token → check the `repo` box → Generate.
2. Copy the token. When git asks for a password, paste the token instead
   (your username is your normal GitHub username).

## 4. Turn on Pages

On GitHub, go to your repo → **Settings** → **Pages** (left sidebar).
- Source: **Deploy from a branch**
- Branch: **main**, folder **/ (root)**
- Save

Wait 1–2 minutes. Your site is now live at:
```
https://YOUR-USERNAME.github.io
```

## Day-to-day: publishing a new post

Every time you add a post/project and want it live:

```bash
python3 build.py
git add .
git commit -m "add post: my new post title"
git push
```

That's it — no separate "deploy" step. GitHub Pages automatically
republishes the `main` branch a minute or two after every push.

## Troubleshooting

- **Site shows a 404**: double check the repo name is exactly
  `YOUR-USERNAME.github.io` and that Pages source is set to `main` / `root`.
- **Changes don't show up**: GitHub Pages can take 1–2 minutes to update,
  and your browser may be caching the old page — hard refresh
  (Ctrl+Shift+R / Cmd+Shift+R).
- **CSS looks broken on the live site but fine locally**: make sure you
  didn't rename or move the `static/` folder — `build.py` expects it to
  stay where it is.
