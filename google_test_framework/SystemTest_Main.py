from library.pages import PageObjectMethod
from testcases import AllTestCases


class SystemTestMain(AllTestCases, PageObjectMethod):
    def __init__(self, application_url="", workspace="", **kwargs):
        super().__init__(**kwargs)
        self.application_url = application_url
        self.workspace = workspace

        self.ST_testcases = {
            "TestCase No1":
                {
                    "method": self.tc_first_case,
                    "setup": [self.start_session],
                    "tc_number": 101,
                    "group": ["home_page"]
                }
        }


if __name__ == '__main__':
    print("Please run start_sequence.py")
