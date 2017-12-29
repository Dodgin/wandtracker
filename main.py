from classes import bootstrap
from classes import wandtracker
from classes import gesture
from pprint import pprint
import time
import cv2

# Bootstrap from config files
bs = bootstrap.Bootstrap();
config = bs.run()

# Debug
#config['iot_devices'][0]['interface'].startApp('Netflix')
g = gesture.Gesture()

# Instantiate wandtracker TODO: this needs to be based on config loads
wt = wandtracker.WandTracker('http://172.16.0.26:8080/stream/video.mjpeg', g);

# Main Loop
while True:

    if(wt.lookForWand()):
        print("Wand found!")
        wt.startTrackingWand();
    else:
        time.sleep(1)

    # exit clause
    if cv2.waitKey(1) == 27:
        exit(0)
