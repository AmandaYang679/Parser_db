import psycopg2

conn = psycopg2.connect(
    dbname="StalcraftSCHelper",
    user="StalcraftSCHelper",
    password="StalcraftSCHelper",
    host="localhost",
    port="5432",
)
cursor = conn.cursor()

cursor.execute("""
    UPDATE items
    SET category = REPLACE(category, '_', '-');
""")

conn.commit()
cursor.close()
conn.close()

print("success")
