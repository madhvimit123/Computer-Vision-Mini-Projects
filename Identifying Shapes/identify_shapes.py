import cv2
import numpy as np

img=cv2.imread("shapes.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Identifying Shapes",img)
cv2.waitKey(0)

ret,thresh=cv2.threshold(gray,127,255,1)
contours,hierarchy=cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    if len(approx)==3:
        shapename="Triangle"
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
        M=cv2.moments(cnt)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        cv2.putText(img,shapename,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
    elif len(approx)==4:
        x,y,w,h=cv2.boundingRect(cnt)
        M=cv2.moments(cnt)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        if abs(w-h)<=3:
            shapename="Square"
            cv2.drawContours(img,[cnt],0,(0,125,255),-1)
            cv2.putText(img,shapename,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
        else:
            shapename="Rectangle"
            cv2.drawContours(img,[cnt],0,(0,0,255),-1)
            M=cv2.moments(cnt)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            cv2.putText(img,shapename,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
    elif len(approx)==10:
        shapename="Star"
        cv2.drawContours(img,[cnt],0,(255,0,0),-1)
        M=cv2.moments(cnt)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        cv2.putText(img,shapename,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
    elif len(approx)>=15:
        shapename="Circle"
        cv2.drawContours(img,[cnt],0,(0,255,255),-1)
        M=cv2.moments(cnt)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        cv2.putText(img,shapename,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
    cv2.imshow("Identifying Shapes",img)
    cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
