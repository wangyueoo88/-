import requests
from lxml import etree
class Spider():
    def __init__(self):
        self.web='https://movie.douban.com/top250'
        self.header={'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    def get_html(self,page):
        if page==0:
            return  self.web
        else:
            return  'https://movie.douban.com/top250?start={}&filter='.format(page*25)
    def get_response(self,url):
        response=requests.get(url,headers=self.header).text
        content_1=etree.HTML(response)
        name=content_1.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/img/@alt')
        return name
    def save_into_text(self,content):
        for n in content:
            with open('豆瓣电影TOP250.txt','a',encoding='utf-8') as cc:
                cc.write(n)
                cc.write('\n')
        print('写入完毕')

    def run(self):
        for i in range(10):
         self.save_into_text(self.get_response(self.get_html(i)))

def main():
    spider=Spider()
    spider.run()
if __name__ == '__main__':
    main()
