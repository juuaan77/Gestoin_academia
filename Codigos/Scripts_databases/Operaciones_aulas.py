import sqlite3

def agregar_aula(db,nombre,club_de_la_tarea):

    #Primero obtengo el cursor de la db

    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_aula ->"+str(e))

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO aulas\
          (nombre,club_de_la_tarea)\
          VALUES(?,?)",(nombre,club_de_la_tarea ,))
        print("El aula se inserto correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al insertar aula, en el metodo agregar_aula -> " + str(e))

def eliminar_aula(db,key):

    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo eliminar_aula ->" + str(e))

    #Elimino el alumno correspondiente a la key dada.
    try:
        cursor.execute("DELETE FROM aulas where ID_aulas=?",(key,))
        print("El aula se elimino correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al eliminar un aula, en el metodo eliminar_aula -> " + str(e))

def actualizo_aula_y_club_de_la_tarea(db,key,nombre,club_de_la_tarea):
    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo actualizo_aula_y_club_de_la_tarea ->" + str(e))

    # Actualizo el email del alumno correspondiente a la key dada.
    try:
        cursor.execute("UPDATE aulas set nombre=?, club_de_la_tarea=? where ID_aulas=?",\
                       (nombre,club_de_la_tarea,key,))
        print("El aula se actualizo correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al actualizar un aula, en el metodo actualizo_aula_y_club_de_la_tarea -> " + str(e))

if __name__ == "__main__":
    database = sqlite3.connect('..\\..\\Databases\\Academia.db')

    #agregar_aula(database,"aula1",False)
    #agregar_aula(database,"cocina",True)
    #eliminar_aula(database,1)
    #actualizo_aula_y_club_de_la_tarea(database,2,"fonoaudiologia",False)
    database.close()