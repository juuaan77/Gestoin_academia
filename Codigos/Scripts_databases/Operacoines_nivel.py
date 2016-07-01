import sqlite3

def agregar_nivel(db,nivel):

    #Primero obtengo el cursor de la db

    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_nivel ->"+str(e))

    #Inserto un nuevo alumno con los parametros dados.
    try:
        cursor.execute("INSERT INTO nivel\
          (Nivel)\
          VALUES(?)",(nivel,))
        print("El nivel se inserto correctamente")
    except Exception as e:
        print("Error al insertar un nivel, en el metodo agregar_nivel -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def eliminar_nivel(db,key):

    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo eliminar_nivel ->" + str(e))

    #Elimino el alumno correspondiente a la key dada.
    try:
        cursor.execute("DELETE FROM nivel where ID_niveles=?",(key,))
        print("El nivel se elimino correctamente")
    except Exception as e:
        print("Error al eliminar un nivel, en el metodo eliminar_nivel -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def actualizo_nivel(db,key,nivel):
    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo actualizo_nivel ->" + str(e))

    # Actualizo el email del alumno correspondiente a la key dada.
    try:
        cursor.execute("UPDATE nivel set nivel=? where ID_niveles=?", (nivel,key,))
        print("El nivel se actualizo correctamente")
    except Exception as e:
        print("Error al actualizar nivel, en el metodo actualizo_nivel -> " + str(e))

    # Comiteo los cambios a la base de datos.
    db.commit()

if __name__ == "__main__":
    database = sqlite3.connect('C:\\Users\\JuanNotebook\\Documents\\GitHub\\Gestoin_academia\\Databases\\Academia.db')

    #agregar_nivel(database,"primario")
    #agregar_nivel(database, "secundaroi")
    #eliminar_nivel(database,1)
    #actualizo_nivel(database,2,"primario y secundario")
    database.close()