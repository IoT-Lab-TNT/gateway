import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anthanh",
  password="25041999"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")