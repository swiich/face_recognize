import dlib, os, glob, numpy
from skimage import io
from tkinter import filedialog, messagebox


def descriptor(path):
    detector = dlib.get_frontal_face_detector()
    shape = dlib.shape_predictor('..\shape_predictor_68_face_landmarks.dat')
    faceRecog = dlib.face_recognition_model_v1('..\dlib_face_recognition_resnet_model_v1.dat')
    windows = dlib.image_window()
    descriptors = []
    for i in glob.glob(os.path.join(path)):
        print('Processing file: {}'.format(i))
        img = io.imread(i)
        windows.clear_overlay()
        windows.set_image(img)
        detect = detector(img, 1)           #人脸检测
        print('Number of faces detected: {}'.format(len(detect)))
        for d in detect:
            sp = shape(img, d)                       #关键点检测
            windows.clear_overlay()
            windows.add_overlay(d)
            windows.add_overlay(sp)
            face_descriptor = faceRecog.compute_face_descriptor(img, sp)            #描述子提取
            arr = numpy.array(face_descriptor)
            descriptors.append(arr)
    return descriptors


def recogFace():
    detector = dlib.get_frontal_face_detector()                # 正脸检测器
    shape = dlib.shape_predictor('..\shape_predictor_68_face_landmarks.dat')        # 关键点检测器
    # 人脸识别模型
    faceRecog = dlib.face_recognition_model_v1('..\dlib_face_recognition_resnet_model_v1.dat')
    # descriptors = []
    descriptors = descriptor('..\img\\faces\*.jpg')
    #读取待检测图片
    img = io.imread(openFile())
    # img = io.imread('..\img\\faces\\torec\\6.jpg')
    detect = detector(img, 1)
    dist = []
    for d in detect:
        sp = shape(img, d)
        face_descriptor = faceRecog.compute_face_descriptor(img, sp)
        d_test = numpy.array(face_descriptor)
        #欧氏距离
        for i in descriptors:
            dist_ = numpy.linalg.norm(i - d_test)
            dist.append(dist_)
    candidate = ['施瓦辛格','马云','马云','斯嘉丽约翰逊','施瓦辛格',
                 '斯嘉丽约翰逊','奥巴马','奥巴马','奥巴马','山下智久','金正恩','金正恩', \
                 '库里', '库里']
    dt = dict(zip(candidate, dist))
    dt_sorted = sorted(dt.items(), key=lambda d:d[1])
    messagebox.showinfo('whosthis',str(dt_sorted[0][0]))
    # print('its:  ',dt_sorted[0][0])
    # dlib.hit_enter_to_continue()

def openFile():
    op = filedialog.askopenfilename(title='打开文件',filetypes = [('Img','*.bmp *.jpg')])
    return op

if __name__ == '__main__':
    recogFace()
