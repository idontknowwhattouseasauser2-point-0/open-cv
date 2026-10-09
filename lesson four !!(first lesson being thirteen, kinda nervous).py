import cv2
horsey=cv2.imread("horsey.jpeg",1)
cv2.imshow("#slayyyyyyyyyyyyyyyyyyy omg baddie!!!!!", horsey)
cv2.waitKey(0)
#drawing a line on our slay horse
thickline=5
startline=0,0
endline=300,500
colourline=255,255,255
cv2.line(horsey,startline,endline,colourline,thickline)
cv2.imshow("my lil sis grabbed the phone",horsey)
#drawing a sigma circle
thickcircle=-1
centerpoint=325,545
radius=50
circlecolour=45,78,39
cv2.circle(horsey,centerpoint,radius,circlecolour,thickcircle,)
cv2.imshow("my screens glitching nooooo",horsey)
#drawing a square or rectangle (not the square shopping center by the way)
startpoint=67,76
endpoint=167,176
rectanglecolor=97,35,98
thickrectangle=5
cv2.rectangle(horsey,startpoint,endpoint,rectanglecolor,thickrectangle)
cv2.imshow("aaaaaaaaaaa",horsey)
#textttttttttttttttttttttt
font=cv2.FONT_HERSHEY_TRIPLEX
fontsize=2
text="neigh"
fontcolour=87,67,25
placingoftext=200,100
thickfont=5
cv2.putText(horsey,text,placingoftext,font,fontsize,fontcolour,thickfont)
cv2.imshow("give me hay now",horsey)
cv2.waitKey(0)