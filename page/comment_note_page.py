import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utils import DriverUtil


class CommentNotePage(BasePage):
    """
    评论日记页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 发回复
        self.comment_fake = (By.ID, "com.douban.frodo:id/input_comment_fake_text")
        # 回复内容
        self.reply_content = (By.ID, "com.douban.frodo:id/reply_content")
        # 发布按钮
        self.send_btn = (By.ID, "com.douban.frodo:id/btn_send")

    def find_comment_fake(self):
        return self.find_element(self.comment_fake)

    def find_reply_content(self):
        return self.find_element(self.reply_content)

    def find_send_btn(self):
        return self.find_element(self.send_btn)


class CommentNoteHandle(BaseHandle):
    """
    写日记页-操作层
    """

    def __init__(self):
        self.comment_note_page = CommentNotePage()

    def click_comment_fake(self):
        self.comment_note_page.find_comment_fake().click()

    def input_reply_content(self, content):
        self.input_text(self.comment_note_page.find_reply_content(), content)

    def click_send_btn(self):
        self.comment_note_page.find_send_btn().click()


class CommentNoteProxy:
    """
    写日记页-业务层
    """

    def __init__(self):
        self.comment_note_handle = CommentNoteHandle()

    def comment_note(self, content):
        """
        写日记
        """
        self.comment_note_handle.click_comment_fake()
        self.comment_note_handle.input_reply_content(content)
        self.comment_note_handle.click_send_btn()
