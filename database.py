import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="mydb")

cursor=mydb.cursor()

cursor.execute("insert into account values(2,'Asif','Asif','1234')")
cursor.execute("Select * from account")

for i in cursor:
     print(i)


