# Example: find who you already know at the companies you want to reach

A worked example of the kit's pattern, applied to sales. You keep a list of companies you want to talk to. A script matches it against your own LinkedIn connections, so the first message at each company goes to someone who knows you. Cold email is the fallback, from a separate domain and inside hard limits.

It is the same pieces as the rest of the kit: an agent with one job, a record it writes to, and rules it cannot widen. Here the rules protect two things: your name and your email domain.

## What is in this folder

| File | What it is |
|---|---|
| `SETUP-PROMPT.md` | Paste it into Claude Code. It builds your own version with you, one step at a time |
| `match.mjs` | The matching script. It reads two files on your computer, writes a third, and sends nothing |
| `prompt.md` | The same job as a prompt, if you would rather paste two files into Claude than run a script |
| `rules.md` | The outreach rules: warm before cold, the separate domain, the caps and the stop rules |

## Get the file first

LinkedIn's "Download my data" page said in November 2026: "As of December 2026, your data download no longer includes your connections' email addresses, current companies, or job titles." If you are reading this before then, request your archive now, on a computer:

1. Settings → Data privacy → Download my data
2. Choose the larger data archive
3. Request archive

The archive holds `Connections.csv`: one row per connection, with name, company, job title and the day you connected. If you are reading this after the change, the script still needs a company for each connection, so you will have to fill that column from another source.

## How it works

1. **A list of companies, scored.** Every day an agent adds companies that fit and gives each a score from 0 to 10 on five criteria, from public pages only. An unknown fact scores zero. Only companies at 6 or more are contacted.
2. **The match.** `match.mjs` compares the list with `Connections.csv` and sorts the people it finds: the buyer first, then senior people, then everyone else. Mine read 2,580 connections and found 250 at 120 companies on my list.
3. **Warm first.** Where you know someone, that person hears from you before anyone else at the company. One personal message, to one person.
4. **Cold as the fallback.** Where you know nobody, the agent finds the right person from public sources, three per company at most, checks that the address exists, and writes to one of them at a time.
5. **Replies and meetings.** The agent answers in the same thread and nudges once. When someone wants to talk, they pick a slot from a booking link and the meeting is in your calendar.

## Before you build this

- **Start with the match alone.** Steps 1 and 2 need no agent and send nothing. You get a list of people worth writing to, and you write to them yourself.
- **The file is a photograph.** Job titles are true on the day you export. Check the profile before you write, and skip anyone who has moved.
- **Keep the file on your computer.** It is a list of people who trusted you with a connection. The script runs locally; do not upload the file to tools you do not know.
- **Warm and cold must never meet.** While someone you know at a company has a message from you, nobody else there gets a cold email. `rules.md` has the rule.
- **Never send cold email from your main domain.** `rules.md` explains the second domain, the warm-up and the caps.
- **Check the rules where you and your recipients live.** Cold email to companies is treated differently from country to country, and platforms have their own terms about automated activity. Read both before an agent sends anything.
