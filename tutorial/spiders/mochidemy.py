from scrapy import Spider
import scrapy
from scrapy.selector import Selector

from tutorial.mochiWord import MochiWord


class TestSpider(Spider):
    name = "mochidemy"
    allowed_domains = ["mochidemy.com"]
    start_urls = [
        "https://mochidemy.com/blog/1000-tu-vung-tieng-anh-co-ban/",
    ]

    def parse(self, response):
        questions = Selector(response).xpath(
            '//table[@class="has-fixed-layout"]/tbody/tr')

        for question in questions:
            item = MochiWord()

            item['TuVung'] = question.xpath(
                'td[1]/text()').extract_first()
            item['PhienAm'] = question.xpath(
                'td[2]/text()').extract_first()
            item['Nghia'] = question.xpath(
                'td[3]/text()').extract_first()

            yield item
