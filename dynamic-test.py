__author__ = "Neil"
__time__ = "2018/5/21 9:06"
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time


caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "6.0"
caps["deviceName"] = "8FS5T16912012187"
caps["appPackage"] = "cn.seu.herald_android"
caps["appActivity"] = "cn.seu.herald_android.app_main.MainActivity"
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


def getClick(id):
    x = driver.find_element_by_id(id)
    x.click()
    time.sleep(0.3)

def getSend(id,keys):
    x = driver.find_element_by_id(id)
    x.send_keys(keys)


time.sleep(3)

# 登陆
getClick("tv_login")
getSend("tv_login_cardnum","213150245")
getSend("tv_login_pwd","Wo19971008")
getClick("btn_login_login")


time.sleep(9)


x=driver.find_element_by_android_uiautomator('new UiSelector().textContains("考试")')
x.click()
time.sleep(3)
driver.back()




service=driver.find_elements_by_id("tv_shortcut")
for i in range(len(service)):
    service[i].click()
    time.sleep(3.5)
    driver.back()

x=driver.find_element_by_android_uiautomator('new UiSelector().textContains("一卡通")')
x.click()
time.sleep(4)
driver.back()



x=driver.find_element_by_android_uiautomator('new UiSelector().textContains("跑操")')
x.click()
time.sleep(4)
driver.back()

driver.swipe(100, 800, 100, 100)

x=driver.find_element_by_android_uiautomator('new UiSelector().textContains("课表")')
x.click()
time.sleep(3.5)
driver.back()

driver.swipe(100, 1650, 100, 800)


x=driver.find_element_by_android_uiautomator('new UiSelector().textContains("实验")')
x.click()
time.sleep(2)
driver.back()
#
#
x=driver.find_element_by_android_uiautomator('new UiSelector().text("人文讲座")')
x.click()
time.sleep(2)
driver.back()

x=driver.find_element_by_android_uiautomator('new UiSelector().textContains("教务")')
x.click()
time.sleep(3)
driver.back()

x=driver.find_element_by_android_uiautomator('new UiSelector().text("校园活动")')
x.click()
time.sleep(3)
driver.back()

time.sleep(1)
TouchAction(driver).tap(x=938, y=1731).perform()
time.sleep(1)
TouchAction(driver).tap(x=680, y=379).perform()
time.sleep(1)
TouchAction(driver).tap(x=863, y=1022).perform()

time.sleep(10)
driver.quit()