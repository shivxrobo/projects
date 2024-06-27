import sqlite3 
import os 


class Connection: 
    def __init__(self,db_path) -> None:
        self.db_path = db_path 
    
    def con(self,action,db_name = None,db_path =None):
        self.db_path = db_path 
        self.action = action 
        if self.db_path != None:
            os.chdir(self.db_path) 
            con = sqlite3.connect(self.db_path) 
            cur = con.cursor() 
            if self.action == True:
                self.table_name = input("Enter Table_name: ") 
                self._amount_of_col = int(input("Enter no of colum: ")) 
                cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name}  ") 
                for i in range(self._amount_of_col):
                    col = input("Enter colum value:  ") 
                    cur.executemany(f"INSERT INTO {self.db_path} VALUES (?,?,?) ",col)
                    con.commit()
                    con.close()
            else:
                pass 


c = Connection(r"E:\web") 

c.con(True,r"E:\web") 