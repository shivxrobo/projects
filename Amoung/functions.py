import sqlite3 
import os
import sys 
def file_exe(file_name):
    file_name_exe = list(file_name) 
    return file_name_exe[:-3] 

python = sys.executable


class connection:
    def __init__(self,) -> None:
        self.cur = None

    def con(self,db_name,db_path = None):
        self.db_name = db_name 
        self.db_path = db_path 
        if self.db_path != None:
             os.chdir(self.db_path)
             os.listdir()
             file_name = input("Enter file Name: ") 
             if file_exe(file_name) == ".db":
                self.conn = sqlite3.connect(self.db_path) 
                self.cur = self.conn.cursor()
                print("Success")
             else:
                 print("The file is not db file: ")  
                 os.execl(python, python, *sys.argv) 

        else:
            name_con =  sqlite3.connect(self.db_name)  
            self.cur = name_con.cursor()
            print("dONE")

    def action(self,action):
            self.data = ['ALICE','mega']
            self.action = action 
            if self.action is not None:
                self.name = input("Enter Table name: ")
                self.cur.execute(f"CREATE TABLE IF NOT EXISTS movie(?,?,?)",self.data) 
                print("Done")
            else:
                pass 
    # def add_user(self,user_name,user_id):
    #     if self.cur is None:
    #         print("Can't connect") 
        
    #     insert_value = 

db_name = "Hello.db" 

Con = connection() 

connect = Con.con(db_name=db_name)  
action = Con.action(True)