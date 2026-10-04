"""Verifica bytes preservados sem importar dependências dos experimentos."""
from pathlib import Path
import hashlib
import json
import sys

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "provenance/file-manifest.json").read_text())
failures = []
for item in manifest["files"]:
    path = root / item["path"]
    if not path.is_file():
        failures.append(f"Ausente: {item['path']}")
        continue
    data = path.read_bytes()
    if len(data) != item["bytes"] or hashlib.sha256(data).hexdigest() != item["sha256"]:
        failures.append(f"Alterado: {item['path']}")
if failures:
    print("\n".join(failures))
    sys.exit(1)
print(f"Integridade confirmada: {len(manifest['files'])} arquivos.")
