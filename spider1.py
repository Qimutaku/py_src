#爬虫测试
import urllib.request
import urllib.parse

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null"
data={}
data['type']='AUTO'
data['i']='i love you'
data['doctype']='json'
data['xmlVersion']='1.6'
data['keyform']='fanyi.web'
data['ue']='UTF-8'
data['typoResult']='true'
data=urllib.parse.urlencode(data).encode('utf-8')
response=urllib.request.urlopen(url,data)
html=response.read().decode('utf-8')
print(html)
