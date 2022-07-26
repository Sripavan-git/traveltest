import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root@2002",database="KITS_GEC")
cu=mydb.cursor()
sql = "INSERT INTO cse (id, name) VALUES (%s, %s)"

val = [("002", "GVSSR"),("003","Raghava"),("004","Vilan"),]
cu.execute(sql, val)

mydb.commit()
mydb.close();print("completed!!")