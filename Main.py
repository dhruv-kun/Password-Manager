#!/usr/bin/env python3

import Database
import AESCipher


# def main():
#     choice = '0'
#     while choice != 'x' and choice != 'X':
#         print("(E)ncrypt, (D)ecrypt, (S)how all ids, (U)pdate id, De(l)ete id, E(x)it")
#         choice = input()
#         if choice == 'E' or choice == 'e':
#             account = input("Website: ")
#             username = input('Username: ')
#             pswd = input("Password: ")
#             key = input("Key: ")
#             if not Database.search_entry(account):
#                 pswd = AESCipher.encrypt(key, pswd)
#                 Database.entry_data(account, pswd)
#         elif choice == 'D' or choice == 'd':
#             account = input("Account: ")
#             username = input('Username: ')
#             key = input("Key: ")
#             if Database.search_entry(account):
#                 pswd = Database.retriveID(account)
#                 pswd = AESCipher.decrypt(key, pswd)
#                 print("Password: %s" % pswd)
#         elif choice == 'S' or choice == 's':
#             data = Database.get_table()
#             print("%-20s %-20s %-20s %-15s" %
#                   ("Website", "Username", "Date Created", "Last Used"))
#             print("~" * 100)
#             for row in data:
#                 print("%-20s %-20s %-20s %-20s" %
#                       (row[0], row[1], row[2], row[3]))
#             print("~" * 100)
#         elif choice == 'U' or choice == 'u':
#             account = input("Account: ")
#             username = input('Username: ')
#             key = input("Key: ")
#             password = input("Password: ")
#             if Database.search_entry(account):
#                 password = AESCipher.encrypt(key, password)
#                 Database.update_entry(password)
#         elif choice == 'L' or choice == 'l':
#             account = input("Account: ")
#             if Database.search_entry(account):
#                 Database.delete_entry(account)
# main()


def main():
    choice = '0'
    while choice not in ('x', 'X'):
        print("(E)ncrypt, (D)ecrypt, (S)how all ids, (U)pdate id, De(l)ete id, E(x)it")
        choice = input('> ')
        if choice in ('e', 'E'):
            website = input('Website: ')
            username = input('Username: ')
            password = input('Password: ')
            key = input('Key: ')
            Database.create_table()
            if Database.search_account(website, username):
                print('Account Exists.')
            else:
                password = AESCipher.encrypt(key, password)
                Database.set_account(website, username, password)
        elif choice in ('d', 'D'):
            website = input('Website: ')
            username = input('Username: ')
            foundResult = Database.search_entry(website, username)
            if foundResult:
                key = input('Key: ')
                password = foundResult[2]
                password = AESCipher.decrypt(key, password)
                print('Password: {}'.format(password))
            else:
                print("Account doesn't exist.")
        elif choice in ('s', 'S'):
            data = Database.get_table()
            print('{:20} {:20} {:20} {:20}'.format('Website', 'Username', 'Date Created', 'Last Used'))
            print('~' * 100)
            for row in data:
                print('{:20} {:20} {:20} {:20}'.format(*row))
            print('~' * 100)
        elif choice in ('u', 'U'):
            website = input('Website: ')
            username = input('Username: ')
            foundResult = Database.search_entry(website, username)
            if foundResult:
                key = input('Key: ')
                temp = AESCipher.sha(key)
                if foundResult[2][:16] == key:
                    password = input('New Password: ')
                    password = AESCipher.encrypt(key, password)
                    Database.update_entry(website, username, password)
                else:
                    print('Unauthorized Password Change.')
        else:
            print('Invalid Option.')

if __name__ == '__main__':
    main()