import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utils import DriverUtil


class ShopPage(BasePage):
    """
    市集页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 商品条目
        self.goods = (By.XPATH, "//p[text()='{}']")
        # 立即购买按钮
        self.buy_btn = (By.LINK_TEXT, "立即购买")
        # 加入购物车按钮
        self.add_cart_btn = (By.LINK_TEXT, "加入购物车")

    def find_goods(self, title):
        location = (self.goods[0], self.goods[1].format(title))
        return self.find_element(location)

    def find_buy_btn(self):
        return self.find_element(self.buy_btn)

    def find_add_cart_btn(self):
        return self.find_element(self.add_cart_btn)


class ShopHandle(BaseHandle):
    """
    市集页-操作层
    """

    def __init__(self):
        self.home_page = ShopPage()

    def click_goods(self, title):
        self.home_page.find_goods(title).click()

    def click_buy_btn(self):
        self.home_page.find_buy_btn().click()

    def click_add_cart_btn(self):
        self.home_page.find_add_cart_btn().click()


class ShopProxy:
    """
    市集页-业务层
    """

    def __init__(self):
        self.home_handle = ShopHandle()

    def add_goods_to_cart(self, goods_name):
        """
        """
        DriverUtil.switch_to_webview()
        time.sleep(3)

        DriverUtil.switch_to_last_window()
        self.home_handle.click_goods(goods_name)
        time.sleep(3)

        DriverUtil.switch_to_last_window()
        self.home_handle.click_buy_btn()
        time.sleep(3)

        DriverUtil.switch_to_last_window()
        self.home_handle.click_add_cart_btn()

