import scrapy


class ChocolatespiderSpider(scrapy.Spider):
    name = 'chocolatespider'
    allowed_domains = ['chocolate.co.uk']
    start_urls = ['http://chocolate.co.uk/collections/all']

    def parse(self, response):
        products = response.css('.product-item ').getall()
        for product in products:
            product_name = product.css('product-item-meta a::text').get()
            product_link = product.css('product-item-meta a::attr(href)').get()

            yield {
                'product_name': product_name,
                'product_link': product_link
            }



