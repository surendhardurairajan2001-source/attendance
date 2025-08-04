import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir,"user.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

cursor.execute("INSERT INTO user(username,password)values(?,?)",("Surendhar","Suren123"))
cursor.execute("INSERT INTO user(username,password)values(?,?)",("Varjeth","Varjeth123"))
cursor.execute("INSERT INTO user(username,password)values(?,?)",("siva","siva123"))

conn.commit()
conn.close()

print("Database Created and User has been added")