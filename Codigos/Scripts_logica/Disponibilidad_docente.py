'''
#Obtengo los horarios ocupados del docente requerido

select clases.horario
from clases
join docentes
where (docentes.id)=(clases.id_docente)
and docentes.ID=2

#Opero con esos horarios para ver su disponibilidad.


'''
import mysql.connector,datetime
from Codigos.Scripts_logica.Obtengo_dias_habiles import *

try:
    database = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='academia')
    print("Conexion exitosa al servidor de base de datos")
except Exception as e:
    print(e)

cursor=database.cursor()
#Realizo una consulta, que me entrega el horario de un docente.
cursor.execute("select clases.horario\
                from clases,docentes\
                where (docentes.id)=(clases.id_docente)")#\
                #and docentes.ID=2")

horarios_docentes=[]
for i in cursor:
    horarios_docentes.append(i)
    print(i)

horarios_docentes.sort()
print(horarios_docentes)
#La variable horarios_docentes es una lista ordenada por fecha y hora de los horarios de los docentes.
#para que sea util, la separo en una lista de lista, quedando de la siguiete forma.
#LISTA=[[DIA_OCUPADO,HORARIO],...]
horarios_docentes_parseado=[[]]
for i in range(len(horarios_docentes)):
    fecha = horarios_docentes[i][0].date()
    hora = horarios_docentes[i][0].time()
    horarios_docentes_parseado[i].append(fecha)
    horarios_docentes_parseado[i].append(hora)
    print("me ejecute")

print(horarios_docentes_parseado)

#dias_habiles=lista_dias_habiles()
#La variable dias_habiles es una lista de los dias habiles

#Ahora debo comprar estas dos variables, para asi obtener la disponibilidad del docente
'''for i in range(len(dias_habiles)-1):
    for j in range(len(horarios_docentes)-1):
        if(dias_habiles[i]!=horarios_docentes[j]):'''

#print(horarios_docentes[0] in dias_habiles)

#fecha=horarios_docentes[0][0].date()
#hora=horarios_docentes[0][0].time()

#print(fecha)
#print(hora)






