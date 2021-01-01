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

    print(rst)


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


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("127.0.0.1", 7852))
print('端口已绑定')

# 监听
sock.listen(3)
print('正在监听,准备接收')

# 接收一个传进来的socket
skt, addr = sock.accept()
print('收到传入的socket{0}'.format(skt))

# 处理请求内容
get_http_header(skt)

# 给对方反馈
msg = 'I love liuyihan.'
skt.send(msg.encode('utf-8'))

skt.close()
sock.close()


