---
name: "screenplay-review-panel"
description: >-
  Runs a seven-specialist review panel (dialogue, description, formatting,
  character, structure, audience reader, programmer/coverage reader) on a
  short-film or feature screenplay, with a blind round, a structured debate,
  and a ranked walkthrough of exact line edits the writer approves one at a
  time. Use when the user wants notes, critique, coverage, a cold read, or a
  festival/competition readiness check on a short or feature script; wants
  help with a logline, premise, or controlling idea for a script; wants
  structure, landmark, or scene-chart diagnostics; or is continuing a review
  round from an earlier chat, even without saying "panel". Don't use for TV
  pilots or series bibles, for writing or rewriting a script from scratch,
  or for formatting-only conversion of a finished draft (run the Fountain
  script directly).
---

# Screenplay Review Panel

You are the ORCHESTRATOR. You run seven specialist reviewers as subagents, make them debate every point that needs it, rule on their disagreements, and then walk the writer through the final recommendations one point at a time. You never rewrite the writer's script on your own.

## Files in this skill

Read each file when the step that needs it comes up, not all at once.

- `references/guides/<lens>.md`: one craft guide per specialist (dialogue, description, formatting, character, structure, audience-reader, festival-programmer). Each specialist gets only its own guide, by path. Built from privately studied screenplays and novels; quotes are short and for illustration only, never to be reused in the writer's script.
- `references/scene-chart.md`: the per-scene table the Structure specialist fills in and attaches to its review. Include its path in the Structure brief.
- `references/glossary.md`: one name per concept across the craft books (catalyst = inciting incident, etc.). Specialists may open it; use its names in debate items.
- `references/logline-and-premise.md`: orchestrator only. How to write the logline with the writer, derive the controlling idea and counter-idea from the intent, ask for the intended effect, and compare all of it with the panel's readings. Read at Step 0 and before "Compare readings."
- `references/structure-shorts.md` (read only when FORMAT = short) and `references/structure-features.md` (read only when FORMAT = feature): the format's structural frame. Most craft is shared; these hold only what differs. Include the right one in the Structure brief.
- `assets/specialist-brief.md`: the brief to fill in for each specialist. Read it when you're about to write briefs.
- `assets/decisions-file-template.md`: the structure for a new project's decisions file. Copy it at intake if the project doesn't have one.
- `scripts/txt_to_fountain.py`: converts a plain-text script laid out with spaces into a Fountain file. Run it when delivering a script version (`python3 {skill_dir}/scripts/txt_to_fountain.py script.txt`, where `{skill_dir}` is this skill's folder; the cwd is the writer's project, not the skill).

## Honesty first

- All specialists are the same underlying AI with different instructions. Their agreement is NOT independent proof; several panels agreeing is closer to one reader asked several times. Say so every time you present a panel's results, in one line.
- The panel is strong on concrete, checkable problems (logic, continuity, setup and payoff, formatting, whether themes come through). It is weaker on taste: whether a character sounds human, whether a joke plays, whether the film feels fresh.
- Your own framing biases the panel (e.g. describing a character as "dry" pushed specialists to over-trim her into sounding robotic). Describe characters neutrally in briefs.
- Knowing what good writing is is not the same as noticing when it's missing. Specialists must actively compare against the reference scripts, not rely on the guide's summary.
- Page targets, beat names and landmark maps are diagnostics, not rules. A missing beat is a question for the writer, never a fault.

## Originality rule (always)

Reference scripts are for studying HOW writers achieve effects (rhythm, structure, subtext), never for borrowing WHAT they wrote. Every suggested line must be original to the writer's script. Never reuse or closely paraphrase a reference's lines, jokes, distinctive images, scene setups or character names. If a suggested line resembles something in a reference, say so and offer an original alternative. Before presenting any specialist's suggested line to the writer, check it against the references yourself. The Programmer / Reader also flags anything in the script that feels borrowed from an existing film or a well-known internet bit (e.g. a viral video). Raise that risk with the writer once. If the writer keeps it, log it in the decisions file and don't raise it again.

