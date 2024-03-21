#SQL Python Connector Documentation can be found here:
# https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html

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

# #Insert a customer data into the tables
# sqlFormula = "INSERT INTO customers (name, age) VALUES (%s, %s)"
# customer1 = ("Sam", 24)
# mycursor.execute(sqlFormula, customer1)
# #Save changes to the DB
# mydb.commit()
    
#Inserting an array of values into the DB
sqlFormula2 = "INSERT INTO customers (name, age) VALUES (%s, %s)"
customers = [("Li", 31),
            ("Ana", 58),
            ("Daniel", 18),
            ("Beatrice", 72),
            ("Omar", 42),
            ("Isabella", 20),
            ("Noah", 6),
            ("Sophia", 35),
            ("William", 88),
            ("Chloe", 27),]

mycursor.executemany(sqlFormula2, customers)
mydb.commit()

#Note: if you want to use the mycursor.execute() command, then you will need to loop through the customers data and implement the sqlFormula. Here is an example:
# for name, age in customers:
#     mycursor.execute(sqlFormula2, (name, age))
# mydb.commit()