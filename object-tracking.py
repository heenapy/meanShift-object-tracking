# _______________________________________________meanShift object tracking______________________________________________________________
import numpy as np
import cv2
cap=cv2.VideoCapture(0)
ret, frame = cap.read()
print(type(frame))
r,h,c,w=240,100,400,160
track_window=(c,r,w,h)
roi=frame[r:r+h,c:c+w]
hsav_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
lower_purple=np.array([125,0,0])
upper_purple=np.array([175,255,255])
mask=cv2.inRange(hsav_roi,lower_purple,upper_purple)
roi_hist=cv2.calcHist([hsav_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
term_crit=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)
while True:
    ret, frame = cap.read()
    if ret==True:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        dst=cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        ret,track_window=cv2.meanShift(dst,track_window,term_crit)
        x,y,w,h=track_window
        img2=cv2.rectangle(frame,(x,y),(x+w,y+h),255,2)
        cv2.imshow("meanshift",img2)
        if cv2.waitKey(1) == 13:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()