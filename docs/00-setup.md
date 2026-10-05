# Exercise 0: Setup

**Time: 20 minutes.**

## 1. Tools

| Tool | Why | Get it |
|------|-----|--------|
| VS Code | editor | https://code.visualstudio.com |
| Chrome or Edge | DevTools | any recent version |
| Git | version control | done in `intern-git-fundamentals` |
| Python 3.9+ | local server and verify script | https://python.org |
| Node.js (optional) | `node --check app.js` locally | https://nodejs.org |

## 2. VS Code extensions

- **Live Server** (Ritwick Dey): auto-reloads the browser on save
- **Prettier**: formatter (turn on Format on Save)
- **ESLint** (optional)
- **HTMLHint** (optional)

Settings (Ctrl+,): enable `Editor: Format On Save`, set `Editor: Tab Size` to 2.

## 3. Run a page

Either:

```bash
python scripts/serve.py        # http://localhost:8000
```

or right-click an HTML file > **Open with Live Server**.

> **Why not double-click the file?** `fetch()` (Exercise 2.4) does not behave the same under `file://`. Always use a server.

## 4. Learn DevTools (10 minutes, do not skip)

Press **F12**.

| Panel | Use it to |
|-------|-----------|
| **Elements** | inspect HTML, edit CSS live, see the box model |
| **Console** | see JS errors, run snippets |
| **Network** | see `fetch` requests, status, timing, throttle to Slow 3G, go Offline |
| **Device toolbar** (Ctrl+Shift+M) | test mobile widths like 375 px |
| **Lighthouse** | accessibility and best-practice score |

Try it now: open any website, right-click a heading > Inspect > change its text and color.

## 5. The three-file mental model

| Language | Job | Analogy |
|----------|-----|---------|
| HTML | structure and meaning | skeleton |
| CSS | look and layout | clothes |
| JavaScript | behavior | muscles |

## 6. Folder for your work

```
submissions/<your-github-username>/2.1/
```

Create it as shown in the README. Never edit `exercises/`; copy from it.

## Checklist

- [ ] VS Code and Live Server installed
- [ ] `python scripts/serve.py` serves the repo
- [ ] You opened DevTools Console, Elements and Network at least once
- [ ] You can emulate a 375 px phone

Next: [Exercise 2.1](01-static-call-log.md).
