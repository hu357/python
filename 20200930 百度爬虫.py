import urllib.request
url = 'https://www.youdao.com'
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)
