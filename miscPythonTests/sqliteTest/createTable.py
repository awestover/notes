
import sqlite3
conn = sqlite3.connect('test.db')

c = conn.cursor()
c.execute('''CREATE TABLE test 
             (blah real, a text)
''')
conn.commit()
conn.close()

