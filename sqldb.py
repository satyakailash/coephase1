import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mksks@369mksks",
    database="ACE",
    auth_plugin='mysql_native_password'
)
c=conn.cursor()
sid=input("Enter SID: ")
sname=input("Enter SNAME: ")
city=input("Enter CITY: ")
marks=input("Enter MARKS: ")
c.execute("insert into Student(sid,sname,city,marks) values (%s,%s,%s,%s)",(sid,sname,city,marks))
conn.commit()
c.close()
conn.close()