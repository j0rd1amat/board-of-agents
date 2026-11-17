# Setup prompt: your own reel maker

Open this folder in Claude Code, then paste everything below the line as your first message.

---

Read every file in this folder before you answer. I want to make short vertical videos from text files, the way this example describes. Do the setup with me.

Work through the steps below in order. Ask me one question at a time, in plain language. Do not install, download or create anything until I have confirmed that step.

1. **What I have.** Check what is installed (Node, Python, ffmpeg, a browser) and tell me what is missing and how big each download is. Tell me the licence of each tool you propose and whether it fits my case (a person, or a company and its size). Let me decide.

2. **The look.** Ask me for my colours, a font and my name or logo. Build a 1080 by 1920 composition with two scenes only: `hook` and `steps`. Render one still of each and show me.

3. **The check.** Write the `check` command from `reel-format.md`: structure, beat count, word count, hook length. Create an empty blocked-words file and ask me what goes in it.

4. **The voice.** Propose a text-to-speech engine that runs on this machine and let me hear two voices saying the same line. Write the `voice` command: one line at a time, cached so that only changed lines are recorded again. Then add the listening check: transcribe every line and print the ones heard differently from what was written.

5. **The stills.** Write the `stills` command: one still per beat and one contact sheet. Run it on `example-reel.json` with the two scenes we have (skip beats whose scene does not exist yet) and show me the sheet.

6. **The render.** Write the `render` command, with loudness set to -14 LUFS. Render the two-scene version and show me the video.

7. **More scenes.** Ask me which of the remaining seven scenes I want next. Build one at a time, each with a still for me to approve.

8. **The review queue.** Create a queue file where every rendered reel waits with its caption and a status (`review`, `approved`, `rejected`), and a page where I can watch them. Nothing in this setup posts anywhere.

Finish with a short summary of what now exists in this folder and the four commands I can run.
