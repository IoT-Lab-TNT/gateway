import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anthanh",
  password="25041999",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")