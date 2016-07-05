import mysql.connector

def agregar_nivel(db,nivel,porcentaje_docente):

    #Primero obtengo el cursor de la db

    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_nivel ->"+str(e))

    #Inserto un nuevo alumno con los parametros dados.
    try:
        cursor.execute("INSERT INTO nivel\
          (Nivel,Porcentaje_docente)\
          VALUES('{}',{})".format(nivel,porcentaje_docente,))
        print("El nivel se inserto correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al insertar un nivel, en el metodo agregar_nivel -> " + str(e))

if __name__ == "__main__":
    database = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='academia')
    database.close()