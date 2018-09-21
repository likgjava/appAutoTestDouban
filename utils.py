import os

import yaml
from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


def is_exist_toast(text):
    """
    判断toast元素是否存在
    :param text: toast内容
    :return: 存在返回True，不存在返回False
    """
    try:
        xpath = "//*[contains(@text, '{}')]".format(text)
        print("find toast xpath={}".format(xpath))
        ele = WebDriverWait(DriverUtil.get_driver(), 10, 0.1).until(lambda x: x.find_element_by_xpath(xpath))
        print("toast text=", ele.text)
        return ele is not None
    except TimeoutException:
        print("not find toast={}".format(text))
        return False


class YamlUtil:
    """
    yaml工具类
    """

    @staticmethod
    def get_all_data(file_name):
        print("getcwd=", os.getcwd())
        file_path = "./data/{}.yaml".format(file_name)
        with open(file_path, encoding="utf-8") as f:
            data = yaml.load(f)
            return data

    @staticmethod
    def get_data_by_key(file_name, key):
        data = YamlUtil.get_all_data(file_name)
        return data.get(key)


class DriverUtil:
    """
    驱动工具类
    """

    _driver = None

    @staticmethod
    def get_driver():
        # print("get_driver")
        if DriverUtil._driver is None:
            cap = {
                "platformName": "Android",
                "deviceName": "emulator",
                "appPackage": "com.douban.frodo",
                "appActivity": ".activity.SplashActivity",
                "automationName": "Uiautomator2",
                "noReset": True,
                "unicodeKeyboard": True,
                "resetKeyboard": True,
                "chromedriverExecutable": r"C:\Program Files (x86)\Appium\\resources\app\node_modules\appium-chromedriver\chromedriver\win\\chromedriver.exe",

            }
            DriverUtil._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
            DriverUtil._driver.implicitly_wait(10)
        return DriverUtil._driver

    @staticmethod
    def quit_driver():
        print("quit_driver")
        DriverUtil._driver.quit()

    @classmethod
    def switch_to_webview(cls):
        driver = cls.get_driver()
        print("page_source=", driver.page_source)
        print("contexts=", driver.contexts)
        driver.switch_to.context(driver.contexts[1])

    @classmethod
    def switch_to_last_window(cls):
        cls.get_driver().switch_to.window(cls.get_driver().window_handles[-1])
