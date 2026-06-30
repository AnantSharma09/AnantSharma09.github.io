#!/usr/bin/env python3
"""
build.py — turns markdown files in content/ into a static website.

HOW TO USE (you never need to touch HTML/CSS):
  1. Add a new post:     content/posts/my-post-slug.md
  2. Add a new project:  content/projects/my-project-slug.md
  3. Add a new paper note: content/papers/my-paper-slug.md
  4. Run:  python3 build.py
  5. Commit + push (see DEPLOY.md)

Each markdown file needs a frontmatter block at the top, e.g.:

  ---
  title: Building an Autograd Engine From Scratch
  date: 2026-01-14
  summary: A one-line description shown in the list view.
  tags: [autograd, backprop, from-scratch]
  ---

  Your markdown content starts here...

For projects, you can add optional fields:
  ---
  title: CORTEX
  date: 2026-02-01
  summary: Persistent multi-object tracking for drone footage.
  tags: [computer-vision, tracking, edge-ai]
  github: https://github.com/youruser/cortex
  demo: https://your-demo-link.com
  status: in-progress     # or "complete"
  ---
"""

import os
import shutil
import datetime
import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")
OUT = ROOT  # we build straight into the repo root for GitHub Pages
TEMPLATES = os.path.join(ROOT, "templates")

# ---------------------------------------------------------------
# EDIT THESE — your site's identity
# ---------------------------------------------------------------
SITE_NAME = "Anant Sharma"
AUTHOR_NAME = "Anant Sharma"
GITHUB_USER = "AnantSharma09"   # <-- change this
TAGLINE = "Building intelligent systems from first principles."
BIO = (
    "I'm Anant Sharma, a recent Computer Science graduate preparing for "
    "research and machine learning engineering roles. I believe the best "
    "way to understand AI is to build it from first principles, so I spend "
    "my time implementing machine learning, deep learning, computer vision, "
    "and reinforcement learning systems from scratch. This website is my "
    "public engineering notebook where I document projects, implementation "
    "details, research paper notes, and the ideas that shape my understanding."
)
LINKS = [
    ("github", f"https://github.com/{GITHUB_USER}"),
    ("email", "mailto:sharmaanant4951@gmail.com"),
]
# ---------------------------------------------------------------

env = Environment(loader=FileSystemLoader(TEMPLATES))
md = markdown.Markdown(extensions=["fenced_code", "codehilite", "tables", "toc"])

PUBLIC_DIRS_TO_KEEP = {"static", "content", "templates", "build.py", "DEPLOY.md",
                        ".git", ".github", ".nojekyll", "README.md", "CNAME"}


def clean_output():
    """Remove previously generated HTML pages (but keep source dirs)."""
    for name in os.listdir(OUT):
        if name in PUBLIC_DIRS_TO_KEEP or name.startswith("."):
            continue
        path = os.path.join(OUT, name)
        if name.endswith(".html"):
            os.remove(path)
        elif name in ("posts", "projects", "papers") and os.path.isdir(path):
            shutil.rmtree(path)


def load_collection(folder):
    items = []
    folder_path = os.path.join(CONTENT, folder)
    if not os.path.isdir(folder_path):
        return items
    for fname in sorted(os.listdir(folder_path)):
        if not fname.endswith(".md"):
            continue
        slug = fname[:-3]
        post = frontmatter.load(os.path.join(folder_path, fname))
        html = md.reset().convert(post.content)
        date = post.get("date", datetime.date.today())
        if isinstance(date, str):
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        items.append({
            "slug": slug,
            "title": post.get("title", slug),
            "summary": post.get("summary", ""),
            "tags": post.get("tags", []),
            "date": date,
            "date_str": date.strftime("%b %Y"),
            "html": html,
            "github": post.get("github"),
            "demo": post.get("demo"),
            "status": post.get("status"),
        })
    items.sort(key=lambda x: x["date"], reverse=True)
    return items


def render(template_name, out_path, root="", active="", **ctx):
    tpl = env.get_template(template_name)
    page = env.get_template("base.html")
    inner = tpl.render(root=root, **ctx)
    html = page.render(
        content=inner,
        root=root,
        active=active,
        site_name=SITE_NAME,
        author_name=AUTHOR_NAME,
        github_user=GITHUB_USER,
        year=datetime.date.today().year,
        page_title=ctx.get("page_title", SITE_NAME),
        page_desc=ctx.get("page_desc", TAGLINE),
    )
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write(html)


def main():
    clean_output()

    posts = load_collection("posts")
    projects = load_collection("projects")
    papers = load_collection("papers")

    # --- individual pages ---
    for p in posts:
        render("post.html", os.path.join(OUT, "posts", f"{p['slug']}.html"),
               root="../", active="posts", entry=p, kind="writing",
               page_title=f"{p['title']} — {SITE_NAME}", page_desc=p["summary"])

    for p in projects:
        render("post.html", os.path.join(OUT, "projects", f"{p['slug']}.html"),
               root="../", active="projects", entry=p, kind="project",
               page_title=f"{p['title']} — {SITE_NAME}", page_desc=p["summary"])

    for p in papers:
        render("post.html", os.path.join(OUT, "papers", f"{p['slug']}.html"),
               root="../", active="papers", entry=p, kind="paper",
               page_title=f"{p['title']} — {SITE_NAME}", page_desc=p["summary"])

    # --- index / list pages ---
    render("index.html", os.path.join(OUT, "index.html"),
           root="", active="home", posts=posts[:5], projects=projects[:5],
           tagline=TAGLINE, bio=BIO, links=LINKS, author_name=AUTHOR_NAME,
           page_title=f"{AUTHOR_NAME} — {TAGLINE}", page_desc=BIO)

    render("list.html", os.path.join(OUT, "posts.html"),
           root="", active="posts", items=posts, kind_root="posts",
           heading="writing", page_title=f"writing — {SITE_NAME}")

    render("list.html", os.path.join(OUT, "projects.html"),
           root="", active="projects", items=projects, kind_root="projects",
           heading="projects", page_title=f"projects — {SITE_NAME}")

    render("list.html", os.path.join(OUT, "papers.html"),
           root="", active="papers", items=papers, kind_root="papers",
           heading="papers", page_title=f"papers — {SITE_NAME}")

    render("about.html", os.path.join(OUT, "about.html"),
           root="", active="about", bio=BIO, links=LINKS,
           author_name=AUTHOR_NAME, tagline=TAGLINE,
           page_title=f"about — {SITE_NAME}")

    # .nojekyll tells GitHub Pages not to run Jekyll on the build
    open(os.path.join(OUT, ".nojekyll"), "w").close()

    print(f"Built {len(posts)} posts, {len(projects)} projects, {len(papers)} papers.")
    print("Open index.html in a browser to preview, or run: python3 -m http.server")


if __name__ == "__main__":
    main()
