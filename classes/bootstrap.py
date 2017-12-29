# Autoloads config, then other necessary files

import json
import time
from pprint import pprint
from classes.iotinterfaces import *

# Files to be loaded
config = [
    'iot_devices',
    'rpi_receiver'
]

# Simple bootstrapper, loads config data into memory and other necessities
class Bootstrap:

    # Constructor
    def __init__(self):
        self.config = {}

    # Main execution, just loads config files
    def run(self):
        print("\nLoading configurations.\n")
        self.loadConfig()
        self.loadIotDevices()
        self.loadRpiReceiver()
        return self.config


    # Loads config files into memory
    def loadConfig(self):

        # Iterate list
        for config_filename in config:

            print('-------------------------------------------------------')
            print('Loaded config for ' + config_filename)
            print("\t_______________________________________________")
            print('\tGUID\t\tType')
            print("\t-----------------------------------------------")

            # Load json file into python dict
            with open('./config/' + config_filename + ".json") as data_file:
                config_data = json.load(data_file)
                for data in config_data:
                    print("\t" + data['guid'] + "\t" + data['device_type'])
                self.config[config_filename] = config_data
                print('-------------------------------------------------------')



        # Return the config data
        return self.config

    # Ensures the IoT devices provided in the config can be seen
    # stores them
    def loadIotDevices(self):

        print("\n\nInitializing IoT Device Interfaces...");

        # Iterate our list of IoT devices, check conns, and save conn data in
        # the respective interfaces
        for iot_device in self.config['iot_devices']:

            # Chromecast
            if iot_device['device_type'] == 'chromecast':
                iot_device['interface'] = chromecast.ChromecastInterface(iot_device)

            # Philips HUE
            #if iot_device['device_type'] == 'philipshuehub':
                #iot_device['interface'] = philipshuehub.PhilipshuehubInterface(iot_device)


    # Loads up this unit's stream
    def loadRpiReceiver(self):
        # Dev is being done on desktop via MJPEG stream- TODO: implement cv camera capture
        return 0
