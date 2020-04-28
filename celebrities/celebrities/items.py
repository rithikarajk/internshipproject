# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CelebritiesItem(scrapy.Item):
    # define the fields for your item here like:


    image_url = scrapy.Field()
    Name = scrapy.Field()
    profession = scrapy.Field()
    source_of_income = scrapy.Field()
    career_high_point = scrapy.Field()
    number_of_times_on_forbes_list_since_2017 = scrapy.Field()
    earnings_2019 = scrapy.Field()
    profile = scrapy.Field()

