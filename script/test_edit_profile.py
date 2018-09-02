import allure
import pytest
import utils
from selenium.common.exceptions import TimeoutException

from page.comment_note_page import CommentNoteProxy
from page.edit_profile_page import EditProfileProxy
from page.home_page import HomeProxy
from page.login_page import LoginProxy
from page.main_page import MainProxy
from page.mine_page import MineProxy
from page.personal_page import PersonalProxy
from page.write_note_page import WriteNoteProxy
from utils import DriverUtil
from utils import YamlUtil


def build_edit_profile_data():
    data = YamlUtil.get_data_by_key("edit_profile", "test_edit_profile")
    print(data)
    data_list = []
    for login in data.values():
        data_list.append((login["name"], login["toast"]))
    print("data_list=", data_list)
    return data_list


class TestEditProfile:

    @classmethod
    def setup_class(cls):
        print('setup_class')
        cls.main_proxy = MainProxy()
        cls.mine_proxy = MineProxy()
        cls.personal_proxy = PersonalProxy()
        cls.edit_profile_proxy = EditProfileProxy()

    # @classmethod
    # def teardown_class(cls):
    #     print('teardown_class')
    #     DriverUtil.quit_driver()

    def setup(self):
        # 进入‘我的’页面
        self.main_proxy.to_mine_page()
        # 进入‘个人主页’页面
        self.mine_proxy.to_personal_page()
        # 进入‘编辑个人资料’页面
        self.personal_proxy.to_edit_profile_page()
        pass

    @allure.step("编辑个人资料功能")
    @pytest.mark.parametrize("name,toast", build_edit_profile_data())
    def test_edit_profile(self, name, toast):
        print("test_write_note name={} toast={}".format(name, toast))

        # 编辑个人资料
        self.edit_profile_proxy.edit_profile(name)

        assert utils.is_exist_toast(toast)
