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
    if database_key == cf.get("database", "database_key"):
        mysql['host'] = cf.get("database", "host")
        mysql['passwd'] = cf.get("database", "password")
        mysql['db'] = cf.get("database", "db")
    return mysql


# 创建连接

def updateClazz(gradeid, clazzid):
    conn = pymysql.connect(**connection('test'))
    # 创建游标
    cursor = conn.cursor()
    gradeid1=gradeid
    clazzid1=clazzid
    # 执行SQL，并返回收影响行数      更新one的值
    effect_row = cursor.execute("UPDATE clazz SET total=(SELECT AVG(flag) FROM student WHERE gradeid=%s AND clazzid=%s) WHERE gradeid=%s AND name= %s班 " %(gradeid,clazzid,gradeid,clazzid))
    # # print(cursor.fetchone())
    print(effect_row)
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

#  1 2 3 grade
def updateGrade(gradeid):
    conn = pymysql.connect(**connection('test'))
    # 创建游标
    cursor = conn.cursor()
    # 执行SQL，并返回收影响行数      更新one的值
    effect_row = cursor.execute("UPDATE grade SET total=(SELECT AVG(total) FROM clazz WHERE gradeid=%s ) WHERE id=%s "% (gradeid ,gradeid))
    # # print(cursor.fetchone())
    print(effect_row)
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()