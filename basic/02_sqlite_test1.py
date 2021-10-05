import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()


data =[
    ('2006-01-05', 'BUY', 'RHAT', 100, 35.14),
    ('2006-03-28', 'BUY', 'IBM', 1000, 45.0),
    ('2006-04-06', 'SELL', 'IBM', 500, 53.0),
    ('2006-04-05', 'BUY', 'MSFT', 1000, 72.0),
]


cur.executemany('insert into stocks values(?,?,?,?,?)',data)
con.commit()
cur.close()
