# Setup prompt: your own AI radar

Open this folder in Claude Code, then paste everything below the line as your first message.

---

Read every file in this folder before you answer. I want an agent that checks the AI posts I save, built the way this example describes. Do the setup with me.

Work through the steps below in order. Ask me one question at a time, in plain language. Do not create, schedule, read or change anything until I have confirmed that step.

1. **Where I save things.** Ask which app I save AI posts in and which lists to read (saved, liked, sent to myself). Tell me what you will be able to read there and what the app's terms say about automated access if you know. Let me decide.

2. **Rules.** Walk me through `rules.md`, fill in the brackets with me, and ask whether I want to tighten anything.

3. **The record.** Create a small local database (SQLite) in this folder for items, concepts, experiments, proposals and incidents, with a `query.py` so later runs never need raw SQL: new items, known addresses, pending proposals.

4. **One read, with me watching.** Do one read-only pass of one list now, following `rules.md`. Show me every item you would save before you save anything.

5. **One research note.** Pick the most interesting item with me and write its note from `research-note.md`. Show me which sources you used and which links you refused to open.

Stop here and suggest I run it like this for a week. When I come back and ask for the next part:

6. **The sandbox.** Write `lab/sandbox.sh` for my operating system: it runs a command so that it can only write inside `lab/<name>/`, cannot read my keys, browser profiles, agent settings or other projects, and starts with an empty environment. Show me the script and prove each limit with a test that tries to break it.

7. **Proposals.** Ask me which automations may be read as targets. Write the apply script: it checks the diff is unchanged since I approved it, checks the target is on the allowed list, takes a backup, applies, and logs. Test it on a copy.

8. **Schedule and permissions.** Propose the daily task from `task-prompt.md`. List every approval I had to give and which ones I could allow permanently, as a settings change for me to review and apply. Do not apply it yourself.

Finish with a short summary of what now exists in this folder, what will run, and when.
