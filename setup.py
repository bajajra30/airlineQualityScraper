from setuptools import setup, find_packages

setup(
    name='airlineQualityScraper',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = airlineQualityScraper.settings']},
)
