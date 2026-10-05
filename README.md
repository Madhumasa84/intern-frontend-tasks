# intern-frontend-tasks

Welcome to **Repository 2** of the SCAI internship. Here you will build small, real UI pieces like the ones used in the SCAI staff portal: a call-log table, a live filter, a validated record form, and an API-driven card grid.

> **Time needed:** 2 days  |  **Level:** beginner to intermediate  |  **Tools:** a browser, VS Code, Git, Python 3 (for a local server and the verify script)
> **Prerequisite:** you finished `intern-git-fundamentals` (fork, branch, PR).

## Rules of the repo

- **Vanilla only.** HTML, CSS and JavaScript. No frameworks, no libraries, no build step, no CSS frameworks.
- **Light, clean design.** White or light backgrounds, readable fonts, good spacing.
- **Everything goes through a PR** (see [CONTRIBUTING.md](CONTRIBUTING.md)).

## The exercises

| # | Exercise | You build | Skills | Guide |
|---|----------|-----------|--------|-------|
| 0 | Setup | Local dev environment | VS Code, Live Server, DevTools | [docs/00-setup.md](docs/00-setup.md) |
| 2.1 | Static call log table | `index.html` | Semantic HTML, CSS, responsive tables | [docs/01-static-call-log.md](docs/01-static-call-log.md) |
| 2.2 | Dynamic filter UI | `index.html` + `app.js` | DOM, events, filtering | [docs/02-dynamic-filter.md](docs/02-dynamic-filter.md) |
| 2.3 | Form with validation | `form.html` + `validation.js` | Forms, regex, dates, a11y, toasts | [docs/03-form-validation.md](docs/03-form-validation.md) |
| 2.4 | Fetch and display API data | `index.html` + `app.js` | `fetch`, async/await, loading and error states | [docs/04-fetch-api-data.md](docs/04-fetch-api-data.md) |

Extras: [Cheat sheet](docs/CHEATSHEET.md) | [Quality checklist](docs/QUALITY_CHECKLIST.md) | [Grading](docs/GRADING.md)

## Folder layout

```
intern-frontend-tasks/
├── README.md
├── CONTRIBUTING.md
├── docs/                       <- guides, cheat sheet, rubric
├── exercises/
│   ├── 2.1-static-call-log/starter/index.html
│   ├── 2.2-dynamic-filter/starter/{index.html, app.js}
│   ├── 2.3-form-validation/starter/{form.html, validation.js}
│   └── 2.4-fetch-api-data/starter/{index.html, app.js}
├── shared/design-tokens.css    <- optional colors and spacing to copy from
├── submissions/                <- YOUR work goes here
│   └── <your-github-username>/2.1/ ...
└── scripts/
    ├── verify.py               <- self-check tool
    └── serve.py                <- tiny local web server
```

## How to submit an exercise

```bash
# 1. fork (untick "Copy the main branch only"), clone, add upstream  (see git-fundamentals)
git switch -c feature/<name>-ex-2-1

# 2. copy the starter into your own folder
mkdir -p submissions/<username>/2.1
cp exercises/2.1-static-call-log/starter/* submissions/<username>/2.1/

# 3. build it, open it in the browser, then self-check
python scripts/verify.py 2.1 --username <username>

# 4. commit, push, open a PR titled "feat: add call log table (2.1) for <name>"
```

Windows PowerShell equivalent of step 2:

```powershell
New-Item -ItemType Directory submissions\<username>\2.1 -Force
Copy-Item exercises\2.1-static-call-log\starter\* submissions\<username>\2.1\
```

**One exercise = one branch = one PR.** Put screenshots (desktop and mobile) in the PR description.

## Run locally

```bash
python scripts/serve.py          # then open http://localhost:8000
```

Or use the **Live Server** extension in VS Code.

## Golden rules

1. Open DevTools (F12) and keep the **Console** visible. Red errors mean something is wrong.
2. Test at desktop width **and** at 375 px (mobile).
3. Do not paste code you do not understand.
4. Commit small and often.
