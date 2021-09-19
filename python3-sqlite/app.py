import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')

# create table
# c.execute(""" CREATE TABLE customers (
#     first_name text,
#     last_name text,
#     email text
# )""")

# create cursor
c = conn.cursor()

#c.execute("INSERT INTO customers VALUES ('Tim','Depp','tmdepp@gmail.com')")

# c.execute("SELECT rowid, * FROM customers")
# c.execute("SELECT * FROM customers WHERE first_name = 'Tim'")
c.execute("SELECT * FROM customers WHERE first_name LIKE '%ohn%'")

items = c.fetchall()

for item in items:
    print(item)

# commit a command
conn.commit()

# close the connecton
conn.close()
