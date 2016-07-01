import sqlite3

def agregar_materia(db,materia,id_nivel):

    #Primero obtengo el cursor de la db

    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_materia ->"+str(e))

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO materias\
          (materia,ID_nivel)\
          VALUES(?,?)",(materia,id_nivel,))
        print("La materia se inserto correctamente")
    except Exception as e:
        print("Error al insertar una materia, en el metodo agregar_materia -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def eliminar_materia(db,key):

    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo eliminar_materia ->" + str(e))

    #Elimino el alumno correspondiente a la key dada.
    try:
        cursor.execute("DELETE FROM materias where ID_materia=?",(key,))
        print("El materia se elimino correctamente")
    except Exception as e:
        print("Error al eliminar una materia, en el metodo eliminar_materia -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def actualizo_materia_y_nivel(db,key,materia,id_nivel):
    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo actualizo_materia_y_nivel ->" + str(e))

    # Actualizo el email del alumno correspondiente a la key dada.
    try:
        cursor.execute("UPDATE materias set materia=?, ID_nivel=? where ID_materia=?",\
                       (materia,id_nivel,key,))
        print("La Materia se actualizo correctamente")
    except Exception as e:
        print("Error al actualizar la materia, en el metodo actualizo_materia_y_nivel -> " + str(e))

    # Comiteo los cambios a la base de datos.
    db.commit()

if __name__ == "__main__":
    database = sqlite3.connect('C:\\Users\\JuanNotebook\\Documents\\GitHub\\Gestoin_academia\\Databases\\Academia.db')

    #agregar_materia(database,"fisica",2)
    #agregar_materia(database, "matematicas", 2)
    #eliminar_materia(database,1)
    #actualizo_materia_y_nivel(database,2,"geografia",2)
    database.close()