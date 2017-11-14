import os, glob, cv2
import numpy as np
from PIL import Image


folder = 'E:\\Python\\PycharmProjects\\ImgHash\\img\\ma'


def pca(data, k):
    data = np.float32(np.mat(data))
    rows, cols = data.shape                       #图像大小
    data_mean = np.mean(data, 0)                  #均值
    Z = data - np.tile(data_mean, (rows, 1))
    T = Z*Z.T
    D, V = np.linalg.eig(T)                   #特征值与特征向量
    V1 = V[:, :k]                                 #取前K个特征向量
    V1 = Z.T*V1
    for i in range(k):                            #特征向量归一化
        V1[:, i] /= np.linalg.norm(V1[:, i])
    data_new = np.dot(Z, V1)
    return data_new, data_mean, V1


#covert image to vector
def img2vector(filename):
    #img = cv2.imread(filename, 0) #read as 'gray'
    img = Image.open(filename)
    img = img.convert('L')
    rows, cols = img.size
    imgVector = np.zeros((1,rows*cols)) #create a none vectore:to raise speed
    imgVector = np.reshape(img,(1,rows*cols)) #change img from 2D to 1D
    return imgVector


def convertL(file):
    img = Image.open(file)
    img = img.convert('L')
    return img

def loadImgSet(folder):
    trainData = []; testData = []; yTrain = []; yTest = []
    for k in range(10):
        data = [convertL(d) for d in glob.glob('E:\\Python\\PycharmProjects\\ImgHash\\img\\ma\\*.jpg')]
        trainData.extend(np.ravel(data[i]) for i in range(10))
        testData.extend(np.ravel(data[0]))
        yTest.extend([k]*1)
        yTrain.extend([k]*10)
    return np.array(trainData), np.array(yTrain), np.array(testData), np.array(yTest)


def main():
    xTrain_, yTrain, xTest_, yTest = loadImgSet(folder)
    num_train, num_test = xTrain_.shape[0], xTest_.shape[0]

    xTrain, data_mean, V = pca(xTrain_, 10)
    xTest = np.array((xTest_- np.tile(data_mean, (num_test, 1))) * V)    #特征脸在特征向量下的数据

    yPredict = [yTrain[np.sum((xTrain-np.tile(d, (num_train, 1)))**2, 1).argmin()] for d in xTest]
    print("欧式距离法识别率：%.2f%%"% ((yPredict == np.array(yTest)).mean()*100))

if __name__ == '__main__':
    main()