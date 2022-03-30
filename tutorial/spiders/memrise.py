from scrapy import Spider
import scrapy
from scrapy.selector import Selector

from tutorial.items import TutorialItem


class TestSpider(Spider):
    name = "memrise"
    allowed_domains = ["app.memrise.com"]
    start_urls = [
        "https://app.memrise.com/course/743532/nihongo-so-matome-n3-vocabulary-5/2/",
    ]

    # def start_requests(self):
    #     for x in range(1, 6):
    #         yield scrapy.Request("https://app.memrise.com/course/743532/nihongo-so-matome-n3-vocabulary-5/" + str(x) + "/", callback=self.parse)

    def parse(self, response):
        questions = Selector(response).xpath(
            '//div[@class="things clearfix"]/div')

        for question in questions:
            item = TutorialItem()

            item['Word'] = question.xpath(
                'div[@class="col_a col text"]/div[@class="text"]/text()').extract_first()
            item['Meaning'] = question.xpath(
                'div[@class="col_b col text"]/div[@class="text"]/text()').extract_first()

            yield item
