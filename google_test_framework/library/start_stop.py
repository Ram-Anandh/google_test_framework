__author__ = 'Ram Anandh'
__email__ = "rsramanandh@gmail.com"
__credits__ = ["rsramanandh@gmail.com"]


class StartStop:
    """@DynamicAttrs"""

    def __init__(self):
        pass

    def start_session(self):
        self.open_browser(self.path_base)
        self.log.info("Browser is Launched")

    def launch_website(self, title, testcase=None):
        self.browser.get(self.website_url)
        self.verify_homepage(home_page_title=title, testcase=testcase)

    def stop_session(self):
        if self.browser:
            self.browser.quit()
        else:
            self.log.error("Browser session is not created")
