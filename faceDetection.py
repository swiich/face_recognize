#-*-coding:utf8-*-#

import cv2
from PIL import Image, ImageDraw
import numpy as np

def detectFaces(image_name):
    #img = cv2.imread(image_name)
    img = Image.open(image_name)
    # face_cascade = cv2.CascadeClassifier("C:\\Users\Asshole\Anaconda3\pkgs\opencv-3.2.0-np112py36_203\Library\etc\haarcascades\haarcascade_frontalface_default.xml")    #face
    # face_cascade = cv2.CascadeClassifier("E:\Python\PycharmProjects\ImgHash\img\ma\\negdata\data\cascade.xml")     #mayun
    face_cascade = cv2.CascadeClassifier("E:\Python\PycharmProjects\ImgHash\img\\brand\\negdata\data\cascade.xml")

    #gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    img = img.convert('L')
    gray = np.asarray(img)
    '''
    参数3：scaleFactor - -表示在前后两次相继的扫描中，搜索窗口的比例系数。默认为1.1
    即每次搜索窗口依次扩大10 %;
    参数4：minNeighbors - -表示构成检测目标的相邻矩形的最小个数(默认为3个)。
    如果组成检测目标的小矩形的个数和小于min_neighbors - 1都会被排除。
    如果min_neighbors为0, 则函数不做任何操作就返回所有的被检候选矩形框，
    这种设定值一般用在用户自定义对检测结果的组合程序上
    '''
    #1.1  即每次图像尺寸减小比例10%
    #5  每一个目标至少检测到4次才算真的目标
    faces = face_cascade.detectMultiScale(gray, 1.07, 5)
    result = []
    for (x, y, width, height) in faces:
        result.append((x, y, x+width, y+height))
    return result

def drawFaces(image_name):
    faces = detectFaces(image_name)
    if faces:
        img = Image.open(image_name)
        draw_instance = ImageDraw.Draw(img)
        for (x1,y1,x2,y2) in faces:
            # region = (x1, y1, x2, y2)
            # cropImg = img.crop(region)
            draw_instance.rectangle((x1,y1,x2,y2), outline=(255, 0, 0))
            # cropImg.save('E:\Python\PycharmProjects\ImgHash\img\\faces\\'+str(x1)+'.jpg')
    # img.save('drawfaces_'+image_name)
    Image._show(img)

if __name__ == '__main__':
    folder = 'E:\\Python\\PycharmProjects\\ImgHash\\img\\'
    picName = 'brd.jpg'
    path = folder + picName
    drawFaces(path)
    # drawFaces('E:\\Python\\PycharmProjects\\ImgHash\\img\\whereisma.jpg')
    # drawFaces('E:\\Python\\PycharmProjects\\ImgHash\\img\\arrow.jpg')
    # drawFaces('E:\\Python\\PycharmProjects\\ImgHash\\img\\bruce.jpg')
    # drawFaces('E:\\Python\\PycharmProjects\\ImgHash\\img\\bat.jpg')
    # drawFaces('E:\\Python\\PycharmProjects\\ImgHash\\img\\gakki.jpg')    #gakki 1.07
    # # drawFaces('E:\\Python\\PycharmProjects\\ImgHash\\img\\prison.jpg')



    # drawFaces('E:\\Python\\PycharmProjects\\ImgHash\\img\\brd.jpg')
    drawFaces('E:\\Python\\PycharmProjects\\ImgHash\\img\\s.jpg')
