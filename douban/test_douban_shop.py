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
    # 'recreateChromeDriverSessions': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    "chromedriverExecutable": r"C:\Program Files (x86)\Appium\\resources\app\node_modules\appium-chromedriver\chromedriver\win\\chromedriver.exe",
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
driver.implicitly_wait(10)


"""
商城购物
"""
print("start.....")

try:
    driver.find_element_by_xpath("//*[@resource-id='com.douban.frodo:id/tab_strip']//*[@text='市集']").click()
    # driver.find_element_by_xpath("//*[@text='豆瓣豆品']").click()
    time.sleep(5)

    # driver.tap([(110, 630)])
    # time.sleep(3)

    print("page_source=", driver.page_source)
    print("contexts=", driver.contexts)

    driver.switch_to.context(driver.contexts[1])
    print("---------------------------------")

    print("contexts=", driver.contexts)
    print("current_context=", driver.current_context)
    print("current_url=", driver.current_url)
    print("title=", driver.title)

    print("window_handles====", driver.window_handles)
    # print("current_window_handle====", driver.current_window_handle)

    driver.switch_to.window(driver.window_handles[-1])
    print("title=========", driver.title)
    # print("page_source=", driver.page_source)

    driver.find_element_by_xpath("//p[text()='豆瓣读书笔记']").click()
    time.sleep(3)

    print("window_handles====", driver.window_handles)
    driver.switch_to.window(driver.window_handles[-1])
    print("title=========", driver.title)
    print("current_url=", driver.current_url)
    # print("page_source9999=", driver.page_source)

    driver.find_element_by_link_text("立即购买").click()
    time.sleep(3)

    print("=====================================================================")
    print("window_handles====", driver.window_handles)
    driver.switch_to.window(driver.window_handles[-1])
    print("title=========", driver.title)
    print("current_url=", driver.current_url)
    driver.find_element_by_link_text("加入购物车").click()
    print("page_source=", driver.page_source)

    fs = driver.find_elements_by_tag_name("iframe")
    print("fs.lenth===", len(fs))
    for f in fs:
        print("f.text===", f.text)

    # for i in range(1000):
        # if "成功加入" in driver.page_source or "iframe" in driver.page_source:
        #     print("找到了。。。")
        # else:
        #     print("i===", i)




    # ele = driver.find_element_by_xpath("//*[contains(text(), '成功加入购物车')]")
    # ele_list = driver.find_elements_by_xpath("//*")
    # for e in ele_list:
    #     print("e.text=======", e.text)

    # driver.switch_to.context(driver.contexts[0])
    # xpath = "//*[contains(@text, '{}')]".format("成功加入购物车")
    # ele = driver.find_element_by_xpath(xpath)
    # print("tttttt===", ele.text)


finally:
    time.sleep(10)
    driver.quit()
