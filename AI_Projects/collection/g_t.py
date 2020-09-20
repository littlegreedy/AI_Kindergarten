import pymysql
def time():
    db = pymysql.connect(host='127.0.0.1', user='root', password='1000', port=3308, db='ssms')
    cursor = db.cursor()
    time=cursor.execute("select number,photo from student")
    db.commit()
    cursor.close()
    db.close()
    return time