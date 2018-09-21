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
from page.shop_page import ShopProxy
from page.write_note_page import WriteNoteProxy
from utils import DriverUtil
from utils import YamlUtil


def build_add_goods_to_cart_data():
    data = YamlUtil.get_data_by_key("shop", "test_add_goods_to_cart")
    print(data)
    data_list = []
    for login in data.values():
        data_list.append((login["goods_name"], login["toast"]))
    print("data_list=", data_list)
    return data_list


class TestEditProfile:

    @classmethod
    def setup_class(cls):
        print('setup_class')
        cls.main_proxy = MainProxy()
        cls.mine_proxy = MineProxy()
        cls.personal_proxy = PersonalProxy()
        cls.shop_proxy = ShopProxy()

    # @classmethod
    # def teardown_class(cls):
    #     print('teardown_class')
    #     DriverUtil.quit_driver()

    def setup(self):
        # 进入‘市集’页面
        self.main_proxy.to_shop_page()
        pass

    @allure.step("添加商品到购物车功能")
    @pytest.mark.parametrize("goods_name,toast", build_add_goods_to_cart_data())
    def test_add_goods_to_cart(self, goods_name, toast):
        print("test_add_goods_to_cart goods_name={} toast={}".format(goods_name, toast))

        #
        self.shop_proxy.add_goods_to_cart(goods_name)

        assert utils.is_exist_web_toast(toast)
