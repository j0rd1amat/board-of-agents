# Release checklist

The agent fills in one of these for every release and appends it to `releases.md`. You should be able to read the first line and stop.

---

**[date, time] · [branch] · shipped | rolled back | not shipped**

One line: what changed, in plain words.

| Check | Result |
|---|---|
| Tests (`[test command]`) | passed / failed: <which> |
| Type check, compared with main | no new errors / <count> new |
| Build | ok / failed |
| Touches money, login or schema? | no / yes: tests for the changed path are in <file> |
| Inside the allowed hours? | yes / no: waiting until <time> |
| Database change needed? | no / yes: applied by me on <date> |
| New secret or outside setup needed? | no / yes: asked in "Needs you" |

**After the deploy**

| Check | Result |
|---|---|
| `[page 1]` | 200 / <status> |
| `[page 2]` | 200 / <status> |
| `[page 3]` | 200 / <status> |
| Server health | healthy / <what it said> |
| Release number | <number> |

**If it was rolled back:** which check failed, the exact output, the release that is live now. Deploys are stopped until you reply.

**Needs you:** anything only you can do, one line each.
