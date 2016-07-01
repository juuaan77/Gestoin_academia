import sqlite3

def agregar_costo(db,id_cant_clases,particular,costo_total):

    #Primero obtengo el cursor de la db

    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_costo ->"+str(e))

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO costo_clase\
          (ID_cant_clas,particular,costo_total)\
          VALUES(?,?,?)",(id_cant_clases,particular,costo_total,))
        print("El costo se inserto correctamente")
    except Exception as e:
        print("Error al insertar el costo, en el metodo agregar_costo -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def eliminar_costo(db,key):

    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo eliminar_costo ->" + str(e))

    #Elimino el alumno correspondiente a la key dada.
    try:
        cursor.execute("DELETE FROM costo_clase where ID_costo_clase=?",(key,))
        print("El costo se elimino correctamente")
    except Exception as e:
        print("Error al eliminar un costo, en el metodo eliminar_costo -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def actualizo_costo(db,key,costo,):
    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo actualizo_costo ->" + str(e))

    # Actualizo el email del alumno correspondiente a la key dada.
    try:
        cursor.execute("UPDATE costo_clase set costo_total=? where ID_costo_clase=?",\
                       (costo,key,))
        print("El costo se actualizo correctamente")
    except Exception as e:
        print("Error al actualizar un costo, en el metodo actualizo_costo -> " + str(e))

    # Comiteo los cambios a la base de datos.
    db.commit()

if __name__ == "__main__":
    database = sqlite3.connect('..\\..\\Databases\\Academia.db')
    #agregar_costo(database,2,True,200)
    #agregar_costo(database, 2, False, 100)
    #eliminar_costo(database,1)
    #actualizo_costo(database,2,150)
    database.close()