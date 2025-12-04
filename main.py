import os, json
from pathlib import Path
from psycopg2.extras import Json
import psycopg2
import jmespath


conn = psycopg2.connect(
    dbname="StalcraftSCHelper",
    user="StalcraftSCHelper",
    password="StalcraftSCHelper",
    host="localhost",
    port="5432",
)
cursor = conn.cursor()


base_dir = Path(r"D:\Projects\stalcraft-database-main\ru")
for root, _, files in os.walk(base_dir / "items"):
    for file in files:
        if file.endswith(".json"):

            json_path = Path(root) / file
            rel_json_path = json_path.relative_to(base_dir / "items")

            icons_dir = base_dir / "icons"
            icon_path = icons_dir / rel_json_path
            icon_path = icon_path.with_suffix(".png")
            rel_icon_path = icon_path.relative_to(base_dir)

            with open(json_path, encoding="utf-8") as f:
                content = json.load(f)

            # Models for DB
            id = file[:-5]
            name = content["name"]["lines"]["en"]
            icon = str(rel_icon_path).replace("\\", "/")
            category = content["category"]
            rank = jmespath.search("infoBlocks[].elements[?key.key=='core.tooltip.info.rank'].value.lines.en | [0][0]", content)
            infoblocks = content["infoBlocks"]


            cursor.execute(
                """
                INSERT INTO items (id, name, icon, category, rank, infoblocks)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
            """,
                (id, name, icon, category, rank, Json(infoblocks)),
            )

conn.commit()
cursor.close()
conn.close()
print("success")