#Establish connection with mysql
import mysql.connector
from config import DB_PASSWORD

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=DB_PASSWORD,
    database="test_db2"
)
# print("Connector is working: ", mydb)

#Initialise the cursor (the object that communicates with MySQL Server)
mycursor = mydb.cursor()

#Create a new database
# mycursor.execute("CREATE DATABASE test_db2")

#Check available databases
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

#Create a table in the database #Remember to add the dtabase name within the connection configuration lines above to point to the database you created!
# mycursor.execute("CREATE TABLE customers(name VARCHAR(255), age INT(30))")

#Check created table
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)



