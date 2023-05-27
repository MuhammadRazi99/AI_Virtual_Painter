import cv2
import numpy as np
import mediapipe as mp
import time
import os
import ch1_HandTracking as HT

##################
vcam,hcam=1280,720
brushThickness=15
eraserThickness=25
##################


folderPath='Header'
headerList=os.listdir(folderPath)
overlayList=[]
for imPath in headerList:
    image=cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

header=overlayList[7]

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector=HT.HandDetector(detectionCon=0.85)
drawColor=(255,255,255)
drawPointer=False
xp,yp=0,0

imgCanvas=np.zeros((720,1280,3),np.uint8)
while True:
    # 1.import image
    success, img=cap.read()
    img=cv2.flip(img,1)
    
    # 2. Find Hand Landmarks
    img=detector.findHands(img)
    lmlist=detector.findPosition(img,draw=False)
    if len(lmlist) != 0:
        # print(lmlist)
        x1,y1=lmlist[8][1],lmlist[8][2]
        x2,y2=lmlist[12][1],lmlist[12][2]
    # 3. Check how many fingers are up
        fingers=detector.fingersUp()
        # print(fingers)
    # 4. if selection mode - two fingers are up
        if fingers[1] and fingers[2]:
            xp,yp=0,0
            # checking for the click
            if y1 < 125:
                if 37<x1<109:
                    header=overlayList[7]
                    drawPointer=False   
                elif 228<x1<314:
                    header=overlayList[0]
                    drawColor=(255,255,255)
                    drawPointer=True
                elif 382<x1<468:
                    header=overlayList[1]
                    drawColor=(255,0,255)
                    drawPointer=True    
                elif 536<x1<622:
                    header=overlayList[2]
                    drawColor=(20,78,242)
                    drawPointer=True
                elif 690<x1<776:
                    header=overlayList[3]
                    drawColor=(242,38,30)
                    drawPointer=True
                elif 844<x1<930:
                    header=overlayList[4]
                    drawColor=(60,192,87)
                    drawPointer=True
                elif 998<x1<1084:
                    header=overlayList[5]
                    drawColor=(109,242,232)
                    drawPointer=True
                elif 1152<x1<1234:
                    header=overlayList[6]
                    drawColor=(0,0,0)
                    drawPointer=True
            if drawPointer:
                cv2.rectangle(img,(x1,y1-25),(x2,y2+25),drawColor,cv2.FILLED)
    # 5. if drawing mode _ index finger is up
        elif fingers[1] and not fingers[2]:
            if drawPointer:
                if xp==0 and yp==0:
                    xp,yp=x1,y1
                if drawColor == (0,0,0):
                    cv2.line(img,(xp,yp),(x1,y1),drawColor,eraserThickness)
                    cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,eraserThickness)
                    cv2.circle(img,(x1,y1),eraserThickness,drawColor,cv2.FILLED)
                    cv2.circle(imgCanvas,(x1,y1),eraserThickness,drawColor,cv2.FILLED)
                else:
                    cv2.circle(img,(x1,y1),brushThickness,drawColor,cv2.FILLED)
                    cv2.circle(imgCanvas,(x1,y1),brushThickness,drawColor,cv2.FILLED)
                    cv2.line(img,(xp,yp),(x1,y1),drawColor,brushThickness)
                    cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,brushThickness)
                xp,yp=x1,y1
            
            
    imgGrey=cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY)
    _,imgInv=cv2.threshold(imgGrey,50,255,cv2.THRESH_BINARY_INV)
    imgInv=cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img=cv2.bitwise_and(img,imgInv)
    img=cv2.bitwise_or(img,imgCanvas)

   
    # setting up the header file
    img[0:125,0:1280]=header
    # img=cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv2.imshow("Virtual Painter",img)
    # cv2.imshow("Canvas",imgCanvas)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
