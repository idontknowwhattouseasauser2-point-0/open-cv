import cv2,os
from PIL import Image
images="Images for i am slowly forgetting your face trend"
os.chdir(images)
meanwidth=0
meanheight=0
noi=len(os.listdir("."))
for file in os.listdir("."):
    if file.endswith(".jpeg"):
        img=Image.open(file)
        width,height=img.size
        meanwidth=meanwidth+width
        meanheight=meanheight+height

meanwidth=meanwidth//noi
meanheight=meanheight//noi
print(meanwidth,meanheight)
