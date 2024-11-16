# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InternshipItem(scrapy.Item):
    _id = scrapy.Field()
    url = scrapy.Field()
    company = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    pass
