import sqlite3

def agregar_alumno(db,nombre_y_apellido,fecha_nacimiento,dni,email,telefono):

    #Primero obtengo el cursor de la db

    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_alumno ->"+str(e))

    #Genero un arreglo con los datos a insertar
    valores = [nombre_y_apellido,fecha_nacimiento,dni,email,telefono]

    #Inserto un nuevo alumno con los parametros dados.
    try:
        cursor.execute("INSERT INTO alumnos\
          (Nombre_y_Apellido, fecha_nacimiento, DNI, Email, Telefono)\
          VALUES(?,?,?,?,?)",valores)
        print("El alumno se inserto correctamente")
    except Exception as e:
        print("Error al insertar un alumno, en el metodo agregar_alumno -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def eliminar_alumno(db,key):

    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo eliminar_alumno ->" + str(e))

    #Elimino el alumno correspondiente a la key dada.
    try:
        cursor.execute("DELETE FROM alumnos where ID_alumnos=?",(key,))
        print("El alumno se elimino correctamente")
    except Exception as e:
        print("Error al eliminar un alumno, en el metodo eliminar_alumno -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def actualizo_email_alumno(db,key,email):
    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo actualizo_email_alumno ->" + str(e))

    # Actualizo el email del alumno correspondiente a la key dada.
    try:
        cursor.execute("UPDATE alumnos set email=? where ID_alumnos=?", (email,key,))
        print("El email del alumno se actualizo correctamente")
    except Exception as e:
        print("Error al actualizar el email de un alumno, en el metodo actualizo_email_alumno -> " + str(e))

    # Comiteo los cambios a la base de datos.
    db.commit()

def actualizo_telefono_alumno(db,key,telefono):
    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo actualizo_telefono_alumno ->" + str(e))

    # Actualizo el email del alumno correspondiente a la key dada.
    try:
        cursor.execute("UPDATE alumnos set telefono=? where ID_alumnos=?", (telefono,key,))
        print("El telefono del alumno se actualizo correctamente")
    except Exception as e:
        print("Error al actualizar el telefono de un alumno, en el metodo actualizo_telefono_alumno -> " + str(e))

    # Comiteo los cambios a la base de datos.
    db.commit()

if __name__ == "__main__":
    database = sqlite3.connect('..\\..\\Databases\\Academia.db')

    #agregar_alumno(database,"juan arese","some day",36935267,"juan_arese@hotmail.com","3564524759")
    #eliminar_alumno(database,3)
    #actualizo_email_alumno(database,1,"fruta@masfruta.com")
    #actualizo_telefono_alumno(database,1,555)
    database.close()


