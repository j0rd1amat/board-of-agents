# Guardrails checklist

Fill this in before any agent runs unattended. Agents read this file; treat it as the board's standing orders.

## 1. Approval gates

Things no agent may release without your approval:

- [ ] Public content (posts, videos, press pitches): ______
- [ ] Messages to people who have never heard from you: ______
- [ ] Anything that touches customer or personal data: ______

Make the gate real: the script that publishes should check an approvals file that only you (or a small review page) can write. A rule in a prompt is a request; a check in the script is a gate.

## 2. Money

- [ ] Agents never pay, upgrade a plan or start a trial. Purchases go to you with the item and the total.
- [ ] If an agent negotiates deals, it may agree only when all of these hold:

| Limit | Value |
|---|---|
| Maximum per deal | ______ |
| Maximum cost per thousand views (or your unit) | ______ |
| Monthly budget, all deals together | ______ |

- [ ] You make the payment yourself.

## 3. Volume caps

Start low and ramp. New sending domains and new accounts need a warm-up.

| Channel | Week 1 | Week 2 | Ceiling |
|---|---|---|---|
| ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ |

## 4. Stop rules

- [ ] Stop all sending and alert me if bounces pass ______ %.
- [ ] Stop and alert me if anyone complains or reports spam.
- [ ] Stop deploying after ______ failed deploys in one day.

## 5. Nothing sent twice

- [ ] Every send or post is recorded in a tracker as it happens, with a status per person or item.
- [ ] Every agent reads the tracker before acting.
- [ ] Runs that are safe to restart automatically (repeating cannot double up): ______
- [ ] Runs that are never restarted automatically (anything that sends messages): ______

## 6. Permissions

- [ ] Start with every action needing your approval.
- [ ] Build an allow-list of exact commands as approvals repeat.
- [ ] Keep a deny-list that always wins: deploys, secrets, force flags, pushing code, editing schedules.
- [ ] Agents never edit their own settings and never work around a refusal.
- [ ] When an agent needs a new permission, it writes a script that grants exactly that. You read it and run it.
- [ ] Review the allow-list once a month.

## 7. Never, whatever happens

- [ ] Enter passwords, card numbers or codes.
- [ ] Create accounts.
- [ ] Change DNS, billing, recovery settings or secrets.
- [ ] Put personal data (lead lists, exports) in version control.

## 8. Escalation

- [ ] What is worth a phone ping: ______
- [ ] One alert per issue. No repeats unless it gets worse.
- [ ] Everything else waits for the daily brief.
