__author__ = 'Ram Anandh'
__email__ = "rsramanandh@gmail.com"
__credits__ = ["rsramanandh@gmail.com"]

import os
import json


class ConfigurationManager:
    def __init__(self):
        self.current_path = os.getcwd()
        self.configuration_file = os.path.join(os.path.abspath(self.current_path), "configurations",
                                               "windows.json")
        try:
            with open(self.configuration_file, "r") as json_file:
                self.configuration_data = json.load(json_file)
        except json.JSONDecodeError:
            print("Cannot load the parameters")
        self.test_sequence = self.configuration_data["test_sequence"]
