import pyautogui
import os
import datetime
import time
import cv2
# Read the video from specified path
currentframe=0
tms=datetime.datetime.now().time()  # to find the instant from where the code starts executing
print(tms)
c=1

try:

    # creating a folder named data
    if not os.path.exists('data1'):
        os.makedirs('data1')

    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')

while (True):
    pic = pyautogui.screenshot(region=(800,0,1200,1100)) #taking image of a par-ticular area . Here the particular area refers to the ECG live streaming
    pic.save('./data1/frame' + str(currentframe) + '.jpg')
    currentframe+=1

    if (currentframe==(c*50)):
        print(datetime.datetime.now().time())
        c+=1
        print(c)

    if  0xFF == ord('q'):

        break
else:
    print("Successful")
