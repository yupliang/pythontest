import urllib.request
import re
import os
import time
ur=urllib.request.urlopen("http://www.nipic.com/index.html")
content=ur.read()
mystr=content.decode("utf8")
ur.close()
# print(mystr)
p=r'(http:\S{1,}.jpg)'
pattern=re.compile(p)
li=re.findall(pattern,mystr)
os.makedirs('/Users/zhangzhongliang/Desktop/aa',exist_ok=True)

for a in li:
    print("下载图片："+a)
    b=a.split('/')[-1]
    urllib.request.urlretrieve(a,'/Users/zhangzhongliang/Desktop/aa/'+b)
    time.sleep(3)