# Contributing Guide

Same conventions as `intern-git-fundamentals` and the SCAI platform.

## Where your files go

```
submissions/<your-github-username>/<exercise>/...
```

Example: `submissions/asha-k/2.3/form.html`. Never edit another intern's folder and never edit the `exercises/` starters.

## Branches

`feature/<name>-ex-2-1`, `feature/<name>-ex-2-2`, and so on. One exercise per branch.

## Commits

Conventional Commits, imperative mood:

```
feat: add call log table
feat: add status filter and search
fix: highlight invalid phone field
style: improve mobile layout of table
docs: add screenshots to PR
```

## Pull requests

- Title: `feat: <what> (2.x) for <name>`
- Use the PR template. Attach **desktop and mobile screenshots**.
- For 2.3 and 2.4, also attach a short screen recording or GIF showing validation errors / loading / error states.
- Respond to every review comment.
- A mentor merges. Do not merge your own PR.

## Code style

| Language | Rules |
|----------|-------|
| HTML | Semantic tags (`header`, `main`, `table`, `form`, `label`); every `img` has `alt`; every input has a `label`; lowercase attributes; 2-space indent |
| CSS | Classes not IDs for styling; no `!important`; use CSS variables for colors; mobile-first or clean `@media` blocks; 2-space indent |
| JS | `const`/`let` only, no `var`; `===`; small named functions; no inline `onclick=""`; no global mess; `addEventListener`; semicolons; 2-space indent; no `console.log` left behind |

## Not allowed

- jQuery, Bootstrap, Tailwind, React, any npm package, any CDN script
- Copy-pasted code from AI or Stack Overflow that you cannot explain in review
- Committing `node_modules`, `.env`, large images, or PDFs

## Automated checks

Every PR runs [.github/workflows/checks.yml](.github/workflows/checks.yml): PR title, JavaScript syntax (`node --check`), and HTML linting. Fix red checks before requesting review.
