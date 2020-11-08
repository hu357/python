import urllib.request
import random

url = 'http://baidu.com'
#多加几个ip进去，每次随机使用ip
iplist = ['60.191.11.229:3128','132.145.89.166:3128','178.132.220.241:8080']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
