import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO login_details (user_id, password) VALUES (?, ?)",
            ('test', 'test')
            )
connection.commit()
connection.close()