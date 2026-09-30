# Kling 3.0 video prompt spec (15 s, 9:16, 720p, sound on)

Each video starts from the concept's generated 9:16 start frame (`start_image`).
There's no end frame, so the video is free to travel. The goal is to compress the
whole three-stage arc into one 15-second, three-shot mini film.

## Structure (use these exact shot labels)
```
Shot 1 (0-4s): ...   the start frame comes alive: calm, precise, one small tell
Shot 2 (4-10s): ...  the workplace disaster: a physical chain reaction, traceable to the source
Shot 3 (10-15s): ... scale reveal: the camera pulls far back or cranes up to show the ruined
                     miniature landscape; a slim lime recovery rig starts rebuilding one thing
Sound: ...           one line of foley and ambience. No voices, no dialogue, no lyrics, no music with words.
Style: ...           one line (see below)
```

## Rules
- **Length:** 170–260 words and under 2,000 characters per prompt.
- **Shot 1** opens on exactly the composition of the supplied image: same objects,
  same light, same framing. The first second is a near-still.
- **Every concept gets a creative device of its own**, woven into its shots. Examples:
  - a rack focus from the lime element to the chaos;
  - a match cut where one object's motion continues into the next shot;
  - a speed ramp into slow motion at the moment of collapse;
  - a timelapse of light;
  - a single held note in the sound that snaps;
  - a camera that orbits;
  - a dolly-zoom as the scale changes;
  - the lime element being the last thing moving.
  Don't reuse the same device across more than 3 of your 25.
- **Motion has physical causes:** paper slides, drifts, flutters and piles; metal
  tips, rolls and clacks; frosted acrylic slides and cracks. No morphing, melting or
  objects appearing from nowhere. In shot 3, objects are the same kinds of things,
  only enormous and weathered.
- **Lime:** only the concept's named lime element and the recovery rig are lime. The
  lime element should be traceable across all three shots.
- **Never** people, hands, faces, silhouettes or figures; readable text, letters, numbers
  or logos; holograms; robots with faces; fire or explosions (a spark is fine); or
  carnival or circus imagery. Set B: no film names, characters or quotes.
- **Style line (end every prompt with this, verbatim):**
  `Style: photoreal handcrafted miniature diorama, ivory paper, matte graphite metal, frosted acrylic and glass, soft upper-left daylight, shallow depth of field, restrained palette with acid-lime #D0F344 accents only, no text, no people, smooth controlled camera.`

## Output
JSON array `[{"id": N, "title": "...", "device": "short name of the creative device", "prompt": "..."}]`

## Example (id 31, Meeting overrun hourglass)
Shot 1 (0-4s): Hold on the graphite hourglass and the row of ivory calendar blocks exactly as framed. A fine thread of ivory sand falls; the last grains of the acid-lime band slip through the neck. Dust motes drift in the upper-left light. A slow push-in begins.
Shot 2 (4-10s): The sand does not stop. Speed ramp: the lower bulb overfills and ivory sand pours over the base plate in a soft rippling drift that slides right, nudging the first calendar block. The blocks tip one after another like dominoes, spines creasing, the last one falling off the table edge in slow motion with a curtain of sand pouring after it. The camera tracks the drift at table height.
Shot 3 (10-15s): Match cut on the falling sand. The camera cranes up and back, revealing that the sand is now a vast dune desert under hazy daylight. The fallen hourglass is building-sized and half-buried, and the calendar blocks jut from the dunes like weathered monoliths. In the midground, a slim graphite sieve conveyor with lime buckets starts turning, lifting sand and dropping small lime tokens into a tray. The final frame is steady and wide.
Sound: soft continuous hiss of falling sand rising to a dry rush, card blocks clacking over one by one, then quiet desert wind and the gentle rhythmic clink of the conveyor.
Style: photoreal handcrafted miniature diorama, ivory paper, matte graphite metal, frosted acrylic and glass, soft upper-left daylight, shallow depth of field, restrained palette with acid-lime #D0F344 accents only, no text, no people, smooth controlled camera.
