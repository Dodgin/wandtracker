import pychromecast
from pprint import pprint

# Handles all things interfacing with a chromecast
class ChromecastInterface:

    # Constructor
    def __init__(self,config_data):
        print("Initializing Chromecast '" + config_data['guid'] + "' at "
            + config_data['ip'] + "... ", end="",flush=True)
        chromecasts = self.getDeviceList()
        self.cast = None
        it = iter(chromecasts)
        try:
            self.cast = next(cc for cc in chromecasts if cc.host == config_data['ip'])
            self.cast.wait()
            print('Loaded \'' + self.cast.device.friendly_name + '\'!')
        except StopIteration:
            print("\nError: Chromecast '" + config_data['guid'] + "' at "
                + config_data['ip'] + " could not be found.")
            pass
        finally:
            del it
        return

    """ Static Methods """

    # Returns a list of all chromecast devices available
    @staticmethod
    def getDeviceList():
        return pychromecast.get_chromecasts()


    """ Instance Methods """

    # Starts up an app
    def startApp(self, app_name):
        pprint(self.cast.status)
        return 0
