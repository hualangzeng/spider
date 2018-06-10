from spider_login.xs_downloader import downloader
from spider_login.xs_parser import xs_parser
from spider_login.xs_urlmanager import url_manager
from spider_login.xs_store import xs_store
import requests
import time

class scheduler(object):
    def __init__(self, start_url, xs_header):
        self.cookies = dict()
        self.start_url = start_url
        self.xs_header = xs_header
    def log_in(self, url):
        xs_header = {'Host':'uniportal.huawei.com',
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

        xs_data = {'actionFlag':	'loginAuthenticate',
                    'lang':	'zh_CN',
                    'redirect':	'http%3A%2F%2Fxinsheng.huawei.com%2Fcn%2Findex',
                    'redirect_local':'',
                    'redirect_modify':	'',
                    'getloginMethod':	'null',
                    'uid':	'z00356451',
                    'password':	'zwy356451f++',
                    'loginFlag':	'byUid'
                   }
        result = requests.post(url, headers = xs_header, data = xs_data,verify=False)
        #print(result.status_code)
        self.cookies = result.cookies

        pass

    def schedule(self):
        if self.start_url is not None:
            xs_u = url_manager()
            xs_d = downloader()
            xs_p = xs_parser()
            xs_st = xs_store()

            xs_u.add_url(self.start_url)
            while xs_u.is_empty(xs_u.new_url) == 0:
                tem_url = xs_u.get_url()
                page = xs_d.download(tem_url, self.xs_header,self.cookies)
                tem_url, tem_data = xs_p.parser(page)
                print(tem_data)
                xs_u.add_url(tem_url)
                xs_st.store(tem_data)
                time.sleep(2)


if __name__ == '__main__':
    start_url = "http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=919&cate=44"
    header1 = {"UserAgent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36"}
    xs_sch = scheduler(start_url, header1)
    xs_sch.log_in("https://uniportal.huawei.com/uniportal/login.do")
    print(xs_sch.cookies)

    xs_sch.schedule()
