import numpy as np
import cv2, os


def loadImg(path):
    matrix = np.mat(np.zeros((9, 64*64)))
    j = 0
    for i in os.listdir(path):
        if i.split('.')[1] == 'jpg':
            try:
                img = cv2.imread(path+i, 0)
            except:
                print('load %s failed' % i)
            matrix[j, :] = np.mat(img).flatten()
            j += 1
    return matrix
'''
step1: load the face image data ,get the matrix consists of all image
step2: average the FaceMat
step3: calculate the difference of avgimg and all image data(FaceMat)
step4: calculate eigenvector of covariance matrix (because covariance matrix will cause memory error)
'''

def recogVector(selecthr = 0.8):
    faceMat = loadImg('E:\Python\PycharmProjects\ImgHash\img\m').T                       ######
    avgImg = np.mean(faceMat, 1)
    diffTrain = faceMat - avgImg
    eigVals, eigVects = np.linalg.eig(np.mat(diffTrain.T * diffTrain))
    eigSortIndex = np.argsort(-eigVals)
    for i in range(np.shape(faceMat)[1]):    ########
        if (eigVals[eigSortIndex[:i]]/eigVals.sum()).sum() >= selecthr:
            eigSortIndex = eigSortIndex[:i]
            break
    covVects = diffTrain * eigVects[:,eigSortIndex]                #the eigenvector of covariance matrix
    #avgImg均值图像，covVects协方差矩阵的特征向量，diffTrain偏差矩阵
    return avgImg, covVects, diffTrain


def whosthis(oringinImg, faceVector, avgImg, difftrain):
    diff = oringinImg.T - avgImg
    wVec = faceVector.T * diff
    res = 0
    resVal = np.inf
    for i in range(9):
        trainVec = faceVector.T * difftrain[:,i]
        if (np.array(wVec - trainVec)**2).sum() < resVal:
            res = i
            resVal = (np.array(wVec - trainVec)**2).sum()
    return res+1


def similar(oriImg):
    avgImg, faceVector, diffTrain = recogVector()
    oriImg = cv2.imread(oriImg, 0)
    gray = np.mat(oriImg).flatten()
    if whosthis(gray, faceVector, avgImg, diffTrain) == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    if similar('D:\\6.bmp'):
        print('1111')
    else:
        print('0')