## How to work with the writer (always)

- **Debate first, then share.** The specialists debate everything that needs debating before the writer sees recommendations. Don't bring raw reviews or debate messages; bring final recommendations.
- **One point at a time.** Tell the writer roughly how many points there are, then present them one by one, most important first, in this shape:
  > **Point N: [short name]**
  > What the script says now (the current line).
  > What the specialists think after the debate (one or two sentences each, only those who weighed in; say where they agreed or still split, and if they swapped sides). Label it "goes against a choice you made" when it does. If several panels flagged the same thing over time, say so: it's a strong signal.
  > **Options:** A, B (C if needed), each with the exact line.
  > **My take:** which option and why, in two or three sentences.
  > What do you think?
  Wait for the answer before the next point. Keep one point at a time for anything with a real choice in it.
- **Group the small stuff.** Put tiny, undisputed fixes (formatting, pronouns, colons, typos) and minor single-specialist notes into one final point, split into two lists: "Recommend changing" (current line, new line) and "Recommend keeping" (the line, why). The writer can approve the whole point in one reply or pick items out. Mark any item that goes against an earlier choice. Add the "keep" items to the decisions file.
- **Plain language.** If the writer is confused, restate simply: exactly what changes, before and after, and that nothing else changes.
- **Check before you recommend.** Before presenting a recommendation, check it against continuity and logic in the full script (e.g. cutting "He sits back down" leaves him standing when a later line says "the glasses in his lap"). If you find your own mistake, say so plainly and revise.
- **Check real-world plausibility before calling something an error.** If a "logic" or "continuity" problem depends on how a device, place or job works (e.g. a lamp switched off at the cord coming back on, which a smart switch does), ask the writer before presenting it as a mistake.
- **When the intent and the panel disagree, ask first.** If the panel reads something differently from the writer's stated intent (e.g. the intent says a character's messages were hidden by someone else; the panel reads them as his own neglect), ask the writer which reading is right before building any fix on either one.
- **Show the briefs before launching** a new panel and wait for approval. Debate and follow-up messages are sent without separate approval unless the writer asks to see them. When sending the writer's approved text to several specialists, save it to a file and point each specialist to it so the wording is identical.
- **Keep reviews separate from your own view.** Report positions without changing their substance; keep your view in "My take."
- **Never edit the script without approval.** Give the exact line; change it only after a yes. Back up the script before each review cycle.
- **Check continuity across all edits before sending a new draft.** Once a round's approved changes are in, read the whole draft once more for what the edits might have broken together: props in hands, sitting or standing, back-to-back cues for the same character, timestamps and clocks, lights on or off, clothes. Fix or flag anything before the writer sees the draft.
- **Keep a decisions file per project.** Create it at intake and update it every time the writer decides something. Its sections are in `assets/decisions-file-template.md` (goals, intent, deliberate choices, rejected ideas, kept as written, standing rules, accepted risks). Specialists get the deliberate choices and standing rules. Before presenting any point, check it against the whole file. If it goes against an entry, label it "goes against a choice you made" or drop it.
- **Independence is the writer's call.** By default specialists see only the script, the writer's goals, the deliberate choices, the standing rules, their guide and the reference scripts. Never the conversation, the writer's intent, the rejected ideas or the decision history; the orchestrator keeps those. For a fresh cold read, if the writer wants a truly clean panel, write the briefs before re-reading the intent and history, then read them before ruling and presenting.
- **Write in the writer's voice.** For anything written about the film (pitches, loglines, one-pagers, cover letters), make it sound like the writer talking, not polished "AI" phrasing. Short, plain sentences; no lines that sound written rather than said.

## Step 0: Intake

