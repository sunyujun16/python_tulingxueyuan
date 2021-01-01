# HTTP项目实战
- 深入理解HTTP协议
- 模拟后台服务程序基本流程和大致框架
- 每个步骤一个文件夹

# v01验证技术
- 验证socket-tcp技术,看能否走通流程
- 使用浏览器发送消息, 访问地址
# v02 解析传入的HTTP协议
    - 根据HTTP协议格式, 诸行读取信息
    - 按行读取后, 拆解
    
# 书籍
- 图解HTTP, 图解系列

# v03-http协议封装返回
- 状态行: "HTTP/1.1 200 OK\r\n"
- 响应头: 
    - 'Content-Length: xxx\r\n'
    - "Date: 20201230\r\n"
- 空行
- 响应内容
    - "I love Liuyihan and she doesnt know."


# v04面向对象重构
- 两个对象
    - 一个负责监听接受socket, WebServer
    - 一个负责通讯, SocketHandler

# v05配置文件的加入
# v06返回静态页面
- 静态: 响应反馈后客户端不再进行修改()

# v07添加路由功能
- 根据请求调用响应处理函数
    1. 理解请求内容
    2. 调用相关的业务处理模块
    
# v08添加静态文件

# 编码问题
- 为什么需要编码问题
    - 本质上计算机只能识别01代码
    - 如何用一长串01代码表达复杂的信息
- 编码简史
    - 二进制
        - bit: 1 一位
        - byte: 00001111 8位, 能表示256个字符
    - 第一阶段: ASCII 0-127
    - 第二阶段: 百花齐放, GB2312, GBK, BIG5, latin1, JIS
        - latin1: 兼容欧洲多数语言
        - 韩国台湾: BIG5
        - 日本: JIS
        - ANSI-MBCS(multi-bytes charecter set, 多字节字符集)微软
    - 第三阶段: Unicode(ISO)
    
# 编码表示方法
- ASCII-american standard code for information interchange
    - 所有控制字符(包括回车,删除等)编码为0-31和127
    - 所有标点符号, 英文大小写为32-126
    - 预留128-255
    - 0xxx xxxx 
- Latin1
    - 兼容ASCII
    - 128-255西欧语言.希腊.泰语.阿拉伯语.希伯莱语
    - 欧元符号
    
- GB2312
    - 1xxxxxxx xxxxxxxx: 表示汉字

# Unicode编码
- 只是一个码表
- 0-0X10FFFF来映射这些字符, 1114112个字符
- 中文4E00-9FCF, 9FC4以后没有使用
- 不包含全角字符,和特殊文字
- UnicodeTransfoemationFormat
- UTF-8
    - 最多6字节
- UTF-16历史遗留问题
- UTF-32浪费空间

- UCS-4/UCS-2

# 常用概念
- 编码/解码:
- 大尾小尾
    - 大尾BigEndian 汉 --> 6C49 --> 011011000001001
    - 小尾LittleEndian 汉 --> 496C
    
- BOM(ByteOrderMark)
    - UTF-8没有字节顺序问题
     
# Python编码问题
- str
- bytes
- bytearray

- 查询码位
    - ord('A') --> 65
    - chr(65) --> A
    
- python文件默认utf-8
    - 声明第一行
    - """# -*- coding: windows-1252 -*-"""
    - 读写文件默认utf-8
- Python源码出现解码错误时, 返回SyntaError
    