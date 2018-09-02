import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

cap = {
    'platformName': 'Android',
    'deviceName': 'emulator',
    'appPackage': 'com.douban.frodo',
    'appActivity': '.activity.SplashActivity',
    'automationName': 'Uiautomator2',
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
driver.implicitly_wait(10)


"""
动态评论
"""
print("start.....")

driver.find_element_by_xpath("//*[@text='动态']").click()
driver.find_element_by_xpath("//*[@text='9999']/../..//*[@resource-id='com.douban.frodo:id/icon_comment']").click()



time.sleep(10)

driver.quit()
