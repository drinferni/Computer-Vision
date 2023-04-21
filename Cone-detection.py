import cv2
import numpy as np
img=cv2.imread("cone.jpg")
img1=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower=np.array([5, 50, 50])
upper=np.array([15, 255, 255])
lower1=np.array([0,100, 20])
upper1=np.array([25, 255, 255])

img1=cv2.inRange(img1,lower1,upper1)
img1=cv2.GaussianBlur(img1,(17,17),0)
img1=cv2.Canny(img1,250,200)
_,img1=cv2.threshold(img1,20,100,cv2.THRESH_BINARY)

cont,__=cv2.findContours(img1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
main=cont[0]
for c in cont:
    if (len(c)>len(main)):
        main=c
    
p=cv2.arcLength(main,True)
a=cv2.approxPolyDP(main,0.01*p,True)
x,y,w,h=cv2.boundingRect(a)
cv2.rectangle(img,(x,y),(int(x+w),int(y+h)),(255,0,0),2)
cv2.putText(img,"Cone Detected",(int(x+w/2),int(y+h/2)),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),3)


cv2.imshow("2",img)
cv2.waitKey(0)
