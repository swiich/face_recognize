import cv2

vc = cv2.VideoCapture('test.avi')

c = 1

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
timF = 1000
while rval:
    rval,frame = vc.read()
    if(c%timF == 0):
        cv2.imwrite('image/'+ str(c) + '.jpg', frame)
    c += 1
    cv2.waitKey(1)
vc.release()