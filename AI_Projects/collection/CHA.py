import pymysql

def inter(expression,number):
    
    if expression == 'disgust':
        ex=0
    elif expression == 'angry':
        ex=1
    elif expression == 'fear':
        ex=2
    elif expression == 'sad':
        ex=4
    elif expression == 'grimace':
        ex=5
    elif expression == 'pouty':
        ex=6
    elif expression == 'neutral':
        ex=7
    elif expression == 'surprise':
        ex=9
    elif expression == 'happy':
        ex=10
    else:
        print("表情出错")
    
    try:
        db = pymysql.connect(host='127.0.0.1', user='root', password='22817181Zsq', port=3306, db='mysql')
        cursor = db.cursor()
        cursor.execute("select face_id from face_diagram")
        sql="insert into face_diagram(expression,number)values('%s','%s')"
        cursor.execute(sql,(ex,number))
        db.commit()
        cursor.close()
        db.close()
    except Exception:
        print("数据库读取失败")
