# Setup prompt: cheaper readers, one judge

Open this folder in Claude Code, then paste everything below the line as your first message.

---

Read every file in this folder before you answer. I want a scheduled scan where cheaper sub-agents do the reading and the main agent only judges, the way this example describes. Do the setup with me.

Work through the steps below in order. Ask me one question at a time, in plain language. Do not create, schedule, read or change anything until I have confirmed that step.

1. **What the scan is for.** Ask what I want to keep an eye on, and what I would want to be told about straight away. Write my answers into `notify-bar.md` and show me.

2. **One source.** Ask which single source to start with. Recommend email if I have no preference. Tell me what you will be able to read there, what the other side might see, and what the service's terms say about automated access if you know. Let me decide.

3. **Rules.** Walk me through `reader-rules.md`, fill in the brackets with me, and ask whether I want to tighten anything.

4. **Models.** Tell me which models are available here, which one you suggest for the readers and which for the judging, and why. Let me choose.

5. **The record.** Create a small local database (SQLite) in this folder and two scripts: one that merges a scan file into it (safe to run twice), and one that answers "what did the last run add".

6. **One scan, with me watching.** Start one reader as a sub-agent on the cheaper model, with the rules pasted in verbatim and access to its own scan file only. Show me every item it would save, each with its quote, before anything is merged. Then judge the result against `notify-bar.md` and tell me whether you would have notified me, and why.

7. **Fill in `scan-prompt.md`** with the one source. Tell me the rough cost of this scan compared with running it all on the main model, if you can measure it.

8. **Schedule and permissions.** Propose a schedule. List every approval I had to give and which ones I could allow permanently, as a settings change for me to review and apply. Do not apply it yourself.

Finish with a short summary of what now exists in this folder, what will run, and when. Remind me to add a second source only after a clean week.
