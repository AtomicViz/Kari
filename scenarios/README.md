# Workplace Escalations: concepts 31-230

Two new sets of 100, each concept in three stages: **start**, **workplace disaster** and
**apocalypse with lime recovery**. The carnival stage has been removed.

| File | What it is |
|---|---|
| `set-a-workplace.md` | Set A catalogue (31-130): everyday agency and office friction |
| `set-b-movies.md` | Set B catalogue (131-230): 9-to-5 misery inspired by 90s and early-2000s films |
| `Set A Image Prompts.md`, `Set B Image Prompts.md` | Every full prompt, ready to copy and paste (6 per concept) |
| `prompts/NNN-slug.json` | Per-concept prompt records for batch generation |
| `concepts/batch-*.json` | Source of truth: the scene paragraphs for each concept |
| `concepts/SPEC.md` | Scene-writing rules and a worked example |
| `concepts/check.py` | Lints scenes for banned words, word counts and the lime rule |
| `build.py` | Rebuilds every output from the batches |

## How a prompt is built

`build.py` joins these parts in order:

1. Medium line (stage-specific)
2. **Concept scene** (90-140 words, unique to the concept and stage)
3. Composition for the aspect ratio and stage (native 16:9 or 9:16 layout)
4. Materials: paper, graphite, frosted acrylic, frosted glass, plus imperfections
5. Palette, with hex values and the single-lime rule
6. Lighting, lens and mood for the stage
7. Exclusions: no people, text, holograms, carnival and so on

Each full prompt is about 420-470 words. To change the house style everywhere, edit
the constants in `build.py` and rerun it. To change one scene, edit its batch file,
run `python3 concepts/check.py`, then run `python3 build.py`.

## Generation settings

Seedream 5.0 Pro (`seedream_v5_pro`) at `1.5k`, text-only with no reference images,
aspect ratio `16:9` or `9:16` as given in each record. That's 6 images per concept at
1.25 credits each: 7.5 credits per concept and 1,500 for all 200.

Suggested output layout, matching the original 30:
`NNN-slug/16x9/{start,end,apocalypse}.png` and `NNN-slug/9x16/...`.
Video pairs are now start → end, then end → apocalypse.
