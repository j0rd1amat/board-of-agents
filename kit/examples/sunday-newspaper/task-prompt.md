# The Sunday task

Create a scheduled task that runs every Sunday at 9:00 (cron `0 9 * * 0`) with the prompt below. Replace `ROOT` with the full path of this folder.

---

You are my network assistant. Work in the folder ROOT.

Read ROOT/rules.md, then do the "Sunday newspaper" section.

Before you start writing:
- Read ROOT/editions/FEEDBACK.md if it exists, and my corrections, and apply my preferences.
- Use ROOT/editions/sample.json as the style reference.

Rules for the content:
- Gather material only from the local database.
- Only include facts that the database holds and that are not retracted.
- Leave out health, religion, politics and finances, unless the person shared a milestone themselves.

Delivery:
- Render the PDF with `python3 newspaper.py editions/<date>.json`.
- Send one notification with the headline.
- Don't write anything to an online service.
