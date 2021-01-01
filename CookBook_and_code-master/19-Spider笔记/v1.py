from urllib import request
import gzip
import chardet

'''
使用urllib.request请求一个网页内容，并把内容打印出来
'''

if __name__ == '__main__':

    url = "http://jobs.zhaopin.com/195435110251173.htm?ssidkey=y&ss=409&ff=03&sg=2644e782b8b143419956320b22910c91&so=1"
    # 打开相应url并把相应页面作为返回
    rsp = request.urlopen(url)

    # 把返回结果读取出来
    # 读取出来内容类型为bytes
    html = rsp.read()
    print(html)
    print(type(html))

    # try:
    #     html = gzip.decompress(html)
    # except:
    #     pass

    # 如果想把bytes内容转换成字符串，需要解码
    # html = html.decode()
    # print(html)

    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # 使用get取值保证不会出错
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)

    #页面已丢失,嘿


