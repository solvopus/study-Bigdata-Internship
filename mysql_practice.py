#https://pymysql.readthedocs.io/en/latest/modules/connections.html

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='admin',
                           charset='utf8')
curs = conn.cursor()


sql = "SHOW DATABASES"
curs.execute(sql)
for i in curs.fetchall():
    print(i[0])
    
conn.close()