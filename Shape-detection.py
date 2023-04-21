import cv2

img=cv2.imread("shapes.jpg")

img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img1=cv2.GaussianBlur(img1,(15,15),0)
_,img1=cv2.threshold(img1,200,255,cv2.THRESH_BINARY)
img1=cv2.Canny(img1,200,200)

cont,hierarchy=cv2.findContours(img1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


for c in cont:
    cv2.drawContours(img,c,-1,(148,0,211),5)
    p=cv2.arcLength(c,True)
    
    approx=cv2.approxPolyDP(c,0.01*p,True)
    obj=str(len(approx))
    x,y,w,h=cv2.boundingRect(approx)
    
    
    if obj=="3":
        cv2.putText(img,"Triangle",(int(x+w/3),int(y+h/2)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    elif obj=="4":
        cv2.putText(img,"Rectangle",(int(x+w/3),int(y+h/2)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    elif obj=="5":
        cv2.putText(img,"Pentagon",(int(x+w/3),int(y+h/2)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    elif obj=="6":
        cv2.putText(img,"Hexagon",(int(x+w/3),int(y+h/2)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    elif obj=="10":
           cv2.putText(img,"Star",(int(x+w/2.5),int(y+h/1.75)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    elif obj>"10":
         cv2.putText(img,"Circle",(int(x+w/3),int(y+h/2)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    else:
        shape="None"
        
  
    
cv2.imshow("1",img)
cv2.waitKey(0)
