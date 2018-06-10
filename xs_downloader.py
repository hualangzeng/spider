import requests

class downloader(object):
    def __init__(self):
        pass

    def download(self, url, xs_headers, xs_cookie):
        page = requests.get(url, headers = xs_headers, cookies = xs_cookie)
        #print(page.content.decode('utf-8'))
        return page.content.decode('utf-8')