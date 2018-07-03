import pymysql as sql

conn = sql.connect(host='35.189.118.151',db='test', user='root', password='killbill4')
cur= conn.cursor()
cur.execute('CREATE TABLE logs(remote_add varchar(100), time_local varchar(100), request varchar(100), status varchar(100), body_bytes_sent varchar(100), http_referer varchar(100), final_browser varchar(100), os varchar(100)' )
cur.close()
conn.close()
