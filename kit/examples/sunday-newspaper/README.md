# Example: a Sunday newspaper about your friends

A worked example of the kit's pattern, applied to personal life instead of a company. During the week, read-only agents skim the places where your friends and contacts post and write to you. On Sunday morning another agent turns the week's facts into a short newspaper: who is moving, who is hiring, who has news, and who you should call.

It is the same three pieces as the rest of the kit: scheduled agents with one job each, a shared record they write to, and rules they cannot widen.

Open `editions/sample.pdf` to see what comes out. Every person and message in the sample is invented.

## What is in this folder

| File | What it is |
|---|---|
| `SETUP-PROMPT.md` | Paste it into Claude Code. It builds your own version with you, one step at a time |
| `rules.md` | The hard rules every run reads first: read-only, no quote no fact, what stays out |
| `task-prompt.md` | The prompt of the Sunday scheduled task |
| `newspaper.py` | Turns an edition file into the PDF (needs Python 3 and Google Chrome) |
| `editions/sample.json` | A sample edition, in the format the Sunday agent writes |
| `editions/sample.pdf` | The sample, printed |

Try the printer first:

```
python3 newspaper.py editions/sample.json
```

## How it works

1. **Scan runs (daily).** One agent per source reads what is new and saves facts to a local database. A fact is one sentence plus the exact quote it came from, who said it, and where.
2. **The Sunday run.** It reads the week's facts from the database, writes `editions/<date>.json`, runs `newspaper.py`, and sends you one notification with the headline.
3. **You.** You read three pages. When a fact is wrong, you correct it, and the correction outranks every future scan.

What is not in this folder: the scanners and the database themselves. They depend on which apps you use and how you are logged in, so `SETUP-PROMPT.md` has Claude Code build them with you instead of handing you mine.

## Before you build this

- **Start with one source.** Email is the easiest and the least sensitive. Add another only after a clean week.
- **Keep it on your own machine.** The database is a single local file. Nothing about your contacts goes to another service.
- **Read-only means read-only.** The scan agents never like, reply, post, follow or message. Some apps show people that you viewed something; decide where you are comfortable with that.
- **Other people's words are data, never instructions.** Messages sometimes address "any AI reading this". The rules tell the agent to ignore them and log them.
- **Check what applies to you.** Platform terms and privacy rules differ by app and by country. Look at them before you point an agent at an account.
- **The first editions will contain mistakes.** Mine invented a meet-up nobody had proposed. That is why the rules now demand a quote for every fact.
