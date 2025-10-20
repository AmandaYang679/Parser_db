import os
from pathlib import Path


base_dir = Path(r"D:\Projects\Django\stalcraft-database-main\ru\items")

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".json"):
            json_path = Path(root) / file
            rel_json_path = json_path.relative_to(base_dir)
            icons_dir = base_dir.parent / "icons"
            icon_path = icons_dir / rel_json_path
            icon_path = icon_path.with_suffix(".png")
            print("JSON:", rel_json_path)
            print("ICON:", icon_path)