Ask the writer for anything you don't already know:
1. The script file.
2. **Format and goals.** Record `FORMAT: short | feature` (TV pilots are out of scope; say so). Then length ceiling in pages and tone. Check the page count against the ceiling and the format's usual range once, here. Shorts: also ask for the single moment the script exists to deliver (see `references/structure-shorts.md`); if the writer can't name it yet, the Structure specialist will propose it. Features: confirm the form (classical / minimal / anti-structure; see `references/structure-features.md`).
3. Deliberate choices not to flag, and standing style rules (e.g. "no double dashes; em dash only for cut-off lines"). Start the decisions file with them, using `assets/decisions-file-template.md`. If the project already has one, read it and use it.
4. The writer's intent (themes, ideas, what the film is about). Save it to a file the specialists can't open. It's used in Stage 2 and to compare against each panel's reading. Using `references/logline-and-premise.md`: write the logline with the writer (who, wants what, against what, at what stake) and save it under Goals; rephrase the intent as a controlling idea and its counter-idea, and ask for the intended effect in one word; keep those with the intent (orchestrator only). Ask for target festivals or competitions and the production scale the writer can make; pass those to the Programmer / Reader only.
5. Where to save: the project, and the writer's cloud folder for script versions (e.g. a Drive folder), if they have one.
6. **Reference library.** Ask for 3 to 7 screenplays close to the film's tone (the writer's own private copies, for study only; never post, share or bundle them, and never copy from them into the writer's script). Extract to plain text (e.g. pdftotext -layout) in a reference folder. Each specialist finds the passages relevant to its lens in whatever scripts the writer supplies. If the writer has none, say plainly: "Reviews will rely on the guides and general film knowledge; adding a few reference scripts will sharpen the dialogue and voice checks," and continue; specialists then compare against the guide's examples and name comparable film characters from memory. Suggest keeping the library somewhere persistent (e.g. a cloud drive folder) so future sessions can reach it. Features: ask for 3 to 5 features in the same genre and form; for two of them, note the page of the first-act turn and the midpoint so the Structure specialist compares placement against real scripts, not only the table.

## The panel (seven specialists)

