import cv2
import os
import time
myPath = "data/images"
cameraNo = 1
cameraBrightness = 190
moduleVal = 10
minBlur = 500
grayImage =False
savaData = True
showImage = True
imgWidht = 180
imgHeight = 120

global countFolder
cap =cv2.VideoCapture(cameraNo)
cap.set(3 ,640)
cap.set(4,480)
cap.set(10,cameraBrightness)


count =0 
countSave = 0

def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists(myPath + str(countFolder)):
        countFolder = countFolder+1
    os.makedirs(myPath + str(countFolder))
if savaData:saveDataFunc()

while True:

    success , img = cap.read()
    img = cv2.resize(img,(imgWidht,imgHeight))
    if grayImage:img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if savaData:
        blur = cv2.Laplacian(img,cv2.CV_64F).var()
        if count % moduleVal == 0 and blur > minBlur:
            nowTime = time.time()
            cv2.imwrite(myPath + str(countFolder) + str(countSave)+ str(int(blur))+ str(nowTime)+".png",img)
            countSave+=1


    if showImage:
        cv2.imshow("IMG",img)

    if cv2.waitKey(1)& 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


