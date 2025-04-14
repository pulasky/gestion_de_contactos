import mysql.connector

# Connect to the MySQL database
personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="personas_db"
)

cursor = personas_db.cursor()

sentencia_sql='INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)'
# Datos a insertar
valores = ('Víctor', 'Ramos', 46)
# Ejecutar la sentencia SQL con los datos
cursor.execute(sentencia_sql, valores)
# Guardar los cambios
personas_db.commit()
print(f'Se ha agregado el nuevo registro: {valores}')
# Cerrar el cursor y la conexión
cursor.close()
personas_db.close()