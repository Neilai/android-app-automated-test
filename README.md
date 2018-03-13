# android-app-automated-test
seu SRTP ，一个安卓安全性及性能评估程序，目前已完成一些初始功能

### 依赖

- 确保已经安装 android sdk 和 apktool，并已配置到环境变量

- 必要的python包

  ```
  pip install jinja2
  ```

### 使用(windows 命令行模式)

- app性能测试

  ```
  python main.py --package  <app包名>  --activity  <app的activity名> 
  ```

​      运行后会自动在当前目录生成一个名为report的html文档，它对app的启动时间，内存占用，cpu占用率进行分析，如下所示

![](https://raw.githubusercontent.com/Neilai/android-app-automated-test/master/img/1.png)



​      

- app反编译分析

  ```
  python main.py --apk <app安装包>
  ```

  会自动在当前目录生成一个名为reverseReport的html文档，对app使用的系统权限进行分析，生成权限等级分析图谱

![](https://raw.githubusercontent.com/Neilai/android-app-automated-test/master/img/2.png)