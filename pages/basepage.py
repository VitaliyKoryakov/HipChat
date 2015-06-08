from config.driver import Driver
from config import hipchat_config as CONST
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BasePage(object):
    def __init__(self, url):
        self.driver = Driver.get()
        self.page_url = url
        self.open_page()

    def open_page(self, url=None):
        if not url:
            url = self.page_url
        self.driver.get(url)
        return self

    def sign_out(self):
        self.driver.find_element_by_class_name(CONST.avatar).click()
        self.driver.find_element_by_id(CONST.sign_out).click()

    def is_element_present(self, element):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, element))
            )
            return True
        except TimeoutException:
            return False