import sqlite3
from datetime import datetime

conn = sqlite3.connect("database.db")
c = conn.cursor()


def get_time():
    today = datetime.today().strftime("%d/%m/%y %I:%M%p")
    return today


def create_database():
    c.execute("""CREATE TABLE IF NOT EXISTS encrypts_storage(
    web TEXT NOT NULL,
    usr TEXT NOT NULL,
    pswd TEXT NOT NULL,
    create_date TEXT,
    last_used TEXT,
    PRIMARY KEY (web, usr))""")
    return


def create_account(web, usr, pswd):
    curr_date = get_time()
    c.execute("""INSERT INTO encrypts_storage
    (web, usr, pswd, create_date, last_used)
    VALUES (?, ?, ?, ?, ?)""",
              (web, usr, pswd, curr_date, curr_date))
    conn.commit()
    return


def search_account(web, usr):
    c.execute("""SELECT *
    FROM encrypts_storage
    WHERE web=? AND usr=?""",
              (web, usr))
    data = c.fetchall()
    attrs = ["website", "username", "password", "last_used", "create_date"]
    data = dict(zip(attrs, data[0])) if data else None
    return data


def delete_account(web, usr):
    c.execute("""DELETE FROM encrypts_storage
    WHERE web=? AND usr=?""",
              (web, usr))
    conn.commit()
    return


def update_account(web, usr, new_usr, new_pswd):
    curr_date = get_time()
    c.execute("""UPDATE encrypts_storage
    SET usr=?, pswd=?, last_used=?
    WHERE web=? AND usr=?""",
              (new_usr, new_pswd, curr_date, web, usr))
    conn.commit()
    return


def show_all():
    c.execute("""SELECT web, usr, create_date, last_used
    FROM encrypts_storage""")
    data = c.fetchall()
    return data
