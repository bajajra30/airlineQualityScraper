# AirlineQualityScraper #
This repo is an experiment with scrapy. A friend wanted to scrape some data from [Airline Quality Website](http://www.airlinequality.com/).
So you can scrape airline review data.

# Usage #
```sh
scrapy crawl airlineQuality -o outputFile -a airline=airlineName
```
outputFile: The file to output the data eg. csv or json 
airlineName: as it can be found in the address.

eg. aegean-airlines

The scraper will scrape the address:
http://www.airlinequality.com/airline-reviews/aegean-airlines/

# More Info #
Check [Scrapy Documentation](http://doc.scrapy.org/en/latest/index.html) for more info.
