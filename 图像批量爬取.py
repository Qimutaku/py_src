#图像批量爬取
import urllib.request as req
import re
import os

def open_url(url):
    rep=req.Request(url)
    rep.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0')
    file=req.urlopen(rep)
    html=file.read().decode('utf-8')
    return html
def cbk(a, b, c):  
    '''回调函数 
    @a: 已经下载的数据块 
    @b: 数据块的大小 
    @c: 远程文件的大小 
    '''  
    per = 100.0 * a * b / c  
    if per > 100:  
        per = 100  
    print ('%.2f\%'%per)
    
def get_img(html):
    p=r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'
    imglist=re.findall(p,html)
    try:
        os.mkdir('NewPics2')
    except FileExistsError:
        pass
    os.chdir('NewPics2')
    for each in imglist:
        filename=each.split('/')[-1]
        req.urlretrieve(each,filename,cbk)

if __name__=='__main__':
    url='https://tieba.baidu.com/p/3823765471'
    get_img(open_url(url))






  

