import cv2


capture = cv2.VideoCapture(0)
while(True):
    # 获取一帧
    ret, frame = capture.read()
    cv2.imshow("capture",frame)
    if cv2.waitKey(1) == ord('q'):
        capture.release() #释放摄像头
        cv2.destroyAllWindows()#删除建立的全部窗口



