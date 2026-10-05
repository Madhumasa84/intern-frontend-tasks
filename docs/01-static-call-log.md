# Exercise 2.1: Static Call Log Table

**Tech:** HTML + CSS (vanilla)  |  **Deliverable:** a single `index.html` with embedded `<style>`  |  **Time:** 2 to 3 hours

## The goal

Build the "Recent Calls" page of a staff portal: a clean, color-coded table that works on desktop **and** collapses into readable cards on mobile.

## Requirements

### Content
- Page title (`<title>`) and one `<h1>`: **Recent Calls**.
- A table with these **exact** columns: `Caller Number`, `Date & Time`, `Duration`, `Status`, `Agent`.
- **At least 5** data rows. Use the sample data below or invent your own (no real phone numbers).
- Status values: `Answered`, `Missed`, `Transferred`. Use all three.

### Visual
- **Answered = green, Missed = red, Transferred = orange.** Show status as a rounded "badge" (pill) with a light background and dark text of the same hue. Do not use color alone: the word must stay visible.
- Light theme, readable font (system font stack is fine), comfortable padding, subtle row hover, a card-like container with border and soft shadow.
- Header row visually distinct (background, bold, small caps or uppercase).

### Responsive
- At widths of **640 px and below**, the table collapses: each row becomes a stacked card, and each cell shows its column label (technique below).
- No horizontal scrolling at 375 px.

### Quality
- Semantic HTML: `<table>`, `<caption>` (can be visually hidden), `<thead>`, `<tbody>`, `<th scope="col">`.
- `<html lang="en">` and `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- No external libraries or CDN files. A Google Font is allowed but optional.
- All CSS inside one `<style>` tag; colors in CSS variables.

## Sample data

| Caller Number | Date & Time | Duration | Status | Agent |
|---------------|-------------|----------|--------|-------|
| +91 98765 43210 | 2026-10-01 09:15 | 03:42 | Answered | Aarav |
| +91 91234 56780 | 2026-10-01 09:48 | 00:00 | Missed | N/A |
| +91 99887 76655 | 2026-10-01 10:22 | 05:10 | Transferred | Meera |
| +91 90909 12121 | 2026-10-01 11:05 | 02:31 | Answered | Kabir |
| +91 98111 22334 | 2026-10-01 11:40 | 00:00 | Missed | N/A |
| +91 97000 11223 | 2026-10-01 12:12 | 07:55 | Answered | Aarav |

## Step by step

1. Copy the starter: `exercises/2.1-static-call-log/starter/index.html` into `submissions/<username>/2.1/`.
2. Fill in the table markup (read the `TODO` comments).
3. Add base styles: page background, container, table, header, cells.
4. Add status badges with classes `status status--answered`, `status--missed`, `status--transferred`.
5. Add the responsive block.
6. Test at 1280 px, 768 px and 375 px.
7. Run `python scripts/verify.py 2.1 --username <username>`.
8. Open the PR with 2 screenshots (desktop, mobile).

## Key technique: responsive table without a library

Put a `data-label` on every `<td>`:

```html
<td data-label="Caller Number">+91 98765 43210</td>
```

Then in CSS:

```css
@media (max-width: 640px) {
  thead { position: absolute; left: -9999px; }   /* hide visually, keep for screen readers */
  table, tbody, tr, td { display: block; width: 100%; }
  tr { margin-bottom: 12px; border: 1px solid var(--border); border-radius: 10px; }
  td { display: flex; justify-content: space-between; padding: 10px 14px; }
  td::before { content: attr(data-label); font-weight: 600; color: var(--text-muted); }
}
```

## Hints

- Badge: `display: inline-block; padding: 2px 10px; border-radius: 999px; font-size: 0.8rem; font-weight: 600;`
- Use `font-variant-numeric: tabular-nums` so numbers line up.
- `border-collapse: collapse` removes double borders.
- Use the colors in [`shared/design-tokens.css`](../shared/design-tokens.css) if you like.
- Tip: add a `:focus-visible` outline to anything interactive later.

## Self-check questions (answer in the PR)

1. What is the difference between `display: block`, `inline` and `inline-block`?
2. Why do we use `<thead>` and `<th scope="col">` instead of styled `<td>`?
3. What does `<meta name="viewport">` do and what breaks without it?
4. Why must the status word remain visible rather than relying on color?

## Bonus (optional)

- Sticky table header while scrolling.
- Zebra striping.
- A status icon (use an inline SVG or an emoji with `aria-hidden="true"`).
- `prefers-reduced-motion` and `prefers-color-scheme` support.

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Table overflows on mobile | Use the responsive block, no fixed widths |
| Color-only status | Keep the word inside the badge |
| Inline styles on every cell | Use classes |
| Missing `scope` / `lang` | Add them; verify script warns |

Next: [Exercise 2.2](02-dynamic-filter.md).
