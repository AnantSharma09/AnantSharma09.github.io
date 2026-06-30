---
title: Building an Autograd Engine From Scratch
date: 2026-01-14
summary: What actually happens inside backprop, traced through a hand-rolled Value class.
tags: [autograd, backprop, from-scratch]
---

Replace this with your real post. A few notes on how this works:

- Write normal markdown. Headings, code blocks, lists, links, all of it works.
- The frontmatter block at the top (between the `---` lines) controls the
  title, date, summary, and tags shown in the list view.
- Run `python3 build.py` after editing, then push to GitHub.

## Why bother building it from scratch

This is where you explain the surprise, the thing the tutorial didn't
tell you, the bug that taught you more than the working code did.

```python
class Value:
    def __init__(self, data, _children=(), _op=""):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
```

Delete this file once you've written your first real post, or keep it
as a template — `cp content/posts/2026-01-14-autograd-from-scratch.md content/posts/my-new-post.md`.
