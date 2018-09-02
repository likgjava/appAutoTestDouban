from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class PersonalPage(BasePage):
    """
    个人主页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 编辑个人资料
        self.edit_profile_btn = (By.ID, "com.douban.frodo:id/card_edit_profile_btn")

    def find_edit_profile_btn(self):
        return self.find_element(self.edit_profile_btn)


class PersonalHandle(BaseHandle):
    """
    我的页面-操作层
    """

    def __init__(self):
        self.edit_profile_page = PersonalPage()

    def click_edit_profile_btn(self):
        self.edit_profile_page.find_edit_profile_btn().click()


class PersonalProxy:
    """
    我的页面-业务层
    """

    def __init__(self):
        self.edit_profile_handle = PersonalHandle()

    def to_edit_profile_page(self):
        self.edit_profile_handle.click_edit_profile_btn()
