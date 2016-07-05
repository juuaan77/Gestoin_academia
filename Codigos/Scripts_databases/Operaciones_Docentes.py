import mysql.connector
from Operaciones_generales import obtengo_cursor

def agregar_docente(db,nombre,apellido,fecha_nacimiento,dni,email,telefono):

    ##Primero obtengo el cursor de la db
    cursor = obtengo_cursor(db)

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO docentes\
          (Nombre,Apellido, fecha_nacimiento, DNI, Email, Telefono)\
          VALUES('{}','{}','{}',{},'{}','{}')".format(nombre,apellido,fecha_nacimiento,dni,email,telefono))
        print("El docente se inserto correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al insertar un docente, en el metodo agregar_docente -> " + str(e))

def obtener_docente_por_nombre(db,apellido):
    # Primero obtengo el cursor de la db
    cursor = obtengo_cursor(db)
    try:
        cursor.execute("select *\
            from docente\
           where apellido='{}'".format(apellido))

        docentes=[]
        for i in cursor:
            docentes.append(i)

        return docentes

    except Exception as e:
        print("Error al obtener alumnos por apellidos -> " + str(e))

def obtener_docente_por_dni(db,dni):
    # Primero obtengo el cursor de la db
    cursor = obtengo_cursor(db)
    try:
        cursor.execute("select *\
            from docentes\
           where dni='{}'".format(dni))

        docentes=[]
        for i in cursor:
            docentes.append(i)

        return docentes

    except Exception as e:
        print("Error al obtener alumnos por apellidos -> " + str(e))

if __name__ == "__main__":
    database = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='academia')
    database.close()

