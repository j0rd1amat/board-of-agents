# Setup prompt: an agent that ships your code

Open your project in Claude Code, copy this folder into it, then paste everything below the line as your first message.

---

Read every file in this folder before you answer. I want an agent that can release my code under written conditions, the way this example describes. Do the setup with me.

Work through the steps below in order. Ask me one question at a time, in plain language. Do not deploy, push, schedule or change anything until I have confirmed that step.

1. **How this project ships today.** Read the repository (package scripts, CI files, deploy configuration, README) and tell me what you found: the test command, the type check or lint, the build, the main branch, how a deploy happens, and how a rollback would happen. Ask me to correct anything you got wrong.

2. **What is sensitive.** Ask me which parts of the product need extra care (money, login, personal data, the database schema, deploy configuration). List the folders and files you think they map to and let me adjust.

3. **Fill in `release-rules.md`.** Replace every bracket with what we agreed. Propose office hours and let me change them. Show me the finished file.

4. **The rollback, by hand.** Write the exact rollback command and walk me through running it once myself against the current release, so we both know it works. Do not run it for me.

5. **A dry run.** Pick a small, safe change (or ask me for one). Do everything in "How to ship" up to, but not including, the push. Fill in `release-checklist.md` for it and show me.

6. **Prepare-only mode.** Add the release rules to my agent's prompt with the push and deploy steps replaced by "stop and tell me the release is ready". Tell me how many clean releases you suggest before I hand over the deploy step.

7. **Permissions.** List every approval I had to give during steps 4 and 5, and which ones I could allow permanently. Write that as a settings change for me to review and apply. Do not apply it yourself.

Finish with a short summary of what now exists, what the agent may do alone, and what still needs me.
