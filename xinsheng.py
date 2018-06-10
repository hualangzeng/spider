import requests


class xs_spider(object):
    def __init__(self):
        self.cookie = None
        pass

    def login(self, login_url):
        pass

    def ethic_spider(self, url):
        pass

if __name__ == "__main__":
    etspider = xs_spider()

    login_url = "https://uniportal.huawei.com/uniportal/login.do"
    url = "http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=919&cate=46"
    login_headers = {
'Host':'uniportal.huawei.com',
'Connection': 'keep-alive',
'Content-Length': '213',
'Cache-Control': 'max-age=0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Origin': 'https://uniportal.huawei.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Referer': 'https://uniportal.huawei.com/uniportal/?redirect=http%3A%2F%2Fxinsheng.huawei.com%2Fcn%2Findex',
'Accept-Encoding': 'gzip,deflate,sdch',
'Accept-Language': 'zh-CN,zh;q=0.8'
}

login_param = {'actionFlag':	'loginAuthenticate',
'lang':	'zh_CN',
'redirect':	'http%3A%2F%2Fxinsheng.huawei.com%2Fcn%2Findex',
'redirect_local':'',
'redirect_modify':	'',
'getloginMethod':	'null',
'uid':	'z00356451',
'password':	'zwy356451f++',
'loginFlag':	'byUid'}
s = requests.session()
r = s.post(login_url, headers = login_headers, data=login_param, verify=False)

#print(r.text)

ethic_cookie = r.cookies

header1 = {"UserAgent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36"}
r = s.post(url,headers = header1    )

with open("zhenghun.html", 'w+') as f:
    f.write(r.content.decode('utf-8 '))

#print(r.content.decode('utf-8'))
#print(r.text)

url1 = "http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=3815583"

r = s.get(url1,headers = header1,cookies = ethic_cookie    )

with open("lostandfound.html", 'w+') as f:
    f.write(r.content.decode('utf-8'))