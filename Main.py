#!/usr/bin/env python3

import Database, AESCipher

# def main():
# 	choice = '0'
# 	while choice != 'x' and choice != 'X':
# 		print("(E)ncrypt, (D)ecrypt, (S)how all ids, (U)pdate id, De(l)ete id, E(x)it")
# 		choice = input()
# 		if choice == 'E' or choice == 'e':
# 			account = input("Account: ")
# 			pswd = input("Password: ")
# 			key = input("Key: ")
# 			if not Database.search_entry(account):
# 				pswd = AESCipher.encrypt(key, pswd)
# 				Database.entry_data(account, pswd)
# 		elif choice == 'D' or choice == 'd':
# 			account = input("Account: ")
# 			key = input("Key: ")
# 			if Database.search_entry(account):
# 				pswd = Database.retriveID(account)
# 				pswd = AESCipher.decrypt(key, pswd)
# 				print("Password: %s" % pswd)
# 		elif choice == 'S' or choice == 's':
# 			data = Database.get_table()
# 			print("%-20s %-20s %-15s" % ("Login ID", "Date Created", "Last Used"))
# 			print("~"*100)
# 			for row in data:
# 				print("%-20s %-20s %-20s" % (row[0], row[1], row[2]))
# 			print("~"*100)
# 		elif choice == 'U' or choice == 'u':
# 			account = input("Account: ")
# 			pswd = input("Password: ")
# 			key = input("Key: ")
# 			if Database.search_entry(account):
# 				pswd = AESCipher.encrypt(key, pswd)
# 				Database.update_entry(pswd)
# 		elif choice == 'L' or choice == 'l':
# 			account = input("Account: ")
# 			if Database.search_entry(account):
# 				Database.delete_entry(account)
# main()


def main():
    while True:
        print("(E)ncrypt, (D)ecrypt, (S)how all ids, (U)pdate id, De(l)ete id, E(x)it")
        choice = input('> ')
        Database.create_database()

        if choice in ('e', 'E'):
            website = input('Website: ')
            username = input("Username: ")
            search_res = Database.search_account(website, username)
            if search_res:
                print("Can't encrypt. Account exists.")
            else:
                key = input("Key: ")
                password = input("Password: ")
                password = AESCipher.encrypt(key, password)
                Database.create_account(website, username, password)
                print('Done')

        elif choice in ('d', 'D'):
            website = input('Website: ')
            username = input("Username: ")
            search_res = Database.search_account(website, username)
            if search_res:
                key = input("Key: ")
                password = search_res['password']
                password = AESCipher.decrypt(key, password)
                print("Password:", password)
            else:
                print("Can't decrypt. Account doesn't exists.")

        elif choice in ('u', 'U'):
            website = input('Website: ')
            username = input("Username: ")
            search_res = Database.search_account(website, username)
            if search_res:
                new_username = input("New Username: ")
                new_password = input("New Password: ")
                key = input("Key: ")
                new_password = AESCipher.encrypt(key, new_password)
                Database.update_account(website, username, new_username, new_password)
                print("Done.")
            else:
                print("Can't update. Account doesn't exists.")

        elif choice in ('l', 'L'):
            website = input('Website: ')
            username = input("Username: ")
            search_res = Database.search_account(website, username)
            if search_res:
                key = input("Key: ")
                password = input("Enter password to delete account: ")
                acc_pass = AESCipher.decrypt(key, search_res['password'])
                if password == acc_pass:
                    Database.delete_account(website, username)
                    print("Done")
                else:
                    print("Can't delete account, unauthorized access.")
            else:
                print("Account doesn't exists.")

        elif choice in ('s', 'S'):
            search_res = Database.show_all()
            print("{:20} {:20} {:20} {:20}".format("Website", "Username", "Last Used", "Create Date"))
            print('~' * 100)
            for data in search_res:
                print("{:20} {:20} {:20} {:20}".format(*data))
            print('~' * 100)

        elif choice in ('x', 'X'):
            break

        else:
            print('Invalid Choice.')

main()
