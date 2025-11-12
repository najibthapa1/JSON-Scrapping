import json
import psycopg2

try:
    with open('data.json', 'r') as file:
        userss = json.load(file)

        conn = psycopg2.connect(
            host="localhost",
            database="DATABASE_NAME",
            user="USERNAME",
            password="PASSWORD"
        )
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS userss (
                id INTEGER PRIMARY KEY,
                data JSONB
            )
        ''')
        conn.commit()
        cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'userss'")
        columns = cursor.fetchall()
        print(columns)
        for user in userss:
            cursor.execute('''
                            INSERT INTO userss (id, data) VALUES (%s, %s)
                            ON CONFLICT (id) DO UPDATE SET data = EXCLUDED.data
                            ''',(user['id'], json.dumps(user)))

        conn.commit()
        cursor.execute("SELECT * FROM userss")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        conn.close()
except FileNotFoundError:
    data=[]


