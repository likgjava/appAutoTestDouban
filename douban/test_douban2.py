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
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
driver.implicitly_wait(5)

"""
发表说说
"""

driver.find_element_by_id("com.douban.frodo:id/btn_post").click()
driver.find_element_by_id("com.douban.frodo:id/mode1_text").click()
msg = "今天天气不错，心情很美丽！"
driver.find_element_by_id("com.douban.frodo:id/dou_broadcast_edittext").send_keys(msg)

# 发表图片
driver.find_element_by_id("com.douban.frodo:id/add").click()
driver.find_element_by_id("com.douban.frodo:id/item_select_layout").click()
driver.find_element_by_id("com.douban.frodo:id/text").click()

driver.find_element_by_id("com.douban.frodo:id/publish").click()




ele = driver.find_element_by_xpath("//*[contains(@text, '发送成')]")
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
