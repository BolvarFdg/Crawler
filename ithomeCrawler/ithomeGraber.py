import htmldownload
import htmlparser
import outputer
import urlmanager


class Graber(object):

    def __init__(self):
        self.urlmanager = urlmanager.UrlManager()
        self.htmldownloader = htmldownload.HtmlDownload()
        self.htmlparser = htmlparser.HtmlParser()
        self.outputer = outputer.Outputer()

    def grab(self, starUrl):
        count = 1
        self.urlmanager.addNewUrl(starUrl)
        while self.urlmanager.hasNewUrl():
            newUrl = self.urlmanager.getNewUrl()
            # 输出当前爬取信息
            print('grab %d : %s' % (count, newUrl))
            resp = self.htmldownloader.download(newUrl)
            urls, data = self.htmlparser.parseHtml(newUrl, resp)
            self.urlmanager.addNewUrls(urls)
            self.outputer.collect_data(data)
            if count == 100:
                break
            count += 1

            self.outputer.output_html()


if __name__ == "__main__":
    url = 'https://www.ithome.com/'
    graber = Graber()
    graber.grab(url)
