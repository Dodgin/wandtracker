
class rpi:

    """

    RPi IR remote Circuit:
                                              (940nm)
                                  -----------(IR LED)---[200 Ohm]----| +3.3V VCC
                                  |  C
    GPIO(22)              B       |
    o------[10k Ohm]------(2N2222 Transistor)
                                 \|/  E
                                  |
                                 ===
                                  =   GND
    """
    # Causes an IR transmission to be sent from the rpi
    def sendRemoteTransmission(self, action):
        os.system("irsend SEND_ONCE " + self.tv_type + " " + action)
