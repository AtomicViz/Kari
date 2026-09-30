"""Validate scene batches against SPEC.md hard rules."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).parent
films = {r["inspired_by"].split(" (")[0].lower() for f in HERE.glob("batch-*.json")
         for r in json.load(open(f)) if "inspired_by" in r}
BANNED = r"\b(person|people|man|woman|worker's hand|hands?|faces?|figures?|silhouettes?|carnival|circus|ferris|carousel|roller coaster|coaster|midway|big top|clown|hologram|robot)\b"
bad = 0
for f in sorted(HERE.glob("batch-*.json")):
    for r in json.load(open(f)):
        for st in ("start", "end", "apocalypse"):
            t = r[st]; n = len(t.split()); low = t.lower()
            probs = []
            if not 85 <= n <= 150: probs.append(f"{n} words")
            probs += [m.group(0) for m in re.finditer(BANNED, low)]
            probs += [fm for fm in films if len(fm) > 4 and fm in low]
            if "lime" not in low: probs.append("no lime")
            if probs:
                bad += 1; print(f"{r['id']} {st}: {sorted(set(probs))}")
print("issues:", bad)
