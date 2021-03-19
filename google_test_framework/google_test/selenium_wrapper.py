__author__ = 'Ram Anandh'
__email__ = "rsramanandh@gmail.com"
__credits__ = ["rsramanandh@gmail.com"]

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common import exceptions
import os
from .reports import Reports


class SeleniumWrapper:
    """@DynamicAttrs"""

    def __init__(self, **kwargs):
        self.log = None
        self.kwargs = kwargs
        self.browser = None
        self.test_suite_dict = dict()
        self.path_base = kwargs["path_base"]
        self.stop_testcase_on_fail = kwargs["stop_testcase_on_fail"]
        self.take_screenshot_on_pass = kwargs["take_screenshot_on_pass"]
        self.take_screenshot_on_fail = kwargs["take_screenshot_on_fail"]
        self.take_screenshots = kwargs["take_screenshots"]
        self.executable_path = kwargs["executable_path"]
        self.website_url = kwargs["website_url"]
        self.close_browser_between_testcases = kwargs["close_browser_between_testcases"]

    def open_browser(self, driver_path):
        """Opening the browser"""
        try:
            self.browser = webdriver.Chrome(
                os.path.join(os.path.abspath(driver_path), self.executable_path,
                             "chromedriver.exe"))
            self.browser.maximize_window()
        except exceptions as error:
            raise Exception("The following error occurred while opening the browser ", error)

    def close_browser(self):
        """Closing the opened browser session"""
        if self.browser:
            self.browser.close()

    def run_test(self, testcase_dict):
        """Running the testcase"""
        method = self.ST_testcases[testcase_dict]["method"]
        method()

    def start_sequence(self, test_sequence):
        """Scripts execution starts from here"""
        for i, test_suite in enumerate(test_sequence):
            if list(test_suite.keys())[0] == "testcase":
                current_testcase = test_suite["testcase"]
                self.log = Reports(testcase_name=current_testcase,
                                   take_screenshot_on_fail=self.take_screenshot_on_fail,
                                   take_screenshot_on_pass=self.take_screenshot_on_pass,
                                   path_base=self.path_base)
                self.log.create_file()
                try:
                    if current_testcase in list(self.ST_testcases.keys()):
                        for setup_methods in self.ST_testcases[current_testcase]['setup']:
                            setup_methods()
                        self.log.write_to_html(text="This is the first step in the testcase",
                                               result_type='info-lite')
                        self.run_test(current_testcase)
                    else:
                        self.log.error("Test case couldn't be found")
                except Exception as e:
                    self.log.error(str(e))
                finally:
                    self.log.finish_report()
                    self.close_browser()
                    self.test_suite_dict[i] = test_suite

    def verify_homepage(self, home_page_title, testcase=None):
        """Method verifies whether displayed page is homepage or not"""
        result = home_page_title in self.browser.title
        self.log.report(result, info_pass="Website is launched",
                        info_fail="Failed to launch the website", testcase=testcase)
        return result

    def get_element(self, locator, should_not_be_found=False, testcase=None):
        """used to get element from the given locator"""
        locator_type = locator[0]
        element = None
        if locator_type == By.XPATH:
            element = self.browser.find_element_by_xpath(locator[-1])
        if testcase:
            if should_not_be_found is False:
                self.log.report(element is not None, info_pass="Element is found",
                                info_fail="Element is not found", testcase=testcase)
            if should_not_be_found:
                self.log.report(element is None, info_pass="Element is not found",
                                info_fail="Element is Found even though it shouldn't have been",
                                testcase=testcase)
        return element

    def send_keys_to_element(self, locator, text="", wait=1, testcase=None):
        element = self.get_element(locator)
        element.send_keys(text)
        sleep(wait)
        element_text = self.get_text_from_element(locator=locator)
        if testcase:
            self.log.report(text == element_text, info_pass="Given text is sent to the element",
                            info_fail="Given text is not sent to the element", testcase=testcase)
        return element_text

    def get_text_from_element(self, locator, expectation=None, testcase=None):
        element = self.get_element(locator)
        element_text = element.text
        if expectation:
            if testcase:
                self.log.report(
                    expectation == element_text,
                    info_pass="Element text matches with the given expectation",
                    info_fail="Element text does not matches with the given expectation",
                    testcase=testcase)
            else:
                self.log.warning("Expectation is given but no testcase is found.")
        return element_text

    def click_element(self, locator, testcase=None):
        element = self.get_element(locator)
        element.click()
        if testcase:
            self.log.report(element, info_pass="Element is clicked",
                            info_fail="Element is not clickable or not found", testcase=testcase)
        return element

    def click_and_hold(self, locator, testcase=None):
        element = self.get_element(locator)
        action_chains = ActionChains(self.browser)
        action_chains.click_and_hold(on_element=element)
        if testcase:
            self.log.report(element, info_pass="Element is clicked and hold",
                            info_fail="Element is not clickable or not found", testcase=testcase)

    def execute_js(self, script):
        self.browser.execute_script(script)

    def element_is_enabled(self, locator, expectation=None, testcase=None):
        element = self.get_element(locator)
        status = element.is_enabled()
        if testcase:
            self.log.report(
                status == expectation, info_pass="Element status matches with expectation",
                info_fail="Element status does not match with expectation. Current status :" + str(
                    status), testcase=testcase)
        return status

    def get_attribute_from_element(self, locator, attribute_name, expectation=None, testcase=None):
        element = self.get_element(locator=locator)
        attribute_value = element.get_attribute(attribute_name)
        if testcase:
            self.log.report(
                attribute_value == expectation,
                info_pass="Attribute value matches with the expectation",
                info_fail="Attribute value does not matches with the expectation, "
                          "Actual attribute value: " + attribute_value, testcase=testcase)
        return attribute_value
