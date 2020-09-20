# -*- coding: utf-8 -*-
import os
import queue
import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
from PyQt5.QtGui import QPixmap

from analyse.studentStatistic import updateEachWeekWhenWeekend, updateSingleDay, updateEachDayStatus, \
    updateSingleDayAfter
from analyse.unityStatistic import updateGrade


os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
matplotlib.use("Qt5Agg")
import sys
sys.path.append('../analyse')





class UI(object):
    def __init__(self, form):
        self.setup_ui(form)

    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(1200, 800)
        # 原图无图时显示的label
        self.label_raw_pic = QtWidgets.QLabel(form)
        self.label_raw_pic.setGeometry(QtCore.QRect(10, 30, 320, 240))
        self.label_raw_pic.setStyleSheet("background-color:#bbbbbb;")
        self.label_raw_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_raw_pic.setObjectName("label_raw_pic")
        # 原图下方分割线
        self.line1 = QtWidgets.QFrame(form)
        self.line1.setGeometry(QtCore.QRect(340, 30, 20, 431))
        self.line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        # 说明label
        self.label_designer = QtWidgets.QLabel(form)
        self.label_designer.setGeometry(QtCore.QRect(20, 700, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_designer.setFont(font)
        self.label_designer.setObjectName("label_designer")
        # 结果布局设置
        self.layout_widget = QtWidgets.QWidget(form)
        self.layout_widget.setGeometry(QtCore.QRect(10, 310, 320, 240))
        self.layout_widget.setObjectName("layoutWidget")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.layout_widget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setObjectName("verticalLayout")
        # 右侧水平线
        self.line2 = QtWidgets.QFrame(self.layout_widget)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.vertical_layout.addWidget(self.line2)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontalLayout")

        self.pushButton_startupAll = QtWidgets.QPushButton(self.layout_widget)
        self.pushButton_startupAll .setObjectName("pushButton_2")
        self.horizontal_layout.addWidget(self.pushButton_startupAll)

        self.pushButton_Update = QtWidgets.QPushButton(self.layout_widget)
        self.pushButton_Update.setObjectName("pushButton_Up")
        self.horizontal_layout.addWidget(self.pushButton_Update)

        self.pushButton_weekend = QtWidgets.QPushButton(self.layout_widget)
        self.pushButton_weekend.setObjectName("pushButton_3")
        self.horizontal_layout.addWidget(self.pushButton_weekend)

        self.pushButton_clear = QtWidgets.QPushButton(self.layout_widget)
        self.pushButton_clear.setObjectName("pushButton_4")
        self.horizontal_layout.addWidget(self.pushButton_clear)

        self.vertical_layout.addLayout(self.horizontal_layout)
        self.graphicsView = QtWidgets.QGraphicsView(form)
        self.graphicsView.setGeometry(QtCore.QRect(360, 210, 800, 500))
        self.graphicsView.setObjectName("graphicsView")
        self.label_result = QtWidgets.QLabel(form)
        self.label_result.setGeometry(QtCore.QRect(361, 21, 71, 16))
        self.label_result.setObjectName("label_result")
        self.label_emotion = QtWidgets.QLabel(form)
        self.label_emotion.setGeometry(QtCore.QRect(715, 21, 71, 16))
        self.label_emotion.setObjectName("label_emotion")
        self.label_emotion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bar = QtWidgets.QLabel(form)
        self.label_bar.setGeometry(QtCore.QRect(720, 170, 80, 180))
        self.label_bar.setObjectName("label_bar")
        self.line = QtWidgets.QFrame(form)
        self.line.setGeometry(QtCore.QRect(361, 150, 800, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_rst = QtWidgets.QLabel(form)
        self.label_rst.setGeometry(QtCore.QRect(700, 50, 100, 100))
        self.label_rst.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rst.setObjectName("label_rst")
        try:
            self.pushButton_startupAll.clicked.connect(self.startupAll)
            self.retranslate_ui(form)
        except:
            print("exit code -1073740791 (0xC0000409)")
        try:
            self.pushButton_Update.clicked.connect(self.updateEmtions)
            self.retranslate_ui(form)
        except:
            print("exit code -1073740791 (0xC0000409)")


        try:
            self.pushButton_weekend.clicked.connect(self.weekendUpdate)
            self.retranslate_ui(form)
        except:
            print("exit code -1073740791 (0xC0000409)")

        try:
            self.pushButton_clear.clicked.connect(self.clearFace_diagram)
            self.retranslate_ui(form)
        except:
            print("exit code -1073740791 (0xC0000409)")


        QtCore.QMetaObject.connectSlotsByName(form)


    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        pix = QPixmap('../image/sunPic.jpg')
        self.label_raw_pic.setText(_translate("Form", "O(∩_∩)O"))
        self.label_raw_pic.setPixmap(pix)
        # self.label_raw_pic.setGeometry(0, 0, 300, 200)
        # self.label_raw_pic.setStyleSheet("border: 2px solid red")
        self.label_designer.setText(_translate("Form", "SUN"))

        self.pushButton_startupAll.setText(_translate("Form", "启动摄像头"))
        self.pushButton_Update.setText(_translate("Form", "自动更新"))
        self.pushButton_weekend.setText(_translate("Form", "周末分析"))
        self.pushButton_clear.setText(_translate("Form", "清除记录"))

        self.label_result.setText(_translate("Form", " "))
        self.label_emotion.setText(_translate("Form", "摄像头"))
        self.label_bar.setText(_translate("Form", "消息框"))
        self.label_rst.setText(_translate("Form", ""))
        # self.label_bar.setPixmap(pix)

    def clearFace_diagram(self):
        updateSingleDayAfter()

    def updateEmtions(self):
        import time
        a = time.localtime()
        updateSingleDay(int(time.strftime("%w", a)))
        updateEachDayStatus()
        for grade in range(1,4):
            # for clazz in range(1,4):
                # updateClazz(grade,clazz)
            updateGrade(grade)

    def weekendUpdate(self):
        updateEachWeekWhenWeekend()

    def startupAll(self):
        generateVideo()
        # angel()
        print("启动测试")


# python3
import cv2
from PIL import Image
from io import BytesIO

from collection.implement import angel


def frame2base64(frame):
    img = Image.fromarray(frame)  # 将每一帧转为Image
    output_buffer = BytesIO()  # 创建一个BytesIO
    img.save(output_buffer, format='JPEG')  # 写入output_buffer
    byte_data = output_buffer.getvalue()  # 在内存中读取
    # base64_data = base64.b64encode(byte_data) #转为BASE64
    return byte_data  # 转码成功 返回base64编码


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
                file = open('time.jpg', 'wb')
                file.write(base64_data)
                file.close()
                print(base64_data)
                angel()
            c = c + 1

            # cv2.imwrite('../' + 'time.jpg', base64_data)  # 存储为图像

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    except Exception as e:
        print(e)
    finally:
        # 释放资源
        camera.release()
        cv2.destroyAllWindows()





def load_model():
    """
    加载本地模型
    :return:
    """
    from src.model import CNN3
    model = CNN3()
    model.load_weights('./models/cnn3_best_weights.h5')
    return model


def generate_faces(face_img, img_size=48):
    """
    将探测到的人脸进行增广
    :param face_img: 灰度化的单个人脸图
    :param img_size: 目标图片大小
    :return:
    """
    # import cv2
    import numpy as np
    face_img = face_img / 255.
    face_img = cv2.resize(face_img, (img_size, img_size), interpolation=cv2.INTER_LINEAR)
    resized_images = list()
    resized_images.append(face_img)
    resized_images.append(face_img[2:45, :])
    resized_images.append(face_img[1:47, :])
    resized_images.append(cv2.flip(face_img[:, :], 1))

    for i in range(len(resized_images)):
        resized_images[i] = cv2.resize(resized_images[i], (img_size, img_size))
        resized_images[i] = np.expand_dims(resized_images[i], axis=-1)
    resized_images = np.array(resized_images)
    return resized_images


def predict_expression():
    """
    实时预测
    :return:
    """
    # import cv2
    import cv2
    # from utils import index2emotion, cv2_img_add_text
    from src.utils import index2emotion, cv2_img_add_text
    import numpy as np
    # 参数设置
    model = load_model()

    border_color = (0, 0, 0)  # 黑框框
    font_color = (255, 255, 255)  # 白字字
    capture = cv2.VideoCapture(0)  # 指定0号摄像头

    while True:
        _, frame = capture.read()  # 读取一帧视频，返回是否到达视频结尾的布尔值和这一帧的图像
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 灰度化
        cascade = cv2.CascadeClassifier('./data/params/haarcascade_frontalface_alt.xml')  # 检测人脸
        # 利用分类器识别出哪个区域为人脸
        faces = cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=1, minSize=(120, 120))
        # 如果检测到人脸
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                face = frame_gray[y: y + h, x: x + w]  # 脸部图片
                faces = generate_faces(face)
                results = model.predict(faces)
                result_sum = np.sum(results, axis=0).reshape(-1)
                label_index = np.argmax(result_sum, axis=0)
                emotion = index2emotion(label_index)
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), border_color, thickness=2)
                frame = cv2_img_add_text(frame, emotion, x+30, y+30, font_color, 20)
                # puttext中文显示问题
                # cv2.putText(frame, emotion, (x + 30, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, font_color, 4)
        cv2.imshow("expression recognition(press esc to exit)", frame)  # 利用人眼假象

        key = cv2.waitKey(30)  # 等待30ms，返回ASCII码

        # 如果输入esc则退出循环
        if key == 27:
            break
    capture.release()  # 释放摄像头
    cv2.destroyAllWindows()  # 销毁窗口






exitFlag = 0

class myThread (threading.Thread,UI):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q =q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3","Thread-4"]
nameList = ["start", "update", "weekend", "clear"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()
print ("退出主线程")

