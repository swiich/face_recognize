# coding=utf-8
import cv2
import dlib

detector = dlib.get_frontal_face_detector()

win = dlib.image_window()

# cap = cv2.VideoCapture('E:\Python\PycharmProjects\ImgHash\Opencv\\1.mp4')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, cv_img = cap.read()
    # OpenCV默认RGB图像，dlib  BGR图像
    img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    dets = detector(img, 0)

    # print("Number of faces detected: {}".format(len(dets)))
    # for i, d in enumerate(dets):
    #     print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
    #         i, d.left(), d.top(), d.right(), d.bottom()))

    win.clear_overlay()
    win.set_image(img)
    win.add_overlay(dets)

cap.release()