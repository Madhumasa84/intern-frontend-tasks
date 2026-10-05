# Frontend Cheat Sheet

## HTML essentials

| Need | Use |
|------|-----|
| Page skeleton | `<!DOCTYPE html><html lang="en"><head>...</head><body>...</body></html>` |
| Responsive | `<meta name="viewport" content="width=device-width, initial-scale=1">` |
| Layout regions | `<header> <nav> <main> <section> <article> <footer>` |
| Table | `<table><caption><thead><tr><th scope="col">` and `<tbody><tr><td>` |
| Form field | `<label for="x">` + `<input id="x" name="x">` |
| Input types | `text tel email date time number search password checkbox radio` |
| Button | `<button type="button">` (does not submit), `type="submit"` (submits) |
| Links | `mailto:a@b.com`, `tel:+919876543210` |
| Hide | `hidden` attribute |

## CSS essentials

```css
* { box-sizing: border-box; }           /* padding included in width */
:root { --primary: #2563eb; }           /* variable */
.btn { background: var(--primary); }
```

| Goal | Snippet |
|------|---------|
| Center a block | `margin: 0 auto; max-width: 960px;` |
| Row with gap | `display: flex; gap: 12px; align-items: center; flex-wrap: wrap;` |
| Responsive grid | `display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 16px;` |
| Pill badge | `padding: 2px 10px; border-radius: 999px;` |
| Card | `border: 1px solid #e3e8ef; border-radius: 10px; box-shadow: 0 1px 3px rgba(0,0,0,.1);` |
| Hover | `.card:hover { transform: translateY(-2px); }` |
| Focus ring | `:focus-visible { outline: 3px solid #bfd3ff; }` |
| Mobile | `@media (max-width: 640px) { ... }` |
| Visually hidden | `position:absolute; width:1px; height:1px; overflow:hidden; clip:rect(0 0 0 0);` |
| Spinner | `border: 4px solid #e3e8ef; border-top-color: #2563eb; border-radius: 50%; animation: spin .8s linear infinite;` |

### Box model

```
margin > border > padding > content
```

### Specificity (low to high)

`tag` < `.class` < `#id` < inline style < `!important` (avoid).

## JavaScript essentials

```js
const el = document.getElementById("x");
const list = document.querySelectorAll(".row");           // NodeList
const rows = Array.from(list);                            // real array
el.addEventListener("input", (event) => { ... });
el.textContent = "safe text";                             // not innerHTML
el.hidden = true;
el.classList.toggle("invalid", isBad);
el.setAttribute("aria-invalid", "true");
el.dataset.status;                                        // reads data-status
```

| Event | Fires when |
|-------|------------|
| `click` | clicked |
| `input` | value changes on every keystroke |
| `change` | value committed (select changed, input blurred after edit) |
| `blur` | field loses focus |
| `submit` | form submitted (use `event.preventDefault()`) |
| `DOMContentLoaded` | HTML parsed (not needed with `defer`) |

### Strings, arrays and regex

```js
"abc".toLowerCase().includes("b");
"98765 43210".replace(/[\s-]/g, "");       // remove spaces and dashes
/^\d{10}$/.test("9876543210");              // exactly 10 digits
[1,2,3].filter(n => n > 1).map(n => n * 2);
```

### Async and fetch

```js
async function load() {
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
  } catch (err) {
    // network failure or the error thrown above
  } finally {
    // always runs
  }
}
```

### Timers

```js
const id = setTimeout(fn, 3000);  clearTimeout(id);
```

### Dates (local time)

```js
const d = new Date();
`${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,"0")}-${String(d.getDate()).padStart(2,"0")}`
```

## DevTools shortcuts

| Task | Shortcut |
|------|----------|
| Open DevTools | F12 / Ctrl+Shift+I |
| Device toolbar | Ctrl+Shift+M |
| Inspect element | Ctrl+Shift+C |
| Hard reload | Ctrl+Shift+R |

## Accessibility quick rules

1. Every input has a label.
2. Never rely on color alone.
3. Everything works with the keyboard.
4. Text contrast at least 4.5:1.
5. Images have `alt`; decorative ones `alt=""`.
6. Use real buttons and links, not clickable `<div>`s.
