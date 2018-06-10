
class url_manager(object):
    def __init__(self):
        self.new_url = set()
        self.old_url = set()

    def add_url(self, url):
        if url is not None:
            if url not in self.old_url:
                self.new_url.add(url)

    def add_url_batch(self,url_list):
        for l in url_list:
            self.add_url(l)

    def get_url(self):
        while self.is_empty(self.new_url) == 0:
            result = self.new_url.pop()
            if result not in self.old_url:
                return result
        return None



    def is_empty(self,url_set):
        if len(url_set) != 0:
            return 0
        else:
            return 1
