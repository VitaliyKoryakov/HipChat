from selenium.webdriver import Firefox


class Driver(object):
    instance = None

    @classmethod
    def get(cls, browser_type=Firefox):
        if not cls.instance:
            cls.instance = browser_type()
        return cls.instance

    @classmethod
    def close(cls):
        cls.get().quit()
        cls.instance = None
