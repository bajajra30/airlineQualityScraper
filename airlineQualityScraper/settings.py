# -*- coding: utf-8 -*-
BOT_NAME = 'airlineQualityScraper'

SPIDER_MODULES = ['airlineQualityScraper.spiders']
NEWSPIDER_MODULE = 'airlineQualityScraper.spiders'
FEED_FORMAT = 'csv'
FEED_EXPORT_FIELDS = [
	'airline',
	'date_published',
	'title',
	'text',
	'date_flown',
	'rating',
	'verified_user',
	'route',
	'aircraft',
	'traveller_type',
	'cabin_flown',
	'seat_comfort',
	'cabin_staff_service',
	'food_beverages',
	'ground_service',
	'inflight_entertainment',
	'value_for_money',
	'wifi_and_connectivity',
	'recommended'
]
# Disable cookies (enabled by default)
COOKIES_ENABLED = False
