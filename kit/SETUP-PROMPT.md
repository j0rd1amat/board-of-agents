# Setup prompt

Open this folder in Claude Code, then paste everything below the line as your first message.

---

Read every file in this folder before you answer. I want to set up my first scheduled agent using this kit, and I want you to do the setup with me.

Work through the steps below in order. Ask me one question at a time, in plain language. Do not create, schedule, send or change anything until I have confirmed that step.

1. **Guardrails.** Interview me to fill in `guardrails-checklist.md`. For each section, explain in one sentence why it matters, suggest a cautious default, and write down my answer. If I am unsure, pick the stricter option.

2. **One job.** Help me choose a single boring, repeatable job for my first agent. Suggest three candidates based on what I tell you about my work, and steer me away from anything that sends messages to strangers or spends money. Then write its job description as `agents/<name>.md`, starting from `worker-agent.md`.

3. **The board.** Create my `runs-board.md` from the template, with this agent's id in it. Keep the rules at the top exactly as they are.

4. **A tracker.** If the job sends, posts or changes things, create the tracker file the agent will check before acting, so nothing is done twice.

5. **Schedule.** Propose a schedule, starting at once a day. Create the scheduled task for me if you are able to in this environment. If you are not, tell me exactly what to click or type to create it myself.

6. **First run, with me watching.** Run the agent once now. Afterwards, list every approval I had to give and tell me which ones I should allow permanently. Write that as a settings change for me to review and apply. Do not apply it yourself.

7. **What happens next.** Tell me what to look at after the first week, and when to add the CEO agent from `ceo-agent.md`.

Finish with a short summary of what now exists in this folder and what will run, and when.
