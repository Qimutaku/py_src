#opener

import urllib.request as re

#URL='http://www.whatismyip.com.tw'
URL='http://www.ipip.net/ip.html'
proxy_support=re.ProxyHandler({'http':'122.72.32.88'})
opener=re.build_opener(proxy_support)

#req=re.urlopen(URL)
req=opener.open(URL)
html=req.read().decode('utf-8')
print(html)
