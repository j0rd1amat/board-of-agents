# Example: cheaper agents read, the main one judges

A worked example of the kit's pattern, applied to cost. Most of what a reading agent does is scrolling, not thinking. So the main agent does not read the sources itself. It starts one sub-agent on a cheaper model per source, one at a time, and keeps the one hard job for itself: deciding whether anything is worth telling you about.

Mine runs twice a day over four sources, and sends one notification at most per scan, or none.

## What is in this folder

| File | What it is |
|---|---|
| `SETUP-PROMPT.md` | Paste it into Claude Code. It builds your own version with you, one step at a time |
| `scan-prompt.md` | The prompt of the scheduled scan: one cheaper reader per source, then the main agent judges |
| `reader-rules.md` | The hard rules every reader gets, pasted in word for word |
| `notify-bar.md` | The written list of what is worth a notification. Everything else waits quietly |

## How it works

1. **One sub-agent per source.** The prompt says it in one line: use a cheaper sub-agent per source. The sources run one at a time.
2. **The same rules, word for word.** Every reader gets the same hard rules pasted in verbatim, not a summary. A summary is where a rule gets lost.
3. **Only what is new, in a fixed shape.** Each reader adds only what is new since the last scan and writes it back to its own file, with the same fields every time.
4. **Text before pictures.** To keep it cheap, a reader tries the page text first and takes a half-size screenshot only when there is no text to read.
5. **The main agent judges.** It looks only at what the run added and decides if anything clears the bar in `notify-bar.md`. If so, one notification under 200 characters. If not, silence.

## Before you build this

- **Split by kind of work, not by topic.** Reading and extracting into a fixed shape is cheap work. Deciding what matters is not. Put the model boundary there.
- **Readers get the least access of anything you run.** They read untrusted content all day. Mine may write to exactly one file each.
- **Readers never send data anywhere.** Once a reader of mine started a temporary server on my Mac and tried to send a contact list to it. It was blocked, and now a rule says readers never start servers, never send data anywhere, and write only to their own scan files.
- **Write the bar down.** If "worth a notification" lives in the model's judgment, you get pinged all day. Mine is a list.
- **Judge from the record, not from memory.** After the readers finish, the main agent asks the database what this run added. It does not rely on what the readers told it.
- **Read-only everywhere.** Readers never like, comment, follow or message anyone, and never post.
