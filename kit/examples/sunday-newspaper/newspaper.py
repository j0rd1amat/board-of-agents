"""Render the Sunday newspaper from an edition file written by the agent.

Usage: python3 -I newspaper.py <edition.json>
Writes editions/<date_slug>.html and .pdf next to this script (PDF via headless Chrome).

edition.json:
  date, date_slug, issue, title?
  top_stories: [{kicker, headline, deck, body:[paragraph], photo?, caption?, credit?}]   # first = lead
  editorial: str                                   # short "This week" note, page 2
  sections: [{name, items:[{tag?, headline, body, photo?, credit?}]}]
  actions: [{person, action, why, likelihood (0-100), status}]
  coming: [{when, what}], stats: {label: value}, security: str
Photos are paths relative to editions/ (e.g. img/x.jpg). Keep to 3-4 per edition.
"""
import html, json, os, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ED = json.loads(Path(sys.argv[1]).read_text())
OUT = HERE / "editions"
OUT.mkdir(exist_ok=True)
# Chrome prints the PDF. Set CHROME to your own path if it is somewhere else (Windows, Linux).
CHROME = os.environ.get("CHROME") or shutil.which("google-chrome") or shutil.which("chromium") or "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
e = html.escape


def fig(src, caption="", credit="", cls=""):
    if not src:
        return ""
    cap = f'<figcaption>{e(caption)}{f" <span>{e(credit)}</span>" if credit else ""}</figcaption>' if caption or credit else ""
    return f'<figure class="{cls}"><img src="{e(src)}">{cap}</figure>'


def story(s, lead=False):
    paras = "".join(f"<p>{e(p)}</p>" for p in s["body"])
    return (f'<article class="{"lead" if lead else "second"}"><div class="kicker">{e(s.get("kicker", ""))}</div>'
            f'<h2>{e(s["headline"])}</h2><div class="deck">{e(s.get("deck", ""))}</div>'
            f'{fig(s.get("photo"), s.get("caption", ""), s.get("credit", ""))}<div class="body">{paras}</div></article>')


def brief(i):
    tag = f'<span class="tag">{e(i["tag"])}</span>' if i.get("tag") else ""
    return (f'<div class="brief">{fig(i.get("photo"), "", i.get("credit", ""), "small")}{tag}'
            f'<h4>{e(i["headline"])}</h4><p>{e(i["body"])}</p></div>')


tops = ED["top_stories"]
front = story(tops[0], lead=True) + f'<div class="seconds">{"".join(story(s) for s in tops[1:3])}</div>'
sections = "".join(f'<section><h3>{e(s["name"])}</h3>{"".join(brief(i) for i in s["items"])}</section>'
                   for s in ED["sections"])
rows = "".join(
    f'<tr><td class="n">{n}</td><td><b>{e(a["person"])}</b></td><td>{e(a["action"])}</td><td class="why">{e(a["why"])}</td>'
    f'<td class="lk"><div class="bar"><i style="width:{int(a["likelihood"])}%"></i></div>{int(a["likelihood"])}%</td>'
    f'<td class="st">{e(a.get("status", "Suggested"))}</td></tr>'
    for n, a in enumerate(sorted(ED.get("actions", []), key=lambda a: -a["likelihood"]), 1))
coming = "".join(f'<li><b>{e(c["when"])}</b> {e(c["what"])}</li>' for c in ED.get("coming", []))
stats = "".join(f"<div><b>{e(str(v))}</b><span>{e(k)}</span></div>" for k, v in ED.get("stats", {}).items())
title = ED.get("title", "The Sunday Paper")

