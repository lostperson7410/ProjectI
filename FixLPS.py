import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

framewidth = 640
frameheight = 480
nPlateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 800
color = (255,0,255)
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgGray = cv2.bilateralFilter(imgGray, 11, 17, 17)

    edged = cv2.Canny(imgGray, 30, 200)

    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)
   
   
    for(x,y,w,h)in numberPlates:
        area = w*h
        if area >minArea:
            cv2.rectangle(img,(x,y),(x + w ,y + h),(255,0,255),2)
            cv2.putText(img,tess.image_to_string(img,lang='tha'),(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

            imgRoi= img[y:y+h,w:x+w]
            cv2.imshow("Roi",imgRoi)
            cv2.imshow("gray",imgGray)

    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

    text = tess.image_to_string(img,lang='tha+digits')
    print("Detected Number is:",text)