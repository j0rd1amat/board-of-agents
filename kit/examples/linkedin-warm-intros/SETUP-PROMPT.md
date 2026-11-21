# Setup prompt: who you already know at the companies you want to reach

Open this folder in Claude Code, then paste everything below the line as your first message.

---

Read every file in this folder before you answer. I want to find who I already know at the companies I want to reach, built the way this example describes. Do the setup with me.

Work through the steps below in order. Ask me one question at a time, in plain language. Do not create, send, schedule or change anything until I have confirmed that step.

1. **The connections file.** Ask whether I have `Connections.csv` from LinkedIn's data archive. If not, tell me the three steps to request it and wait. Never ask me to upload it anywhere: it stays in this folder.

2. **The list of companies.** Ask what I want to reach companies for (sales, a job, investors) and help me write `companies.csv` with one column, `company`. If I want scores, agree the criteria with me first, score only from facts I give you or public pages, and give an unknown fact zero.

3. **Never-contact.** Ask which companies must never appear (my employer, clients I may not approach) and write `never.txt`.

4. **The buyer.** Ask which job titles count as the buyer for me and change the `BUYER` line in `match.mjs` to match. Show me the line before you save it.

5. **One match, with me watching.** Run `node match.mjs Connections.csv companies.csv`. Show me the summary and the first ten rows, and ask whether any match looks wrong.

6. **Pick and draft.** Ask me to pick up to five people. For each, ask how I know them, then draft one short message using `prompt.md`. Show me every draft. Send nothing: I send them myself.

Stop here and suggest I work like this for two weeks. When I come back and ask for the next part:

7. **Rules.** Walk me through `rules.md`, fill in the brackets with me, and ask whether I want to tighten anything.

8. **The second domain.** Explain what I need before any cold email: a second domain, a mailbox on it, its SPF, DKIM and DMARC records, and a warm-up period. Check the records with me. Tell me to check the rules on cold email where I and my recipients live; do not tell me whether it is allowed.

9. **Schedule and permissions.** Only if I ask for it: propose a daily task that follows `rules.md`. List every approval I had to give and which ones I could allow permanently, as a settings change for me to review and apply. Do not apply it yourself.

Finish with a short summary of what now exists in this folder, what will run, and when.
