__author__ = "Neil"
__time__ = "2018/3/12 14:10"
from app import App
import optparse
from reverse import reverseApp
import time
from jinja2 import Environment, PackageLoader
import codecs


if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("--package", dest="package", help="目标APP的包名")
    parser.add_option("--activity", dest="activity", help="目标activity")
    parser.add_option("--apk", dest="apk", help="目标APP的安装包")
    options, _ = parser.parse_args()
    if options.apk:
        data = reverseApp("QQ_794.apk")
        env = Environment(loader=PackageLoader('templates', 'html'))
        template = env.get_template('reverseResult.html')
        report = template.render(permission=data)
        with codecs.open("reverseReport.html", "w", encoding="utf-8") as f:
            f.write(report)
    elif options.package and options.activity:
        testApp=App(options.package,options.activity)
        testApp.testLaunchtime(5)
        testApp.LaunchApp()
        time.sleep(2)
        testApp.testCpuStatus()
        testApp.testMem()

        env = Environment(loader=PackageLoader('templates', 'html'))
        template = env.get_template('result.html')
        report=template.render(memData=testApp.memData,timeData=testApp.timeData,cpuStatus=testApp.cpuStatus[0][1])
        with codecs.open("report.html","w",encoding="utf-8") as f:
            f.write(report)
        testApp.StopApp()

# calculator=App("com.android.calculator2",".Calculator")
# calculator.testLaunchtime(3)
# calculator.LaunchApp()
# calculator.testCpuStatus()
# env = Environment(loader=PackageLoader('templates', 'html'))
# template = env.get_template('result.html')
# # report=template.render(cpuStatus=calculator.cpuStatus[0][1])
# # with codecs.open("report.html","w",encoding="utf-8") as f:
# #     f.write(report)
# calculator.StopApp()
# calculator.LaunchApp()
# time.sleep(1)
# calculator.testTraffic()
# calculator.StopApp()


