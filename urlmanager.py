

class UrlManager(object):

    def __init__(self):
        self.newUrls = set()
        self.oldUrls = set()

    def getNewUrl(self):
        newUrl = self.newUrls.pop()
        self.oldUrls.add(newUrl)
        return newUrl
    
    def addNewUrls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            if url not in self.newUrls or url not in self.oldUrls:
                self.newUrls.add(url)

    def addNewUrl(self,url):
        if url is None:
            return
        if url not in self.newUrls or url not in self.oldUrls:
            self.newUrls.add(url)

    def hasNewUrl(self):
        return len(self.newUrls) != 0
