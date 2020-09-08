import mysql.connector
 
# tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "anthanh",
        passwd = "25041999", database = "demo")
   
# tạo đối tượng cursor
cur = myconn.cursor()  
   
try:
    # tạo bảng Employee gồm 4 cột name, id, salary, và department id  
    dbs = cur.execute("create table data(name varchar(20) not null, "
        + "id int(20) not null primary key, "
        + "u float not null, "
        + "i int not null, "
        + "w int not null)")
except:
    myconn.rollback()
 
myconn.close()