import mysql.connector
 
# tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "trung",
        passwd = "raspberry", database = "TNTHOLDINGS")
print(myconn)   
# tạo đối tượng cursor
cur = myconn.cursor()  
   
try:
    
    cur.execute("SELECT*FROM user")
    result =  cur.fetchall()
    for x in result:
     print(x)
except:
    myconn.rollback()
 
myconn.close()
