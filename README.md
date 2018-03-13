# android-app-automated-test
seu SRTP ，一个安卓安全性及性能评估程序

### 依赖

确保已经安装 android sdk 和apktool，并已配置到环境变量

### 使用(windows 命令行模式)

- app性能测试

```
python main.py --package  <app包名>  --activity  <app初始activity名> 
```

运行后会自动在当前目录生成一个名为report的html文档