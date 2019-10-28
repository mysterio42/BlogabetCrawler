# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy,os
from scrapy.loader.processors import MapCompose,TakeFirst
from w3lib.html import remove_tags,replace_escape_chars,strip_html5_whitespace

class BlogabetParserItem(scrapy.Item):
    # define the fields for your item here like:
    teams = scrapy.Field(input_processor = MapCompose(remove_tags,lambda x : x.strip()))
    goals = scrapy.Field(input_processor = MapCompose(remove_tags,replace_escape_chars,strip_html5_whitespace,lambda x : x.strip()))
    feed_odd = scrapy.Field(input_processor = MapCompose(remove_tags,lambda x : x.strip()))
    how_many = scrapy.Field(input_processor = MapCompose(remove_tags,lambda x : x.strip()))
    bet = scrapy.Field(input_processor = MapCompose(remove_tags,lambda x : x.strip()))
    time = scrapy.Field(input_processor = MapCompose(remove_tags,lambda x : x.strip()))
    live = scrapy.Field(input_processor = MapCompose(remove_tags,lambda x : x.strip()))
    sport = scrapy.Field(input_processor = MapCompose(remove_tags,lambda x : x.strip()))
    casino = scrapy.Field(input_processor = MapCompose(remove_tags,lambda x : x.strip()))
    detail = scrapy.Field(input_processor = MapCompose(remove_tags,lambda x : x.strip()))

