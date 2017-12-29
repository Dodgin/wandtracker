import phue
from pprint import pprint

# Handles all things interfacing with a philips hue
class PhilipshuehubInterface:

    # Constructor
    def __init__(self,config_data):
        print("Initializing Philips Hue Hub '" + config_data['guid'] + "' at "
            + config_data['ip'] + "... ", end="",flush=True)
        self.hue = None
        try:
            self.hue = phue.Bridge(config_data['ip'])
        except phue.PhueRegistrationException as err:
            print(err)
            raise

        return

    # Returns a list of all chromecast devices available
    @staticmethod
    def getDeviceList():
        return pychromecast.get_chromecasts()
