import requests
from bs4 import BeautifulSoup
import urllib
import ssl
import os
import re

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'referer': 'https://www.menworld.org/mnwny/'
}
count = 1
newUrls = set()
oldUrls = set()

# 下载器


def download(url):

    res = requests.get(url)
    res.encoding = 'utf-8'
    return res.text

# 解析器：获取下一页和所有图片链接
def getData(linktext):
    soup = BeautifulSoup(linktext, 'html.parser')
    # 获取下一页链接
    link = soup.find('a', rel='next')
    # 获取所有图片
    images = soup.find_all('img', src=re.compile(
        r'http://bimgs.plmeizi.com/images/bing/.+\.jpg-listpic'))

    return link['href'], images

# 下载页面所有图片


def downloadImage(savepath, images):
    global count
    for image in images:
        print('downloading : '+str(count))
        res = requests.get(image['src'],stream=True, headers=HEADERS)
        with open(savepath + str(count) + '.jpg', 'wb') as imageW:
            for dataImage in res:
                imageW.write(dataImage)
        count += 1


# 添加新的url
def addUrl(link):
    if link not in newUrls or link not in oldUrls:
        newUrls.add(link)

# 获取一个url


def getUrl():
    url = newUrls.pop()
    oldUrls.add(url)
    return url

# 判断知否还有新的url


def hasUrl():
    return len(newUrls) != 0

# 调度中心


def mession(homeUrl):
    newUrls.add(homeUrl)
    while hasUrl:
        newUrl = getUrl()
        restext = download(newUrl)
        link, imageLinks = getData(restext)
        dirPath = newDir()
        downloadImage(dirPath, imageLinks)
        addUrl(link)
        oldUrls.add(newUrl)


# 在当前目录下新建文件夹
def newDir():
    path = os.getcwd() + '/bingCrawler/images/'
    
    if not os.path.exists(path):
        os.mkdir(path)
    return path


if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context

    pageUrl = 'http://bing.plmeizi.com/'
    print('messsion start.....')
    mession(pageUrl)
    print('mession complete....')
