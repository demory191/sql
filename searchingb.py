#SELECT STATEMENT, without unicode characters

import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#why u no select :()
	c.execute("SELECT firstname, lastname from employees")

	#fetchall() retrieves all records from the query
	rows = c.fetchall()

	#output the rows to the screen, row by row
	for r in rows:
		print ("{0},{1}". format(r[0], r[1]))
