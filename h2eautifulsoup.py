#词条爬取
import urllib.request
from bs4 import BeautifulSoup
import re

def main():
    name=input('请输入关键词：')
    name=urllib.parse.urlencode({'word':name})
    reponse=urllib.request.urlopen('http://baike.baidu.com/search/word?%s'%name)
    html=reponse.read()
    soup=BeautifulSoup(html,'html.parser')

    for each in soup.find_all(href=re.compile('view')):
        try:
            content=''.join([each.text])
            url2=''.join(['https://baike.baidu.com',each['href']])
            response2=urllib.request.urlopen(url2)
            htm2=response2.read()
            soup2=BeautifulSoup(htm2,'html.parser')
            if soup2.h2:
                content=''.join([content,soup2.h2.text])
            
            content=''.join([content,'->',url2])
            print(content)
        except urllib.error.URLError:
            print("继续")
            continue

if __name__=='__main__':
    main()
