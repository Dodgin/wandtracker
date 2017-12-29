import cv2
from collections import deque
import imutils
import numpy as np
import time

# Provides wand gesture processing capabilities
class Gesture:
    def __init__(self):
        self.test = "yay"


    # returns this gesture's context if any
    def getContext(self):
        return 0

    # returns the result of self.raw_wand_data against the spell database
    def convertGestureToSpell(self):
        return 0
