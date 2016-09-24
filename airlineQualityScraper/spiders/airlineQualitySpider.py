# -*- coding: utf-8 -*-
import scrapy
import csv
from scrapy.selector import Selector
from airlineQualityScraper.items import AirlineQualityScraperItem


class AirlineQualitySpider(scrapy.Spider):
    name = "airlineQuality"  # Name of the spider
    # The xpaths we use to get the corresponding data
    xpaths_main = {
        'date_published': 'meta[@itemprop="datePublished"]/@content',
        'title': 'div[@class="body"]/h2[@class="text_header"]/text()',
        'text': 'div[@class="body"]/div[@class="tc_mobile"]/div' +
                '[@itemprop="reviewBody"]/text()',
        'rating': 'div[@itemprop="reviewRating"]/span[@itemprop=' +
                  '"ratingValue"]/text()'
    }
    xpaths_sec = {
        'date_flown': 'td[contains(@class, "date_flown")]/' +
                      'following-sibling::td/text()',
        'route': 'td[contains(@class, "route")]/following-sibling' +
                 '::td/text()',
        'aircraft': 'td[contains(@class, "aircraft")]/following-sibling' +
                    '::td/text()',
        'traveller_type': 'td[contains(@class, "type_of_traveller")]/' +
                          'following-sibling::td/text()',
        'cabin_flown': 'td[contains(@class, "cabin_flown")]/' +
                       'following-sibling::td/text()',
        'seat_comfort': 'td[contains(@class, "seat_comfort")]/' +
                        'following-sibling::td/' +
                        'span[contains(@class, "fill")]',
        'cabin_staff_service': 'td[contains(@class, "cabin_staff_' +
                               'service")]/following-sibling::td/' +
                               'span[contains(@class, "fill")]',
        'food_beverages': 'td[contains(@class, "food_and_beverages")]' +
                          '/following-sibling::td/span[contains(@class,' +
                          ' "fill")]',
        'ground_service': 'td[contains(@class, "ground_service")]/' +
                          'following-sibling::td/span[contains(@class,' +
                          ' "fill")]',
        'value_for_money': 'td[contains(@class, "value_for_money")]/' +
                           'following-sibling::td/span[contains(@class,' +
                           ' "fill")]',
        'inflight_entertainment': 'td[contains(@class, "inflight_' +
                                  'entertainment")]/following-sibling::' +
                                  'td/span[contains(@class, "fill")]',
        'wifi_and_connectivity': 'td[contains(@class, "wifi_and_' +
                                 'connectivity")]/following-sibling::td/' +
                                 'span[contains(@class, "fill")]',
        'recommended': 'td[contains(@class, "recommended")]/' +
                       'following-sibling::td/text()'
    }
    len_values = [
        'seat_comfort',
        'value_for_money',
        'inflight_entertainment',
        'wifi_and_connectivity',
        'food_beverages',
        'ground_service',
        'cabin_staff_service'
    ]

    def start_requests(self):
        """
        This is the init method of the spider. You set the url to scrape
        """
        url = 'http://www.airlinequality.com/airline-reviews/'
        self.airline = getattr(self, 'airline', None)
        if self.airline is not None:
            url = url + self.airline
            yield scrapy.Request(url, self.parse)
        else:
            print('Please give airline')

    def parse(self, response):
        # The main selector of the review items
        reviews = Selector(response).xpath('//article[@itemprop="review"]')
        # Loop through the review items and get the data we want
        for review in reviews:
            # Create a ratings object to save the data
            rating = AirlineQualityScraperItem()
            rating['airline'] = self.airline
            rating['verified_user'] = 'False'
            # Get the main data(The one that is not contained in the table)
            for key, value in self.xpaths_main.iteritems():
                data = review.xpath(value).extract()
                if len(data) > 1:
                    rating[key] = data[1]
                    rating['verified_user'] = 'True'
                else:
                    rating[key] = data[0]
            # Set the path of the table rows
            path = 'div[@class="body"]/div[@class="tc_mobile"]/div[@class="review-stats"]/table/tr'
            # Get the rows and get the data from each row
            for row in review.xpath(path):
                # Check if the data we want is in this row
                for key, value in self.xpaths_sec.iteritems():
                    data = row.xpath(value).extract()
                    if len(data) and key in self.len_values:
                        rating[key] = len(data)
                    elif len(data):
                        rating[key] = data[0]
            yield rating
        # Get the next page link
        next_page = response.xpath(
            '//div[@class="col-content"]/article/ul/li/a/@href'
        ).extract()[-1]
        # Parse next page
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
