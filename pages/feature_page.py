from pages.basepage import BasePage
from config import hipchat_config as CONST


class HipChatFeaturePage(BasePage):
    def __init__(self):
        super(HipChatFeaturePage, self).__init__(CONST.hip_chat_url_features)

    def get_invite_url(self):
        invite_field = self.driver.find_element_by_id(CONST.invite_link_field)
        return invite_field.get_attribute('value')