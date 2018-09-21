from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utils import DriverUtil


class WriteVideoCommentPage(BasePage):
    """
    书影音页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 评分
        self.rating_bar = (By.ID, "com.douban.frodo:id/rating_bar")
        # 标题
        self.title = (By.ID, "com.douban.frodo:id/rd__title")
        # 内容
        self.content = (By.ID, "com.douban.frodo:id/rd__text")
        # 内容
        self.go_no_btn = (By.ID, "com.douban.frodo:id/menu_item")
        # 发布按钮
        self.submit_btn = (By.XPATH, "//*[@text='发布']")

    def find_rating_bar(self):
        return self.find_element(self.rating_bar)

    def find_title(self):
        return self.find_element(self.title)

    def find_content(self):
        return self.find_element(self.content)

    def find_go_no_btn(self):
        return self.find_element(self.go_no_btn)

    def find_submit_btn(self):
        return self.find_element(self.submit_btn)


class WriteVideoCommentHandle(BaseHandle):
    """
    书影音页-操作层
    """

    def __init__(self):
        self.home_page = WriteVideoCommentPage()

    def click_rating_bar(self):
        e = self.home_page.find_rating_bar()
        TouchAction(DriverUtil.get_driver()).tap(e, e.size["width"] / 2, e.size["height"] / 2).perform()

    def input_title(self, title):
        self.input_text(self.home_page.find_title(), title)
        self.deal_input_bug(self.home_page.find_title())

    def input_content(self, content):
        self.input_text(self.home_page.find_content(), content)
        self.deal_input_bug(self.home_page.find_content())

    def click_go_no_btn(self):
        self.home_page.find_go_no_btn().click()

    def click_submit_btn(self):
        self.home_page.find_submit_btn().click()


class WriteVideoCommentProxy:
    """
    书影音页-业务层
    """

    def __init__(self):
        self.home_handle = WriteVideoCommentHandle()

    def write_video_comment(self, title, content):
        """
        写影评
        """
        self.home_handle.click_rating_bar()
        self.home_handle.input_title(title)
        self.home_handle.input_content(content)
        self.home_handle.click_go_no_btn()
        self.home_handle.click_submit_btn()

