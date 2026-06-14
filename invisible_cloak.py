import cv2
import time
import numpy as np
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Webcam not opening")
    exit()

print("Move away from camera...capturing background in 3 seconds")
print("Stay still..Capturing background")
time.sleep(3)

background = None

for i in range(30):

    ret, frame = cap.read()

    frame = cv2.flip(frame,1)

    if background is None:
        background = frame.astype(float)

    else:
        cv2.accumulateWeighted(frame, background, 0.5)

background = cv2.convertScaleAbs(background)

print("Background captured! Press 'q' to exit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("ERROR: Failed to read frame")
        break
    frame=cv2.flip(frame,1)

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red1=(0,70,70)
    upper_red1=(15,255,255)

    lower_red2=(150,70,70)
    upper_red2=(180,255,255)

    mask1=cv2.inRange(hsv,lower_red1,upper_red1)
    mask2=cv2.inRange(hsv,lower_red2,upper_red2)

    mask=mask1+mask2


    kernel=np.ones((8,8),np.uint8)
    mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel,iterations=2)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)
    

    mask_inv=cv2.bitwise_not(mask)


    res1=cv2.bitwise_and(background,background,mask=mask)
    res2=cv2.bitwise_and(frame,frame,mask=mask_inv)

    final=res1+res2

    
    cv2.imshow("Invisible Cloak",final)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
