from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class EditProfilePage(BasePage):
    """
    编辑个人资料页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 昵称
        self.name = (By.ID, "com.douban.frodo:id/input_name")
        # 选择性别按钮
        # self.select_gender_btn = (By.ID, "com.douban.frodo:id/select_gender_action")
        # 选择性别
        # self.select_gender = (By.XPATH,
        # "//*[@resource-id='com.douban.frodo:id/select_dialog_listview']/*[@text='{}']")
        # 保存
        self.save_btn = (By.ID, "com.douban.frodo:id/save")

    def find_name(self):
        return self.find_element(self.name)

    def find_save_btn(self):
        return self.find_element(self.save_btn)


class EditProfileHandle(BaseHandle):
    """
    我的页面-操作层
    """

    def __init__(self):
        self.edit_profile_page = EditProfilePage()

    def input_name(self, name):
        self.input_text(self.edit_profile_page.find_name(), name)

    def click_save_btn(self):
        self.edit_profile_page.find_save_btn().click()


class EditProfileProxy:
    """
    我的页面-业务层
    """

    def __init__(self):
        self.mine_handle = EditProfileHandle()

    def edit_profile(self, name):
        self.mine_handle.input_name(name)
        self.mine_handle.click_save_btn()
