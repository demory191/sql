#importing the sqlite library
import sqlite3

#create new db connection
conn = sqlite3.connect("cars.db")

#get cursor object to execute sqlite statements
cursor = conn.cursor()

#create car table
cursor.execute("""CREATE TABLE cars(Make TEXT, Model TEXT, Quantity NUMERIC)""")

#close connection
conn.close()









