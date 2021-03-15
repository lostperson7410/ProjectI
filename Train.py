import numpy as np
from PIL import Image
import os,cv2

def train_classifier(data_dir):
    path = [os.path.join (data_dir,f) for f in os.listdir(data_dir)]
    
    lsps=[]
    ids=[]

    for image in path:
        img=Image.open(image).convert("L") 
        imageNp = np.array(img,'uint8')
        id=int(os.path.split(image)[1].split(".")[1])
        lsps.append(imageNp)
        ids.append(id)

    ids=np.array(ids)

    clf=cv2.lsps.LBPHRecognizer_create()
    clf.train(lsps,ids)
    clf.write("LPSclassifier.xml")

train_classifier("data")
