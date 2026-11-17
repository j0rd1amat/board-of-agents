# The reel file

One reel is one JSON file. The `check` command refuses a file that breaks any limit below.

```json
{
  "id": "R1a",
  "topic": "<which use case this reel is about>",
  "look": "animation",
  "beats": [
    { "key": "hook", "say": "<spoken line>", "scene": "hook", "text": "<the big line on screen>" },
    { "key": "b1",   "say": "<spoken line>", "scene": "<scene>", "...": "the scene's own fields" },
    { "key": "end",  "say": "<spoken line>", "scene": "end", "line": "<end card line>" }
  ]
}
```

## Limits

- 6 to 9 beats. The first is `hook`, the last is `end`.
- 60 to 110 spoken words in all. That comes to 25 to 40 seconds.
- The hook text is under 70 characters and is on screen from frame 0.
- No word from your blocked-words file anywhere in the file.
- Every person, message and figure about someone else is invented.

## Text marks

- `*word*` sets the word in the accent colour, in `text` and `title`.
- `|` forces a line break at that point.
- `at` on an item is a spoken word. The item comes in when that word is said. Tie items to early words: an item tied to the last word of a line appears too late to read.

## The nine scenes

| Scene | Fields | What it shows |
|---|---|---|
| `hook` | `text` | The big line, from frame 0 |
| `cards` | `title?`, `items` (2 to 4) of `{icon, h, p?, at?}` | Cards that pop in |
| `steps` | `title?`, `items` (2 to 5) of `{h, p?, at?}` | A numbered list |
| `record` | `title?`, `rows` (5 at most) of `[key, value]`, `hot?` | A data record. `hot` names the row to highlight |
| `terminal` | `title?`, `lines` (8 at most) of `{t, text, at?}` | A terminal. `t` is `cmd`, `text` or `hl` (highlighted) |
| `stat` | `title?`, `n`, `label` | One huge number and what it is |
| `strike` | `title?`, `items` (1 to 4) of `{h, at?}`, `lock?` | Things crossed out, then one line with a lock |
| `quote` | `title?`, `kicker`, `headline` | A newspaper clipping |
| `end` | `line` | The end card: your name, where to go, and the made-up note |

Any beat may also have `tag`: a small label in the top left corner.

## What each command checks

| Command | What it does | What stops it |
|---|---|---|
| `check <id>` | Reads the file | Wrong structure, wrong length, a blocked word |
| `voice <id>` | Records the lines whose text changed, then prints what speech recognition heard | A line heard differently from what was written: take it again, and after two bad takes reword it |
| `stills <id>` | One still per beat and one contact sheet | Nothing stops it. **Look at the sheet**: cut-off text, overlaps, empty scenes, anything too small for a phone |
| `render <id>` | The video, with loudness set to -14 LUFS | A missing voice line or still |
