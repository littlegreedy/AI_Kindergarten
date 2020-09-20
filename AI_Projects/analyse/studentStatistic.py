import configparser
import os
import pymysql
import pymysql.cursors


cf = configparser.ConfigParser()
cpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(cpath, "init.ini")
cf.read(cfgpath,encoding="utf-8")
sec = cf.sections()

def connection(database_key):
    mysql = {'host': '', 'port': 3308, 'user': 'root', 'passwd': '', 'db': '', 'charset': 'utf8'}
    if database_key == cf.get("database","database_key"):
        mysql['host'] = cf.get("database","host")
        mysql['passwd'] = cf.get("database","password")
        mysql['db'] = cf.get("database","db")
    return mysql

# 创建连接

def updateSingleDay(index ):
    # index range of 1 2 3 4 5
    a = ["null", "one", "two", "three", "four", "five"]
    conn = pymysql.connect(**connection('test'))
    # 创建游标
    cursor = conn.cursor()
    # 执行SQL，并返回收影响行数      更新one的值
    effect_row = cursor.execute("UPDATE student,face_diagram SET %s =  (SELECT AVG(expression)*10 FROM face_diagram where face_diagram.number=student.number ) WHERE student.number=face_diagram.number"%(a[index]))
    print(effect_row)
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

def updateSingleDayAfter():
    conn = pymysql.connect(**connection('test'))
    # 创建游标
    cursor = conn.cursor()
    # 执行SQL，并返回收影响行数      更新one的值
    effect_row = cursor.execute("DELETE FROM face_diagram")
    # print(cursor.fetchone())
    print(effect_row)

    print(effect_row)
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

def updateEachDayStatus():
    # index range of 1 2 3 4 5
    a = ["null", "one", "two", "three", "four", "five"]
    conn = pymysql.connect(**connection('test'))
    # 创建游标
    cursor = conn.cursor()

    import time
    a = time.localtime()

    SQL="UPDATE student SET flag= ( "
    if int(time.strftime("%w", a))>= 5:
        today=5
    else:
        today = int(time.strftime("%w", a))

    for num in range(1,today+1):
        if num!=today:
            SQL=SQL+str(a[num])+"+ "
        else:
            SQL = SQL + str(a[num]) + " "
    print(SQL+") / %s "%today)
    # 执行SQL，并返回收影响行数      更新one的值
    effect_row = cursor.execute(SQL+") / %s "%today)
    # print(cursor.fetchone())
    print(effect_row)
    # 提交，不然无法保存新建或者修改的数据
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


def updateEachWeekWhenWeekend():
    # index range of 1 2 3 4 5
    a = ["null", "one", "two", "three", "four", "five"]
    conn = pymysql.connect(**connection('test'))
    # 创建游标
    cursor = conn.cursor()
    # 执行SQL，并返回收影响行数      更新one的值
    effect_row = cursor.execute("UPDATE student SET one=0,two=0,three=0 ,four=0,five=0, last_week=flag, flag=0")
    # print(cursor.fetchone())
    print(effect_row)
    # 提交，不然无法保存新建或者修改的数据
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

def setupPhoto():

    import sys

    try:
        # 用读文件模式打开图片
        # fin = open("../web.jpg")
        fin=open("F:/FileRecv/tupian/1.jpg")
        # 将文本读入img对象中
        img = fin.read().decode("gb18030","ignore")
        # 关闭文件
        fin.close()
    except IOError as e:
        print(e)
    # except IOError  e:
    #     # 如果出错，打印错误信息
    #     # print("Error %d: %s" % (e.args[0], e.args[1])
    #     sys.exit(1)

    # 链接mysql，获取对象
    conn = pymysql.connect(**connection('test'))
    # 获取执行cursor
    cursor = conn.cursor()
    # 直接将数据作为字符串，插入数据库
    cursor.execute("UPDATE student SET PHOTO='%s' WHERE id=1" % pymysql.Binary(img))
    # 提交数据
    conn.commit()
    # 提交之后，再关闭cursor和链接
    cursor.close()
    conn.close()
