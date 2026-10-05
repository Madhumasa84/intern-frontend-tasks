# Exercise 2.4: Fetch and Display API Data

**Tech:** HTML + CSS + vanilla JavaScript + `fetch()`  |  **Deliverable:** `index.html` + `app.js`  |  **Time:** 3 hours

## The goal

Fetch a list of users from a public API and show them as cards, with proper **loading** and **error** states. This is the pattern behind every dashboard screen in SCAI.

API: `https://jsonplaceholder.typicode.com/users` (returns 10 users, no key needed).

Each user looks like:

```json
{
  "id": 1,
  "name": "Leanne Graham",
  "email": "Sincere@april.biz",
  "phone": "1-770-736-8031 x56442",
  "company": { "name": "Romaguera-Crona" }
}
```

## Requirements

### Data
- Use `fetch()` with `async/await`.
- Check `response.ok`; if not OK, throw an error with the status code.
- Show for each user: **name, email, phone, company name**.

### Layout
- **Card grid**: responsive columns using CSS Grid (`repeat(auto-fill, minmax(260px, 1fr))`).
- Each card: avatar circle with the user's initials, name, email (as a `mailto:` link), phone (as a `tel:` link), company badge.

### States (the heart of this exercise)
| State | What the user sees |
|-------|--------------------|
| **Loading** | A CSS spinner and the text "Loading users..." (no images) |
| **Success** | The card grid; spinner hidden |
| **Error** | A red message box: "Could not load users. (reason)" with a **Retry** button |
| **Empty** (bonus) | "No users found." |

Only **one** state is visible at a time.

### Markup contract
| Element | id |
|---------|----|
| loading spinner container | `loader` |
| card grid | `userGrid` |
| error box | `errorBox` |
| retry button | `retryBtn` |

### Code quality
- `app.js` with `<script src="app.js" defer></script>`.
- Functions: `fetchUsers()`, `renderUsers(users)`, `showLoading()`, `showError(msg)`, `showSuccess()`.
- Use `try / catch / finally`.
- Build DOM safely with `createElement` + `textContent` (avoid `innerHTML` with API data).
- No libraries.

## Step by step

1. Copy `exercises/2.4-fetch-api-data/starter/*` to `submissions/<username>/2.4/`.
2. Build static HTML for the three state containers.
3. Style the grid, card, spinner and error box.
4. Implement `fetchUsers` and log the result.
5. Implement `renderUsers`.
6. Add state switching.
7. Test **all states** (below).
8. `python scripts/verify.py 2.4 --username <username>`.
9. PR with screenshots of loading, success and error.

## Core pattern

```js
async function loadUsers() {
  showLoading();
  try {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error(`Server responded with ${response.status}`);
    const users = await response.json();
    renderUsers(users);
    showSuccess();
  } catch (err) {
    showError(err.message);
  }
}
```

Note: `fetch` only rejects on **network** failure. A 404 or 500 still "succeeds", which is why `response.ok` matters.

## How to test every state

| State | How |
|-------|-----|
| Loading | DevTools > Network > Throttling: **Slow 3G** > Retry |
| Error (offline) | DevTools > Network > **Offline** > reload or Retry |
| Error (HTTP) | Temporarily change the URL to `.../userz` (returns 404) |
| Retry works | Go back online, click Retry, grid appears |

Include screenshots of each in your PR.

## Spinner CSS

```css
.spinner {
  width: 36px; height: 36px; border-radius: 50%;
  border: 4px solid #e3e8ef; border-top-color: #2563eb;
  animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
@media (prefers-reduced-motion: reduce) { .spinner { animation-duration: 3s; } }
```

## Hints

- Initials: `name.split(" ").map(w => w[0]).slice(0, 2).join("")`.
- Disable the Retry button while loading.
- Add `role="status"` to the loader and `role="alert"` to the error box.
- Keep a `finally` block that always hides the spinner.

## Self-check questions

1. Why doesn't `fetch` throw on a 404?
2. What does `await` do, and what is a Promise?
3. Why avoid `innerHTML` with API data?
4. What are the 3 states of every data-driven screen?

## Bonus

- Search box that filters the loaded cards (reuse ideas from 2.2).
- Cache the result in `sessionStorage` to avoid refetching.
- Skeleton cards instead of a spinner.
- Add a timeout using `AbortController` (abort after 8 s and show an error).

## Common mistakes

| Mistake | Result |
|---------|--------|
| No `response.ok` check | 404 renders an empty/broken UI |
| Forgetting `await response.json()` | You render a Promise: `[object Promise]` |
| Spinner never hidden on error | UI stuck |
| Opening via `file://` | Possible CORS or origin quirks; use `python scripts/serve.py` |

## You finished the frontend repo

Next repository: `intern-backend-tasks`.
