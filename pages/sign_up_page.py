from pages.basepage import BasePage
import random
import string


class HipChatSingUpPage(BasePage):
    def __init__(self, url):
        super(HipChatSingUpPage, self).__init__(url)
        ##self.name_field = self.driver.find_element_by_id('name')
        ##self.email_field = self.driver.find_element_by_id('email')
        ##self.job_title_field = self.driver.find_element_by_id('title')
        ##self.password_field = self.driver.find_element_by_id('password')
        ##self.signup_field = self.driver.find_element_by_id('signup')

    def sign_up(self, full_name, title, password):
        self.enter_full_name(full_name).enter_email().enter_job_title(title).enter_password(password)
        self.click_sign_up_button()
        return self

    def enter_full_name(self, full_name):
        self.name_field = self.driver.find_element_by_id('name')
        self.name_field.clear()
        self.name_field.send_keys(full_name)
        return self

    def enter_email(self):
        self.email_field = self.driver.find_element_by_id('email')
        self.email_field.clear()
        email = ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(10)) + '@delete.me.com'
        self.email_field.send_keys(email)
        return self

    def enter_job_title(self, title):
        self.job_title_field = self.driver.find_element_by_id('title')
        self.job_title_field.clear()
        self.job_title_field.send_keys(title)
        return self

    def enter_password(self, password):
        self.password_field = self.driver.find_element_by_id('password')
        self.password_field.clear()
        self.password_field.send_keys(password)
        return self

    def click_sign_up_button(self):
        self.signup_field = self.driver.find_element_by_id('signup')
        self.signup_field.click()
        return self