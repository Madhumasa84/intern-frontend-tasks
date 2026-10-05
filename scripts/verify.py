#!/usr/bin/env python3
"""Self-check tool for the intern-frontend-tasks exercises.

Usage:
    python scripts/verify.py 2.1 --username <github-username>
    python scripts/verify.py 2.2 --username <github-username>
    python scripts/verify.py 2.3 --username <github-username>
    python scripts/verify.py 2.4 --username <github-username>

Static checks only (it reads your files; it does not run a browser).
[FAIL] items are required. [WARN] items are recommended and do not fail the run.
A passing run does NOT replace opening the page and testing it by hand.
"""
import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATUSES = ["Answered", "Missed", "Transferred"]
COLUMNS = ["caller number", "date & time", "duration", "status", "agent"]

required_ok = []


def check(ok, label, hint="", required=True):
    if required:
        required_ok.append(ok)
    tag = "[PASS]" if ok else ("[FAIL]" if required else "[WARN]")
    print(f"  {tag} {label}")
    if not ok and hint:
        print(f"         hint: {hint}")


class Page(HTMLParser):
    """Collects the facts we care about from an HTML document."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = {}
        self.ids = set()
        self.html_lang = None
        self.viewport = False
        self.title = ""
        self.in_title = False
        self.in_style = False
        self.style = ""
        self.in_thead = False
        self.in_tbody = False
        self.in_th = False
        self.th_text = []
        self.th_scopes = 0
        self.body_rows = 0
        self.tds_with_label = 0
        self.tds = 0
        self.scripts = []
        self.external = []
        self.inline_handlers = []
        self.label_for = set()
        self.class_stack = []
        self.status_with_class = set()
        self.form_attrs = {}
        self.input_types = {}
        self.has_caption = False
        self.has_h1 = 0
        self.attr_hits = set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags[tag] = self.tags.get(tag, 0) + 1
        if "id" in a:
            self.ids.add(a["id"])
        for name in a:
            if name.startswith("on"):
                self.inline_handlers.append(name)
        if tag == "html":
            self.html_lang = a.get("lang")
        elif tag == "meta" and a.get("name") == "viewport":
            self.viewport = True
        elif tag == "title":
            self.in_title = True
        elif tag == "style":
            self.in_style = True
        elif tag == "h1":
            self.has_h1 += 1
        elif tag == "caption":
            self.has_caption = True
        elif tag == "thead":
            self.in_thead = True
        elif tag == "tbody":
            self.in_tbody = True
        elif tag == "th":
            self.in_th = True
            self.th_text.append("")
            if a.get("scope"):
                self.th_scopes += 1
        elif tag == "tr" and self.in_tbody:
            self.body_rows += 1
        elif tag == "td":
            self.tds += 1
            if a.get("data-label"):
                self.tds_with_label += 1
        elif tag == "script":
            if a.get("src"):
                self.scripts.append(a["src"])
                if a["src"].startswith(("http://", "https://", "//")):
                    self.external.append(a["src"])
        elif tag == "link" and a.get("href", "").startswith(("http://", "https://", "//")):
            if "fonts.googleapis" not in a["href"] and "fonts.gstatic" not in a["href"]:
                self.external.append(a["href"])
        elif tag == "label" and a.get("for"):
            self.label_for.add(a["for"])
        elif tag == "form":
            self.form_attrs = a
        elif tag == "input":
            self.input_types[a.get("id", "")] = a.get("type", "text")
        for key in ("aria-live", "aria-describedby", "aria-invalid", "role", "hidden", "min", "novalidate"):
            if key in a:
                self.attr_hits.add(key)
        if a.get("role") in ("alert", "status"):
            self.attr_hits.add("role:" + a["role"])
        self.class_stack.append((tag, a.get("class", "")))

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "style":
            self.in_style = False
        elif tag == "thead":
            self.in_thead = False
        elif tag == "tbody":
            self.in_tbody = False
        elif tag == "th":
            self.in_th = False
        for i in range(len(self.class_stack) - 1, -1, -1):
            if self.class_stack[i][0] == tag:
                del self.class_stack[i:]
                break

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_style:
            self.style += data
        if self.in_th and self.th_text:
            self.th_text[-1] += data
        word = data.strip()
        if self.in_tbody and word in STATUSES:
            has_class = any(cls for (_t, cls) in self.class_stack[-2:] if cls)
            if has_class:
                self.status_with_class.add(word)


def load(folder, filename):
    path = folder / filename
    if not path.exists():
        check(False, f"{filename} exists in {folder.relative_to(ROOT)}", "copy the starter first (see the README)")
        return None, None
    check(True, f"{filename} exists")
    text = path.read_text(encoding="utf-8")
    page = Page()
    if filename.endswith(".html"):
        page.feed(text)
    return text, page


def common_html(page, text):
    check(page.html_lang is not None, '<html lang="..."> is set')
    check(page.viewport, "viewport meta tag is present", 'add <meta name="viewport" content="width=device-width, initial-scale=1">')
    check(bool(page.title.strip()), "<title> is not empty")
    check(page.has_h1 == 1, f"exactly one <h1> (found {page.has_h1})")
    check(not page.external, "no external libraries or CDN files", ", ".join(page.external))
    check(not page.inline_handlers, "no inline event handlers (onclick=...)", ", ".join(page.inline_handlers), required=False)


def verify_2_1(folder):
    print("Exercise 2.1: Static call log table")
    text, page = load(folder, "index.html")
    if not page:
        return
    common_html(page, text)
    check("table" in page.tags, "has a <table>")
    check("thead" in page.tags and "tbody" in page.tags, "uses <thead> and <tbody>")
    headers = [t.strip().lower() for t in page.th_text]
    missing = [c for c in COLUMNS if c not in headers]
    check(not missing, "has all 5 column headers", f"missing: {', '.join(missing)}")
    check(page.body_rows >= 5, f"at least 5 data rows (found {page.body_rows})")
    check(page.th_scopes >= 5, 'every <th> has scope="col"', required=False)
    check(page.has_caption, "table has a <caption>", required=False)
    body = text
    for s in STATUSES:
        check(s in body, f"status '{s}' is used")
    check(len(page.status_with_class) == 3, "each status is wrapped in an element with a class (for color)", required=True)
    css = page.style
    check(bool(css.strip()), "CSS is embedded in a <style> tag")
    check("@media" in css and "max-width" in css, "has a responsive @media (max-width ...) block")
    check("var(--" in css, "uses CSS variables", required=False)
    check(page.tds > 0 and page.tds_with_label == page.tds, 'every <td> has data-label (for the mobile layout)', required=False)
    color_rules = len(re.findall(r"status--?\w*", css))
    check(color_rules >= 3, "defines at least 3 status style rules", required=False)
    check(not page.scripts, "no JavaScript needed for 2.1", required=False)


def js_text(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return re.sub(r"(^|\s)//[^\n]*", r"\1", text)


def verify_2_2(folder):
    print("Exercise 2.2: Dynamic filter UI")
    text, page = load(folder, "index.html")
    js, _ = load(folder, "app.js")
    if not page or js is None:
        return
    code = js_text(js)
    common_html(page, text)
    for ident in ("statusFilter", "searchInput", "callsTable", "resultCount", "clearFilters", "emptyState"):
        check(ident in page.ids, f"id='{ident}' is present")
    check("select" in page.tags and "input" in page.tags, "has a <select> and an <input>")
    check(any("app.js" in s for s in page.scripts), "index.html loads app.js")
    check("addEventListener" in code, "uses addEventListener")
    check(bool(re.search(r"""["']input["']""", code)), "listens to the 'input' event (live search)")
    check(bool(re.search(r"""["']change["']""", code)), "listens to the 'change' event (dropdown)")
    check("function" in code or "=>" in code, "logic is organized in functions")
    check("hidden" in code or "display" in code, "rows are shown/hidden with JS")
    check("includes" in code or "indexOf" in code or "test(" in code or "match(" in code, "search compares text")
    check("toLowerCase" in code, "search is case-insensitive", required=False)
    check(bool(re.search(r"replace\(", code)), "search text is normalized (strips spaces/dashes)", required=False)
    check("innerHTML" not in code, "avoids innerHTML", required=False)
    check("console.log" not in code, "no leftover console.log", required=False)
    check("var " not in code, "no 'var' (use const/let)", required=False)
    check("aria-live" in text, "result count has aria-live", required=False)
    check("preventDefault" in code or "form" not in page.tags, "form submit does not reload the page")


def verify_2_3(folder):
    print("Exercise 2.3: Form with validation")
    text, page = load(folder, "form.html")
    js, _ = load(folder, "validation.js")
    if not page or js is None:
        return
    code = js_text(js)
    common_html(page, text)
    for ident in ("recordForm", "contactName", "phone", "apptDate", "apptTime", "notes", "toast"):
        check(ident in page.ids, f"id='{ident}' is present")
    for ident in ("contactName", "phone", "apptDate", "apptTime", "notes"):
        check(ident in page.label_for, f"a <label for='{ident}'> exists", required=False)
        check(f"{ident}-error" in page.ids, f"error element '{ident}-error' exists")
    check("novalidate" in page.form_attrs, "<form> has novalidate")
    check(page.input_types.get("phone") == "tel", "phone input is type='tel'", required=False)
    check(page.input_types.get("apptDate") == "date", "date input is type='date'")
    check(page.input_types.get("apptTime") == "time", "time input is type='time'")
    check("textarea" in page.tags, "notes uses a <textarea>")
    check(any("validation.js" in s for s in page.scripts), "form.html loads validation.js")
    check(bool(re.search(r"""["']submit["']""", code)), "listens to 'submit'")
    check("preventDefault" in code, "calls preventDefault")
    check(bool(re.search(r"\\d\{10\}|\[0-9\]\{10\}|length\s*(===|==|!==|!=)\s*10", code)), "checks for exactly 10 digits")
    check(bool(re.search(r"""["']blur["']""", code)) or bool(re.search(r"""["']focusout["']""", code)), "validates on blur", required=False)
    check(bool(re.search(r"""["']input["']""", code)), "re-validates on input")
    check("focus()" in code, "focuses the first invalid field")
    check("200" in code, "enforces the 200 character notes limit")
    check("reset()" in code, "resets the form after success")
    check("setTimeout" in code, "toast auto-hides with setTimeout")
    check("aria-invalid" in code, "toggles aria-invalid", required=False)
    check("textContent" in code, "uses textContent for messages", required=False)
    check("innerHTML" not in code, "avoids innerHTML", required=False)
    check(bool(re.search(r"new Date\(\s*[\w.]*(value|apptDate)", code)) is False, "does not parse the date string with new Date(value) (timezone trap)", required=False)
    check("getFullYear" in code or "toLocaleDateString" in code or "padStart" in code, "builds today's date in local time", required=False)
    check("min" in code, "sets the min attribute on the date input", required=False)
    check("console.log" not in code, "no leftover console.log", required=False)


def verify_2_4(folder):
    print("Exercise 2.4: Fetch and display API data")
    text, page = load(folder, "index.html")
    js, _ = load(folder, "app.js")
    if not page or js is None:
        return
    code = js_text(js)
    common_html(page, text)
    for ident in ("loader", "userGrid", "errorBox", "retryBtn"):
        check(ident in page.ids, f"id='{ident}' is present")
    check(any("app.js" in s for s in page.scripts), "index.html loads app.js")
    check("jsonplaceholder.typicode.com/users" in code, "uses the JSONPlaceholder users endpoint")
    check("fetch(" in code, "uses fetch()")
    check("async" in code and "await" in code, "uses async/await")
    check(bool(re.search(r"\.ok\b", code)), "checks response.ok")
    check("catch" in code, "has a catch block")
    check("finally" in code, "uses finally (recommended)", required=False)
    check(".json()" in code, "parses the response with .json()")
    check("addEventListener" in code, "uses addEventListener for Retry")
    check("name" in code and "email" in code and "phone" in code and "company" in code, "renders name, email, phone and company")
    check("mailto:" in code, "email is a mailto: link", required=False)
    check("tel:" in code, "phone is a tel: link", required=False)
    check("textContent" in code, "builds content with textContent")
    check("innerHTML" not in code, "avoids innerHTML with API data", required=False)
    check("spinner" in page.style.lower() or "@keyframes" in page.style, "has a CSS spinner (@keyframes)", required=False)
    check("grid" in page.style, "uses CSS grid for the cards")
    check("role:alert" in page.attr_hits, "error box has role='alert'", required=False)
    check("console.log" not in code, "no leftover console.log", required=False)
    check("var " not in code, "no 'var' (use const/let)", required=False)


RUNNERS = {"2.1": verify_2_1, "2.2": verify_2_2, "2.3": verify_2_3, "2.4": verify_2_4}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("exercise", choices=sorted(RUNNERS))
    parser.add_argument("--username", required=True, help="your GitHub username (your folder name)")
    parser.add_argument("--path", help="override the folder to check (mentors)")
    args = parser.parse_args()
    folder = Path(args.path) if args.path else ROOT / "submissions" / args.username / args.exercise
    if not folder.exists():
        print(f"Folder not found: {folder}\nCreate it and copy the starter files first (see README).")
        return 1
    RUNNERS[args.exercise](folder)
    print()
    if all(required_ok):
        print("All required checks passed. Now test it by hand in the browser, then open your PR!")
        return 0
    print("Some required checks failed. Fix them and run again.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
