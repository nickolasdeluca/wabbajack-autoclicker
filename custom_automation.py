import pyautogui
import cv2
import numpy

import glob
import time

import keyboard
import os

from threading import Thread

# Custom Variables
max_loop = 99999
click_interval = 1
loop_interval = 3

# search and click image in the center
def clickImage(image, threshold=0.5):

    # grab windows print screen
    screen_img = pyautogui.screenshot() 

    screen_img_rgb = numpy.array(screen_img)
    
    # convert screen img to grayscale
    screen_img_gray = cv2.cvtColor(screen_img_rgb, cv2.COLOR_BGR2GRAY) 
    
    # read image
    template = cv2.imread(image,cv2.IMREAD_GRAYSCALE)
    template.shape[::-1]

    # search for matching image in screen
    res = cv2.matchTemplate(screen_img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)    
    
    # no image is found 
    if max_val < threshold:
        return -1;
    
    # move mouse to center of image    
    pyautogui.moveTo(max_loc[0]+template.shape[1]/2, max_loc[1]+template.shape[0]/2, 0.5, pyautogui.easeOutQuad)    
        
    # left click   
    pyautogui.click()     
    return 0;    

#main thread
def main():
    loop = 1    
    time.sleep(1) 
    while loop < max_loop:
        key_listener()
        for file in glob.glob("./input_images/*.png"):
            print(f"Searching for {file}, Iteration {loop}")
            ret = clickImage(file)            
            if (ret == -1):
                print(f"Iteration {loop} not found")
            else:
                print(f"Iteration {loop} found and clicked")                                
            time.sleep(click_interval)
        loop += 1
        time.sleep(loop_interval) 
    os._exit(0)    

#interrupt thread
def key_listener():    
    if keyboard.is_pressed("esc"):
        print("Interrupted")
        os._exit(0)
        
try:
    print("Hold 'Escape' to quit this application while the loop is running.")
    thread1 = Thread(target = main)    
    thread1.start()    
    thread1.join()    
    
except:
    print ("Exiting")
    os._exit(0)


 
