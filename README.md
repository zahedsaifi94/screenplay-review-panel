# Screenplay Review Panel

A Claude skill that gives a screenwriter a full round of notes on a short film or feature screenplay, the way a good development process would: seven specialist readers review the script blind, argue out their disagreements, and one orchestrator walks the writer through the settled recommendations one point at a time. The script is never changed without the writer's approval.

It works for **shorts and features**. The craft rules are shared; the few places where the two formats genuinely differ (page proportions, what a short can't afford, how a feature is walked through) are handled by a format switch at intake.

## What it does

1. **Intake.** Asks what it doesn't know: format, length, where the script is headed, the writer's intent, choices the panel should never flag, reference scripts. Writes a logline with the writer and turns the intent into a one-sentence controlling idea. Nothing launches until the writer has seen and approved the briefs.
2. **Blind round.** Seven specialists read in parallel, each with its own craft guide and none of the writer's intent: Dialogue, Description, Formatting, Character, Structure, an Audience Reader (a first-time viewer), and a Programmer / Reader (a festival programmer for shorts, a competition coverage reader for features).
3. **Debate and tally.** Every disagreement goes into one shared file; all seven answer it; the orchestrator counts sides, notes who changed their mind, and rules in a fixed order (the writer's intent wins, then what's on the page, then the fix that solves more, then the smaller change).
4. **Compare readings.** What each specialist thinks the film is about, next to the writer's logline and intent: what's landing, what's too hidden, what's too stated.
5. **Walkthrough.** One point at a time, most important first: the current line, what the specialists think after debate, two or three options with exact replacement lines, the orchestrator's own take, and a question. Small undisputed fixes are grouped into one final point. Features are walked through in tiers (structure and character, then scenes, then lines) so a long script doesn't become sixty points.
6. **Apply and deliver.** Approved edits go in, the whole script is re-read for continuity, and the new version is saved as plain text and as a Fountain file that imports into Final Draft, Highland or WriterDuet.
7. **Later rounds.** An intent round (the same panel now sees what the writer meant) and a fresh cold read (a brand-new panel, blind) when the script is close to final.

Every decision the writer makes is logged in a per-project decisions file and never raised again.

## What's in the folder

```
SKILL.md                            the workflow the orchestrator follows (start here)
assets/
  specialist-brief.md               the brief filled in for each specialist
  decisions-file-template.md        the per-project decisions file
references/
  guides/                           one craft guide per specialist (seven files)
  structure-shorts.md               landmark table by page count; what a short can't afford
  structure-features.md             landmark map in percentages; sequences; tiered walkthrough
  scene-chart.md                    the per-scene table the Structure specialist fills in
  logline-and-premise.md            logline, controlling idea, intended effect (orchestrator only)
  glossary.md                       one name per concept across the craft books
scripts/
  txt_to_fountain.py                converts a plain-text script to Fountain
evals/                              tests for the skill (not needed to use it)
```

The orchestrator reads `SKILL.md` when the skill triggers and opens the other files only at the step that needs them. Each specialist sees only its own guide, the script, the writer's reference scripts, and the glossary.

## Where the craft rules come from

The guides draw on the standard screenwriting references (Field, McKee, Trottier, Snyder), two books on short-film writing (Bunn, Phillips), and published guidance from festival programmers and competition readers. The examples in the guides are invented to illustrate each principle; nothing is quoted from produced screenplays. Page targets and beat names are treated as diagnostics, not rules: a missing beat is a question for the writer, never a fault.

## Installing

**Option 1 — Ask your agent to install it for you (easiest, no Terminal or Finder needed):**

Open Google Antigravity (or Claude Code) and paste this into the chat:

> Install the skill from https://github.com/zahedsaifi94/screenplay-review-panel into my global skills folder (`~/.gemini/config/skills/screenplay-review-panel` for Antigravity, or `~/.claude/skills/screenplay-review-panel` for Claude Code).

**Option 2 — Manual install:**

- **Google Antigravity:** download the ZIP from GitHub (or clone the repo), rename the folder to `screenplay-review-panel`, and place it in `~/.gemini/config/skills/screenplay-review-panel/`.
- **Claude Code:** copy or clone this folder into `~/.claude/skills/screenplay-review-panel/`.
- **Claude app:** zip the folder (without `evals/`) as a `.skill` file and upload it under your skills.
- **Other agents** that support folder skills: point the skills directory at this folder, or symlink it there.

It needs subagents, to run the seven specialists in parallel. Python 3 for the Fountain converter.

## Using it

Open a chat and ask for notes on your script, for example:

> can you give me notes on my short? (attach the script)

or

> I've got a 95-page drama. Can the panel take a look before I enter it in competitions?

The skill triggers on requests for notes, critique, coverage, a cold read, or a festival or competition readiness check, and on logline or structure questions about a script. It will ask a few intake questions, show you the briefs, and then run the panel. Expect the blind round to take a while; the walkthrough is interactive.

**Reference scripts.** At intake it asks for three to seven screenplays close to your film's tone, from your own private copies, for study only. The specialists use them to ground taste judgments (what sounds human, what's funny, where a turn lands). Without them the panel relies on the guides and general film knowledge, and says so. Keep them in one folder (local or cloud) so later sessions can reach them.

**Honesty.** The seven specialists are one model with seven sets of instructions. Their agreement is one careful reader asked seven times, not seven readers; the skill says so every time it presents results, and ends every round by recommending a table read and human readers.

## Tests

Each folder in `evals/` is one test: a prompt, a sample script, and yes/no checks in `graders/`. They test the process (intake before launch, one point at a time, the format switch, respecting the decisions file, the shared debate file, Fountain delivery, declining a TV pilot), not the taste of the notes. Run them with Claude Code from this folder:

```
claude plugin eval . --allow-tools Write,Edit,Bash --scaffold
```

These are real, billed model runs.

## Scope

Shorts and features. TV pilots and series bibles are out of scope. The skill reviews a draft; it does not write or rewrite a script from scratch.

## Licence

MIT. See [LICENSE](LICENSE). Written by Zahed Al Saifi.
