import scrapy
from bs4 import BeautifulSoup
import lxml
from docx import Document








class CommunistpartySpider(scrapy.Spider):
    name = "communistParty"
    allowed_domains = ["example.com"]


    def start_requests(self):
        # 定义起始URL
        urls = [
            'https://www.12371.cn/2021/11/16/ARTI1637053491464119.shtml'
        ]
        for url in urls:
            yield scrapy.Request(url, callback=self.parseContents)

    def parseContents(self,resonse):
        soup = BeautifulSoup(response.text, 'lxml')
        fulltext = soup.find('div', {'class': 'dangyuanwang160317_ind01'})
    def parseArticle(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        fulltext=soup.find('div',{'class': 'dangyuanwang160317_ind01'})

        title=fulltext.find('h1',{'class': 'big_title'})
        fulltext=fulltext.find('div',{'class': 'font_area_mid'})
        mainText=fulltext.find_all('p')

        # 创建一个新的 Word 文档
        doc = Document()

        # 添加标题
        title = doc.add_heading(title.text, level=1)
        for p in mainText:
            paragraph = doc.add_paragraph(f'{p.text}')
        # 设置标题的样式（可选）
        title.bold = True
        title.italic = False
        title.underline = False

        # 保存文档到本地，如果文件已存在则覆盖
        doc.save(f'{title.text}.docx')