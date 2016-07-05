import sqlite3

def agregar_docente_y_materia(db,id_materia,id_docente):

    #Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
        cursor.execute("PRAGMA foreign_keys = ON")
        db.commit()
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_docente_y_materia ->"+str(e))

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO docentes_y_materias\
          (id_mat,id_doc)\
          VALUES(?,?)",(id_materia,id_docente ,))
        print("El docente y la materia se inserto correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al insertar docente y la materia, en el metodo agregar_docente_y_materia -> " + str(e))

if __name__ == "__main__":
    database = sqlite3.connect('..\\..\\Databases\\Academia.db')
    #agregar_docente_y_materia(database,1,1)
    #agregar_docente_y_materia(database, 1, 1)
    eliminar_docente_y_materia(database,1)
    database.close()