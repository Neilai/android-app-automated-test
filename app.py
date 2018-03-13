__author__ = "Neil"
__time__ = "2018/3/12 14:11"

import csv
import os
import time

class App(object):

    def __init__(self,package,activity):
        self.content = ""
        self.startTime = 0
        self.package=package
        self.activity=activity

        self.timeData=[]
        self.cpuStatus=[]
        self.memData=[]
        self.trafficData=[]
    #启动App
    def LaunchApp(self):
        cmd = 'adb shell am start -W -n '+self.package+"/"+self.activity
        self.content=os.popen(cmd)


    #停止App
    def StopApp(self):
        #cmd = 'adb shell am force-stop com.android.browser'
        cmd = 'adb shell input keyevent 3'
        os.popen(cmd)

    #获取启动时间
    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime


    #获取当前时间
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    #测试启动时间
    def testLaunchtime(self,cnt=1):
        while cnt>0:
            currenttime = self.getCurrentTime()
            self.LaunchApp()
            time.sleep(5)
            elpasedtime = self.GetLaunchedTime().strip()
            self.StopApp()
            time.sleep(2)
            self.timeData.append((currenttime, elpasedtime))
            cnt=cnt-1

    def testCpuStatus(self):
        cmd="adb shell dumpsys cpuinfo | findstr "+self.package
        print(cmd)
        result = os.popen(cmd)
        cpuvalue=0
        for line in result.readlines():
            if "%" in line:
                cpuvalue =line.strip().split("%")[0].strip()
        currenttime = self.getCurrentTime()
        self.cpuStatus.append((currenttime, cpuvalue))

    def testMem(self):
        cmd = "adb shell procrank| findstr "+self.package
        content = os.popen(cmd).readline()
        if content:
            print(content)
            line = "#".join(content.split())
            vss = line.split("#")[1].strip("K")
            rss = line.split("#")[2].strip("K")
            currenttime = '"'+str(self.getCurrentTime())+'"'
            self.memData.append((currenttime,vss,rss))

    def testTraffic(self):
        # 执行获取进程的命令
        cmd="adb shell ps | findstr "+self.package
        result = os.popen(cmd)
        pid = result.readlines()[0].split(" ")[1]
        cmd="adb shell cat /proc/" + pid + "/net/dev"
        traffic = os.popen(cmd)
        print(cmd)
        for line in traffic:
            if "eth0" in line:
                line = "#".join(line.split())
                receive = line.split("#")[1]
                transmit = line.split("#")[9]
            elif "eth1" in line:
                line = "#".join(line.split())
                receive2 = line.split("#")[1]
                transmit2 = line.split("#")[9]

        alltraffic = int(receive) + int(transmit) + int(receive2) + int(transmit2)
        alltraffic = alltraffic / 1024
        currenttime = self.getCurrentTime()
        self.trafficData.append((currenttime, alltraffic))


