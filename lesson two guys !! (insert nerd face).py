import cv2
space=cv2.imread("outerspace.jpg",1)
sand=cv2.imread("desert.jpg",1)
cv2.imshow("IS THAT NEIL ARMSTONG??",space)
cv2.imshow("wOOOOoOOoOoO So ScArYyYyyYy!", sand)

#mixing
spane=cv2.addWeighted(space ,0.5 ,sand ,0.5 ,1)
cv2.imshow("WHY IS THE DESERT CLASHING WITH THE SPACE??",spane)
cv2.waitKey(0)
cv2.destroyAllWindows()

#subtracting
diamond=cv2.imread("diamond.jpg",1)
star=cv2.imread("whitestar.jpg",1)
cv2.imshow("shine bright like a diamond ✧˖°.",diamond)
cv2.imshow("aim for the moon, if you miss, you will hit me! -this star",star)
stamond=cv2.subtract(star,diamond)
cv2.imshow("not sure what to put here", stamond)
cv2.waitKey(0)
cv2.destroyAllWindows()

#resizing
cat=cv2.imread("shockedshocked.jpg",1)
cv2.imshow("weow! (get it? its not meow)",cat)
caty=cv2.resize(cat,(300,150))
cv2.imshow("weow! (but smaller)",caty)
cv2.waitKey(0)
cv2.destroyAllWindows()

#erosion
import numpy as np
kernel=np.ones((3,3),np.uint8)
newcat=cv2.erode(cat,kernel)
cv2.imshow("woaw",newcat)
cv2.waitKey(0)
cv2.destroyAllWindows()

#bordering around images
trapcat=cv2.copyMakeBorder(cat,50,50,50,50,cv2.BORDER_CONSTANT,value=1)
cv2.imshow("helppp im trapped!!!",trapcat)
cv2.waitKey(0)


#bordering around images (reflected)
catx=cv2.copyMakeBorder(cat,50,50,50,50,cv2.BORDER_REFLECT,value=1)
cv2.imshow("b",catx)

#blurring technique 1
tiiger=cv2.imread("tiiger.jpg")
cv2.imshow("#rawr",tiiger)
#gaussian blurring
bone=cv2.GaussianBlur(tiiger,(11,11),0)
cv2.imshow("#rawrbutimstillbadatphotograpysoishoulddefitinlyhiresomeonenexttime",bone)

#median blurring
btwo=cv2.medianBlur(tiiger,13)
cv2.imshow("#idonthaveenoughmoneytokiresomebodyandnowsomeonewantsmetorecoredamoviebutineedthemoneysoiwilldoitwithmybadphotograpyskillsandprobablybadcamera",btwo)

#bilateral blurring
bilateral=cv2.bilateralFilter(tiiger,9,75,75)
cv2.imshow("#igotfiredoffmyjobtobeamovierecorderbecaueof myskillsandtheyharshlytodmethatimtheproblemandmycameraisfineandactuallygoodqualitysoimusttakephotographyskills",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
