import cv2
reading=cv2.imread("tuffdude.png",cv2.IMREAD_COLOR) #you can just put 1
readings=cv2.imread("tuffdude.png",cv2.IMREAD_GRAYSCALE) #0
readingss=cv2.imread("tuffdude.png",cv2.IMREAD_UNCHANGED) #-1
cv2.imshow("stonks",reading)
cv2.imshow("stonks.but.old.skool",readings)
cv2.imshow("stonks.but.unchanged",readingss)
cv2.waitKey(0)
cv2.imwrite("pics.png",readings)

b,g,r=cv2.split(reading)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
cv2.waitKey(0)