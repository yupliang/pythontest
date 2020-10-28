import urllib.request
import re
import os
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
ur=urllib.request.urlopen("http://42.159.89.141/confluence/pages/viewpage.action?pageId=20873895")
content=ur.read()
mystr=content.decode("utf8")
ur.close()
# print(mystr)
p=r'(https:\S{1,}.png)'
pattern=re.compile(p)
li=re.findall(pattern,mystr)
os.makedirs('/Users/zhangzhongliang/Desktop/aa/a',exist_ok=True)

for a in li:
    print("下载图片："+a)
    b=a.split('/')[-1]
    urllib.request.urlretrieve(a,'/Users/zhangzhongliang/Desktop/aa/a/'+b)
    time.sleep(3)