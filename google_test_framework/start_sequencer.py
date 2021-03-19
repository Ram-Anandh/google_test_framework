__author__ = 'Ram Anandh'
__email__ = "rsramanandh@gmail.com"
__credits__ = ["rsramanandh@gmail.com"]

from configurations import ConfigurationManager
from SystemTest_Main import SystemTestMain
conf = ConfigurationManager()

with SystemTestMain(**conf.configuration_data) as test:
    test.start_sequence(conf.test_sequence)
    test.stop_session()
