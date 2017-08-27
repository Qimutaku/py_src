#百科初爬
import urllib.request
from bs4 import BeautifulSoup
import re

def go():
    url='https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fr=aladdin'
    response=urllib.request.urlopen(url)
    html=response.read()
    soup=BeautifulSoup(html,'html.parser')

    for each in soup.find_all(href=re.compile('item')):
        print(each.text,'->',''.join(['https://baike.baidu.com',each['href']]))

if __name__=='__main__':
    go()
