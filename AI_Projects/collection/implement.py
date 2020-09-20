from collection.face_location import Face_location

def angel():
    pt = "time.jpg"
    p = r"time.jpg"

    location = Face_location(p, pt)
    judge = location.gan()

    try:
        for i in range(1, 4):
            if judge['result']['face_num'] > 0:
                print(judge['result']['face_num'])
                location.cut()
    except Exception:
        print('已经查完')