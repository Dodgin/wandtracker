"""
TV Spell class, handles all things TV
"""
import os
from iotinterfaces import rpi

class tv:

    # Constructor
    def __init__(self):
        self.tv_type = "Vizio"

    # Causes an IR transmission to be sent from the rpi
    def sendRemoteTransmission(self, action):
        rpi.rpi().sendRemoteTransmission(action)
