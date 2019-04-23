"""

sudo apt-get install sqlitebrowser


python sqlite is very nice

it is a miny sql

it has some stuff but not a lot of stuff

import sqlite3

etc
"""
import sqlite3

"""

Very usefull
https://www.youtube.com/watch?v=o-vsdfCBpsU

"""

conn = sqlite3.connect("tutorial.db")

c= conn.cursor()


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datetimestamp TEXT, keyword TEXT, value REAL)')



def data_entry():
	c.execute("INSERT INTO stuffToPlot VALUES(12341234, '2016-01-01', 'Python', 5)")
	conn.commit()
	c.close()
	conn.close()

create_table()
data_entry()


