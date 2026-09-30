"""Assemble Seedream 5.0 text-only image prompts for concepts 31-230.

    python3 build.py

Reads concepts/batch-*.json (the per-concept scene paragraphs) and writes:
  set-a-workplace.md / .json      concepts 31-130, catalogue
  set-b-movies.md / .json         concepts 131-230, catalogue
  prompts/NNN-slug.json           6 prompts per concept (3 stages x 2 aspects)
  Set A Image Prompts.md / Set B Image Prompts.md   collated, copy-paste ready

Prompt = medium line + concept scene + aspect composition + materials + palette
         + stage lighting and camera + exclusions.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).parent
STAGES = ("start", "end", "apocalypse")

MEDIUM = {
    "start": "Photorealistic macro photograph of a handcrafted miniature tabletop diorama.",
    "end": "Photorealistic macro photograph of a handcrafted miniature tabletop diorama, captured mid-disaster.",
    "apocalypse": "Photorealistic photograph of a vast handcrafted miniature landscape diorama.",
}

COMPOSITION = {
    ("16x9", "start"): (
        "Wide 16:9 landscape frame. The hero object sits slightly left of centre on the lower third, "
        "with the related objects extending to the right so the workflow reads left to right. "
        "Clean, generous negative space above."),
    ("16x9", "end"): (
        "Wide 16:9 landscape frame, same layout and angle as the calm version of this scene. The hero "
        "object stays slightly left of centre, and the spread of the disaster runs to the right and toward "
        "the camera so its path can be traced back to the source."),
    ("16x9", "apocalypse"): (
        "Wide 16:9 panoramic frame. The main ruin anchors the left or centre foreground, terrain rolls "
        "back to a distant horizon on the upper third, and the lime recovery rig sits in the right midground."),
    ("9x16", "start"): (
        "Tall 9:16 portrait frame composed natively for vertical, not a crop. The hero object sits in the "
        "lower-middle third, with the related objects stacked upward or receding into depth so the "
        "workflow reads bottom to top. Clean negative space at the top."),
    ("9x16", "end"): (
        "Tall 9:16 portrait frame composed natively for vertical, same layout as the calm version of this "
        "scene. The disaster climbs and spills vertically, piling up or cascading down through the frame "
        "while remaining traceable to the hero object."),
    ("9x16", "apocalypse"): (
        "Tall 9:16 portrait frame. The ruin fills the foreground at the bottom, terrain layers upward into "
        "the distance with a high horizon, the lime recovery rig is centred in the midground, and open "
        "hazy sky fills the top."),
}

MATERIALS = (
    "Shot as a real physical model, not a 3D render. Materials are limited and tactile: heavyweight "
    "ivory cotton paper and card with visible fibres, soft folds and slightly deckled edges; matte, "
    "bead-blasted graphite metal with fine machining lines, chamfered edges and tiny hex fasteners; "
    "frosted acrylic with milky edges and a soft internal glow; sandblasted frosted glass. Surfaces "
    "carry believable imperfections: fine dust, paper grain, hairline creases, light scuffs on metal. "
    "Every object has convincing miniature scale and weight and rests firmly on its surface."
)

PALETTE = (
    "Colour palette is restrained and nearly monochrome: white #FFFFFF, warm ivory, pale neutral "
    "#F3F5F2, soft grey-green #DCE1DA, muted graphite #626A64 and deep graphite #191D1B. Acid lime "
    "#D0F344 appears only on the lime element named in the scene, as the single signal colour, with "
    "olive #718D0B on its shadowed sides. Nothing else is lime or saturated; no red, orange or blue accents."
)

LIGHT_CAMERA = {
    "start": (
        "Lighting: one large soft key light from the upper left at about 45 degrees, like diffused "
        "north-window daylight, with a gentle white bounce fill from the right; soft grounded contact "
        "shadows fall to the lower right. Camera: 100mm macro lens at f/4, eye level with the tabletop, "
        "three-quarter view. The hero object is tack sharp and the background melts into smooth, creamy "
        "blur on a seamless pale neutral sweep. Mood: calm, precise, orderly and quietly premium, like "
        "high-end editorial product photography."),
    "end": (
        "Lighting: the same soft upper-left key and right-side bounce fill as a calm studio setup, "
        "unchanged, so the disorder reads as physical and real rather than theatrical. Airborne paper, "
        "grains and fragments catch the key light with crisp edge highlights. Camera: 85mm lens at "
        "f/5.6, same three-quarter tabletop angle, fast shutter freezing everything mid-air. Focus sits "
        "where the chain reaction started, and the spread softens into the depth of field. Mood: absurd "
        "but plausible, an orderly system that got out of hand, still clean and editorial. No fire, "
        "smoke or explosions unless the scene names them."),
    "apocalypse": (
        "Lighting: soft overcast late-afternoon daylight still falling from the upper left, with long "
        "soft shadows grounding the ruins and atmospheric haze fading distant forms into pale grey-green. "
        "Camera: wide 24mm view from a low vantage just above the terrain, deep focus through the "
        "midground, with a gentle tilt-shift falloff at the top and bottom edges so the vast scene still "
        "reads as a miniature diorama. Mood: quiet, desolate and monumental, but hopeful at the lime "
        "recovery rig, which is the sharpest and brightest point of interest."),
}

EXCLUDE = (
    "Strictly no people, figures, faces, hands or silhouettes. No readable text, letters, numbers, "
    "clock digits, logos, signage or user-interface graphics anywhere. No holograms, floating screens, "
    "robots with faces, dense cable tangles, carnival or circus elements, cartoon or plastic CGI look, "
    "oversaturated colour, lens flare or heavy vignette."
)

ASPECT_RATIO = {"16x9": "16:9", "9x16": "9:16"}


def slug(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def build_prompt(scene, stage, aspect):
    return " ".join([MEDIUM[stage], scene, COMPOSITION[(aspect, stage)], MATERIALS, PALETTE,
                     LIGHT_CAMERA[stage], EXCLUDE])


def load():
    recs = []
    for f in sorted((HERE / "concepts").glob("batch-*.json")):
        recs += json.loads(f.read_text())
    recs.sort(key=lambda r: r["id"])
    ids = [r["id"] for r in recs]
    assert ids == list(range(31, 231)), f"expected ids 31-230, got {len(ids)}"
    return recs


def main():
    recs = load()
    pdir = HERE / "prompts"
    pdir.mkdir(exist_ok=True)
    for old in pdir.glob("*.json"):
        old.unlink()

    for r in recs:
        r["slug"] = f"{r['id']:03d}-{slug(r['title'])}"
        images = [{"file": f"{a}/{st}.png", "aspect_ratio": ASPECT_RATIO[a],
                   "prompt": build_prompt(r[st], st, a)}
                  for a in ASPECT_RATIO for st in STAGES]
        (pdir / f"{r['slug']}.json").write_text(json.dumps(
            {"id": r["id"], "title": r["title"], "model": "seedream_v5_pro",
             "resolution": "1.5k", "images": images}, indent=2) + "\n")

    sets = [
        ("set-a-workplace", "Set A Image Prompts", recs[:100],
         "Set A: 100 more workplace annoyances (31-130)",
         "Everyday agency and office friction, grouped by category."),
        ("set-b-movies", "Set B Image Prompts", recs[100:],
         "Set B: 100 movie-inspired 9-to-5 escalations (131-230)",
         "Inspired by 1990s and early-2000s films about hating the day job. The film is a "
         "reference note only: prompts never name films, characters, quotes or iconic props, "
         "and people stay off-screen."),
    ]
    for name, prompts_name, rs, heading, blurb in sets:
        (HERE / f"{name}.json").write_text(json.dumps(
            [{k: r[k] for k in r if k != "slug"} | {"slug": r["slug"]} for r in rs], indent=2) + "\n")
        cat, pr = [f"# {heading}", "", blurb, ""], [f"# {prompts_name}", "",
                   "Seedream 5.0 Pro, 1.5k, text-only. One prompt per stage and aspect ratio.", ""]
        group = None
        for r in rs:
            g = r.get("category")
            if g and g != group:
                cat += [f"## {g}", ""]
                group = g
            src = f" *({r['inspired_by']})*" if "inspired_by" in r else ""
            cat += [f"### {r['id']}. {r['title']}{src}", "",
                    f"**Start.** {r['start']}", "",
                    f"**Workplace disaster.** {r['end']}", "",
                    f"**Apocalypse.** {r['apocalypse']}", ""]
            pr += [f"## {r['slug']}", ""]
            for a in ASPECT_RATIO:
                for st in STAGES:
                    pr += [f"### {a} / {st}", "", "```text", build_prompt(r[st], st, a), "```", ""]
        (HERE / f"{name}.md").write_text("\n".join(cat))
        (HERE / f"{prompts_name}.md").write_text("\n".join(pr))
    print(f"{len(recs)} concepts, {len(recs) * 6} prompts")


if __name__ == "__main__":
    main()
