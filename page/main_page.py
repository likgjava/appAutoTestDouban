from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class MainPage(BasePage):
    """
    主页面-对象库层
    """

    def __init__(self):
        super().__init__()

        # 首页
        self.home_btn = (By.XPATH, "//*[@text='首页']")
        # 我的
        self.mine_btn = (By.XPATH, "//*[@text='我的']")
        # 书影音
        self.bav_btn = (By.XPATH, "//*[@text='书影音']")
        # 市集
        self.shop_btn = (By.XPATH, "//*[@text='市集']")

    def find_home_btn(self):
        return self.find_element(self.mine_btn)

    def find_mine_btn(self):
        return self.find_element(self.mine_btn)

    def find_bav_btn(self):
        return self.find_element(self.bav_btn)

    def find_shop_btn(self):
        return self.find_element(self.shop_btn)


class MainHandle(BaseHandle):
    """
    主页面-操作层
    """

    def __init__(self):
        self.main_page = MainPage()

    def click_home_btn(self):
        self.main_page.find_home_btn().click()

    def click_mine_btn(self):
        self.main_page.find_mine_btn().click()

    def click_bav_btn(self):
        self.main_page.find_bav_btn().click()

    def click_shop_btn(self):
        self.main_page.find_shop_btn().click()


class MainProxy:
    """
    主页面-业务层
    """

    def __init__(self):
        self.main_handle = MainHandle()

    def to_home_page(self):
        self.main_handle.click_mine_btn()

    def to_mine_page(self):
        self.main_handle.click_mine_btn()

    def to_bav_page(self):
        self.main_handle.click_bav_btn()

    def to_shop_page(self):
        self.main_handle.click_shop_btn()
