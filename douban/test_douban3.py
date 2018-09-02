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
写日记
"""
print("start.....")

driver.find_element_by_id("com.douban.frodo:id/btn_post").click()
driver.find_element_by_id("com.douban.frodo:id/mode1_note").click()

msg = "今天天气不错！"
driver.find_element_by_id("com.douban.frodo:id/rd__title").send_keys("hello123")
# driver.find_element_by_id("com.douban.frodo:id/rd__title").click()
driver.press_keycode(29)
# driver.press_keycode(112)
driver.press_keycode(67)
time.sleep(1)


driver.find_element_by_id("com.douban.frodo:id/rd__text").send_keys(msg)
driver.find_element_by_id("com.douban.frodo:id/rd__text").click()
# driver.press_keycode(29)
driver.press_keycode(67)
driver.find_element_by_id("com.douban.frodo:id/menu_item").click()

driver.find_element_by_xpath("//*[@text='读书']").click()

driver.find_element_by_xpath("//*[@text='发布']").click()




ele = driver.find_element_by_xpath("//*[contains(@text, '日记发布成功')]")
print(ele.text)

# time.sleep(5)
#
# # 关闭版本升级
# driver.find_element_by_id("com.fenbi.android.servant:id/close_btn").click()
#
# while True:
#     try:
#         xpath = "//*[@resource-id='com.fenbi.android.servant:id/title' and @text='练习']"
#         driver.find_element_by_xpath(xpath)
#         print("找到了")
#         break
#     except Exception:
#         print("没找到，点击一下屏幕")
#         TouchAction(driver).tap(x=100, y=100).perform()

time.sleep(10)

driver.quit()
