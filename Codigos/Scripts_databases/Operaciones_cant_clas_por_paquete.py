import sqlite3

def agregar_paquete(db,cantidad):

    #Primero obtengo el cursor de la db

    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_paquete ->"+str(e))

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO cant_clas_por_paquete\
          (cantidad)\
          VALUES(?)",(cantidad,))
        print("El paquete se inserto correctamente")
    except Exception as e:
        print("Error al insertar un paquete, en el metodo agregar_paquete -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def eliminar_paquete(db,key):

    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo eliminar_paquete ->" + str(e))

    #Elimino el alumno correspondiente a la key dada.
    try:
        cursor.execute("DELETE FROM cant_clas_por_paquete where ID_cant_clas_por_paquete=?",(key,))
        print("El paquete se elimino correctamente")
    except Exception as e:
        print("Error al eliminar un paquete, en el metodo eliminar_paquete -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def actualizo_paquete(db,key,cantidad):
    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo actualizo_paquete ->" + str(e))

    # Actualizo el email del alumno correspondiente a la key dada.
    try:
        cursor.execute("UPDATE cant_clas_por_paquete set cantidad=? where ID_cant_clas_por_paquete=?",\
                       (cantidad,key,))
        print("El paquete se actualizo correctamente")
    except Exception as e:
        print("Error al actualizar un paquete, en el metodo actualizo_paquete -> " + str(e))

    # Comiteo los cambios a la base de datos.
    db.commit()

if __name__ == "__main__":
    database = sqlite3.connect('..\\..\\Databases\\Academia.db')
    #agregar_paquete(database,1)
    #agregar_paquete(database,4)
    #eliminar_paquete(database,1)
    #actualizo_paquete(database,2,8)
    database.close()