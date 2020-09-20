from collection.queryImp import Query


def b_p(a,db):
    c=Query(db)
    f=c[a][1]

    try:
        fout = open('fin.jpg','wb')
        fout.write(f)
        fout.close()
        ku = 'fin.jpg'
        return ku
    except Exception:
        print ("读取错误")