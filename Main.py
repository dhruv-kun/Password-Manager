#!/usr/bin/env python3

import Database, AESCipher

def main():
	choice = '0'
	while choice != 'x' and choice != 'X':
		print("(E)ncrypt, (D)ecrypt, (S)how all ids, (U)pdate id, De(l)ete id, E(x)it")
		choice = input()
		if choice == 'E' or choice == 'e':
			account = input("Account: ")
			pswd = input("Password: ")
			key = input("Key: ")
			if not Database.search_entry(account):
				pswd = AESCipher.encrypt(key, pswd)
				Database.entry_data(account, pswd)
		elif choice == 'D' or choice == 'd':
			account = input("Account: ")
			key = input("Key: ")
			if Database.search_entry(account):
				pswd = Database.retriveID(account)
				pswd = AESCipher.decrypt(key, pswd)
				print("Password: %s" % pswd)
		elif choice == 'S' or choice == 's':
			data = Database.get_table()
			print("%-20s %-20s %-15s" % ("Login ID", "Date Created", "Last Used"))
			print("~"*100)
			for row in data:
				print("%-20s %-20s %-20s" % (row[0], row[1], row[2]))
			print("~"*100)
		elif choice == 'U' or choice == 'u':
			account = input("Account: ")
			pswd = input("Password: ")
			key = input("Key: ")
			if Database.search_entry(account):
				pswd = AESCipher.encrypt(key, pswd)
				Database.update_entry(pswd)
		elif choice == 'L' or choice == 'l':
			account = input("Account: ")
			if Database.search_entry(account):
				Database.delete_entry(account)
main()