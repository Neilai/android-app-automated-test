__author__ = "Neil"
__time__ = "2018/6/1 21:17"
from uiautomator import Device
import time
d = Device('192.168.181.101:5555', adb_server_host='localhost', adb_server_port=5037)
d.dump("hierarchy.xml")
def clickText(arr):
    for each in arr:
        d(text=each).click()
        time.sleep(1.5)
        d.press.back()
        time.sleep(0.5)
items=["校园网络","场馆预约","图书馆","成绩查询","课外研学","校车助手","校历查询","权益服务","空教室","跑操助手","教务通知"]
clickText(items)
d.swipe(89,1000,89,500)
items=["课表助手","实验助手","考试助手","人文讲座","校园活动"]
clickText(items)