__author__ = 'Ram Anandh'
__email__ = "rsramanandh@gmail.com"
__credits__ = ["rsramanandh@gmail.com"]

from library import AllLibraryMethods
from library.locators import HomepageLocators
from library.constants import HomePageConstants, AttributeConstants


class US1001(AllLibraryMethods):

    def tc_first_case(self):
        """
            Dummy testcase to check the logo of the website
            Author           : Ram Anandh
            Testcase number  : 1000
        """

        # Step-1: Launch google website
        self.launch_website(title=HomePageConstants.page_title, testcase=1)

        # Step-2: Verify the presence of google logo
        self.element_is_enabled(locator=HomepageLocators.google_logo, expectation=True,
                                testcase=2)

        # Step-3: Verify the presence of search bar
        self.element_is_enabled(locator=HomepageLocators.search_bar, expectation=True,
                                testcase=3)

        # Step-4: Verify the presence of search icon
        self.element_is_enabled(locator=HomepageLocators.search_icon, expectation=True,
                                testcase=4)

        # Step-5: Verify the presence of mic icon
        self.element_is_enabled(locator=HomepageLocators.mic_icon, expectation=True,
                                testcase=5)

        # Step-6: Verify google search button
        self.get_attribute_from_element(locator=HomepageLocators.google_search_btn,
                                        attribute_name=AttributeConstants.value,
                                        expectation=HomePageConstants.google_search, testcase=6)
