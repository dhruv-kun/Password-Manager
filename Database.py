import sqlite3
from datetime import datetime

conn = sqlite3.connect("database.db")
c = conn.cursor()

def get_time():
	today = datetime.today().strftime("%d/%m/%y %I:%M%p")
	return today

def create_database():
	c.execute("""CREATE TABLE IF NOT EXISTS encrypts_stor
		(login_id TEXT, password TEXT, create_date TEXT, last_used TEXT)""")

def entry_data(loginID, text):
	entry = search_entry(loginID)
	if entry:
		print("Login ID already exists")
	else:
		create_date = get_time()
		c.execute("""INSERT INTO encrypts_stor
			VALUES (?, ?, ?, ?)""", (loginID, text, create_date, create_date))
		conn.commit()

def search_entry(loginID = None):
	if loginID:
		c.execute("""SELECT * FROM encrypts_stor""")
		for row in c.fetchall():
			if row[0] == loginID:
				return True
		else:
			return False
	else:
		print("Invalid")
		return

def update_entry(loginID = None, text = None):

	c.execute("""UPDATE encrypts_stor SET password=? WHERE login_id=?""", (text, loginID))

def retriveID(loginID):
	c.execute("""SELECT login_id, password FROM encrypts_stor WHERE login_id=?""", (loginID, ))
	data = c.fetchone()
	return data[1]

def get_table():
	c.execute("""SELECT login_id, create_date, last_used FROM encrypts_stor""")
	return c.fetchall()



def delete_entry(loginID = None):
	c.execute("""DELETE FROM encrypts_stor WHERE login_id=?""", (loginID, ))
	conn.commit()