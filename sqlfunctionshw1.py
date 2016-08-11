#counting the total nnumber of orders for each make

import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	sql = {'fordcount' : "SELECT count(make) from orders WHERE make = 'Ford'", 
			'hondacount' : "SELECT count(make) from orders WHERE make = 'Honda'", 
			}

	for keys,values in sql.iteritems():
		c.execute(values)

		#result 
		result = c.fetchone()

		#output
		print keys + ";", result