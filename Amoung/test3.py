import sqlite3 
import os
 
def file_exe(file_name):
    list(file_name)
    len(file_name) 
    return file_name[-3:] 


file_name = 'Hello.txt' 
file = file_exe(file_name) 
print(file) 


def connect(db_path):
    if db_path is not None:
        path = os.chdir(db_path) 
        file_name = input("Enter the file name: ")
        os.listdir(path)
        file_exe_ = file_exe(file_name) 
        full_path = os.path.join(db_path, file_name)
        print(file_exe_)
        if file_exe_ == ".db":
            conn =  sqlite3.connect(full_path) 
            cur = conn.cursor() 
            cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'") 
            cur.execute("SELECT name FROM sqlite_master WHERE type='table'; ")
            exists = cur.fetchall() 
            if exists:
                count = 0
                print("No of table are: ")
                for table in exists:
                    table[0]
                    count = count +1  
                print(count)

path = "H:\Amoung"

connect(path)