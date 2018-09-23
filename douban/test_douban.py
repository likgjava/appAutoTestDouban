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

driver.find_element_by_id("com.douban.frodo:id/left").click()


# driver.find_element_by_xpath("//android.widget.EditText[1]").clear()
driver.find_element_by_id("com.douban.frodo:id/input_user_name").send_keys("13012345678")
# time.sleep(1)
driver.find_element_by_id("com.douban.frodo:id/input_password").send_keys("123")
# driver.find_elements_by_xpath("//android.widget.EditText")[1].clear()
# driver.find_elements_by_xpath("//android.widget.EditText")[1].send_keys("123")
#
driver.find_element_by_id("com.douban.frodo:id/sign_in_douban").click()


ele = driver.find_element_by_xpath("//*[contains(@text, '登录成功')]")
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
