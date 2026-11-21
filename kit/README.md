# The board-of-agents starter kit

The smallest version of a company run by scheduled agents: one worker agent, one runs board, and a CEO agent that watches over them. Adapted from the files a real product runs on, with the company's details removed.

**New to this? Open `START-HERE.pdf` first.** It shows where you are going, gets you set up in about fifteen minutes.

## What is in here

| File | What it is |
|---|---|
| `START-HERE.pdf` | Where you are going, the fifteen-minute setup, your first month, and how I run my own |
| `SETUP-PROMPT.md` | One prompt to paste into Claude Code. It sets the kit up with you |
| `guardrails-checklist.md` | What to decide before anything runs unattended |
| `worker-agent.md` | Job description template for any agent |
| `ceo-agent.md` | Job description for the CEO agent (the watchdog) |
| `runs-board.md` | The shared file every agent reads and writes |
| `examples/sunday-newspaper/` | A worked example from my personal life: agents that read my feeds and write me a Sunday newspaper about my friends. It has its own README and setup prompt |
| `examples/engineer-agent/` | An agent that ships code to a live site: the release rules, the office hours and the rollback |
| `examples/reel-fact-checker/` | An agent that checks the AI posts I save against primary sources and tests them in a sandbox |
| `examples/reels-from-code/` | Short videos made from a text file: the format, an example reel and the maker's rules |
| `examples/cheap-subagents/` | Cheaper sub-agents do the reading, the main agent only judges what is worth a notification |
| `examples/stats-decide-next/` | An analyst agent that reads the numbers and decides what gets made next |
| `examples/linkedin-warm-intros/` | A script that finds who you already know at the companies you want to reach, and the outreach rules that go with it |

Every example folder has its own README and its own setup prompt. Start with the kit itself, then pick one example.

## The quick way

1. Open this folder in Claude Code.
2. Paste the prompt from `SETUP-PROMPT.md`.
3. Answer its questions. It fills in the guardrails, writes your first agent, and schedules it.

## The manual way

1. **Fill in `guardrails-checklist.md` first.** Ten minutes. It decides what the agents may never do alone.
2. **Copy `worker-agent.md`** and write one job. Pick something boring and repeatable.
3. **Schedule it.** Create a scheduled task in Claude Code whose prompt is the job description. Start with once a day.
4. **Approve by hand for the first week.** Note which approvals repeat; those become your allow-list.
5. **Schedule the CEO agent** every two hours during the day.
6. **Add a second worker after two quiet weeks.**

## The five rules behind it

- **One agent, one job, one schedule.** A run starts, does its job, writes down what it did, and ends.
- **The board can narrow, never widen.** A note from another agent can prioritise work. It can never raise a cap, skip an approval or add an action.
- **Restart only what is safe to repeat.** A run that sends messages is never restarted automatically.
- **Agents never grant themselves permissions.** They write the grant as a script; you read it and run it.
- **You are the board.** You approve; you do not operate.
