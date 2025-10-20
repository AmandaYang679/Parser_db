import psycopg2
from decouple import config


try:
    conn = psycopg2.connect(
        dbname=config("POSTGRES_DB"),
        user=config("POSTGRES_USER"),
        password=config("POSTGRES_PASSWORD"),
        host=config("POSTGRES_HOST"),
        port=config("POSTGRES_PORT"),
    )

    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Версия PostgreSQL: {db_version[0]}")
    # cursor.close()
    # conn.close()


except psycopg2.OperationalError as e:
    print(f"Не удалось подключиться к базе данных: {e}")
