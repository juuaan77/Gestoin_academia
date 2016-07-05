import mysql.connector
import datetime

db = mysql.connector.connect(user='root',password='root',host='127.0.0.1', database='academia')
cursor = db.cursor()
'''cursor.execute("CREATE TABLE fecha\
    (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
    fecha_y_hora DATETIME NOT NULL)")'''

dt = datetime.datetime(2016, 7, 6, 14, 00)
print (dt)
'''
cursor.execute("insert into fecha\
(fecha_y_hora)\
value('{}')".format(dt))'''

fecha=datetime.date(2016,7,6)
print (fecha)

db.commit()

