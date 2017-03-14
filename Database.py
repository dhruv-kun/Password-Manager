import sqlite3
from datetime import datetime

conn = sqlite3.connect("database.db")
c = conn.cursor()


def get_time():
    today = datetime.today().strftime("%d/%m/%y %I:%M%p")
    return today


def create_database():
    c.execute("""CREATE TABLE IF NOT EXISTS encrypts_storage(
    website TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    create_date TEXT,
    last_used TEXT,
    PRIMARY KEY (website, username))""")
    return


def create_account(website, username, password):
    curr_date = get_time()
    c.execute("""INSERT INTO encrypts_storage
    (website, username, password, create_date, last_used)
    VALUES (?, ?, ?, ?, ?)""",
              (website, username, password, curr_date, curr_date))
    conn.commit()
    return


def search_account(website, username):
    c.execute("""SELECT *
    FROM encrypts_storage
    WHERE website=? AND username=?""",
              (website, username))
    data = c.fetchall()
    attrs = ["website", "username", "password", "last_used", "create_date"]
    data = dict(zip(attrs, data[0])) if data else None
    return data


def delete_account(website, username):
    c.execute("""DELETE FROM encrypts_storage
    WHERE website=? AND username=?""",
              (website, username))
    conn.commit()
    return


def update_account(website, username, new_username, new_password):
    curr_date = get_time()
    c.execute("""UPDATE encrypts_storage
    SET username=?, password=?, last_used=?
    WHERE website=? AND username=?""",
              (new_username, new_password, curr_date, website, username))
    conn.commit()
    return


def show_all():
    c.execute("""SELECT website, username, create_date, last_used
    FROM encrypts_storage""")
    data = c.fetchall()
    return data
