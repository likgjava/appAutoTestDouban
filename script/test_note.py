import allure
import pytest
import utils
from selenium.common.exceptions import TimeoutException

from page.comment_note_page import CommentNoteProxy
from page.home_page import HomeProxy
from page.login_page import LoginProxy
from page.write_note_page import WriteNoteProxy
from utils import DriverUtil
from utils import YamlUtil


def is_exist_text(driver, text):
    """
    判断页面中是否存在指定的文本内容
    :param driver: 驱动对象
    :param text: 文本内容
    :return: 存在返回True，不存在返回False
    """
    try:
        xpath = "//*[contains(@text, '{}')]".format(text)
        ele = driver.find_element_by_xpath(xpath)
        print("ele=====", ele)
        return ele is not None
    except TimeoutException:
        print("not find toast={}".format(text))
        return False


def build_write_note_data():
    data = YamlUtil.get_data_by_key("note", "test_write_note")
    print(data)
    data_list = []
    for login in data.values():
        data_list.append((login["title"], login["content"], login["toast"]))
    print("data_list=", data_list)
    return data_list

def build_comment_note_data():
    data = YamlUtil.get_data_by_key("note", "test_comment_note")
    print(data)
    data_list = []
    for login in data.values():
        data_list.append((login["title"], login["content"], login["toast"]))
    print("data_list=", data_list)
    return data_list


class TestNote:

    @classmethod
    def setup_class(cls):
        print('setup_class')
        cls.home_proxy = HomeProxy()
        # cls.mine_proxy = MineProxy()
        cls.write_note_proxy = WriteNoteProxy()
        cls.comment_note_proxy = CommentNoteProxy()
        # cls.setting_proxy = SettingProxy()


    # @classmethod
    # def teardown_class(cls):
    #     print('teardown_class')
    #     DriverUtil.quit_driver()

    def setup(self):
        # 进入‘写日记’页面
        # self.home_proxy.to_write_note_page()
        pass
    #
    #     # 如果是已登录状态，则要先退出
    #     is_login = self.mine_proxy.is_login()
    #     print("is_login=", is_login)
    #     if is_login:
    #         self.mine_proxy.to_setting_page()
    #         self.setting_proxy.logout()
    #
    #     # 进入‘登录’页面
    #     self.mine_proxy.to_login_page()

    # def teardown(self):
    #     print('teardown')
    #     # 如果是登录页面，则返回到‘我的’页面
    #     is_login_page = self.login_proxy.is_login_page()
    #     if is_login_page:
    #         self.login_proxy.back_to_mine_page()

    @pytest.mark.skip()
    @allure.step("写日记功能")
    @pytest.mark.parametrize("title,content,toast", build_write_note_data())
    def test_write_note(self, title, content, toast):
        print("test_write_note title={} content={} toast={}".format(title, content, toast))
        allure.attach("用例参数：", "title={} content={} toast={}".format(title, content, toast))

        # 进入‘写日记’页面
        self.home_proxy.to_write_note_page()

        # 写日记
        self.write_note_proxy.write_note(title, content)

        # 截图
        png = DriverUtil.get_driver().get_screenshot_as_png()
        allure.attach("截图", png, allure.attach_type.PNG)

        assert utils.is_exist_toast(toast)

    @allure.step("评论日记功能")
    @pytest.mark.parametrize("title,content,toast", build_comment_note_data())
    def test_comment_note(self, title, content, toast):
        print("test_write_note title={} content={} toast={}".format(title, content, toast))
        allure.attach("用例参数：", "title={} content={} toast={}".format(title, content, toast))

        # 跳转到“动态评论”页面
        self.home_proxy.to_comment_page(title)

        # 评论
        self.comment_note_proxy.comment_note(content)

        # 断言
        assert utils.is_exist_toast(toast)
