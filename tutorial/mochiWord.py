import scrapy


class MochiWord(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    TuVung = scrapy.Field()
    PhienAm = scrapy.Field()
    Nghia = scrapy.Field()
    pass
