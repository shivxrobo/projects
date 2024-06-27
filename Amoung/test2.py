import sqlite3 
def user_cre(db_name):
    con = sqlite3.connect(db_name) 
    cur = con.cursor() 
    name = input("Enter name of table: ")
    col1 = input("Enter col1: ") 
    col2 = input("Enter col2: ") 
    col3 = input("Enter col3: ") 
    cur.execute(f"CREATE TABLE {name}({col1},{col2},{col3}) ") 
    name_of = cur.execute("SELECT name FROM sqlite_master  ")
    res = name_of.fetchall() 
    print(res)

connection = sqlite3.connect("Name.db") 

cur = connection.cursor() 

# cre= cur.execute("CREATE TABLE movie(name,rating,year)") 

name_of_table = cur.execute("SELECT name FROM sqlite_master  ")
res = name_of_table.fetchall() 


user_cre("test.db")

print(res)