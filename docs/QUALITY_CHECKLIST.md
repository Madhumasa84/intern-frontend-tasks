# Quality Checklist (use before every PR)

## Functionality
- [ ] Does exactly what the exercise asks
- [ ] No errors in the DevTools Console
- [ ] `python scripts/verify.py <ex> --username <you>` shows no [FAIL]
- [ ] Tested by hand with unusual input (empty, very long, special characters)

## Responsive design
- [ ] Looks right at 1280 px, 768 px and 375 px
- [ ] No horizontal scrollbar at 375 px
- [ ] Tap targets are at least 40 px tall on mobile

## Visual design
- [ ] Light, clean theme with consistent spacing
- [ ] Max two font sizes per area, clear heading hierarchy
- [ ] Colors defined once as CSS variables
- [ ] Hover and focus states exist for interactive elements

## Accessibility
- [ ] `lang` attribute on `<html>`
- [ ] Every input has a `<label>`
- [ ] Status and errors are conveyed with text, not only color
- [ ] Keyboard-only walkthrough works (Tab, Shift+Tab, Enter, Space)
- [ ] Run Lighthouse > Accessibility: score 90 or more

## Code quality
- [ ] Semantic HTML (no `<div>` soup)
- [ ] No inline `style=""` or `onclick=""`
- [ ] No `!important` (except the documented `[hidden]` fix)
- [ ] `const`/`let`, `===`, small named functions
- [ ] No `innerHTML` with user or API data
- [ ] No `console.log`, commented-out code or unused CSS
- [ ] Consistent 2-space indentation

## Git and PR
- [ ] Branch `feature/<name>-ex-2-x`, files only inside `submissions/<you>/2.x/`
- [ ] Conventional commit message
- [ ] PR title `feat: ... (2.x) for <name>`
- [ ] Screenshots (desktop and mobile) attached
- [ ] Self-check questions answered
