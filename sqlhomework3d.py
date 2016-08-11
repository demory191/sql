#print data from the order and cars table concurrently

import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("""SELECT DISTINCT vehicle.Make, vehicle.Model, vehicle.Quantity, orders.order_date WHERE
				vehicle.Model = orders.model ORDER by vehicle.Model ASC""")

	rows = c.fetchall()

	for r in rows:
		print ("Make: {0}, Model {1}". format(r[0], r[1]))
		print "Quantity: " + r[2] 
		print "order dates " + str(r[3])
		print  