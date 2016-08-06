#update quantity of cars and output all records

#import sqlite3
import sqlite3

connection = sqlite3.connect("cars.db")

c = connection.cursor()

c.execute("UPDATE cars SET Quantity = 60 WHERE Model = 'civic'")


for row in (c.fetchall()):
	print row[0], row [1], row[2]

#printing all ford vehicles
fordcars = c.execute("SELECT * FROM cars WHERE Make = 'Ford'")

for eachrow in fordcars:
	print eachrow 

connection.commit()

connection.close()