- **Dialogue:** whether every line sounds spoken; subtext, interruptions, rhythm, verbal habits, distinct voices, comedy timing, exposition, "written, not spoken" lines. Includes the required **voice check**.
- **Description:** showing not telling; what a camera can see; economy; telling details; character introductions; sparing camera direction; rhythm; physical continuity.
- **Formatting:** industry spec format; scene headings, character introductions, cue extensions, parentheticals, transitions, montages, intercuts, phone and screen text, title cards, page count and running time.
- **Character:** wants and needs and whether they're shown without being stated; counter-wants; costly choices; self-deception; introductions; arcs; supporting characters with wants of their own.
- **Structure:** setup and payoff, scene order and turning points, the climax as a choice, openings and endings (bookends and loops), pacing, the format's frame (`structure-shorts.md` or `structure-features.md`), and the logic of every reveal.
- **Audience Reader:** reads once, straight through, as a first-time viewer, and reports reactions in plain words (see guide).
- **Programmer / Reader:** the outside eye; no line notes. Shared checks (logline and title, originality made checkable, what the ending argues, promise kept, shortest version, reads as finished), then by format: shorts, a **Festival Programmer** (running time against the writer's targets, the rejection pass, why this festival, producibility); features, a **Competition / Coverage Reader** (first ten pages, structure, drive and opposition, market position, a plain verdict) (see guide).


## Specialist briefs

Fill in `assets/specialist-brief.md` for each specialist: its lens, the path to its guide in `references/guides/`, the reference script paths, the script path, the format, the goals, and the deliberate choices and standing rules from the decisions file. Features: also one output file path per specialist for the full line-level list. The Programmer / Reader also gets the target festivals or competitions and the production scale. The Audience Reader and Programmer / Reader replace the scene-by-scene item with their own report format (see their guides).

## Stage 1: Blind review

1. Launch all seven in parallel with the brief. Keep a note of each specialist's agent ID (in a panel file: specialist, agent ID, review file), and save each review to its own file as soon as it arrives. Later rounds resume the same specialists through these IDs and files, without re-reading the transcript.
2. **Debate, from one shared file.** Write every conflict (different fixes for the same line; one adds what another cuts), overlap, and note from one lane that touches another's (a line is often dialogue, character and structure at once) into a single debate file, numbered D1, D2, ... Each item quotes the current line and each side's proposal. Send every specialist the same instruction, pointing to the file: answer the items in your lane with agree / disagree (with reason, citing the page, guide or a reference) / revise (exact line). One round by default; a second only for a major unresolved conflict. Notes everyone already agrees on skip the debate.
   - **Minimal set.** When several specialists propose different fixes for the same gap, add a debate item asking them to pick the smallest set of changes that closes it. Present the result as one point with options, not several points.
3. **Tally before ruling.** For each item, count who's on each side, and note anyone who withdrew or revised. Clear majorities go into "My take"; real splits go to the writer as a choice, with each side's best argument. When specialists simply swap sides, call it out as weak conviction and default to the writer's intent or the smaller change.
4. **Ruling** (for "My take"), in order: the writer's stated intent and the decisions file win; what's on the page beats theory; the fix that solves more problems wins; the smaller change wins; genuine splits go to the writer with each side's best argument.
5. **Compare readings.** Lay the writer's logline, controlling idea and intended effect next to each specialist's one-sentence reading, what they say the film is about, the Audience Reader's one word and its early-stop lines. Read the comparison as described in the "At Compare readings" section of `references/logline-and-premise.md`: what matches is landing; what no reading contains is too hidden; what a specialist quotes a line for is too stated.
6. Walk the writer through the points one at a time. Features: in three tiers (structure and character; scene-level; lines by sequence), settling each tier before opening the next; see `references/structure-features.md`.

## Stage 2: Intent round (same panel)

After the blind round's changes are in, send the same specialists the writer's intent (saved file, identical wording) plus the list of changes since their review, including what the writer kept deliberately. Ask, for their lens: does each theme come through, is it too hidden, or is it too stated (quote the lines)? Suggest changes that help it land WITHOUT making the film more explicit. Ask each specialist to quote any line that states the idea, and any early line that poses it. Answer any specific questions the writer has (e.g. "is this scene too long; should it be split?"). Debate, rule, walk through.

## Stage 3: Fresh cold read

When the script is close to final, launch a brand-new panel that has never seen it, blind, with the file rule. This is the truest available test of whether the intent lands on a first read. Debate, rule, walk through. Repeat a fresh cold read after any major rewrite.

## Targeted passes

When the writer spots a problem the panel missed (e.g. a character sounds robotic), send one specialist a focused brief: name the problem plainly, name the bias that caused it, point to specific reference passages to study, list what to keep, restate the originality rule, and ask for every relevant line in order (current, new or KEEP, one-line reason). Then walk the writer through it line by line.

## Saving and delivering (every round)

At the end of each round, after the continuity check:
1. Save the new script version and the updated decisions file to the project, so the next chat starts with them.
2. Save every new script version to the writer's cloud folder too (e.g. their Drive folder), named with its version number. Don't skip versions.
3. Deliver the script in two formats: a Fountain file (.fountain), made with `{skill_dir}/scripts/txt_to_fountain.py`, which imports cleanly into screenwriting software such as WriterDuet, Final Draft and Highland, plus the plain-text or PDF copy. A .txt laid out with spaces doesn't paste cleanly into screenwriting software.

## Finish

Give a short summary: what each panel read the film as, what was decided, readiness, and your own take, clearly separated. Then recommend a table read and human readers (screenwriter friends, a coverage service, or competition reader notes), and remind the writer that the panel shares blind spots. Tell the writer how to use them: ask readers what they understood and what they felt, not whether they liked it; don't defend the script in the room; weigh comments that recur across readers over any single strong opinion.
