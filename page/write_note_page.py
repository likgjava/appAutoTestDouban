import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utils import DriverUtil


class WriteNotePage(BasePage):
    """
    写日记页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 标题
        self.title = (By.ID, "com.douban.frodo:id/rd__title")
        # 内容
        self.content = (By.ID, "com.douban.frodo:id/rd__text")
        # 继续按钮
        self.go_on_btn = (By.ID, "com.douban.frodo:id/menu_item")
        # 成长频道
        self.channel = (By.XPATH, "//*[@text='读书']")
        # 发布按钮
        self.post_btn = (By.XPATH, "//*[@text='发布']")

    def find_title(self):
        return self.find_element(self.title)

    def find_content(self):
        return self.find_element(self.content)

    def find_go_on_btn(self):
        return self.find_element(self.go_on_btn)

    def find_channel(self):
        return self.find_element(self.channel)

    def find_post_btn(self):
        return self.find_element(self.post_btn)


class WriteNoteHandle(BaseHandle):
    """
    写日记页-操作层
    """

    def __init__(self):
        self.write_note_page = WriteNotePage()

    def input_title(self, title):
        self.input_text(self.write_note_page.find_title(), title)
        self.deal_input_bug(self.write_note_page.find_title())

    def input_content(self, content):
        self.input_text(self.write_note_page.find_content(), content)
        self.deal_input_bug(self.write_note_page.find_content())

    def click_go_on_btn(self):
        self.write_note_page.find_go_on_btn().click()

    def click_channel(self):
        self.write_note_page.find_channel().click()

    def click_post_btn(self):
        self.write_note_page.find_post_btn().click()


class WriteNoteProxy:
    """
    写日记页-业务层
    """

    def __init__(self):
        self.write_note_handle = WriteNoteHandle()

    def write_note(self, title, content):
        """
        写日记
        """
        self.write_note_handle.input_title(title)
        self.write_note_handle.input_content(content)
        self.write_note_handle.click_go_on_btn()
        self.write_note_handle.click_channel()
        self.write_note_handle.click_post_btn()
