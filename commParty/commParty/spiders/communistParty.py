import scrapy
from bs4 import BeautifulSoup
import lxml
import docx
class CommunistpartySpider(scrapy.Spider):
    name = "communistParty"
    allowed_domains = ["example.com"]


    def start_requests(self):
        # 定义起始URL
        urls = [
            'https://www.12371.cn/2021/07/01/ARTI1625122624003841.shtml'
        ]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        fulltext=soup.find('div',{'class': 'dangyuanwang160317_ind01'})
        title=fulltext.find_all('h1',{'class': 'big_title'})
        mainText=fulltext.find_all('')

        pass
