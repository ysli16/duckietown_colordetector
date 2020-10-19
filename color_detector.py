import cv2
import numpy as np
from time import sleep
import os

cap = cv2.VideoCapture(2)
#frame=cv2.imread('test.jpg')
N_SPLITS=int(os.environ['N_SPLITS'])
#N_SPLITS=10

white_lower=np.array([0,255*0.8,0],dtype=np.int32)
white_upper=np.array([180,255,255*0.3],dtype=np.int32)

yellow_lower=np.array([20,0,255*0.3],dtype=np.int32)
yellow_upper=np.array([40,255,255],dtype=np.int32)

red_lower_1=np.array([0,0,255*0.3],dtype=np.int32)
red_upper_1=np.array([10,255,255],dtype=np.int32)
red_lower_2=np.array([170,0,255*0.3],dtype=np.int32)
red_upper_2=np.array([180,255,255],dtype=np.int32)

result=np.zeros(shape=(N_SPLITS,4)) #number of pixels in white/yellow/red/others
np.set_printoptions(suppress=True)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    imgsize=frame.shape
    grid=np.linspace(0,imgsize[0],N_SPLITS+1,dtype=np.int32)
    #Put here your code!
    # You can now treat output as a normal numpy array
    # Do your magic here
    imgHLS=cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)
    #white color
    
    white_mask = cv2.inRange(imgHLS, white_lower, white_upper)
    
    #yellow color
    
    yellow_mask = cv2.inRange(imgHLS, yellow_lower, yellow_upper)
    
    #red color
    
    red_mask_1=cv2.inRange(imgHLS, red_lower_1, red_upper_1)
    red_mask_2=cv2.inRange(imgHLS, red_lower_2, red_upper_2)
    red_mask=cv2.bitwise_or(red_mask_1, red_mask_2)
    
    #split image
    for i in range(N_SPLITS):
        white_num=int(np.sum(white_mask[grid[i]:grid[i+1],:])/255)
        yellow_num=int(np.sum(yellow_mask[grid[i]:grid[i+1],:])/255)
        red_num=int(np.sum(red_mask[grid[i]:grid[i+1],:])/255)
        other_num=imgsize[1]*round(imgsize[0]/N_SPLITS)-white_num-yellow_num-red_num
        result[i]=[white_num,yellow_num,red_num,other_num]
    print(imgHLS[:,:,0])
    print("white","yellow","red","other")
    print(result)
    sleep(1)

