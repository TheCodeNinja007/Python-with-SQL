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
mycursor.execute("CREATE TABLE IF NOT EXISTs customers(name VARCHAR(255), age INT(30))")

#Check created table
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

# #Insert a customer data into the tables
# sqlInsert = "INSERT INTO customers (name, age) VALUES (%s, %s)"
# customer1 = ("Sam", 24)
# mycursor.execute(sqlInsert, customer1)
# #Save changes to the DB
# mydb.commit()
    
#Inserting an array of values into the DB
# sqlInsertMany = "INSERT INTO customers (name, age) VALUES (%s, %s)"
# customers = [("Li", 31),
#             ("Ana", 58),
#             ("Daniel", 18),
#             ("Beatrice", 72),
#             ("Omar", 42),
#             ("Isabella", 20),
#             ("Noah", 6),
#             ("Sophia", 35),
#             ("William", 88),
#             ("Chloe", 27),]

# mycursor.executemany(sqlInsertMany, customers)
# mydb.commit()

#Note: if you want to use the mycursor.execute() command, then you will need to loop through the customers data and implement the sqlFormula. Here is an example:
# for name, age in customers:
#     mycursor.execute(sqlFormula2, (name, age))
# mydb.commit()

#Selecting & Getting Data
#Select the required data
# mycursor.execute("SELECT * FROM customers")
# #save it to a variable
# results = mycursor.fetchall()
# #print it to the screen
# for row in results:
#     print(row)

#Select specific data
# mycursor.execute("SELECT age FROM customers")
# age_results = mycursor.fetchall()
# for row in age_results:
#     print(row)

#Select one entry
# mycursor.execute("SELECT age FROM customers")
# #return first result with fetchone() method
# one_entry = mycursor.fetchone()
# for row in one_entry:
#     print(row)

#Filtering results
# sqlFilter = "SELECT * FROM customers WHERE name='Ana'"
# mycursor.execute(sqlFilter)
# results = mycursor.fetchall()

# for row in results:
#     print(row)

#Wildcard charatcers (fetch any thing that matches what is inside, before or after the % signs)
# sqlWildCard = "SELECT * FROM customers WHERE name LIKE '%W%'"

# mycursor.execute(sqlWildCard)
# wildcard_results = mycursor.fetchall()
# for row in wildcard_results:
#     print(row)

# # Updating Entries and Limiting Queries
# mycursor = mydb.cursor()
# sqlUpdate = "UPDATE customers SET age = 31 WHERE name = 'Ana'"
# mycursor.execute(sqlUpdate)
# mydb.commit()

# #Limiting the number of results from a query (add the 'OFFSET' statement to start after a specific row)
# sqlSelect = "SELECT * FROM customers LIMIT 5 OFFSET 2"
# mycursor.execute(sqlSelect)
# results = mycursor.fetchall()
# for row in results:
#     print(row)

# #Ordering Query Results
# sqlOrder = "SELECT * FROM customers ORDER BY name"
# mycursor.execute(sqlOrder)
# results = mycursor.fetchall()
# for row in results:
#     print(row)

# sqlOrderDesc = "SELECT * FROM customers Order BY age DESC"
# mycursor.execute(sqlOrderDesc)
# results = mycursor.fetchall()
# for row in results:
#     print(row)

# #Deleting Records and Droping Tables
# sqlDelete = "DELETE FROM customers WHERE name = 'Ana' "
# mycursor.execute(sqlDelete)
# mydb.commit()

# results = mycursor.fetchall()
# for row in results:
#     print(row)

# #Dropping a table
# sqlDrop = "DROP TABLE IF EXISTS customers"
# mycursor.execute(sqlDrop)
# mydb.commit()