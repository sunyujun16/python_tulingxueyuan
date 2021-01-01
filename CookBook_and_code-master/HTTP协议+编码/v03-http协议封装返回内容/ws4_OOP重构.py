import socket


# 理解两个参数的含义
# 理解创建socket的过程
def get_http_header(skt):
    """
    得到传入socket的http请求头
    :param skt: 通信的socket
    :return: 解析后的请求头, 字典格式
    """
    # 读取一行,直到读取的行是空行(HTTP报文)
    rst = {}
    line = get_line(skt)
    while line:
        """
        判断得到的行是请求行还是请求头
        """
        li = line.split(': ')
        if len(li) == 2:
            rst[li[0]] = li[1]
        else:
            print('请求行')
        line = get_line(skt)

    return rst


def get_line(skt):
    """
    从socket中读取某一行
    :param skt: socket
    :return: 返回读取到的一行str格式内容
    """
    # 前提:
    # http协议传输内容是ASCII编码
    # 真正传输是网络流传输byte流
    # 回车换行: b'\r',b'\n'

    # 每次从socket读取一个byte内容
    b1 = skt.recv(1)
    b2 = 0
    data = b''

    while b2 != b'\r' or b1 != b'\n':
        b2 = b1
        data += b1
        b1 = skt.recv(1)

    return data.strip(b'\r'b'\n').decode()


def send_rsp(skt, rsp_content):
    """
    发送返回值
    :param skt: 通信的socket
    :rsp_content: 响应正文
    :return:
    """

    # 响应状态行
    rsp_status = "HTTP/1.1 200 OK\r\n"
    # 响应头
    rsp_date = "Date: 20201230\r\n"
    rsp_length = "Content-Length: {0}\r\n".format(len(rsp_content))
    # 空行
    rsp_crlf = "\r\n"

    rsp = rsp_status + rsp_date + rsp_length + rsp_crlf + rsp_content

    skt.send(rsp.encode())


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("127.0.0.1", 7859))
print('端口已绑定')

# 监听
sock.listen(3)
print('正在监听,准备接收')

# 接收一个传进来的socket
skt, addr = sock.accept()
print('收到传入的socket{0}'.format(skt))

# 处理请求内容
http_info = get_http_header(skt)
print(http_info)

# 给对方反馈
msg = 'I love liuyihan yet she doesnt know it, doesnt matter, its not true love after all.'
send_rsp(skt, msg)

skt.close()
sock.close()


