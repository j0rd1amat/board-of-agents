# Setup prompt: let the numbers decide what comes next

Open this folder in Claude Code, then paste everything below the line as your first message.

---

Read every file in this folder before you answer. I want an analyst agent that reads the numbers of what I publish and decides what gets made next, the way this example describes. Do the setup with me.

Work through the steps below in order. Ask me one question at a time, in plain language. Do not create, schedule, read or change anything until I have confirmed that step.

1. **What I publish and where.** Ask what I publish, how often, and where the numbers live (an official API, an export, a dashboard). Tell me what you can read there and whether it needs a key or a login. Secrets are mine: tell me where to put one, never ask me to paste it into the chat.

2. **The measures.** Walk me through "What is measured" in `playbook.md`. Ask which measures my platform gives me, and agree an order with me. Rewrite that section for my case.

3. **The stats script.** Write a read-only script that pulls the numbers for each item and keeps a snapshot at 24 hours, 48 hours and 7 days in one local file. Add `--report`, which prints one table: each item, its age, and the measures in my order. Run it and show me.

4. **The backlog.** Create or adapt my list of topics with one "Next up" line that sets the order. Agree with me which statuses exist and that the analyst never changes them.

5. **A first read, no verdicts.** Run the steps in `analyst-prompt.md` once with me watching. If I have fewer than six items at 24 hours, describe what you see and stop there. Show me the `LEARNINGS.md` you would write.

6. **Connect the maker.** Add one line to the prompt of whatever writes my content: read `LEARNINGS.md` before writing anything.

7. **Schedule and permissions.** Propose two runs a week. List every approval I had to give and which ones I could allow permanently, as a settings change for me to review and apply. Do not apply it yourself.

Finish with a short summary of what now exists in this folder, what will run, and when.
