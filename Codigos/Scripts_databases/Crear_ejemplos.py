import mysql.connector,datetime
from Codigos.Scripts_databases.Operaciones_aulas import *
from Codigos.Scripts_databases.Operaciones_alumnos import *
from Codigos.Scripts_databases.Operaciones_nivel import *
from Codigos.Scripts_databases.Operaciones_materias import *
from Codigos.Scripts_databases.Operaciones_cant_clas_por_paquete import *
from Codigos.Scripts_databases.Operaciones_Costo_clase import *
from Codigos.Scripts_databases.Operaciones_Docentes import *
from Codigos.Scripts_databases.Operaciones_docentes_y_materias import *
from Codigos.Scripts_databases.Operaciones_clases import *
from Codigos.Scripts_databases.Operaciones_Alumnos_y_clases import *

def inserto_datos_ejemplo():
    try:
        database = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='academia')
        print("Conexion exitosa al servidor de base de datos")
    except Exception as e:
        print(e)
    '''
    Primero inserto 4 aulas, fonoaudiologia y cocina.
    agregar_aula(database, "Aula 1",False)
    agregar_aula(database, "Aula 2", False)
    agregar_aula(database, "Aula 3", False)
    agregar_aula(database, "Aula 4", False)
    agregar_aula(database, "Fonoaudiologia", False)
    agregar_aula(database, "Cocina", False)

    fecha=datetime.date(1992,8,18)
    agregar_alumno(database,"Juan","Arese",str(fecha),36935267,"juan_arese@hotmail.com","3564-524759")
    fecha=datetime.date(1991,8,18)
    agregar_alumno(database, "Arian", "Giles Garcia", str(fecha), 36201187, "arian2822@gmail.com", "2923-440464")
    fecha=datetime.date(1992,8,17)
    agregar_alumno(database, "Pablo", "Galarza", str(fecha), 36935282, "pablo_galarza@hotmail.com", "3564-525252")

    agregar_nivel(database, "Primario",10)
    agregar_nivel(database, "Secundario", 20)
    agregar_nivel(database, "Terciario", 30)
    agregar_nivel(database, "Universitario", 40)

    agregar_materia(database, "Fisica", 1)
    agregar_materia(database, "Matematica", 2)
    agregar_materia(database, "Informatica", 3)
    agregar_materia(database, "Arquitectura de computadoras", 4)

    agregar_paquete(database, 1)
    agregar_paquete(database, 2)
    agregar_paquete(database, 4)
    agregar_paquete(database, 8)
    agregar_paquete(database, 12)

    agregar_costo(database, 1, True, 200)
    agregar_costo(database, 2, True, 350)
    agregar_costo(database, 3, True, 650)
    agregar_costo(database, 1, False, 100)
    agregar_costo(database, 2, False, 250)

    fecha=datetime.date(1954,4,24)
    agregar_docente(database, "Gerardo", "Morelli", str(fecha), 15789685, "Gerardo.moreli@gmail.com", "351-545859")
    fecha=datetime.date(1965,5,15)
    agregar_docente(database, "Orlando", "Micolini", str(fecha), 17779685, "Orlando.micolini@gmail.com", "351-748596")
    fecha=datetime.date(1970,8,12)
    agregar_docente(database, "daniel", "Joaquin", str(fecha), 19789685, "Daniel.Joaquin@gmail.com", "351-124578")

    agregar_docente_y_materia(database, 13, 1)
    agregar_docente_y_materia(database, 16, 2)
    agregar_docente_y_materia(database, 14, 3)

    dt = datetime.datetime(2016, 7, 6, 14, 00)
    agregar_clase(database, 1, 13, 2, 1, False, str(dt))
    dt = datetime.datetime(2016, 7, 7, 14, 00)
    agregar_clase(database, 2, 16, 3, 1, False, str(dt))

    agregar_alumno_y_clase(database, 1, 1)
    agregar_alumno_y_clase(database, 2, 1)
    agregar_alumno_y_clase(database, 3, 2)
    '''
if __name__ == "__main__":
    inserto_datos_ejemplo()