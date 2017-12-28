import cv2
from collections import deque
import imutils
import numpy as np
import time

# Provides core functions for tracking a wand
class WandTracker:

    # Constructor
    def __init__(self, camera_stream_uri):
        self.camera_stream_uri = camera_stream_uri # camera unit uri
        self.cap = cv2.VideoCapture(self.camera_stream_uri) # init opencv cam
        self.wand_present = False   # flag for if wand present
        self.upper = (360, 255, 255)    # upper bounds of wand color detection
        self.lower = (0, 0, 135)    # lower bounds of wand color detection
        self.tracked_wand_history = None    # history of tracked wand movement
        self.spell_resolution_time = 2  # time until spell cast when wand found


    # Retrieves basic wand data from the camera
    def getWandDataFromCamera(self):
        
        # grab the current frame
        (grabbed, frame) = self.cap.read()

        # resize the frame, blur it, and convert it to the HSV
        # color space
        frame = imutils.resize(frame, width=640)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # construct a mask for the retroreflective tip, then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        mask = cv2.inRange(hsv, self.lower, self.upper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        retDict = {}
        retDict["contours"] = cnts
        retDict["frame"] = frame
        retDict["hsv"] = hsv
        retDict["mask"] = mask
        return retDict


    # Loops looking for a wand, returns when wand present for > 1 sec
    def lookForWand(self):

        # start the timer
        start_time = time.time();

        # loop forever
        while True:

            camera_data = self.getWandDataFromCamera()
            cnts = camera_data["contours"]

            # only proceed if at least one contour was found, and it's been
            # present for at least 1 second
            if len(cnts) > 0:
                if (time.time() - start_time) >= self.spell_resolution_time:
                    return True

            # breakout
            if cv2.waitKey(1) == 27:
                exit(0)


    # Starts tracking a wand for a gesture
    def startTrackingWand(self):
        self.wand_present = True

        return 0

    def hasWandMoved(self):
        return 0


class Gesture:
    def __init__(self):
        self.test = "yay"