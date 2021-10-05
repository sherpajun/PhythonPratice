import sqlite3
import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

con= sqlite3.connect('example.db')

cru=con.cursor()

cru.execute('''CREATE TABLE if not exists stocks
               (date text, trans text, symbol text, qty real, price real)''')

cru.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
con.commit()
cru.close()
