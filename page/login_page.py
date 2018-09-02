from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    """
    登录页面-对象库层
    """

    def __init__(self):
        super().__init__()

        # 账号密码登录按钮
        self.pwd_login_btn = (By.ID, "com.douban.frodo:id/left")
        # 用户名
        self.username = (By.ID, "com.douban.frodo:id/input_user_name")
        # 密码
        self.pwd = (By.ID, "com.douban.frodo:id/input_password")
        # 登录按钮
        self.login_btn = (By.ID, "com.douban.frodo:id/sign_in_douban")

    def find_pwd_login_btn(self):
        return self.find_element(self.pwd_login_btn)

    def find_username(self):
        return self.find_element(self.username)

    def find_pwd(self):
        return self.find_element(self.pwd)

    def find_login_btn(self):
        return self.find_element(self.login_btn)


class LoginHandle(BaseHandle):
    """
    登录页面-操作层
    """

    def __init__(self):
        self.login_page = LoginPage()

    def click_pwd_login_btn(self):
        self.login_page.find_pwd_login_btn().click()

    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    def input_pwd(self, pwd):
        self.input_text(self.login_page.find_pwd(), pwd)

    def click_login_btn(self):
        self.login_page.find_login_btn().click()



    def exist_login_btn(self):
        try:
            element = self.login_page.find_login_btn()
            return element is not None
        except Exception:
            return False


class LoginProxy:
    """
    登录页面-业务层
    """

    def __init__(self):
        self.login_handle = LoginHandle()

    def to_pwd_login_page(self):
        """
        跳转到“账号密码登录”页面
        :return:
        """
        self.login_handle.click_pwd_login_btn()

    def login(self, username, pwd):
        self.login_handle.input_username(username)
        self.login_handle.input_pwd(pwd)
        self.login_handle.click_login_btn()

    # def back_to_mine_page(self):
    #     self.login_handle.click_back_btn()

    def is_login_page(self):
        return self.login_handle.exist_login_btn()
