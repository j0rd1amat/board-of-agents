# Proposal [P-number]: [title]

The agent writes this and the diff next to it. It applies nothing. You approve or reject.

| | |
|---|---|
| **Concept** | [which research note this comes from] |
| **Target file** | [full path of the one file it would change] |
| **Risk** | low / medium / high |

## Why

What is slow, costly, unreliable or missing today, in one or two sentences.

## Expected effect

What gets better, and how you would notice.

## How it was tested

The lab evidence (where it is, what it showed), or "not testable" and why.

## How to roll back

The backup that is taken before applying, and the one command that restores it.

## The change

See `[P-number].diff`: a diff against the current target file. If the diff changes after you approve it, the apply script refuses it.

---

Rules for the agent writing this: one target file per proposal. Small and reversible only. Prefer prompts and runbooks over code. Never propose anything that loosens a security, privacy or read-only rule.
