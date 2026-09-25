import cv2
doog=cv2.imread("doggie.jpg",1)
cv2.imshow("#itookphotographylessonsandimsoohappy",doog)
#converting to greyscale
thedoog=cv2.cvtColor(doog,cv2.COLOR_BGR2GRAY)
cv2.imshow("iwashappybutmycameraisnowbrokensoimalsonowsad",thedoog)
cv2.imwrite("deperesseddoggo.jpg",thedoog)
#converting to hsv
cursedbird=cv2.imread("budgie.jpeg",1)
cb=cv2.cvtColor(cursedbird,cv2.COLOR_BGR2HSV)
cv2.imshow("iaminyourwallsss",cb)
#rotating images
cursedpigeon=cv2.imread("pigeon.jpeg",1)
(rows,column)=cursedpigeon.shape[0:2]

matrix=cv2.getRotationMatrix2D((column/2,rows/2),180,1)
result=cv2.warpAffine(cursedpigeon,matrix,(column,rows))
cv2.imshow("happybirthhdayyytoyouuuuuuu",result)
cv2.waitKey(0)