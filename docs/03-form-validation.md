# Exercise 2.3: Form with Validation

**Tech:** HTML + CSS + vanilla JavaScript  |  **Deliverable:** `form.html` + `validation.js`  |  **Time:** 3 to 4 hours

## The goal

Build a **New Record** form like the one in the SCAI staff portal (creating an appointment for a contact), with friendly client-side validation and a success toast.

## Fields

| Field | id | Type | Rules |
|-------|----|------|-------|
| Contact Name | `contactName` | text | required, not just spaces, at least 2 characters |
| Phone Number | `phone` | tel | required, **exactly 10 digits** (spaces and dashes typed by user are ignored) |
| Appointment Date | `apptDate` | date | required, **not in the past** (today is allowed) |
| Appointment Time | `apptTime` | time | required |
| Notes | `notes` | textarea | optional, max 200 characters, show a live counter `0 / 200` |

## Required behavior

1. On **Submit**, validate every field.
2. **Invalid fields:** red border plus an error message **below** the field (text, not just color).
3. **Valid submit:** show a green **success toast** ("Record saved for <name>"), reset the form, auto-hide the toast after about 3 seconds.
4. Move keyboard focus to the **first invalid field** on failed submit.
5. After an error is shown, **clear it as soon as the user fixes the field** (validate on `input`), and validate a field on `blur` the first time it is touched.
6. **No page reload** and no real network call: just `console`-free front-end behavior.

## Markup contract

- `<form id="recordForm" novalidate>` (so *your* messages show instead of the browser's).
- Each field: `<label for="...">`, the input, and `<p class="error" id="<id>-error" role="alert"></p>`.
- Inputs get `aria-describedby="<id>-error"` and you toggle `aria-invalid="true|false"`.
- Toast container: `<div id="toast" role="status" aria-live="polite" hidden></div>`.
- Give the date input a `min` attribute set from JavaScript to today.

## validation.js structure (suggested)

```js
const validators = {
  contactName: (v) => (v.trim().length >= 2 ? "" : "Please enter the contact's name (min 2 characters)."),
  phone: (v) => (/^\d{10}$/.test(v.replace(/[\s-]/g, "")) ? "" : "Phone number must be exactly 10 digits."),
  apptDate: (v) => { /* required + not in the past */ },
  apptTime: (v) => (v ? "" : "Please choose a time."),
  notes: (v) => (v.length <= 200 ? "" : "Notes must be 200 characters or fewer."),
};
```

Each validator returns **an empty string when valid, or the error message when invalid.** One function (`validateField(name)`) shows or clears the message; one function (`validateForm()`) loops over all fields.

## Date handling trap

`new Date("2026-10-05")` is parsed as **UTC**, which can make "today" look like yesterday in India. Compare **strings** instead:

```js
function todayISO() {
  const d = new Date();
  const pad = (n) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}
// YYYY-MM-DD strings compare correctly with < and >
const isPast = value < todayISO();
```

## Step by step

1. Copy `exercises/2.3-form-validation/starter/*` to `submissions/<username>/2.3/`.
2. Build the form HTML with labels and error placeholders.
3. Style: card layout, inputs, focus ring, `.invalid` border, `.error` text, toast.
4. Write validators.
5. Wire `submit`, `blur` and `input` events.
6. Add toast and reset.
7. Test the **test matrix** below.
8. `python scripts/verify.py 2.3 --username <username>`.
9. Open PR with a GIF showing an error state and the success toast.

## Test matrix (paste your results in the PR)

| Input | Expected |
|-------|----------|
| Name empty | error, name field focused |
| Name `A` | error (min 2) |
| Name `   ` (spaces) | error |
| Phone `12345` | error |
| Phone `98765 43210` | valid |
| Phone `98765-43210` | valid |
| Phone `9876543210a` | error |
| Phone 11 digits | error |
| Date yesterday | error |
| Date today | valid |
| Time empty | error |
| Notes 201 chars | error |
| Everything valid | toast, form reset |
| Fix a field after error | error disappears immediately |

## Accessibility checklist

- [ ] Every input has a visible `<label>`
- [ ] Errors are text and connected with `aria-describedby`
- [ ] `aria-invalid` toggles
- [ ] Focus moves to the first invalid field
- [ ] Works with keyboard only (Tab, Enter)
- [ ] Color contrast of error text at least 4.5:1

## Self-check questions

1. Why `novalidate` on the form?
2. Why can client-side validation never be the only validation?
3. What is wrong with `new Date("2026-10-05") < new Date()`?
4. Why show errors as text and not only as a red border?

## Bonus

- Format the phone as the user types (`98765 43210`).
- Prevent double submit with a short disabled state.
- Remember the last appointment in `localStorage`.
- Add a "Preview" panel that updates live.

## Common mistakes

| Mistake | Result |
|---------|--------|
| Using `type="number"` for phone | drops leading zeros, allows `e` |
| Validating only on submit | frustrating UX |
| Not clearing old errors | stale red borders |
| `innerHTML` with the name in the toast | XSS; use `textContent` |

Next: [Exercise 2.4](04-fetch-api-data.md).
