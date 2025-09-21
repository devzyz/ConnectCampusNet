### 简介
    用于PC端自动登录华理校园网
### 配置及环境问题
    1. 需要安装selenium, yaml,  pyinstaller(打包为.exe文件时需要使用)
    2. 安装chromeDriver（chrome驱动程序）, 可点击以下链接安装，注意对应驱动与chrome的版本  
    https://developer.chrome.google.cn/docs/chromedriver
    注意：要将其放入与main.py同一目录下
    3. 配置config.yml文件，其结构如下
        config.yml
            username: root1
            password: root2
        将root1与root2替换为对应的账号和密码
### 使用方法
    1. 可直接运行main.py文件
    2. 将其打包为.exe文件，可执行以下代码
    pyinstaller -F -w --add-data "chromeDriver.exe;." --add-data "config.yml;." main.py
### 更新日志
    2025.9.21 提交
### 联系作者
    1358451905@qq.com (请备注来意)

