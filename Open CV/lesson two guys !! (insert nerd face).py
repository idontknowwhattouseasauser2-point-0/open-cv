import cv2
space=cv2.imread("outerspace.jpg",1)
sand=cv2.imread("desert.jpg",1)
cv2.imshow("IS THAT NEIL ARMSTONG??",space)
cv2.imshow("wOOOOoOOoOoO So ScArYyYyyYy!", sand)

spane=cv2.addWeighted(space ,0.5 ,sand ,0.5 ,1)
cv2.imshow("WHY IS THE DESERT CLASHING WITH THE SPACE??",spane)
cv2.waitKey(0)
cv2.destroyAllWindows()