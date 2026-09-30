# Scene-writing spec (Kari Tech escalations, 3 stages)

Stages: **start → end (workplace disaster) → apocalypse**. There is no carnival stage.

Each scene is a single paragraph of **90–140 words** describing what the camera sees.
Shared style, lighting, lens and aspect-ratio text are added later by `build.py`, so
**do not** repeat generic style boilerplate. Spend every word on this concept's specifics.

## Every scene must specify
1. **Hero object**: what it is, rough real-world size, construction and parts.
2. **Materials per object**, from the brand set only: ivory paper/card (fibre, folds,
   deckled or crisp edges), matte or brushed graphite metal (machining marks,
   chamfers, fasteners), frosted acrylic (milky edges, soft internal glow),
   sandblasted frosted glass. Pale neutral tabletop.
3. **Layout**: where things sit in the frame (foreground, midground, background,
   left, right) and how they relate spatially, so the workflow is readable.
4. **Exactly one acid-lime element** per scene (two at most in the apocalypse,
   where the second is the recovery rig), named precisely: which part and why it matters.
5. **Physical cause and state**: what is moving or stuck, frozen mid-motion (airborne
   paper, sliding objects, dust), with traceable direction back to the source.
6. **Texture details** that sell the miniature: dust, grain, creases, scuffs, fibres.

## Stage rules
- **start**: calm and orderly, everything aligned. The single annoyance is visible
  but small. Tabletop scale, 3 to 6 objects.
- **end**: the same objects and layout, now mid-disaster. Show a chain reaction whose
  path can be traced back to the start object. Name what has fallen, piled, jammed,
  spilled or multiplied, and where. Freeze the motion.
- **apocalypse**: a wide miniature landscape long after the collapse. The start objects
  are now enormous, weathered ruins (snapped, half-buried, bleached, cracked), hard to
  identify at first but still there. The disorder is embedded in the terrain
  (dunes of paper, drifts of cards, sediment of forms). Give a horizon or depth cue.
  **Lime recovery**: slim, non-humanoid graphite machines with lime components
  (cranes, conveyors, survey stakes, rails, sorting rigs) are beginning to rebuild
  or reconnect *one specific thing*.

## Hard rules
- No people, faces, hands, silhouettes or figures. Show absent people through what
  they left behind (a jacket on a chair, a cold mug, a half-packed box).
- No readable text, letters, numbers, clock digits, logos or UI. Write "blank label",
  "unmarked tab" and "plain dial with tick marks" instead.
- No floating holograms, screens full of UI, robots with faces, or dense cable tangles.
- Set B: never name the film, characters, quotes or iconic prop designs. Evoke the
  situation generically.
- No carnival or circus imagery at any stage.
- Plain, concrete language, as used in product photography briefs. Don't use "magical",
  "surreal", "epic" or "chaos ensues".
- You may strengthen a weak idea (a better hero object or a clearer chain reaction)
  but keep its id, title and core annoyance.

## Output format (JSON array)
```json
[{"id": 31, "title": "...", "category": "..." /* or "inspired_by": "..." */,
  "hero": "one short phrase naming the focal object",
  "start": "...", "end": "...", "apocalypse": "..."}]
```

## Worked example (id 31)
```json
{"id": 31, "title": "Meeting overrun hourglass", "category": "Meetings & calendar",
 "hero": "graphite-framed hourglass",
 "start": "A single hourglass about the height of a coffee cup stands at the centre of a pale neutral tabletop. Its frame is matte graphite metal with four slim turned pillars and chamfered end caps. The bulbs are sandblasted-frosted at the rims and clear in the middle. The upper bulb holds fine ivory sand, and a thin band of acid-lime sand marks one booked hour that is just about to run through. To the right, five ivory paper calendar blocks stand upright on a slim graphite rail, evenly spaced like dominoes waiting their turn, each a thick folded card with a crisp spine and blank face. The falling thread of sand is sharp and fine, and a faint dust of grains rests on the base plate. Everything is orderly, quiet and precisely aligned.",
 "end": "The same graphite hourglass now leans forward on its base with the lower bulb overflowing. Pale ivory sand pours in a continuous stream over the base plate and spreads across the tabletop in a soft rippled drift. The lime band has long since run through and lies buried under ivory sand in the lower bulb. The drift has reached the calendar rail: the first two blocks are half buried and leaning, the third is being shoved sideways and creasing at its spine, and the last is caught mid-fall off the table edge with a fine curtain of sand pouring after it. Airborne grains catch the light, a thin haze of dust hangs over the drift, and ripples in the sand run straight back to the hourglass.",
 "apocalypse": "A vast miniature desert of pale ivory sand dunes rolls to a hazy horizon, seen from a low, wide viewpoint. Half buried in the nearest dune lies the building-sized fallen frame of a graphite hourglass. One pillar is snapped, and the frosted bulbs are cracked and packed with sand. Around it, the tops of ivory calendar blocks jut from the dunes like weathered monoliths, tilted and broken, their spines bleached and frayed. Wind ripples cross the sand. In the middle distance, a slim graphite sieve conveyor with lime-painted buckets climbs one dune, lifting sand into a rotating frosted drum and dropping small recovered lime tokens into a neat tray. A second graphite rig stakes a taut lime survey line from the drum back to the fallen frame."}
```
