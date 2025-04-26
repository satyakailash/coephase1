import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mksks@369mksks",
    database="ACE",
    auth_plugin='mysql_native_password'
)
c=conn.cursor()
sid=input("Enter SID to update marks: ")
marks=input("Enter marks to update: ")
c.execute("update Student set marks=%s where sid=%s",(marks,sid))
conn.commit()
c.close()
conn.close()