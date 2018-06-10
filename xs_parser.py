from bs4 import BeautifulSoup

class xs_parser(object):
    def parser(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')
        new_url = self._url_parser("http://xinsheng.huawei.com")
        #print(page)
        #print("new_url", new_url)
        data = self._data_parser()
        return new_url, data

    def _url_parser(self, base_url):
        try:
            #print(self.soup)
            next_url = self.soup.find('div',class_='bbs_page fr').find_all('li')
            next_url = next_url[-1].a['href']
            print("next_url", next_url)
            #print(next_url)


            return base_url + next_url
        except:
            print("parse_url error")
            return None
        pass

    def _data_parser(self):
        #print("soup",self.soup)
        contents = self.soup.find('div',class_="bbs_list").find_all('ul')[-1].find_all('li')

        print("contents", contents)
        data = []
        try:
            for l in contents:
                print("l", l)
                link = l.font.a['href']
                print("link",link)
                title = l.font.a['title']
                data.append((link,title))
            print("data",data)
            return data
        except:
            print("error content")
        pass
