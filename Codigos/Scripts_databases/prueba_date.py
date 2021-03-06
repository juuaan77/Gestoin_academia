#import mysql.connector
#import datetime

'''db = mysql.connector.connect(user='root',password='root',host='127.0.0.1', database='academia')
cursor = db.cursor()
cursor.execute("CREATE TABLE fecha\
    (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
    fecha_y_hora DATETIME NOT NULL)")

dt = datetime.datetime(2016, 7, 6, 14, 00)
print (dt)

cursor.execute("insert into fecha\
(fecha_y_hora)\
value('{}')".format(dt))'''


from datetime import date, timedelta

(MON, TUE, WED, THU, FRI, SAT, SUN) = range(7)

def addworkdays(start, days, holidays=(), workdays=(MON,TUE,WED,THU,FRI)):
    weeks, days = divmod(days, len(workdays))
    result = start + timedelta(weeks=weeks)
    lo, hi = min(start, result), max(start, result)
    count = len([h for h in holidays if h >= lo and h <= hi])
    days += count * (-1 if days < 0 else 1)
    for _ in range(days):
        result += timedelta(days=1)
        while result in holidays or result.weekday() not in workdays:
            result += timedelta(days=1)
    return result

today = date.today()
print(addworkdays(today, 2))
dias_habiles=[]
for i in range(0,25):
    dias_habiles.append(addworkdays(today, i))

print(dias_habiles)

