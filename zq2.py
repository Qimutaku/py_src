#爬取2
import urllib.request as req
import re
import os

def open_url(url):
    rep=req.Request(url)
    rep.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60')
    file=req.urlopen(rep)
    html=file.read().decode('utf-8')
    return html

def get_img(html):
    p=r'<img class="BDE_Image".*?src="([^"].*?\.jpg)".*?>'
    imglist=re.findall(p,html)
    os.chdir("C:\\Users\\Qimutaku\\Pictures\\Camera Roll")
    
    try:
        os.mkdir('newpic')
    except FileExistsError:
        pass
    os.chdir('newpic')
    for each in imglist:
        filename=each.split('/')[-1]
        req.urlretrieve(each,filename,None)

if __name__=='__main__':
    url='https://tieba.baidu.com/p/3488531865'
    get_img(open_url(url))
        
