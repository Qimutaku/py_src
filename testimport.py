#test
from urllib import request as re
t=re.urlopen('http://www.baidu.com')
ht=t.read().decode('utf-8')
print(ht)
