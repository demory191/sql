import sqlite3

connection = sqlite3.connect("newnum.db")
c = connection.cursor()

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

while True:
	user_choice = raw_input(prompt)

	print "track1"
	if user_choice in set(["1","2","3","4"]):
		operation = {1: "avg", 2:"max", 3:"min", 4:"sum"}[int(user_choice)]

		#retrieve data
		c.execute("SELECT {}(num) from numbers".format(operation))

		get = c.fetchone()

		print operation + ": %f" %get[0]

	elif user_choice == "5":
		print "exiting..."
		break
