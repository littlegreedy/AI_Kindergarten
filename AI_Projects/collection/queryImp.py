import pymysql

#插入数据库
def Op(ho,us,pa,po,d):
    db = pymysql.connect(host=ho, user=us, password=pa, port=po, db=d)
    return db
def Cl(db):
    db.close()

def Cha(db,expression,number,ti):
    
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
         c = number
         cursor = db.cursor()
         sql="insert into face_diagram(Expression,number)values('%s','%s')"%(ex,c)
         cursor.execute(sql)
         db.commit()
         cursor.close()
         ti=ti+1
         print("录入成功")
         return ti
    except Exception:
        print("数据库存入失败")
#获取number和photo
def Query(db):
    
    cursor = db.cursor()
    cursor.execute("select number,photo from student")
    result = cursor.fetchall()
    db.commit()
    cursor.close()
    return result

#获取数据库个数
def time(db):
    
    cursor = db.cursor()
    time=cursor.execute("select number from student")
    db.commit()
    cursor.close()
    
    return time