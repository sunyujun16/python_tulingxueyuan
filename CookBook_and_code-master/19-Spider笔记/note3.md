# 动态HTML

## 爬虫跟反爬虫

## 动态HTML介绍
- JavaScrapt
- jQuery
- Ajax
- DHTML
- Python采集动态数据
    - 从Javascript代码入手采集
    - Python第三方库运行JavaScript，直接采集你在浏览器看到的页面

## Selenium + PhantomJS
- Selenium: web自动化测试工具
    - 自动加载页面
    - 获取数据
    - 截屏
    - 安装： pip install selenium==2.48.0
    - 官网： http://selenium-python.readthedocs.io/index.html
- PhantomJS(幽灵)
    - 基于Webkit 的无界面的浏览器 
    - 官网： http://phantomjs.org/download.html
- Selenium 库有有一个WebDriver的API
- WebDriver可以跟页面上的元素进行各种交互，用它可以来进行爬取
- 案例 v36
- chrome + chromedriver
    - 下载安装chrome： 下载+安装
    - 下载安装chromedriver：
- Selenium操作主要分两大类：
    - 得到UI元素
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by_xpath
        - find_elements_by_link_text
        - find_elements_by_partial_link_text
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作的模拟
        - 单击
        - 右键
        - 拖拽
        - 输入
        - 可以通过导入ActionsChains类来做到
    - 案例37
    
# 验证码问题
- 验证吗: 防止机器人或者爬虫
- 分类:
    - 简单图片
    - 极验,官网www.geetest.com
    - 12306
    - 电话
    - google验证
- 破解:
    - 通用方法
        - 下在网页和验证码
        - 手动输入验证号码
    - 简单图片
        - 使用图像识别软件或者文字识别软件
        - 可以使用第三方图像验证码破解网站,超级鹰
    - 极验
        - 破解比较麻烦
        - 可以模拟鼠标移动
        - 一直在进化,有团队在更新
    - 12306
        - 蛋疼
    - 电话(国外公司用的多): 
        - 语音识别
    - google验证
    
# Tesseract
- 机器视觉领域的基础软件
- OCR:OpticalChracterRecognition,光学文字识别
- Tesseract: 一个OCR库, google赞助
- 安装:
    - win/MacOS
    - apt-get install tesseract-ocr
    