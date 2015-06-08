from base_test import BaseTest
from config import hipchat_config as CONST
from pages.log_in_page import HipChatLogInPage
from pages.sign_up_page import HipChatSingUpPage


class TestHipChat(BaseTest):
    def test_incorrect_password(self):
        log_in_page = HipChatLogInPage()
        log_in_page.authorization(CONST.login, CONST.incorrect_pass)

    def test_invitation_url(self):
        log_in_page = HipChatLogInPage()
        feature_page = log_in_page.authorization(CONST.login, CONST.correct_pass)
        invite_url = feature_page.get_invite_url()
        feature_page.sign_out()
        signup_page = HipChatSingUpPage(invite_url)
        #signup_page.sign_up(CONST.full_name, CONST.title, CONST.sign_up_password)
        while not signup_page.is_element_present(CONST.lobby):
            signup_page.sign_up(CONST.full_name, CONST.title, CONST.sign_up_password)

