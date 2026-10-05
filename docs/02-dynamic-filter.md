# Exercise 2.2: Dynamic Filter UI

**Tech:** HTML + CSS + vanilla JavaScript  |  **Deliverable:** `index.html` + `app.js`  |  **Time:** 3 hours
**Builds on:** [Exercise 2.1](01-static-call-log.md). Start from your own finished 2.1 page (or use the starter, which already contains one).

## The goal

Add two live controls to the call-log table:

1. A **Status** dropdown: `All`, `Answered`, `Missed`, `Transferred`.
2. A **search** box that matches the **Caller Number**.

Both must work **in real time**, **together**, with **no page reload**.

## Requirements

### Behavior
- Changing the dropdown filters instantly.
- Typing in the search box filters instantly (on every keystroke).
- Filters combine with AND: "Missed" + "98111" shows only rows that are both.
- Search is case-insensitive and ignores spaces, dashes and the `+` sign: typing `9876543210` or `98765 43210` or `+91 98765` all match `+91 98765 43210`.
- When nothing matches, show a friendly row or message: **"No calls match your filters."**
- Show a live count: **"Showing 3 of 6 calls"**.
- A **Clear filters** button resets both controls.

### Markup contract (the verify script depends on these ids)
| Element | id |
|---------|----|
| status select | `statusFilter` |
| search input | `searchInput` |
| table | `callsTable` |
| result count text | `resultCount` |
| clear button | `clearFilters` |
| empty message | `emptyState` |

### Code quality
- All JavaScript lives in `app.js`, loaded with `<script src="app.js" defer></script>`.
- **No inline handlers** (`onclick="..."`). Use `addEventListener`.
- Do not wrap controls in a `<form>` that submits. If you do, call `event.preventDefault()`.
- Read rows from the DOM; do not duplicate the data in JS (bonus: render from a JS array instead).
- Small functions: `normalize`, `matches`, `applyFilters`, `updateCount`.
- Every control has a `<label>` (can be visually hidden).
- The count has `aria-live="polite"` so screen readers announce changes.

## Step by step

1. Copy `exercises/2.2-dynamic-filter/starter/*` to `submissions/<username>/2.2/`.
2. Add the controls bar above the table.
3. In `app.js`, select elements with `document.getElementById`.
4. Write `normalize(text)`: lowercase and strip everything except letters and digits.
5. Write `applyFilters()`: loop over `tbody tr`, decide visibility, toggle the `hidden` attribute.
6. Attach `change` listener to the select and `input` listener to the search box.
7. Update the count and empty state.
8. Wire the clear button.
9. Self-check: `python scripts/verify.py 2.2 --username <username>`.
10. Open PR with a GIF or short recording of filtering.

## Key ideas

```js
const normalize = (s) => s.toLowerCase().replace(/[^a-z0-9]/g, "");

function applyFilters() {
  const status = statusFilter.value;               // "all" | "Answered" | ...
  const query = normalize(searchInput.value);
  let visible = 0;

  rows.forEach((row) => {
    const rowStatus = row.dataset.status;
    const caller = normalize(row.cells[0].textContent);
    const show = (status === "all" || rowStatus === status) && caller.includes(query);
    row.hidden = !show;
    if (show) visible += 1;
  });

  resultCount.textContent = `Showing ${visible} of ${rows.length} calls`;
  emptyState.hidden = visible !== 0;
}
```

Add `data-status="Answered"` on each `<tr>` so JS does not parse the text.

## Hints

- `input` fires on every keystroke; `change` fires when a select changes.
- `element.hidden = true` is the simplest show/hide; make sure CSS does not override it (`tr[hidden] { display: none; }`).
- Use `Array.from(table.tBodies[0].rows)` to get rows as an array.
- Debug with `console.log` while building, then remove them.

## Self-check questions

1. What is the difference between the `input` and `change` events?
2. Why `defer` on the script tag?
3. Why normalize the search text?
4. What does "no page reload" mean and what would cause a reload accidentally?

## Bonus

- Persist filters in the URL (`?status=Missed&q=981`) with `URLSearchParams` and `history.replaceState`.
- Debounce the search by 150 ms.
- Highlight the matched digits.
- Add a "sort by date" toggle on the Date column.

## Common mistakes

| Mistake | Result |
|---------|--------|
| Using `display: none` in JS styles only on status filter | Search and filter fight each other; compute both together |
| `innerHTML` with user text | XSS risk; use `textContent` |
| Forgetting the empty state | Confusing blank table |
| Script placed before the table without `defer` | `null` errors in console |

Next: [Exercise 2.3](03-form-validation.md).
