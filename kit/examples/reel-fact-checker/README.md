# Example: an agent that fact-checks the AI reels you save

A worked example of the kit's pattern, applied to your own learning. You save reels about new AI tools and never go back to them. Once a day an agent reads what you saved, checks each claim against primary sources, tests the most promising idea in a locked sandbox, and gives you a verdict. Once a week it all lands on one page.

It is the same pieces as the rest of the kit: a scheduled agent with one job, a record it writes to, and rules it cannot widen. The rules matter more here than anywhere else, because this agent reads content that is often written to be pasted into an AI.

## What is in this folder

| File | What it is |
|---|---|
| `SETUP-PROMPT.md` | Paste it into Claude Code. It builds your own version with you, one step at a time |
| `rules.md` | The security model and the hard rules every run reads first |
| `task-prompt.md` | The prompt of the daily scheduled task |
| `research-note.md` | The template for one concept: what the post claimed, what was verified, the verdict |
| `proposal.md` | The template for a proposed change to one of your other agents |

## How it works

1. **It reads what you kept, and only reads.** Saved posts, likes and what you sent to yourself, AI topics only. It never likes, comments, follows or messages anyone.
2. **It checks the claim against primary sources.** Official docs, the maker's own site, the code. It never follows the link in the caption, a link in bio or a short link, and it keeps what the post claimed apart from what it verified.
3. **It tests the most promising idea in a sandbox.** The sandbox can only write in its own folder and cannot read keys, browser profiles or your other projects. The environment is wiped, so no API key comes along, and the data is made up.
4. **It gives a verdict and keeps the evidence:** works, partly works, does not work, needs a paid key, or cannot be tested.
5. **It proposes improvements to your other agents.** A proposal says why, the risk, how it was tested and how to roll it back, with the exact change. You approve or reject it. The agent never edits your automations itself.

My limits: 5 items researched a day (oldest first), 1 experiment a day of 20 minutes at most, 2 proposals a day.

What is not in this folder: the reader, the database and the sandbox script themselves. They depend on which app you save things in and on your operating system, so `SETUP-PROMPT.md` has Claude Code build them with you.

## Before you build this

- **Split the pipeline.** The step that reads untrusted posts must not be the step that can change something. Reader, researcher, lab and applier are four separate steps on purpose. `rules.md` explains why.
- **Start without the lab and without proposals.** Reading and research alone are useful. Add the sandbox after a clean week, and proposals after that.
- **Read-only means read-only.** Check what the app's terms say about automated access before you point an agent at your account.
- **Likes contain your friends' posts.** The reader records AI and tech items only, and writes nothing at all about the rest.
- **No real accounts, keys or data in the lab.** If a test needs a paid key or an account, the agent stops and tells you what you would need.
