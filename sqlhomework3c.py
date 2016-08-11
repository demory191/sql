#adding another table to the cars table

import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	#create table
	#c.execute("""CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)""")

	orderlist = [
				("Ford", "Taurus", "2010-08-07"),
				("Ford", "Taurus", "2011-08-07"),
				("Ford", "Taurus", "2012-08-07"),
				("Ford", "explorer", "2010-08-07"),
				("Ford", "explorer", "2011-08-07"),
				("Ford", "explorer", "2012-08-07"),
				("Ford", "Mustang", "2010-08-07"),
				("Ford", "Mustang", "2011-08-07"),
				("Ford", "Mustang", "2012-08-07"),
				("Honda", "Accord", "2010-08-07"),
				("Honda", "Accord", "2011-08-07"),
				("Honda", "Accord", "2012-08-07"),
				("Honda", "civic", "2010-08-07"),
				("Honda", "civic", "2011-08-07"),
				("Honda", "civic", "2012-08-07"),
				]

	c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orderlist)

	c.execute("SELECT * FROM orders ORDER by model ASC")

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]

