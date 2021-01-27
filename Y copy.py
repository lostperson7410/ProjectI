import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
from pytesseract.pytesseract import Output


img_id=0

cap = cv2.VideoCapture(0)



def detect(img,img_id):
      img = cv2.resize(img, (620,480) )

      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
      gray = cv2.bilateralFilter(gray, 11, 17, 17)

      edged = cv2.Canny(gray, 30, 200)

      cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      cnts = imutils.grab_contours(cnts)
      cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
      screenCnt = None

      for c in cnts:
                # approximate the contour
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.018 * peri, True)
                # if our approximated contour has four points, then
                # we can assume that we have found our screen
                if len(approx) == 4:
                      screenCnt = approx
                      x, y, w, h = cv2.boundingRect(c)
                      lp = gray[y:y + h+1,x:x + w]
                      id=1
                      getdataset(img,id,img_id)

                      break                  
                      
      if screenCnt is None:
       detected = 0
       print ("No contour detected")
      else:
       detected = 1

      if detected == 1:
       cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)  

        

      mask = np.zeros(gray.shape,np.uint8)
      #new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
      new_image = cv2.bitwise_and(img,img,mask=mask)
     
      

      return img

def getdataset(img,id,img_id):
    cv2.imwrite("data/pic."+str(id)+"."+str(img_id)+".jpg",img)



while (True):
      ret,frame = cap.read()
      
      frame=detect(frame,img_id)

      cv2.imshow('out',frame)
      img_id+1
      
      text = pytesseract.image_to_string(frame,lang='tha+digits')
      print("Detected Number is:",text)
      if(cv2.waitKey(1) & 0xff == ord('q')):
            break
cap.release()
cv2.destroyAllWindows()