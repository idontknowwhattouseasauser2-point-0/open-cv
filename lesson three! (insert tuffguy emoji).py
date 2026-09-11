import cv2
doog=cv2.imread("doggie.jpg",1)
cv2.imshow("#itookphotographylessonsandimsoohappy",doog)
#converting to greyscale
thedoog=cv2.cvtColor(doog,cv2.COLOR_BGR2GRAY)
cv2.imshow("iwashappybutmycameraisnowbrokensoimalsonowsad",thedoog)
cv2.waitKey(0)