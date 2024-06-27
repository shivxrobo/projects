import sqlite3 
con = sqlite3.connect('test.db') 
cur  = con.cursor() 
# cur.execute("CREATE TABLE Hello(Name,Age,Score)") 
res = cur.execute("SELECT name FROM sqlite_master ") 
a = res.fetchone() 
print(a)
exe = cur.execute(""" INSERT INTO Hello VALUES
                  ('Shivam',23,45) """ ) 
con.commit() 
b = cur.execute("SELECT Age FROM Hello") 
res2 = b.fetchall() 
print(res2)