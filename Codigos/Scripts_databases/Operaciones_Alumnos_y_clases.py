import mysql.connector

def agregar_alumno_y_clase(db,id_alumno,id_clase):

    #Primero obtengo el cursor de la db

    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
        cursor.execute("PRAGMA foreign_keys = ON")
        db.commit()
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_alumno_y_clase ->"+str(e))

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO alumnos_y_clases\
          (id_alumno,id_clase)\
          VALUES({},{})".format(id_alumno,id_clase))
        print("El alumno y clase se inserto correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al insertar alumno y clase, en el metodo agregar_alumno_y_clase -> " + str(e))

if __name__ == "__main__":
    database = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='academia')
    database.close()