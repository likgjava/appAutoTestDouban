from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class HomePage(BasePage):
    """
    首页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 发表按钮
        self.post_btn = (By.ID, "com.douban.frodo:id/btn_post")
        # 写日记按钮
        self.note_btn = (By.ID, "com.douban.frodo:id/mode1_note")
        # 动态
        self.trend = (By.XPATH, "//*[@text='动态']")
        # 评论按钮
        self.comment_btn = (By.XPATH, "//*[@text='{}']/../..//*[@resource-id='com.douban.frodo:id/icon_comment']")

    def find_post_btn(self):
        return self.find_element(self.post_btn)

    def find_note_btn(self):
        return self.find_element(self.note_btn)

    def find_trend(self):
        return self.find_element(self.trend)

    def find_comment_btn(self, title):
        location = (self.comment_btn[0], self.comment_btn[1].format(title))
        return self.find_element(location)


class HomeHandle(BaseHandle):
    """
    首页-操作层
    """

    def __init__(self):
        self.home_page = HomePage()

    def click_post_btn(self):
        self.home_page.find_post_btn().click()

    def click_note_btn(self):
        self.home_page.find_note_btn().click()

    def click_trend(self):
        self.home_page.find_trend().click()

    def click_comment_btn(self, title):
        self.home_page.find_comment_btn(title).click()


class HomeProxy:
    """
    首页-业务层
    """

    def __init__(self):
        self.home_handle = HomeHandle()

    def to_write_note_page(self):
        """
        跳转到“写日记”页面
        """
        self.home_handle.click_post_btn()
        self.home_handle.click_note_btn()

    def to_trend_page(self):
        """
        跳转到“动态”页面
        """
        self.home_handle.click_trend()

    def to_comment_page(self, title):
        """
        跳转到“动态评论”页面
        """
        self.to_trend_page()
        self.home_handle.click_comment_btn(title)
