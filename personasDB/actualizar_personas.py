import mysql.connector

# Connect to the MySQL database
personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="personas_db"
)

cursor = personas_db.cursor()

# SQL statement to update a record in the personas table
sentencia_sql = 'UPDATE personas SET nombre = %s, apellido = %s, edad = %s WHERE id = %s'
# Data to update
valores = ('Víctoria', 'Flores', 45, 5)
cursor.execute (sentencia_sql, valores) 
personas_db.commit()
print('Se ha actualizado el registro: ', valores)
# Close the cursor and connection
cursor.close()
personas_db.close()