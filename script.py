import psycopg2
import datetime
from config import settings

timezone_offset = datetime.timedelta(hours=5, minutes=30)
now = datetime.datetime.now(datetime.timezone(timezone_offset))


conn = psycopg2.connect(
    host=settings.database_hostname,
    database=settings.database_name,
    user=settings.database_username,
    password=settings.database_password,
    port=settings.database_port,
)


cur = conn.cursor()
cutoff_time = now - datetime.timedelta(days=30)
print(cutoff_time)
sql_query = f"DELETE FROM video_data WHERE created_at < '{cutoff_time}'"
cur.execute(sql_query)
conn.commit()
cur.close()
conn.close()