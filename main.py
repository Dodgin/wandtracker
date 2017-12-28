from classes import wandtracker
import time
import cv2

wt = wandtracker.WandTracker('http://172.16.0.26:8080/stream/video.mjpeg');

# Main Loop
while True:

    if(wt.lookForWand()):
        print("Wand found!")
        time.sleep(1)

    # exit clause
    if cv2.waitKey(1) == 27:
        exit(0)
