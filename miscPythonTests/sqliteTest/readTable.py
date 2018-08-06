
import sqlite3
conn = sqlite3.connect('test.db')

c = conn.cursor()
c.execute('''SELECT * FROM test''')
print(c.fetchall())
conn.close()

