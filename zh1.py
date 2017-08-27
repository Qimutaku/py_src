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
    print ('%.2f%%'%per)
    
def get_img(html):
    p=r'<img .*?src="([^"]*\.jpg)".*?>'
    
    imglist=re.findall(p,html)
    try:
        os.mkdir('NewPics3')
    except FileExistsError:
        pass
    os.chdir('NewPics3')
    for each in imglist:
        filename=each.split('/')[-1]
        try:
            req.urlretrieve(each,filename,cbk)
        except ValueError:
            pass
        execute_times(5)

def execute_times(times):

    for i in range(times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 滑动到浏览器底部
        time.sleep(2) # 等待页面加载
        try:
            driver.find_element_by_css_selector('button.QuestionMainAction').click() # 选中并点击页面底部的加载更多
            print("page" + str(i)) # 输出页面页数
            time.sleep(1) # 等待页面加载
        except:
            break

if __name__=='__main__':
    url='https://www.zhihu.com/question/20196263'
    get_img(open_url(url))
