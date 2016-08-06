#adding execption handling to the insert command

#import sqlite3 library
import sqlite3

#create the connecton object
connection = sqlite3.connect("new.db")

#get a cursor object used to execure sql commands
c = connection.cursor()

try:
	#insert data
	c.execute("INSERT INTO populations VALUES('New York City',\'NY', 8200000)")

	c.execute("INSERT INTO populations VALUES('San Francisco',\'CA',800000)")

	#commit changes
	c.commit()

except sqlite3.OperationalError:
	print "Oops! something went wrong. Try again..."

#close the database connection
c.close()

