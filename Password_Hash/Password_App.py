import getpass
import pbkdf2
import pickle

ans = True
while ans:
    print("""
                   ---------------------
                  | 1. Shutdown         | 
                  | 2. Items            |
                  | 3. Hash Password    |
                   ---------------------
    """)
    ans=getpass.getpass("""
             Please Enter A Number: """)
    if ans == "1":
        exit(0)
    elif ans == "3":
        pa=getpass.getpass("""
             Enter password to be encrypted: """)
        stored_password = pbkdf2.hash_password(pa)
        print('\r\nCopy this string to the code.\r\n')
        print(stored_password)
        f = open('C:\\Users\\csb003\\Documents\\NCHpython\\Password_Hash\\hashPW.conf', 'wb')
        pickle.dump(stored_password, f)
        f.close()
        continue
    elif ans == "2":
        f = open('C:\\Users\\csb003\\Documents\\NCHpython\\Password_Hash\\hashPW.conf', 'rb')
        stored_password = pickle.load(f)
        f.close()
        pa=getpass.getpass("""
             Please Enter Password: """)
        if pbkdf2.verify_password(stored_password, pa):
            print("""
                   ----------------
                  | 1. Pi password |
                  | 2. Shutdown    |
                   ----------------
            """)
            pe=getpass.getpass("""
             Please Enter A Number: """)
            if pe == "1":
                print ("""
                    Pi's Password Is 'Jesus Saves'""")
                import time
                time.sleep(1)
                exit(0)
            elif pe == "2":
                exit(0)
            else:
                print("""
                    You Have Entered An Inccoredt Option. Terminating Programm""")
                import time
                time.sleep(1)
                exit(0)
        else:
                print("""
                    You Have Entered An Inccorect Password. Terminating Programm""")
                import time
                time.sleep(1)
                exit(0)