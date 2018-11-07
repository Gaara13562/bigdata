import cv2

vc = cv2.VideoCapture('D:/test.mp4')  # 读入视频文件
c = 0
rval = vc.isOpened()
timeF = 65  # 视频帧计数间隔频率
while rval:  # 循环读取视频帧
    c = c + 1
    rval, frame = vc.read()
    if c % timeF == 0:  # 每隔timeF帧进行存储操作
        cv2.imwrite('D:/videos/' + str(c).zfill(8) + '.jpg', frame)  # 存储为图像
    # if rval:
    #     cv2.imwrite('D:/videos/' + str(c).zfill(8) + '.jpg', frame)  # 存储为图像
    #     cv2.waitKey(1)
    # else:
    #     break
vc.release()
