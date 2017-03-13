import sqlite3
from datetime import datetime

conn = sqlite3.connect("database.db")
c = conn.cursor()


def get_time():
    today = datetime.today().strftime("%d/%m/%y %I:%M%p")
    return today

def create_database():
    c.execute("""CREATE TABLE IF NOT EXISTS encrypts_storage
		(website TEXT, username TEXT, password TEXT, create_date TEXT, last_used TEXT)""")


def set_account(website, username, password):
    curr_date = get_time()
    c.execute("""INSERT INTO encrypts_storage (website, username, password, create_date, last_used)
    VALUES (?, ?, ?, ?, ?)""", (website, username, password, curr_date, curr_date))
    conn.commit()

def search_account(website, username):
    c.execute("""SELECT * FROM encrypts_storage
    WHERE website=? AND usernane=?""", (website, username))
    return c.fetchall()


# def entry_data(website, username, text):
#     entry = search_entry(website, username)
#     if entry:
#         print("Login ID already exists")
#     else:
#         create_date = get_time()
#         c.execute("""INSERT INTO encrypts_stor
# 					VALUES (?, ?, ?, ?)""", (website, username, text, create_date, create_date))
#         conn.commit()
#
#
# def search_entry(website=None, username=None):
#     if website and username:
#         c.execute("""SELECT * FROM encrypts_stor""")
#         for row in c.fetchall():
#             if row[0] == website and row[1] == username:
#                 return True
#         else:
#             return False
#     else:
#         print("Invalid")
#         return
#
#
# def update_entry(website=None, text=None):
#
#     c.execute(
#         """UPDATE encrypts_stor SET password=? WHERE website=?""", (text, website))
#
#
# def retrieve_id(website, username):
#     c.execute(
#         """SELECT website, password FROM encrypts_stor WHERE website=? AND username=?""", (website, username))
#     data = c.fetchone()
#     return data[1]
#
#
# def get_table():
#     c.execute(
#         """SELECT website, create_date, last_used FROM encrypts_stor """)
#     return c.fetchall()
#
#     # c.execute("""IF EXISTS (SELECT website, create_date, last_used
#     # FROM encrypts_stor)""")
#     # return c.fetchall()
#
#
# def delete_entry(loginID=None):
#     c.execute("""DELETE FROM encrypts_stor WHERE website=?""", (loginID, ))
#     conn.commit()
