from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class MinePage(BasePage):
    """
    我的页面-对象库层
    """

    def __init__(self):
        super().__init__()

        # 个人主页
        self.personal_page_btn = (By.ID, "com.douban.frodo:id/personal_page")

    def find_personal_page_btn(self):
        return self.find_element(self.personal_page_btn)


class MineHandle(BaseHandle):
    """
    我的页面-操作层
    """

    def __init__(self):
        self.mine_page = MinePage()

    def click_personal_page_btn(self):
        self.mine_page.find_personal_page_btn().click()


class MineProxy:
    """
    我的页面-业务层
    """

    def __init__(self):
        self.mine_handle = MineHandle()

    def to_personal_page(self):
        self.mine_handle.click_personal_page_btn()
