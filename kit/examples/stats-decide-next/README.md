# Example: the numbers decide what gets made next

A worked example of the kit's pattern, applied to content. One agent makes a lot of reels. Another reads their numbers. Twice a week it looks at every reel that has been out for a day, gives each one a verdict, writes down what it learned in one short file, and moves the topics that look like the winners to the top of the list. The agent that makes the reels reads that file before it writes anything.

It works for anything you publish in volume: reels, posts, emails, ads.

## What is in this folder

| File | What it is |
|---|---|
| `SETUP-PROMPT.md` | Paste it into Claude Code. It builds your own version with you, one step at a time |
| `analyst-prompt.md` | The prompt of the scheduled analyst: when it judges, in what order, and what it may change |
| `playbook.md` | The method: what is measured, when the numbers are read, and what each verdict means |
| `LEARNINGS.md` | The lessons file, as an empty template with the fixed headings |

## How it works

1. **Only reels that are a day old.** It judges a reel at 24 hours. On my first trial reels the numbers hardly moved after that.
2. **A fixed order.** First the 3-second hold, then how much of the reel was watched, then views, then shares and saves. Shares and saves win the moment a reel has any.
3. **One verdict per reel:** double down, keep or kill, with the reason written down. Reels are compared with each other, never with benchmarks from the internet.
4. **Lessons and the next list.** It rewrites one short lessons file with five hooks to try next, and moves the topics that look like the winners to the top of the list.
5. **The maker reads it first.** The agent that writes and renders the reels reads the lessons file before every run.

Mine runs on Monday and Thursday morning, waits for six reels with a full day of numbers before it gives any verdict, and keeps the lessons file under 60 lines.

What is not in this folder: the script that pulls the numbers. It depends on where you publish and how you are logged in, so `SETUP-PROMPT.md` has Claude Code write it with you.

## Before you build this

- **Too few numbers, no verdicts.** With fewer than six reels at 24 hours the analyst only describes what it sees. Two reels that look alike are a hint, not a rule, and it has to say how sure it is.
- **It can reorder, never allow.** It changes the order of the list, never which topics are allowed. It never approves anything.
- **Rewrite, do not append.** A lessons file that only grows stops being read. Mine is rewritten each time and capped.
- **Pick the order of your measures on purpose, and change it when the data says so.** My first ten trial reels had no shares at all, so shares could not rank anything, and the 3-second hold took the lead.
- **Structures, not copies.** The analyst may search the web for hook formats. It takes the structure only, never another creator's wording or footage.
- **Quiet unless there is something to do.** It notifies you only when you need to act.
