# Example: an agent that ships code to your live site

A worked example of the kit's pattern, applied to releases. An agent works on a branch, runs the checks, deploys, and then checks its own work. If a check fails after a deploy, it puts the previous release back, tells you, and stops deploying until you reply.

The agent is not the interesting part. The conditions are: when it may ship, what it can never touch, and what it does when something breaks.

## What is in this folder

| File | What it is |
|---|---|
| `SETUP-PROMPT.md` | Paste it into Claude Code, in your project. It fills in the release rules with you, one step at a time |
| `release-rules.md` | The block that goes into your agent's prompt: the conditions for shipping, the office hours, the rollback |
| `release-checklist.md` | What the agent writes down for every release, so you can read one line and know what happened |

## How it works

1. **Every change starts on its own branch.** It is built and tested on your machine before anything else happens.
2. **Three checks must pass:** the tests, the type check (no new errors compared with the main branch) and the build. A change that touches money or login also needs tests for the exact path that changed.
3. **The release is built in a separate copy of the code.** Other sessions may be working in the same folder, so the agent merges, tests and builds in its own copy, pushes to the main branch without ever forcing, deploys, and removes the copy.
4. **Then it checks its own work.** It opens a short list of pages and checks that each one answers and that the server is healthy. Each deploy is verified before the next one.
5. **If a check fails, it rolls back.** It redeploys the previous release at once, sends you a notification, and stops deploying until you reply.

## Before you build this

- **Start with "prepare, do not deploy".** For the first two weeks, let the agent do steps 1 to 3 and stop. You deploy. Give it the deploy step only after you have read a dozen of its release notes and agreed with all of them.
- **Keep the database and the secrets yours.** My agent cannot reach the production database. If a release needs a database change or a new secret, it asks me and deploys after I say it is done.
- **Give it office hours.** Mine ships ordinary changes between 08:00 and 22:00, and anything touching money, login or the database only on weekdays, nine to five, so someone can react.
- **Write the rollback before the first deploy.** The agent needs the exact command that puts the previous release back, and you need to have run it once by hand.
- **Two failures and it stops.** If two deploys in one day fail their checks, it stops deploying until you reply.
- **It needs tests to lean on.** With no tests, "the checks passed" means nothing. Start by having the agent write tests, not ship code.
