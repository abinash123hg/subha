"""Print a notebook's cell outline: type, line count and first line."""

import json
import sys


def outline(path):
    with open(path, encoding="utf-8") as handle:
        notebook = json.load(handle)
    for i, cell in enumerate(notebook.get("cells", [])):
        source = cell.get("source", [])
        first = source[0].strip() if source else ""
        print(f"[{i}] {cell.get('cell_type')}: {len(source)} lines | {first[:60]}")


if __name__ == "__main__":
    outline(sys.argv[1] if len(sys.argv) > 1 else "Untitled-1[1] (3).ipynb")
