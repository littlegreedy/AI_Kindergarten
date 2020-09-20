# -*-coding:utf-8-*-

#摄像头前端界面+初步处理
def load_model():
    """
    本地模型
    :return:
    """
    from model import CNN3
    model = CNN3()
    model.load_weights('../models/cnn3_best_weights.h5')
    return model


def generate_faces(face_img, img_size=48):
    """
    探测到的人脸进行增广处理
    :param face_img: 灰度化的单个人脸
    :param img_size: 图片大小
    :return:
    """
    import cv2
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
    预测函数
    :return:
    """
    import cv2
    from utils import index2emotion, cv2_img_add_text
    import numpy as np

    # 参数设置
    model = load_model()

    border_color = (255, 0, 0)  # 黑框
    font_color = (255, 255, 255)  # 白字
    capture = cv2.VideoCapture(0)  # 指定0号摄像头

    while True:
        _, frame = capture.read()  # 读取一帧视频，返回是否到达视频结尾的布尔值和这一帧的图像
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 灰度化
        cascade = cv2.CascadeClassifier('../data/params/haarcascade_frontalface_alt.xml')  # 检测人脸
        # 利用分类器识别出哪个区域为人脸
        faces = cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
        '''在进行眼睛检测的时候多了几个参数。detectMultiScale有许多可选参数；在人脸检测时，默认选项足以检测人脸，但是眼睛是一个比较小的人脸特征，
        并且胡子或者鼻子的本身阴影以及帧的随机阴影都会产生假阳性。通过限制对眼睛搜索的最小尺寸为40x40像素，可以去掉假阳性。然后测试这些参数，
        直至应用程序可以满足预期(例如可以尝试指定特征的最大尺寸，或增加比例因子以及近邻的数量)。
        下面我们来总结一下detectMultiScale函数：
        detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]])
        image：表示的是要检测的输入图像
        scaleFactor：为每一个图像尺度中的尺度参数，默认值为1
        .1。scaleFactor参数可以决定两个不同大小的窗口扫描之间有多大的跳跃，这个参数设置的大，则意味着计算会变快，但如果窗口错过了某个大小的人脸，则可能丢失物体。
        minNeighbors：参数为每一个级联矩形应该保留的邻近个数，默认为3。minNeighbors控制着误检测，默认值为3表明至少有3次重叠检测，我们才认为人脸确实存。
        flags：对于新的分类器没有用（但目前的haar分类器都是旧版的，CV_HAAR_DO_CANNY_PRUNING, 这个值告诉分类器跳过平滑（无边缘区域）。
        利用Canny边缘检测器来排除一些边缘很少或者很多的图像区域；CV_HAAR_SCALE_IMAGE，这个值告诉分类器不要缩放分类器。而是缩放图像（处理好内存和缓存的使用问题，这可以提高性能。）就是按比例正常检测；CV_HAAR_FIND_BIGGEST_OBJECTS，告诉分类器只返回最大的目标（这样返回的物体个数只可能是0或1）只检测最大的物，CV_HAAR_DO_ROUGH_SEARCH，他只可与CV_HAAR_FIND_BIGGEST_OBJECTS一起使用，这个标志告诉分类器在任何窗口，只要第一个候选者被发现则结束寻找（当然需要足够的相邻的区域来说明真正找到了。）, 只做初略检测.
        minSize：为目标的最小尺寸
        maxSize：为目标的最大尺寸
        '''
        # 如果检测到人脸
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                face = frame_gray[y: y + h, x: x + w]  # 脸部图片
                #人脸检测
                faces = generate_faces(face)
                results = model.predict(faces)
                result_sum = np.sum(results, axis=0).reshape(-1)
                label_index = np.argmax(result_sum, axis=0)
                emotion = index2emotion(label_index)
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), border_color, thickness=2)
                frame = cv2_img_add_text(frame, emotion, x+30, y+30, font_color, 20)

        cv2.imshow("sun (press esc to exit)", frame)  # 利用人眼假象

        key = cv2.waitKey(30)  # 等待30ms，返回ASCII码
        # 如果输入esc则退出循环
        if key == 27:
            break
    # 释放摄像头
    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    predict_expression()
