
import cv2
from PIL import ImageGrab
#import keyboard
import random
import imutils
import win32api, win32con
import numpy as np
import time


#code from Here

def click(x,y):
    
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

frame5 = np.array(ImageGrab.grab(bbox=(192,85,735,1051)))
frame5 = cv2.cvtColor(frame5,cv2.COLOR_BGR2GRAY)
frame5 = imutils.resize(frame5,width=400,height= 700)
frame1 = cv2.imread("finalA.jpg",0)
frame2 = cv2.imread("finalB.jpg",0)
frame3 = cv2.imread("finalC.jpg",0)
frame4 = cv2.imread("FinalD.jpg",0)



i= 0
j = 0
k=0
l=0
m = 0
n = 0
o =0
p = 0

m1_location = 1
m2_location = 3
color_match1 = 0
color_match2 = 0
color_match3 = 0
color_match4 = 0

time_start = time.time()
while True:

    image = np.array(ImageGrab.grab(bbox=(192,85,735,1051)))
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image = imutils.resize(image,width=400,height= 700)
    
    
    sub_image = image[350:350+75, 10:100]
    sub_image1 = image[350:350+75, 100:180]
    sub_image2 = image[350:350+75, 220:300]
    sub_image3 = image[350:350+75, 300:390]


    
    
    cv2.rectangle(image, (10,350), (100,425), (255,0,0), 2)  #White rectangle with thickness 2.
    cv2.rectangle(image, (100,350), (180,425), (255,0,0), 2)
    cv2.rectangle(image, (210,350), (300,425), (255,0,0), 2)
    cv2.rectangle(image, (300,350), (390,425), (255,0,0), 2)


    
    #First Box:
    diff = cv2.absdiff(sub_image,frame1)
    _, th = cv2.threshold(diff, 75, 100, cv2.THRESH_BINARY)
    cnts,hierarchy = cv2.findContours(th.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    
    for contor in cnts:
        
        
        if cv2.contourArea(contor) > 400:
            cv2.rectangle(image, (10,350), (90,425), (0,255,0), 3)
            color_match1 = 1
            i = i+1
          
       
    if i > 3:
        j = j+1
        print("j = ",j)
        i = 0
    
    
    
    #Second Box

    diff1 = cv2.absdiff(sub_image1,frame2)
    _, th1 = cv2.threshold(diff1, 75, 100, cv2.THRESH_BINARY)
    cnts1,hierarchy1 = cv2.findContours(th1.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    
    for contorss in cnts1:
        
        
        if cv2.contourArea(contorss) > 120:
            cv2.rectangle(image, (100,350), (180,425), (0,255,0), 3)
            color_match2 = 2
            k = k+1
          
       
    if k > 4:
        l = l+1
        print("l = ",l)
        k = 0
    
    if(color_match1 == m1_location or color_match2 == m1_location):
        click(318,791)
        if m1_location == 1:
            m1_location = 2
        else: 
            m1_location = 1
        color_match1 = 0
        color_match2 = 0

    # Third Box

    diff2 = cv2.absdiff(sub_image2,frame3)
    _, th2 = cv2.threshold(diff2, 75, 100, cv2.THRESH_BINARY)
    cnts2,hierarchy2 = cv2.findContours(th2.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    
    for contorss in cnts2:
        
        
        if cv2.contourArea(contorss) > 70:
            cv2.rectangle(image, (210,350), (300,425), (0,255,0), 3)
            color_match3 = 3
            m = m+1
          
       
    if m > 4:
        n = n+1
        print("n = ",n)
        m = 0
        

    #Fourth Box
    diff3 = cv2.absdiff(sub_image3,frame4)
    _, th3 = cv2.threshold(diff3, 75, 100, cv2.THRESH_BINARY)
    cnts3,hierarchy4 = cv2.findContours(th3.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    
    for contorss in cnts3:
        
        
        if cv2.contourArea(contorss) > 190:
            cv2.rectangle(image,(300,350), (390,425), (0,255,0), 3)
            color_match4 = 4
            o = o+1
          
       
    if o > 4:
        p = p+1
        print("p = ",p)
        o = 0
    
    if(color_match3 == m2_location or color_match4 == m2_location):
        click(550,800)
        if m2_location == 3:
            m2_location = 4
        else: 
            m2_location = 3
        color_match3 = 0
        color_match4 = 0

    cv2.imshow("Matched image", image)
    


    time_end = time.time()
    print(time_end-time_start)
    if time_end-time_start >= 60*2:
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



 
cv2.destroyAllWindows()






    


    

    
    

