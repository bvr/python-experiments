
# pip install mysql-connector-python
# pip install PyMySQL
# pip install pony

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="packet_parser")
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x) 
