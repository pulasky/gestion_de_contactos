import mysql.connector
# Connect to the MySQL database
personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="personas_db"
)

cursor = personas_db.cursor()
# Select all personas from the personas table
cursor.execute("SELECT * FROM personas")
resultado=cursor.fetchall()
for persona in resultado:
    print(persona)
# Close the cursor and connection
cursor.close()
personas_db.close()