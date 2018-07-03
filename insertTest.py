import pymysql as sql

conn = sql.connect(host='35.189.118.151',db='test', user='root', password='killbill4')
cur= conn.cursor()


curr.execute("INSERT INTO logs VALUES('T', 'T', 'T', 'T, 'T', 'T', 'T', 'T')")

cur.close()
conn.close()