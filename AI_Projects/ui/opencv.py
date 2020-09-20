import base64
import os
import time
from io import BytesIO

import cv2
from PIL.Image import Image, new

from ui.opencv2 import capture


class K:
    #存base64
    def new(self,i,base64):
        os.makedirs('pic',exist_ok=True)
        
        with open(os.path.join('pic',i+'.txt'),'w') as f:
            f.write(base64)

    def screenshot(self,i):
        capture = cv2.VideoCapture(0)
        ret, frame = capture.read()
        cv2.imshow('capture',frame)
        base64= self.base64n(frame)
        new(i,base64)
        capture.release() #释放摄像头
        cv2.destroyAllWindows()#删除建立的全部窗口
        return 1

    def base64n(self,frame):
        img = Image.fromarray(frame)              #将每一帧转为Image
        output_buffer = BytesIO()                 #创建一个BytesIO
        img.save(output_buffer, format='JPEG')    #写入output_buffer
        byte_data = output_buffer.getvalue()      #在内存中读取
        base64_data = base64.b64encode(byte_data) #转为BASE64
        return base64_data

    def time(self):
        
        c=1
        while(self.screenshot(c)):
            self.screenshot(c)
            if c == 3:
                c=0
            time.sleep(3)
            c=c+1
            
            
    


timeF = 30  #视频帧计数间隔频率
c=1
while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    while ret:
        if(c%timeF == 0): # 每隔timeF帧进行存储操作
            cv2.imwrite('image/'+str(c) + '.jpg',frame) # 存储为图像
        c =c+1
        if cv2.waitKey(1) == ord('q'):
            capture.release() #释放摄像头
            cv2.destroyAllWindows()#删除建立的全部窗口
            break
