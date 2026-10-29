# import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="123456",
#         database="demoapp"
#     )

#     # con = mysql.connector
#     # print("Connected to MySQL successfully")

# except Exception as e:
#     print("Connection failed: ",e)

# cursor = conn.cursor()

# query = "INSERT INTO student (name, course) VALUES (%s, %s)"
# values = ("Rahul", "Python")

# cursor.execute(query, values)
# conn.commit()

# print("Record inserted successfully!")

# cursor.close()
# conn.close()



import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="demoapp"
    )
except Exception as e:
    print("Connected to MySQL successfully")

else:
    print("Connected to MySQL succesfully!")

    cursor = conn.cursor()

    query = "INSERT INTO student (name, course) VALUES (%s, %s)"
    values = ("Rahul", "Python")

    cursor.execute(query, values)
    conn.commit()

    print("Record inserted successfully")

    cursor.execute("SELECT * FROM student")

    for row in cursor:
        print(row)