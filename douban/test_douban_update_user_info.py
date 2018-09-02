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


def select_date(year, month, day):
    select_year(year)
    select_month(month)
    select_day(day)


def select_year(year):
    select_date_item(0, year)


def select_month(month):
    select_date_item(1, month)


def select_day(day):
    select_date_item(2, day)


def select_date_item(item, num):
    xpath = "//android.widget.NumberPicker[@index={}]/android.widget.EditText".format(item)

    # 获取当前的年份
    selected_btn = driver.find_element_by_xpath(xpath)
    current_year = int(selected_btn.text)
    print("current_year==", current_year)

    # 一样大
    if num == current_year:
        print("一样大，不需要滑动了")
        return

    # 比当前年份大

    if num > current_year:
        print("向上滑动")
        swipe_date_element2(xpath, True, num - current_year)
    else:
        print("向下滑动")
        swipe_date_element2(xpath, False, current_year - num)


def swipe_date_element2(xpath, is_to_up, times):
    print("xpath=", xpath)
    print("is_to_up=", is_to_up)
    print("times=", times)
    print("==============================================")

    element = driver.find_element_by_xpath(xpath)
    start_x = element.location["x"] + element.size["width"] / 2
    start_y = element.location["y"]
    end_x = start_x
    end_y = element.location["y"] + element.size["height"] * 1.1

    for i in range(times):
        print("滑动次数==", i)
        if is_to_up:
            driver.swipe(end_x, end_y, start_x, start_y, 1000)
        else:
            driver.swipe(start_x, start_y, end_x, end_y, 1000)
        time.sleep(1)


# def swipe_date_element(xpath1, xpath2, is_to_up, times):
#     print("xpath1=", xpath1)
#     print("xpath2=", xpath2)
#     print("is_to_up=", is_to_up)
#     print("times=", times)
#     print("==============================================")
#     for i in range(times):
#         print("滑动次数==", i)
#         element1 = driver.find_element_by_xpath(xpath1)
#         element2 = driver.find_element_by_xpath(xpath2)
#         print("element1.text={} element2.text={}".format(element1.text, element2.text))
#         if is_to_up:
#             driver.drag_and_drop(element2, element1)
#         else:
#             driver.drag_and_drop(element1, element2)
#         time.sleep(5)


try:
    driver.find_element_by_xpath("//*[@text='我的']").click()
    driver.find_element_by_id("com.douban.frodo:id/personal_page").click()
    driver.find_element_by_id("com.douban.frodo:id/card_edit_profile_btn").click()

    # 头像
    # avatar = driver.find_element_by_id("com.douban.frodo:id/avatar")
    # avatar = driver.find_element_by_id("com.douban.frodo:id/arrow")
    # avatar.click()
    # driver.find_element_by_xpath("//*[resource-id='android:id/icon'][2]").click()
    # driver.find_element_by_id("com.douban.frodo:id/sure").click()

    # driver.find_element_by_id("com.douban.frodo:id/input_name").clear()
    # driver.find_element_by_id("com.douban.frodo:id/input_name").send_keys("OutMan2")
    # driver.find_element_by_id("com.douban.frodo:id/select_gender_action").click()
    # driver.find_element_by_xpath("//*[@resource-id='com.douban.frodo:id/select_dialog_listview']/*[@text='女']").click()
    #
    # driver.find_element_by_id("com.douban.frodo:id/select_city_action").click()
    # driver.find_element_by_xpath("//*[@resource-id='com.douban.frodo:id/city_list']//*[@text='广州']").click()
    #

    # driver.find_element_by_id("com.douban.frodo:id/birthday").set_text("2001-10-10")

    driver.find_element_by_id("com.douban.frodo:id/birthday").click()

    select_date(2000, 1, 1)

    driver.find_element_by_id("android:id/button1").click()

    driver.find_element_by_id("com.douban.frodo:id/save").click()

    ele = driver.find_element_by_xpath("//*[contains(@text, '修改成功')]")
    print(ele.text)

finally:
    time.sleep(10)

    driver.quit()































# 1.打开‘注册A.html’页面
#     2.使用CSS定位方式中id选择器定位用户名输入框，并输入：admin
#     3.使用CSS定位方式中属性选择器定位密码输入框，并输入：123456
#     4.使用CSS定位方式中class选择器定位电话号码输入框，并输入：18600000000
#     5.使用CSS定位方式中元素选择器定位注册用户按钮，并点击




