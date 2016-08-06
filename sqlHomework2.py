#inserting data into the cars.db

#import sqlite3
import sqlite3

#create database connecton:
connection = sqlite3.connect("cars.db") 

#get cursor object
c = connection.cursor()

#list of Tupule each car

carlist=[
		('Ford', 'Taurus', 15),
		('Ford', 'explorer', 25),
		('Ford', 'Mustang' , 5),
		('Honda', 'Accord', 50),
		('Honda', 'civic', 40)
		]

#insert 5 records
c.executemany('INSERT INTO  cars VALUES(?,?,?)', carlist)

#commit into db
connection.commit()

#close connection
connection.close()