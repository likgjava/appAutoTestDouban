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
商城购物
"""
print("start.....")

try:
    driver.find_element_by_xpath("//*[@text='市集']").click()
    driver.find_element_by_xpath("//*[@text='豆瓣豆品']").click()
    time.sleep(2)

    driver.tap([(110, 630)])

    time.sleep(3)

    # for i in range(100):
    #     driver.swipe(100, 300, 100, 100, 3000)
    #     time.sleep(1)
    #     print("i==", i)

    print("page_source=", driver.page_source)
    print("contexts=", driver.contexts)
    # time.sleep(2)

    driver.switch_to.context("WEBVIEW_com.douban.frodo")
    print("---------------------------------")

    print("contexts=", driver.contexts)
    print("current_context=", driver.current_context)
    print("current_url=", driver.current_url)

    for i in range(3):
        # driver.swipe(100, 300, 100, 100, 3000)
        time.sleep(1)
        print("i==", i)

    page_source = driver.page_source
    print("page_source=", driver.page_source)
    print("读书笔记" in page_source)


    driver.find_element_by_link_text("立即购买").click()
finally:
    time.sleep(10)

    driver.quit()
