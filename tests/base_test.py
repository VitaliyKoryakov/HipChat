from config.driver import Driver
import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = Driver.get()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        Driver.close()