#importing random generator module
import random

#import sqlite3
import sqlite3

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	#create table into db
	c.execute("DROP TABLE if exists numbers")
	c.execute("CREATE TABLE numbers(num int)")

	#insert random values from 1-100
	for i in range(100):
		c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0,100),))
