import mysql.connector

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
            VALUES('{}',{})".format(nombre, club_de_la_tarea))
        print("El aula se inserto correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al insertar aula, en el metodo agregar_aula -> " + str(e))

if __name__ == "__main__":
    database = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='academia')
    agregar_aula(database, "Aula 1", False)
    database.close()