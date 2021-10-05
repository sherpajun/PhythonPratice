import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()
symbol=('IBM',)#중요
sql = f'select * from stocks where symbol = {symbol}'
sql = 'select * from stocks where symbol = {}'.format(symbol)
sql= 'select * from stocks where symbol = %s' % symbol
sql= 'select * from stocks where symbol = ?'

cur.execute(sql,symbol)
#print(cur.fetchall())
data = cur.fetchmany(1) #many일때 갯수지정
for item in data:
    print(item[0],item[2])


data = cur.fetchall() # 전부 다가지고 오는것
for item in data:
    print(item[0],item[2])
cur.close()