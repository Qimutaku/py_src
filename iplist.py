#iplist
import urllib.request as re
import random

url='http://www.ipip.net/ip.html'
iplist=input('请输入IP：').split(sep=';')
while True:
    ip=random.choice(iplist)
    proi=re.ProxyHandler({'http':ip})
    opener=re.build_opener (proi)
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/54.0')]
    try:
        print('正在尝试使用%sIP访问'%ip)
        req=opener.open(url)
    except re.URLError:
        print('访问出错！')
    else:
        print('访问成功！')
    if input("请问是否继续访问？")=='N':
        break
                    
