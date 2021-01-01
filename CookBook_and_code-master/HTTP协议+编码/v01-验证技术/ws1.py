import socket

# 理解两个参数的含义
# 理解创建socket的过程
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("127.0.0.1", 9527))
print('端口已绑定')

# 监听
sock.listen(3)
print('正在监听,准备接收')

# 接收一个传进来的socket
skt, addr = sock.accept()
print('收到传入的socket{0}'.format(skt))

# 读取消息
# 需要注意读取的信息的长度一定要小于等于世纪消息的长度,否则读不到数据,假死
msg = skt.recv(100)
print(type(msg))
print(msg.decode('utf-8'))

# 给对方反馈
msg = 'I love liuyihan.'
skt.send(msg.encode('utf-8'))

skt.close()
sock.close()

