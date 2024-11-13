import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='UTPL2023',
    database='utpl',
    port=3306
)

def consultar_modalidad():
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM modalidad;')
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila[1])
    except Exception as e:
        print(f"Error al consultar modalidades: {e}")
    finally:
        cursor.close()

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

def insertar_carrera(codigo, nombre, modalidad_id):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO carrera(codigo, nombre, modalidad_id) VALUES (%s, %s, %s);"
        cursor.execute(query, (codigo, nombre, modalidad_id))
        conn.commit()
        print(f"Carrera {nombre} insertada correctamente.")
    except Exception as e:
        print(f"Error al insertar carrera: {e}")
    finally:
        cursor.close()

insertar_modalidad('Presencial')
insertar_modalidad('Virtual')
consultar_modalidad()
insertar_carrera('COMP_02', 'INGENIERIA EN COMPUTACION', 1)
conn.close()
