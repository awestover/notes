
import sqlite3

conn = sqlite3.connect("test.db")
c=conn.cursor()
entries = [(1,"asdf"), (2, "asdfff")]
c.executemany('INSERT INTO test VALUES (?,?)', entries)
conn.commit()
conn.close()

