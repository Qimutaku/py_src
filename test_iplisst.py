#写一个用代理IP列表随机访问的测试程序
import urllib.request
import random

url='http://www.ipip.net/ip.html'
iplist=input('请输入IP：').split(';')
while True:
    ip=random.choice(iplist)
    proxy_ip=urllib.request.ProxyHandler({'http':ip})
    opener=urllib.request.build_opener(proxy_ip)
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0')]
    try:
        print("正在用IP:%s访问"%ip)
        opener.open(url)
    except urllib.error.URLError:
        print("访问失败！")
    else:
        print("访问成功！")
    if input("是否继续访问？")=='N':
        break
