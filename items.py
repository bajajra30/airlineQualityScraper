# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirlineQualityScraperItem(scrapy.Item):
    # define the fields for your item here like:
    airline = scrapy.Field()
    date_published = scrapy.Field()
    verified_user = scrapy.Field()
    rating = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    aircraft = scrapy.Field()
    traveller_type = scrapy.Field()
    cabin_flown = scrapy.Field()
    route = scrapy.Field()
    date_flown = scrapy.Field()
    seat_comfort = scrapy.Field()
    cabin_staff_service = scrapy.Field()
    food_beverages = scrapy.Field()
    ground_service = scrapy.Field()
    value_for_money = scrapy.Field()
    recommended = scrapy.Field()
    inflight_entertainment = scrapy.Field()
    wifi_and_connectivity = scrapy.Field()
