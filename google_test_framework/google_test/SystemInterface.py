from .selenium_wrapper import SeleniumWrapper


class SystemTest(SeleniumWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self
