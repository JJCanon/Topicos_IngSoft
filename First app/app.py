import mysql.connector

# Configuración de conexión a la base de datos
config = {
    'host': 'localhost', #host
    'user': 'root',        # databse username
    'password': 'rootdatabase01.',  # password
    'database': 'databaseOne' # database name
}

def guardar_nombre(nombre):
    try:
        # Connection to database
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()

        # Insert table name
        query = "INSERT INTO nombres (nombre) VALUES (%s)"
        cursor.execute(query, (nombre,))
        conexion.commit()

        print(f"Nombre '{nombre}' guardado con éxito.")
    except mysql.connector.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def main():
    nombre = input("Introduce un nombre: ")
    guardar_nombre(nombre)

if __name__ == "__main__":
    main()
