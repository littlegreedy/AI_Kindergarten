
#python3
import cv2
from pillow import Image
from io import BytesIO

from collection.implement import angel


def frame2base64(frame):
    img = Image.fromarray(frame) #将每一帧转为Image
    output_buffer = BytesIO() #创建一个BytesIO
    img.save(output_buffer, format='JPEG') #写入output_buffer
    byte_data = output_buffer.getvalue() #在内存中读取
    # base64_data = base64.b64encode(byte_data) #转为BASE64
    return byte_data #转码成功 返回base64编码
 
def generateVideo():
    camera = cv2.VideoCapture(0)
    timeF = 1000  # 视频帧计数间隔频率
    c = 1
    try:
        while True:
            ret, frame = camera.read()
            cv2.imshow("camera", frame)
            base64_data = frame2base64(frame)
            if (c % timeF == 0):  # 每隔timeF帧进行存储操作
                file = open('../ui/time.jpg', 'wb')
                file.write( base64_data)
                file.close()
                print(base64_data)
                angel()
                print("完毕")
            c=c+1

            # cv2.imwrite('../' + 'time.jpg', base64_data)  # 存储为图像

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    except Exception as e:
        print(e)
    finally:
        # 释放资源
        camera.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':

    generateVideo()