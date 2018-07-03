import pymysql as sql
def lineReaderandLoad(file):
    conn = sql.connect(host='35.189.118.151', db='test', user='root', password='killbill4')
    cur = conn.cursor()
    unparsed = open(file, mode='r')
    for line in unparsed:
        splitted_line = line.split(' ')
        remote_add = splitted_line[0]
        time_local = splitted_line[3]

        get_line = line.split('"')
        request = get_line[1]

        status = splitted_line[8]
        body_bytes_sent = splitted_line[9]
        http_referer = splitted_line[10]

        browser = splitted_line[11]
        browser1 = browser.split('"')
        b1 = browser1[1]
        final = b1.split('/')
        final_browser = final[0]

        os = splitted_line[12]  + splitted_line[13] + splitted_line[14] + splitted_line[15]

        cur.execute('INSERT INTO logs VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')' %(remote_add,time_local,request,status,body_bytes_sent,http_referer,final_browser,os))




lineReaderandLoad('log_b.txt')

