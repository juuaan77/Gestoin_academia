import sqlite3

def agregar_docente(db,nombre_y_apellido,fecha_nacimiento,dni,email,telefono):

    #Primero obtengo el cursor de la db

    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_docente ->"+str(e))

    #Genero un arreglo con los datos a insertar
    valores = [nombre_y_apellido,fecha_nacimiento,dni,email,telefono]

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO docentes\
          (Nombre_y_Apellido, fecha_nacimiento, DNI, Email, Telefono)\
          VALUES(?,?,?,?,?)",valores)
        print("El docente se inserto correctamente")
    except Exception as e:
        print("Error al insertar un docente, en el metodo agregar_docente -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def eliminar_docente(db,key):

    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo eliminar_docente ->" + str(e))

    #Elimino el alumno correspondiente a la key dada.
    try:
        cursor.execute("DELETE FROM docentes where ID_docentes=?",(key,))
        print("El docente se elimino correctamente")
    except Exception as e:
        print("Error al eliminar un docente, en el metodo eliminar_docente -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def actualizo_email_docente(db,key,email):
    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo actualizo_email_docente ->" + str(e))

    # Actualizo el email del alumno correspondiente a la key dada.
    try:
        cursor.execute("UPDATE docentes set email=? where ID_docentes=?", (email,key,))
        print("El email del docente se actualizo correctamente")
    except Exception as e:
        print("Error al actualizar el email de un docente, en el metodo actualizo_email_docente -> " + str(e))

    # Comiteo los cambios a la base de datos.
    db.commit()

def actualizo_telefono_docente(db,key,telefono):
    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo actualizo_telefono_docente ->" + str(e))

    # Actualizo el email del alumno correspondiente a la key dada.
    try:
        cursor.execute("UPDATE docentes set telefono=? where ID_docentes=?", (telefono,key,))
        print("El telefono del docente se actualizo correctamente")
    except Exception as e:
        print("Error al actualizar el telefono de un docente, en el metodo actualizo_telefono_docente -> " + str(e))

    # Comiteo los cambios a la base de datos.
    db.commit()

if __name__ == "__main__":
    database = sqlite3.connect('C:\\Users\\JuanNotebook\\Documents\\GitHub\\Gestoin_academia\\Databases\\Academia.db')

    #agregar_docente(database,"juan arese","el 18 de agosto",36935267,"juan_arese@hotmail.com","3564524759")
    #eliminar_docente(database,1)
    #actualizo_email_docente(database,1,"fruta")
    #actualizo_telefono_docente(database,1,6667)
    database.close()

