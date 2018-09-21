from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class VideoPage(BasePage):
    """
    书影音页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 影评按钮
        self.video_comment_btn = (By.XPATH, "//*[@resource-id='com.douban.frodo:id/overlay_tab_layout']//*[@text='影评']")
        # 发布按钮
        self.post_btn = (By.ID, "com.douban.frodo:id/btn_post")
        # 写影评按钮
        self.write_video_comment_btn = (By.ID, "com.douban.frodo:id/mode2_review_text")

    def find_video_comment_btn(self):
        return self.find_element(self.video_comment_btn)

    def find_post_btn(self):
        return self.find_element(self.post_btn)

    def find_write_video_comment_btn(self):
        return self.find_element(self.write_video_comment_btn)


class VideoHandle(BaseHandle):
    """
    书影音页-操作层
    """

    def __init__(self):
        self.home_page = VideoPage()

    def click_video_comment_btn(self):
        self.home_page.find_video_comment_btn().click()

    def click_post_btn(self):
        self.home_page.find_post_btn().click()

    def click_write_video_comment_btn(self):
        self.home_page.find_write_video_comment_btn().click()


class VideoProxy:
    """
    书影音页-业务层
    """

    def __init__(self):
        self.home_handle = VideoHandle()

    def to_write_video_comment_page(self):
        """
        跳转到“写影评”页面
        """
        self.home_handle.click_video_comment_btn()
        self.home_handle.click_post_btn()
        self.home_handle.click_write_video_comment_btn()
