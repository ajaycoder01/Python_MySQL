# pip i mysql-connector-python-----------
import mysql.connector as ms

# Create Database Connection-----------

mydb = ms.connect(
    host="localhost",
    user="root",
    password="",
    database = "ajaypy"  # Apply All Query in Database
)

mycursor = mydb.cursor()

# # Create database-----------------------------------------
# mycursor.execute("CREATE DATABASE ajaypy")
# print("Database created!")

# # Show database--------------------------------------------
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)



# # --------Create Table --------------------------------------------
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# # ---------Alter Table --------------------------------------------
# mycursor.execute("ALTER TABLE customers ADD COLUMN age VARCHAR(255)")

# # ----------Insert single Data --------------------------------------------   
# sql = "INSERT INTO customers (name, address, age) VALUES (%s, %s, %s)"
# val = ('Peter', 'Lowstreet 4',34)
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

# # ----------Insert Multiple Data --------------------------------------------
# val = [
# ('Peter', 'Lowstreet 4',34),
# ('Amy', 'Apple st 652',20),
# ('Hannah', 'Mountain 21',21),
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

# -----------Show Last Row Id ------------------------------------------------------
# print("1 record inserted, ID:", mycursor.lastrowid)


# ---------Select All Data----------------------------------------------------
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# ----------Select Name Column Data----------------------------------------------------
# mycursor.execute("SELECT name FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

#------------- Single Row Data --------------------------------------------------
# myresult = mycursor.fetchone()
# print(myresult)

# --------------Where ----------------------------------------------------
# sql = "SELECT * FROM customers WHERE address='Lowstreet 4'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
#-------------------
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ('Highway 21',)
# mycursor.execute(sql,adr)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# Like ----------------------------------------------------
# sql = "SELECT * FROM customers WHERE address Like '%ow%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# Order By & DESC---------------------------------------------------
# sql = "SELECT * FROM customers ORDER BY name "
# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# Delete Row Data-----------------------------------------------------------
# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
#--------------------
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Lowstreet 4", )
# mycursor.execute(sql,adr)
# mydb.commit()
# print(mycursor.rowcount, "records deleted")

# Drop Table ------------------------------------------------------------
# sql = "DROP TABLE customers"
# mycursor.execute(sql)
#-------------------
# sql = "DROP TABLE IF EXISTS customers"
# mycursor.execute(sql)

#----------------- Update Table Data --------------------------------------------------------
# sql = "UPDATE customers SET address = 'Mumbai 105' WHERE address = 'Apple st 652'"
# mycursor.execute(sql)
# mydb.commit() 
# print(mycursor.rowcount, "records affected")
#----------------------
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Apple st 652","Mumbai 105",)
# mycursor.execute(sql,val)
# mydb.commit()
# print(mycursor.rowcount, "records affected")

# #---------------- Limit & Offset -----------------------------------------------------------
# mycursor.execute("SELECT * FROM customers LIMIT 4")
# mycursor.execute("SELECT * FROM customers LIMIT 3 offset 2")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# # ----------------Create Products Table-----------------------------------------------------------
# mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY,  name VARCHAR(255))")
# #---------------
# mycursor.execute("ALTER TABLE customers ADD COLUMN fav VARCHAR(255)")
# #---------------
# sql = "INSERT INTO products (name) VALUES (%s)"
# val = [('Laptop',), ('Mobile',),('Laptop',),("Keyboard",)]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")
# #----------------
# sql = "INSERT INTO customers (name, address, age,fav) VALUES (%s, %s, %s, %s)"
# val = ('Peter', 'Lowstreet 4',34,3)
# mycursor.execute(sql, val)


# # Inner Join -----------------------------------------------------------------
# sql = "SELECT " \
# "customers.name AS customer," \
# "products.name AS favourite  " \
# "FROM customers  " \
# "INNER JOIN products ON customers.fav = products.id "

# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# # Left Join ------------------------------------------------------------------------
# sql = "SELECT " \
# "customers.name AS customer," \
# "products.name AS favourite  " \
# "FROM customers  " \
# "LEFT JOIN products ON customers.fav = products.id "

# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# # Right Join ------------------------------------------------------------------------
# sql = """ SELECT  
# customers.name AS customer, 
# products.name AS favourite  
# FROM customers   
# RIGHT JOIN products ON customers.fav = products.id """

# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)







