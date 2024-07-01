import sqlite3 
import os
import sys 
def file_exe(file_name):
    file_name_exe = list(file_name) 
    return file_name_exe[:-3] 

python = sys.executable


class connection:
    def __init__(self,) -> None:
      self.conn = None 
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
                return self.cur
             else:
                 print("The file is not db file: ")  
                 os.execl(python, python, *sys.argv) 
        elif self.db_path == None:
            self.connect = sqlite3.connect(db_name) 
            self.cur1 = self.connect.cursor() 
            return self.cur1

        else:
            print("The entered value if nether path nor value please enter a specific path or value.") 
    def add_user(self,user_name,user_id,type_of_con):
         if type_of_con == self.cur:
            self.table_name = input("Enter the name of table: ")
            self.user_id = user_id 
            self.user_name = user_name 
            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name}({self.user_name,self.user_id})") 
            self.data = [self.user_name,self.user_id] 
            self.cur.executemany(f"INSERT INTO {self.table_name} VALUE(?,?) ",self.data)  
            print("Success")
         else:
             self.table_name = input()
             if type_of_con == self.cur1:
                 self.cur1.executemany(f"INSERT INTO {self.table_name} VALUE(?,?)",self.data) 
                 print("Success")

db_name = input()

Con = connection() 

connect = Con.con(db_name=db_name)  
type_of_con = connect 
user_name = "Shivam"
user_id = 98754

Con.add_user(user_name=user_name,user_id=user_id,type_of_con=type_of_con)   
