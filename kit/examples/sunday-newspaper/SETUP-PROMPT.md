# Setup prompt: your own Sunday newspaper

Open this folder in Claude Code, then paste everything below the line as your first message.

---

Read every file in this folder before you answer. I want my own Sunday newspaper about the people I know, built the way this example describes. Do the setup with me.

Work through the steps below in order. Ask me one question at a time, in plain language. Do not create, schedule, read or change anything until I have confirmed that step.

1. **Sources.** Ask which single source I want to start with. Recommend email if I have no preference. Tell me what you will be able to read there, what the other person might see (for example, a view on a story), and what the app's terms say about automated access if you know. Let me decide.

2. **Rules.** Walk me through `rules.md` and ask whether I want to tighten anything: topics to leave out, people or groups to never read, a cap on pages per run.

3. **The database.** Create `facts.db` (SQLite) in this folder, with tables for people, facts (text, quote, speaker, chat, date, status, confidence), events, incidents and corrections. Write a small `query.py` so later runs never need raw SQL: recent facts, upcoming events, incidents, corrections, and the people I have not talked to for longest.

4. **One scan, with me watching.** Run a read-only scan of my one source now, following `rules.md`. Show me every fact you would save, each with its quote, before you save anything. Let me delete the ones I don't want.

5. **A first edition.** Write an edition from what the database holds, print it with `newspaper.py`, and show me the PDF. Ask me what to change, and save my answers to `editions/FEEDBACK.md`.

6. **Schedule.** Propose a daily scan and the Sunday task from `task-prompt.md`. Create the scheduled tasks if you are able to in this environment. If you are not, tell me exactly what to click or type.

7. **Permissions.** List every approval I had to give during steps 4 and 5, and tell me which ones I could allow permanently. Write that as a settings change for me to review and apply. Do not apply it yourself.

Finish with a short summary of what now exists in this folder, what will run, and when.
