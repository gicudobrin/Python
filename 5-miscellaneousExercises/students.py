import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mihai1987",
  database="ana"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
			