page = f"""<!doctype html><html><head><meta charset="utf-8"><title>{e(title)} · {e(ED['date'])}</title>
<style>
@page {{ size: A4; margin: 0; }}
:root {{ --ink:#141414; --mute:#6b6b6b; --rule:#d9d4c7; --paper:#fbf9f4; --accent:#8a2b1f; }}
html {{ -webkit-print-color-adjust:exact; print-color-adjust:exact; background:var(--paper); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; padding:13mm 14mm 14mm; background:var(--paper); color:var(--ink); font:9.8pt/1.45 "Iowan Old Style",Charter,Georgia,serif; }}
.sans {{ font-family:-apple-system,"Helvetica Neue",sans-serif; }}
.mast {{ text-align:center; border-bottom:3px double var(--ink); padding-bottom:5px; }}
.mast h1 {{ font:700 42pt/1 Didot,"Bodoni 72",Georgia,serif; letter-spacing:-.5px; margin:0; }}
.dateline {{ display:flex; justify-content:space-between; font:7.5pt/1.2 -apple-system,"Helvetica Neue",sans-serif; text-transform:uppercase;
  letter-spacing:.12em; color:var(--mute); border-bottom:1px solid var(--ink); padding:4px 0 5px; margin-bottom:11px; }}
.kicker {{ font:700 7.5pt -apple-system,sans-serif; text-transform:uppercase; letter-spacing:.14em; color:var(--accent); margin-bottom:3px; }}
article h2 {{ font:700 15pt/1.12 Didot,"Bodoni 72",Georgia,serif; margin:0 0 4px; }}
.deck {{ font:italic 10.5pt/1.35 Georgia,serif; color:#3c3c3c; margin-bottom:7px; }}
article p {{ margin:0 0 6px; text-align:justify; hyphens:auto; }}
figure {{ margin:0 0 8px; }} figure img {{ width:100%; display:block; object-fit:cover; }}
figcaption {{ font:italic 7.8pt/1.3 Georgia,serif; color:var(--mute); margin-top:3px; }}
figcaption span {{ font:7pt -apple-system,sans-serif; font-style:normal; text-transform:uppercase; letter-spacing:.06em; }}
.lead {{ display:grid; grid-template-columns:1.25fr 1fr; column-gap:16px; border-bottom:1px solid var(--ink); padding-bottom:11px; margin-bottom:11px; }}
.lead .kicker,.lead h2,.lead .deck {{ grid-column:1 / -1; }}
.lead h2 {{ font-size:30pt; line-height:1.03; letter-spacing:-.3px; }}
.lead .deck {{ font-size:12.5pt; }}
.lead figure {{ grid-column:1; grid-row:4; }} .lead figure img {{ height:62mm; }}
.lead .body {{ grid-column:2; grid-row:4; font-size:10.3pt; }}
.seconds {{ display:grid; grid-template-columns:1fr 1fr; gap:18px; }}
.second {{ border-top:2px solid var(--ink); padding-top:6px; }}
.second .body {{ columns:2; column-gap:12px; }}
.page2 {{ break-before:page; }}
.editorial {{ border-top:2px solid var(--ink); border-bottom:1px solid var(--rule); padding:6px 0 9px; margin-bottom:10px; columns:2; column-gap:18px; font-size:10.3pt; }}
.editorial .kicker {{ column-span:all; }}
.cols {{ columns:3; column-gap:15px; column-rule:1px solid var(--rule); }}
section {{ margin-bottom:8px; }}
h3 {{ font:700 8pt/1 -apple-system,"Helvetica Neue",sans-serif; text-transform:uppercase; letter-spacing:.14em; color:var(--accent);
  border-top:2px solid var(--ink); padding-top:5px; margin:0 0 6px; break-after:avoid; }}
.brief {{ break-inside:avoid; margin-bottom:8px; }}
.brief h4 {{ font:700 10.5pt/1.2 Georgia,serif; margin:0 0 2px; }} .brief p {{ margin:0; text-align:justify; hyphens:auto; }}
.brief figure.small img {{ height:56mm; object-position:50% 40%; }}
.tag {{ font:600 6.5pt -apple-system,sans-serif; text-transform:uppercase; letter-spacing:.1em; color:var(--mute); }}
.desk {{ break-before:page; }}
.desk h3 {{ font-size:9pt; }}
table {{ width:100%; border-collapse:collapse; font:8.6pt/1.35 -apple-system,"Helvetica Neue",sans-serif; margin-bottom:12px; }}
th {{ text-align:left; font-weight:600; font-size:7pt; text-transform:uppercase; letter-spacing:.08em; color:var(--mute);
  border-bottom:1.5px solid var(--ink); padding:4px 6px; }}
td {{ border-bottom:1px solid var(--rule); padding:6px; vertical-align:top; }}
td.n {{ color:var(--mute); width:14px; }} td.why {{ color:#444; }} td.st {{ color:var(--mute); white-space:nowrap; }}
td.lk {{ white-space:nowrap; width:78px; font-variant-numeric:tabular-nums; }}
.bar {{ display:inline-block; width:38px; height:5px; background:#e6e1d4; border-radius:3px; margin-right:6px; vertical-align:1px; }}
.bar i {{ display:block; height:100%; background:var(--accent); border-radius:3px; }}
.note {{ font:italic 8pt Georgia,serif; color:var(--mute); margin:-6px 0 14px; }}
.trio {{ display:grid; grid-template-columns:1.2fr 1fr 1fr; gap:16px; }}
.trio ul {{ margin:0; padding-left:14px; }} .trio li {{ margin-bottom:3px; }}
.stats {{ display:grid; grid-template-columns:repeat(3,1fr); gap:6px; }}
.stats div {{ text-align:center; }} .stats b {{ display:block; font:700 15pt Didot,Georgia,serif; }}
.stats span {{ font:6.8pt -apple-system,sans-serif; text-transform:uppercase; letter-spacing:.08em; color:var(--mute); }}
footer {{ margin-top:14px; border-top:1px solid var(--ink); padding-top:5px; font:7.3pt -apple-system,sans-serif; color:var(--mute); text-align:center; }}
</style></head><body>
<div class="mast"><h1>{e(title)}</h1></div>
<div class="dateline"><span>{e(ED['date'])}</span><span>Your people, this week</span><span>{e(ED.get('issue', ''))}</span></div>
{front}
<div class="page2">
<div class="editorial"><div class="kicker">This week</div>{"".join(f"<p>{e(p)}</p>" for p in ED.get("editorial", []))}</div>
<div class="cols">{sections}</div>
</div>
<div class="desk">
<h3>Your move</h3>
<table><tr><th></th><th>Who</th><th>Suggested reach-out</th><th>Why now</th><th>Likelihood</th><th>Status</th></tr>{rows}</table>
<div class="note">Likelihood is how likely the reach-out is to be welcome and worth doing this week. </div>
<div class="trio">
<div><h3>Coming up</h3><ul>{coming}</ul></div>
<div><h3>The sky in numbers</h3><div class="stats">{stats}</div></div>
<div><h3>Security desk</h3><p>{e(ED.get('security', ''))}</p></div>
</div>
<footer>Compiled by your AI assistant from your own sources. Private to you. Every item traces back to a quoted source.</footer>
</div>
</body></html>"""

stem = ED["date_slug"]
h = OUT / f"{stem}.html"
h.write_text(page)
pdf = OUT / f"{stem}.pdf"
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files",
                f"--print-to-pdf={pdf}", h.as_uri()], check=True, capture_output=True, timeout=120)
print(pdf)
