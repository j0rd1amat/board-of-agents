# Example: reels made from a text file

A worked example of the kit's pattern, applied to video. Nobody films or records anything. Each reel is a small text file: a list of beats, each with a line to say and a scene to show. Four commands turn that file into a video, with a check after each one for the script, the voice and the picture. Nothing is posted until you have watched it and said yes.

## What is in this folder

| File | What it is |
|---|---|
| `SETUP-PROMPT.md` | Paste it into Claude Code. It builds your own reel maker with you, one step at a time |
| `reel-format.md` | The format of a reel file, the nine kinds of scene, and the limits the check enforces |
| `example-reel.json` | A complete reel in that format. It is a sample: the agent it describes, and every person and figure in it, is invented |
| `maker-rules.md` | The block that goes into the prompt of the agent that writes reels: the four commands and when to throw a reel away |

## How it works

The four commands are `check`, `voice`, `stills` and `render`.

1. **The reel is written as a text file.** Six to nine beats and 60 to 110 spoken words, which comes to 25 to 40 seconds.
2. **`check` reads the script first.** It refuses a file with the wrong structure or length, and it runs a list of blocked words. One hit means the script is rewritten.
3. **`voice` generates each line, then listens to it.** The voice is made on your own machine, one line at a time. Speech recognition transcribes every line and flags the ones it heard differently. A bad line is taken again, and after two bad takes it is reworded.
4. **`stills` makes one picture per beat, on one sheet.** Before rendering, the sheet is checked for cut-off text, empty scenes and anything too small to read on a phone.
5. **`render` makes the video.** It also sets the loudness to the level Instagram uses.

What is not in this folder: the renderer, the voice model and the scene components themselves. Mine are tied to my own look and my own machine, so `SETUP-PROMPT.md` has Claude Code build yours with you.

## What mine is built with

All of it is free and runs offline.

- **Picture:** Remotion, which renders video from React components. It is free for individuals and for companies of up to three people; check its licence for your case.
- **Voice:** Chatterbox (MIT licence), running locally. About five seconds per line.
- **Listening check:** Whisper, running locally.
- **Music:** generated from scratch by a small script, so there is nothing to license.
- **Footage, when a reel has any:** free-licence stock only, with the source and licence of each clip written to a file.

## Before you build this

- **Start with one scene type.** A hook and a numbered list are enough for a first reel. Add a scene when you have a line that needs it.
- **The hook is on screen from the first frame.** No logo intro.
- **Look at the stills sheet every time.** Most problems (cut-off text, an empty scene, something too small for a phone) are visible there, and stills take seconds where a render takes minutes.
- **Throw weak reels away.** If one still looks wrong after two rounds of fixes, drop it. Reviewing a weak reel costs you more than making a new one costs the agent.
- **Say what is invented.** Mine are true about my own setup and invented about everyone else, and the end card says so.
- **Nothing posts without you.** A rendered reel waits in a review queue. Only your own yes moves it on.
