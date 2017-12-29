# Autoloads config, then other necessary files

import json
import pprint

# Files to be loaded
config = [
    'iot_devices',
    'rpi_receivers'
]

# Simple bootstrapper, loads config data into memory and other necessities
class Bootstrap:

    # Constructor
    def __init__(self):
        self.config = {}

    # Main execution, just loads config files
    def run(self):
        return self.loadConfig()


    # Loads config files into memory
    def loadConfig(self):

        # Iterate list
        for config_filename in config:

            # Load json file into python dict
            with open('../config/' + config_filename + ".json")) as data_file:
                config_data = json.load(data_file)
                pp(config_data)
                self.config[config_filename] = config_data

        # Return the config data
        return self.config
