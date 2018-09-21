from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class BavPage(BasePage):
    """
    书影音页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 搜索框
        self.search_hint = (By.ID, "com.douban.frodo:id/search_hint")
        # 搜索输入框
        self.search = (By.ID, "com.douban.frodo:id/search")
        # 电影
        self.video_item = (By.XPATH, "//*[@resource-id='com.douban.frodo:id/recycler_view']//*[contains(@text, '{}')]")

    def find_search_hint(self):
        return self.find_element(self.search_hint)

    def find_search(self):
        return self.find_element(self.search)

    def find_video_item(self, kw):
        location = (self.video_item[0], self.video_item[1].format(kw))
        return self.find_element(location)


class BavHandle(BaseHandle):
    """
    书影音页-操作层
    """

    def __init__(self):
        self.home_page = BavPage()

    def click_search_hint(self):
        self.home_page.find_search_hint().click()

    def input_search(self, kw):
        self.input_text(self.home_page.find_search(), kw)

    def click_video_item(self, kw):
        self.home_page.find_video_item(kw).click()


class BavProxy:
    """
    书影音页-业务层
    """

    def __init__(self):
        self.home_handle = BavHandle()

    def to_video_page(self, kw):
        """
        跳转到电影详情页面
        """
        self.home_handle.click_search_hint()
        self.home_handle.input_search(kw)
        self.home_handle.click_video_item(kw)

