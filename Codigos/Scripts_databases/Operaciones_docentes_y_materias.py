import sqlite3

def agregar_docente_y_materia(db,id_materia,id_docente):

    #Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_docente_y_materia ->"+str(e))

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO docentes_y_materias\
          (id_mat,id_doc)\
          VALUES(?,?)",(id_materia,id_docente ,))
        print("El docente y la materia se inserto correctamente")
    except Exception as e:
        print("Error al insertar docente y la materia, en el metodo agregar_docente_y_materia -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def eliminar_docente_y_materia(db,key):

    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo eliminar_docente_y_materia ->" + str(e))

    #Elimino el alumno correspondiente a la key dada.
    try:
        cursor.execute("DELETE FROM docentes_y_materias where ID_doc_mat=?",(key,))
        print("El docente y materia se elimino correctamente")
    except Exception as e:
        print("Error al eliminar un docente y materia, en el metodo eliminar_docente_y_materia -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

if __name__ == "__main__":
    database = sqlite3.connect('..\\..\\Databases\\Academia.db')
    #agregar_docente_y_materia(database,1,1)
    #agregar_docente_y_materia(database, 1, 1)
    eliminar_docente_y_materia(database,1)
    database.close()