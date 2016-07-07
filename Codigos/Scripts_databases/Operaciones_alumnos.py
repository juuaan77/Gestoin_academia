import mysql.connector
from Codigos.Scripts_databases.Operaciones_generales import obtengo_cursor


def agregar_alumno(db, nombre, apellido, fecha_nacimiento, dni, email, telefono):
    # Primero obtengo el cursor de la db
    cursor = obtengo_cursor(db)

    # Inserto un nuevo alumno con los parametros dados.
    try:
        cursor.execute("INSERT INTO alumnos\
          (nombre, apellido, fecha_nacimiento, dni, email, telefono)\
          VALUES('{}','{}','{}',{},'{}','{}')".format(nombre, apellido, fecha_nacimiento, dni, email, telefono))
        print("El alumno se inserto correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
        return True
    except Exception:
        raise ErrorAgregarAlumno


def obtener_alumnos_por_nombre(db,apellido):
    # Primero obtengo el cursor de la db
    cursor = obtengo_cursor(db)
    try:
        cursor.execute("SELECT *\
            FROM alumnos\
            WHERE apellido='{}'".format(apellido))

        alumnos=[]
        for i in cursor:
            alumnos.append(i)

        return alumnos
    except Exception:
        raise ErrorAlumnoPorNombre


def obtener_alumnos_por_dni(db,dni):
    # Primero obtengo el cursor de la db
    cursor = obtengo_cursor(db)
    try:
        cursor.execute("SELECT *\
            FROM alumnos\
            WHERE dni='{}'".format(dni))

        alumnos=[]
        for i in cursor:
            alumnos.append(i)

        return alumnos

    except Exception:
        raise ErrorAlumnoPorDNI


class ErrorAgregarAlumno(Exception):
    def __str__(self):
        return "No se pudo crear el alumno"


class ErrorAlumnoPorNombre(Exception):
    def __str__(self):
        return "No se pudo buscar el alumno por nombre"


class ErrorAlumnoPorDNI(Exception):
    def __str__(self):
        return "No se pudo buscar el alumno por DNI"


if __name__ == "__main__":
    database = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='academia')
    # agregar_alumno(database, "Juan", "Arese", "18/08/1992", 36935267, "juan_arese@hotmail.com", "3564-524759")
    database.close()

