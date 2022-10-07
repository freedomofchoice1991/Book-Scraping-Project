#/usr/bin/env/python3
#copyright ©reza.karami.arbeiten@gmail.com

#####  Using Scrapy framework for this website:
##   https://books.toscrape.com/
#####
### First we should install Scrapy

## $ python3 -m pip install scrapy
import scrapy

class BooksSpider(scrapy.Spider):
    name = "bookspider"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        for article in response.css("article.product_pod"):
            yield {
                'price': article.css(".price_color::text").extract_first(),
                'title': article.css("h3 > a::attr(title)").extract_first()
            }
            next = response.css('.next > a::attr(href)').extract_first()
            if next:
                yield response.follow(next, self.parse)

print()

### To run it use the command:
### $ scrapy runspider -o NAME_OF_FILE_STORED_IN  nameOfPythonFIle
### $ scrapy runspider -o books.csv book_scrapy.py
### Or store as json
### ### $ scrapy runspider -o books.json book_scrapy.py


#End