import pymysql

# Conectar a la base de datos
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='UTPL2023',  # Cambia la contraseña si es necesario
    database='utpl',
    port=3306
)

# Función para consultar modalidades
def consultar_modalidad():
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM modalidad;')
        resultados = cursor.fetchall()

        for fila in resultados:
            print(fila[1])  # Imprime solo el nombre de la modalidad
    except Exception as e:
        print(f"Error al consultar modalidades: {e}")
    finally:
        cursor.close()

# Función para insertar una nueva modalidad
def insertar_modalidad(nombre):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO modalidad(nombre) VALUES (%s);", (nombre,))
        conn.commit()
        print(f"Modalidad {nombre} insertada correctamente.")
    except Exception as e:
        print(f"Error al insertar modalidad: {e}")
    finally:
        cursor.close()

# Función para insertar una nueva carrera
def insertar_carrera(codigo, nombre, modalidad_id):
    try:
        cursor = conn.cursor()
        # Asegúrate de que modalidad_id existe en la tabla modalidad antes de insertar
        query = "INSERT INTO carrera(codigo, nombre, modalidad_id) VALUES (%s, %s, %s);"
        cursor.execute(query, (codigo, nombre, modalidad_id))
        conn.commit()
        print(f"Carrera {nombre} insertada correctamente.")
    except Exception as e:
        print(f"Error al insertar carrera: {e}")
    finally:
        cursor.close()

# Insertar modalidades si aún no existen
insertar_modalidad('Presencial')
insertar_modalidad('Virtual')

# Consultar modalidades para verificar que existen
consultar_modalidad()

# Insertar una nueva carrera con un modalidad_id existente
insertar_carrera('COMP_02', 'INGENIERIA EN COMPUTACION', 1)  # Asegúrate de que el ID 1 exista en modalidad

# Cerrar la conexión después de realizar las operaciones
conn.close()
