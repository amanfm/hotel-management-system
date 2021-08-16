import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "amanshah",
)
my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE hms")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)
