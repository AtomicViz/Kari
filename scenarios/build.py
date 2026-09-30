"""Build catalogues and Seedream 5.0 text-only prompts for both idea sets.

    python3 build.py

Writes, next to this file:
  set-a-workplace.md / .json      concepts 31-130
  set-b-movies.md / .json         concepts 131-230
  prompts/NNN-slug.json           8 image prompts per concept (4 stages x 2 aspects)
"""
import json
import pathlib
import re

from ideas import IDEAS as SET_A
from ideas_movies import IDEAS as SET_B

HERE = pathlib.Path(__file__).parent

STYLE = (
    "Photoreal miniature tabletop scene. Ivory paper, graphite metal, frosted acrylic "
    "and frosted glass. Soft daylight from the upper left, grounded believable shadows, "
    "shallow depth of field with one sharp focal mechanism. Palette: white #FFFFFF, "
    "graphite #191D1B, pale neutral #F3F5F2, muted graphite #626A64, soft border #DCE1DA, "
    "olive #718D0B, with restrained acid lime #D0F344 accents marking only the active "
    "route or key object. No people, no faces, no hands. No text, letters, numbers, "
    "logos or UI labels anywhere in the image."
)

STAGE_FRAMING = {
    "start": "Calm, controlled, readable composition. One recognizable problem, nothing escalated yet.",
    "end": "The same mechanism mid-disaster. The chain reaction is physically traceable back to its source.",
    "carnival": ("The broken workflow rebuilt as a literal miniature amusement ride or circus mechanism "
                 "in graphite metal and frosted acrylic. The ride expresses the office process itself."),
    "apocalypse": ("Wide, large-scale ruin long after the collapse. The original source is hard to identify "
                   "but evidence of the disorder is embedded in the wreckage. Lime recovery rigs are "
                   "beginning to reconnect the pieces."),
}

ASPECTS = {
    "16x9": ("16:9", "Wide landscape composition, eye-level three-quarter camera."),
    "9x16": ("9:16", "Native tall portrait composition, not a crop: stack the mechanism vertically, "
                     "slightly high camera looking down."),
}


def slug(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def concepts():
    for n, (title, cat, *stages) in enumerate(SET_A, start=31):
        yield "a", n, title, {"category": cat}, stages
    for n, (title, film, *stages) in enumerate(SET_B, start=131):
        yield "b", n, title, {"inspired_by": film}, stages


def prompt(scene, stage, aspect):
    return f"{scene} {STAGE_FRAMING[stage]} {ASPECTS[aspect][1]} {STYLE}"


def main():
    out = {"a": [], "b": []}
    pdir = HERE / "prompts"
    pdir.mkdir(exist_ok=True)
    for s, n, title, meta, (start, end, carnival, apocalypse) in concepts():
        rec = {"id": n, "slug": f"{n:03d}-{slug(title)}", "title": title, **meta,
               "start": start, "end": end, "carnival": carnival, "apocalypse": apocalypse}
        out[s].append(rec)
        scenes = {"start": start, "end": end, "carnival": carnival, "apocalypse": apocalypse}
        prompts = [{"file": f"{a}/{st}.png", "aspect_ratio": ASPECTS[a][0],
                    "prompt": prompt(scenes[st], st, a)}
                   for a in ASPECTS for st in scenes]
        (pdir / f"{rec['slug']}.json").write_text(json.dumps(
            {"id": n, "title": title, "model": "seedream_v5_pro", "resolution": "1.5k",
             "images": prompts}, indent=2) + "\n")

    for s, name, heading, blurb in [
        ("a", "set-a-workplace", "Set A: 100 more workplace annoyances (31-130)",
         "Everyday agency and office friction, grouped by category."),
        ("b", "set-b-movies", "Set B: 100 movie-inspired 9-to-5 escapes (131-230)",
         "Inspired by 1990s and early-2000s films about hating the day job. The film is a "
         "reference note only: prompts never name films, characters, quotes or logos, and "
         "people stay off-screen."),
    ]:
        (HERE / f"{name}.json").write_text(json.dumps(out[s], indent=2) + "\n")
        lines = [f"# {heading}", "", blurb, ""]
        group = None
        for r in out[s]:
            g = r.get("category")
            if g and g != group:
                lines += [f"## {g}", ""]
                group = g
            src = f" *({r['inspired_by']})*" if "inspired_by" in r else ""
            lines += [f"### {r['id']}. {r['title']}{src}", "",
                      f"- **Start:** {r['start']}",
                      f"- **Workplace disaster:** {r['end']}",
                      f"- **Carnival:** {r['carnival']}",
                      f"- **Apocalypse:** {r['apocalypse']}", ""]
        (HERE / f"{name}.md").write_text("\n".join(lines))
    print(len(out["a"]), len(out["b"]), len(list(pdir.glob("*.json"))))


if __name__ == "__main__":
    main()
