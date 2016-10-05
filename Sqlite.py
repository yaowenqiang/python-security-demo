import sqlite3

conn = sqlite3.connect('dbname.db')

cur = conn.cursor()
for row in cur.execute('select * from table'):
    print(row)
