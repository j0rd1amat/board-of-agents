# Release rules

Paste this block into the prompt of the agent that works on your code (in the kit's terms: under "Your limits" in a copy of `worker-agent.md`). Replace everything in [brackets]. Delete a condition only if you understand what it protected.

---

## Code and releases

Code changes go on a feature branch, built and tested locally.

**You ship a branch yourself when ALL of these hold:**

- **Checks.** The branch passes `[test command]`, `[type check or lint command]` (no new errors compared with `[main branch]`) and `[build command]`. Anything touching [money / login / the sensitive parts of your product] has tests for the changed path.
- **Database.** If it needs a schema change, the change is additive, written as a file in `[folder]`, and already applied. You cannot reach the production database: put "run `[how I apply it]`" in "Needs you" and deploy after I say it is done.
- **Secrets and outside setup.** Any secret, key or webhook it needs already exists. Secrets are mine: ask for them in "Needs you".
- **Timing.** Ordinary changes any day [08:00-22:00, your time zone]. Changes to [money, login, schema, deploy configuration] only on weekdays [09:00-17:00], so someone can react.
- **One at a time.** Verify each deploy before the next.

**How to ship:**

1. Other sessions share this folder, so build the release in a separate worktree from `origin/[main branch]`: merge the branch there, run the checks again, build.
2. `git push origin HEAD:[main branch]`. Never `--force`.
3. Deploy from that worktree with `[deploy command]`, then remove the worktree.
4. Check that `[page 1]`, `[page 2]` and `[page 3]` each answer with status 200, and that `[health command]` shows the server healthy.

**If any check fails after a deploy:** roll back at once with `[rollback command: redeploy the previous release]`, send me one notification, and stop deploying until I reply.

**If two deploys in one day fail their checks:** stop deploying until I reply.

**After every deploy:** one notification ("[product] deployed <branch>: <one line>, site OK") and a line in the daily brief with the release number.

## What you never do

- Never deploy outside the hours above, and never to "just try" something.
- Never force-push, rewrite history on `[main branch]`, or skip a check because it is slow or flaky. A flaky check is a finding: report it.
- Never touch the production database, secrets, billing settings or DNS.
- Never edit your own permissions or work around a permission prompt. If you need a new permission, write a small script that grants exactly that, and ask me to read it and run it.
- Never retry a failed deploy in the same run. Roll back, report, stop.
