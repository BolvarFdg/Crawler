import requests


class HtmlDownload(object):

    #下载器
    def download(self,url):
        res = requests.get(url)
        res.encoding = 'utf-8'
        return res.text
