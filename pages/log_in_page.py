from pages.feature_page import HipChatFeaturePage
from pages.basepage import BasePage
from config import hipchat_config as CONST


class HipChatLogInPage(BasePage):
    def __init__(self):
        super(HipChatLogInPage, self).__init__(CONST.hip_chat_url)
        self.login_field = self.driver.find_element_by_id('email')
        self.password_field = self.driver.find_element_by_id('password')

    def enter_email(self, login):
        self.login_field.clear()
        self.login_field.send_keys(login)

    def enter_pass(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)

    def click_signin_button(self):
        self.driver.find_element_by_id(CONST.signin_button).click()

    def authorization(self, login, password):
        self.enter_email(login)
        self.enter_pass(password)
        self.click_signin_button()
        if not self.is_element_present(CONST.error_message):
            return HipChatFeaturePage()