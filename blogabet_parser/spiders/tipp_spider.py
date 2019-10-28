import scrapy
from scrapy.http import FormRequest, Request
from blogabet_parser import readgm
from blogabet_parser.items import BlogabetParserItem
from scrapy.loader import ItemLoader


class BetSpider(scrapy.Spider):
    name = 'blogabet'
    start_urls = [
        'https://blogabet.com/#login'
    ]

    def parse(self, response):
        for el in response.xpath("//div[@class='feed-pick-title']"):
            loader = ItemLoader(item=BlogabetParserItem(), selector=el)
            loader.add_xpath('teams', "./div/h3/text()")
            loader.add_xpath('goals', "./div/div[@class='pick-line']/text()")
            loader.add_xpath('feed_odd', "./div/div[@class='pick-line']/span[@class='feed-odd']/text()")
            loader.add_xpath('how_many', "./div/div[@class='labels']/span[@class='label label-default']/text()")
            loader.add_xpath('bet', "./div/div[@class='labels']/a/text()")

            loader.add_xpath('sport', "./div/div[@class='sport-line']/small/span[@class='hidden-xs'][1]/text()")

            loader.add_xpath('live', "./div/div[@class='labels']/span[@class='label label-danger']/text()")
            loader.add_xpath('detail', "./div/div[@class='sport-line']/small/span[@class='hidden-xs'][2]/text()")

            loader.add_xpath('casino', "./div/div[@class='sport-line']/small/text()[2]")
            loader.add_xpath('time', "./div/div[@class='sport-line']/small/text()[3]")

            yield loader.load_item()
