import sqlite3
from datetime import datetime


def init_db():
    conn = sqlite3.connect("universal.db")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        full_name VARCHAR,
        username VARCHAR,
        phone_number VARCHAR,
        city TEXT,
        created_at TEXT                       
    )""")

    conn.commit()
    conn.close()




def add_user(user_id, full_name, username, phone_number):
    conn = sqlite3.connect("universal.db")
    cur = conn.cursor()
    created_at = datetime.now().isoformat()
    cur.execute("INSERT INTO users (user_id, full_name, username, phone_number, created_at) VALUES (?,?,?,?,?)", (user_id, full_name, username, phone_number, created_at))
    conn.commit()
    conn.close()



def get_user(user_id):
    conn = sqlite3.connect("universal.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cur.fetchone()
    conn.commit()
    conn.close()
    return user



def update_city(user_id, city):
    conn = sqlite3.connect("universal.db")
    cur = conn.cursor()
    cur.execute("UPDATE users SET city = ? WHERE user_id = ?",(city, user_id))
    conn.commit()
    conn.close()


def get_user_city(user_id):
    conn = sqlite3.connect("universal.db")
    cur = conn.cursor()
    cur.execute("SELECT city FROM users WHERE user_id = ?",(user_id,))
    row = cur.fetchone()
    return row[0] if row and row[0] else None



def get_users(offset=0, limit=5):
    conn = sqlite3.connect("universal.db")
    cur = conn.cursor()
    cur.execute("SELECT user_id, full_name, username, phone_number, created_at FROM users LIMIT ? OFFSET ?",(limit, offset))
    return cur.fetchall()


def users_count():
    conn = sqlite3.connect("universal.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users")
    return cur.fetchone()[0]