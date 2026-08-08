# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

md = Path("assets/images/maquettes/prestations/PROMPTS-IMAGES.md").read_text(encoding="utf-8")
out = {}
m = re.search(r"## Cadres categories.*?\n\n(.*?)\n## Cartes", md, re.S)
sec = m.group(1) if m else ""
for mm in re.finditer(r"^### ([a-z0-9-]+)\n(.+?)(?=\n### |\Z)", sec, re.M | re.S):
    out["cat:" + mm.group(1)] = " ".join(mm.group(2).strip().split())
for mm in re.finditer(r"^#### ([a-z0-9-]+)\n(.+?)(?=\n#### |\n### |\Z)", md, re.M | re.S):
    out["card:" + mm.group(1)] = mm.group(2).strip().split("\n")[0].strip()
Path("scripts/_prestation_image_prompts.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(len(out), "prompts")
