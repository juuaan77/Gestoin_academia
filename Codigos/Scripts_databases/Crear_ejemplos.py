import mysql.connector
from Operaciones_aulas import agregar_aula

def inserto_datos_ejemplo():
    try:
        database = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='academia')
        print("Conexion exitosa al servidor de base de datos")
    except Exception as e:
        print(e)

    #Primero inserto 4 aulas, fonoaudiologia y cocina.
    agregar_aula(database, "Aula 1",False)
    agregar_aula(database, "Aula 2", False)
    agregar_aula(database, "Aula 3", False)
    agregar_aula(database, "Aula 4", False)
    agregar_aula(database, "Fonoaudiologia", False)
    agregar_aula(database, "Cocina", False)


if __name__ == "__main__":
    inserto_datos_ejemplo()