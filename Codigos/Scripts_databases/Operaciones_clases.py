import mysql.connector

def agregar_clase(db,id_docente,id_materia,id_aula,id_costo_clase,reprogramo,horario):

    #Primero obtengo el cursor de la db

    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
        cursor.execute("PRAGMA foreign_keys = ON")
        db.commit()
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_clase ->"+str(e))

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO clases\
          (id_docente,id_materia,id_aula,reprogramo,horario)\
          VALUES(?,?,?,?,?,?)",(id_docente,id_materia,id_aula,id_costo_clase,reprogramo,horario,))
        print("La clase se inserto correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al insertar una clase, en el metodo agregar_clase -> " + str(e))

def actualizo_reprogramo(db,key,horario):
    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
        cursor.execute("PRAGMA foreign_keys = ON")
        db.commit()
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo actualizo_reprogramo ->" + str(e))

    # Actualizo el email del alumno correspondiente a la key dada.
    try:
        cursor.execute("UPDATE clases set reprogramo=?,horario=? where ID_clases=?",\
                       (True,horario,key,))
        print("Se reprogramo la clase con exito")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al reprogramar la clase, en el metodo actualizo_reprogramo -> " + str(e))

if __name__ == "__main__":
    database = sqlite3.connect('..\\..\\Databases\\Academia.db')
    #agregar_clase(database,1,1,5,False,"a las 3")
    #agregar_clase(database, 1, 1, 5, False, "a las 5")
    #eliminar_clase(database,1)
    #actualizo_aula_de_clase(database,2,6)
    #actualizo_docente_de_clase(database,2,2)
    #actualizo_reprogramo(database,2,"a las 9")
    database.close()