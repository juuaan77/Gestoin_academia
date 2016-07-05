import sqlite3
from Operaciones_generales import obtengo_cursor

def agregar_alumno(db,nombre,apellido,fecha_nacimiento,dni,email,telefono):

    #Primero obtengo el cursor de la db
    cursor = obtengo_cursor(db)

    #Genero un arreglo con los datos a insertar
    valores = [nombre,apellido,fecha_nacimiento,dni,email,telefono]

    #Inserto un nuevo alumno con los parametros dados.
    try:
        cursor.execute("INSERT INTO alumnos\
          (Nombre_y_Apellido, fecha_nacimiento, DNI, Email, Telefono)\
          VALUES(?,?,?,?,?,?)",valores)
        print("El alumno se inserto correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al insertar un alumno, en el metodo agregar_alumno -> " + str(e))

def obtener_alumnos_por_nombre(db,apellido):
    # Primero obtengo el cursor de la db
    cursor = obtengo_cursor(db)
    try:
        cursor.execute("select *\
            from alumnos\
           where apellido='{}'".format(apellido))

        alumnos=[]
        for i in cursor:
            alumnos.append(i)

        return alumnos

    except Exception as e:
        print("Error al obtener alumnos por apellidos -> " + str(e))

def obtener_alumnos_por_dni(db,dni):
    # Primero obtengo el cursor de la db
    cursor = obtengo_cursor(db)
    try:
        cursor.execute("select *\
            from alumnos\
           where dni='{}'".format(dni))

        alumnos=[]
        for i in cursor:
            alumnos.append(i)

        return alumnos

    except Exception as e:
        print("Error al obtener alumnos por apellidos -> " + str(e))

if __name__ == "__main__":
    database = sqlite3.connect('..\\..\\Databases\\Academia.db')

    #print(obtener_alumnos_por_nombre(database,"arese"))
    #print(obtener_alumnos_por_dni(database,36935267))
    database.close()


