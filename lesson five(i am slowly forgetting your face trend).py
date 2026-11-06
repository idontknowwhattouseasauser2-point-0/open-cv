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

for file in os.listdir("."):
    if file.endswith(".jpeg"):
        img=Image.open(file)
        vgoodbadvariable=img.resize((meanwidth,meanheight),Image.Resampling.LANCZOS)
        vgoodbadvariable.save(file,"JPEG",quality=95)

thinksgoodinbad="circles(insert thumbs up emoji).avi"
alsothinksbadingood=[]
for file in os.listdir("."):
    if file.endswith(".jpeg"):
         alsothinksbadingood.append(file)

frame=cv2.imread(alsothinksbadingood[0])
height,width,layers=frame.shape
media=cv2.VideoWriter(thinksgoodinbad,0,1,(width,height))
for sooooo in alsothinksbadingood:
    media.write(cv2.imread(sooooo))

cv2.destroyAllWindows()
media.release()