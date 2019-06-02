from bs4 import BeautifulSoup
import re


class HtmlParser(object):

    # 解析器
    def parseHtml(self, pageurl, linktext):

        urls = set()
        data = {}

        soup = BeautifulSoup(linktext, 'html.parser')

        # 获取所有该页面所有url
        links = soup.find_all('a', href=re.compile(
            r'https://www.ithome.com/0/425/.+\.htm'))

        # 获取标题
        title = soup.find('div', class_='post_title')
        if title != None:
            title = title.find('h1').get_text()

        # 获取正文
        text = soup.find('div', class_='post_content')
        if text != None:
            text = text.get_text()

        for link in links:
            urls.add(link['href'])

        data['title'] = title
        data['htmltext'] = text
        data['url'] = pageurl

        return urls, data
