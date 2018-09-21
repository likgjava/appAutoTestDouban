import time
import traceback

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

XPATH = "//*[@resource-id='com.douban.frodo:id/overlay_tab_layout']//*[@text='影评']"

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
影评
"""
print("start.....")

try:
    driver.find_element_by_xpath("//*[@text='书影音']").click()
    driver.find_element_by_id("com.douban.frodo:id/search_hint").click()
    video_name = "寄宿学校"
    driver.find_element_by_id("com.douban.frodo:id/search").send_keys(video_name)
    driver.find_element_by_xpath("//*[@resource-id='com.douban.frodo:id/recycler_view']//*[contains(@text, '{}')]".format(video_name)).click()
    driver.find_element_by_xpath("%s" % XPATH).click()

    driver.find_element_by_id("com.douban.frodo:id/btn_post").click()
    driver.find_element_by_id("com.douban.frodo:id/mode2_review").click()

    e = driver.find_element_by_id("com.douban.frodo:id/rating_bar")
    TouchAction(driver).tap(e, e.size["width"]/2, e.size["height"]/2).perform()

    driver.find_element_by_id("com.douban.frodo:id/rd__title").send_keys("真搞笑2")
    driver.find_element_by_id("com.douban.frodo:id/rd__title").click()
    driver.press_keycode(7)  # 数字键0
    driver.press_keycode(67)  # 退格键

    content = "真的太搞笑了！真的太搞笑了！真的太搞笑了！真的太搞笑了！真的太搞笑了！真的太搞笑了！" \
              "真的太搞笑了！真的太搞笑了！真的太搞笑了！真的太搞笑了！真的太搞笑了！真的太搞笑了！" \
              "真的太搞笑了！真的太搞笑了！真的太搞笑了！真的太搞笑了！真的太搞笑了！真的太搞笑了！" \
              "真的太搞笑了！真的太搞笑了！真的太搞笑了！"
    driver.find_element_by_id("com.douban.frodo:id/rd__text").send_keys(content)
    driver.find_element_by_id("com.douban.frodo:id/rd__text").click()
    driver.press_keycode(7)  # 数字键0
    driver.press_keycode(67)  # 退格键

    # 继续
    driver.find_element_by_id("com.douban.frodo:id/menu_item").click()
    driver.find_element_by_xpath("//*[@text='发布']").click()

    xpath = "//*[contains(@text, '{}')]".format("发布成功")
    print("find toast xpath={}".format(xpath))
    ele = WebDriverWait(driver, 10, 0.1).until(lambda x: x.find_element_by_xpath(xpath))
    print("toast===", ele.text)


except Exception:
    traceback.print_exc()
finally:
    time.sleep(10)
    driver.quit()
