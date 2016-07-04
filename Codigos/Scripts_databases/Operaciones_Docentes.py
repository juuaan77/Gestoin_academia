import sqlite3
from Operaciones_generales import obtengo_cursor

def agregar_docente(db,nombre,apellido,fecha_nacimiento,dni,email,telefono):

    ##Primero obtengo el cursor de la db
    cursor = obtengo_cursor(db)

    #Genero un arreglo con los datos a insertar
    valores = [nombre,apellido,fecha_nacimiento,dni,email,telefono]

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO docentes\
          (Nombre_y_Apellido, fecha_nacimiento, DNI, Email, Telefono)\
          VALUES(?,?,?,?,?,?)",valores)
        print("El docente se inserto correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al insertar un docente, en el metodo agregar_docente -> " + str(e))

def eliminar_docente(db,key):
    # Primero obtengo el cursor de la db
    cursor = obtengo_cursor(db)

    #Elimino el alumno correspondiente a la key dada.
    try:
        cursor.execute("DELETE FROM docentes where ID_docentes=?",(key,))
        print("El docente se elimino correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al eliminar un docente, en el metodo eliminar_docente -> " + str(e))


def actualizo_email_docente(db,key,email):
    # Primero obtengo el cursor de la db
    cursor = obtengo_cursor(db)

    # Actualizo el email del alumno correspondiente a la key dada.
    try:
        cursor.execute("UPDATE docentes set email=? where ID_docentes=?", (email,key,))
        print("El email del docente se actualizo correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al actualizar el email de un docente, en el metodo actualizo_email_docente -> " + str(e))


def actualizo_telefono_docente(db,key,telefono):
    # Primero obtengo el cursor de la db
    cursor = obtengo_cursor(db)

    # Actualizo el email del alumno correspondiente a la key dada.
    try:
        cursor.execute("UPDATE docentes set telefono=? where ID_docentes=?", (telefono,key,))
        print("El telefono del docente se actualizo correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al actualizar el telefono de un docente, en el metodo actualizo_telefono_docente -> " + str(e))

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
    database = sqlite3.connect('..\\..\\Databases\\Academia.db')
    agregar_docente(database,"juan arese","el 18 de agosto",36935267,"juan_arese@hotmail.com","3564524759")
    #eliminar_docente(database,1)
    #actualizo_email_docente(database,1,"fruta")
    #actualizo_telefono_docente(database,1,6667)
    database.close()

