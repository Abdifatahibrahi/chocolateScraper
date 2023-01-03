import scrapy


class ChocolatespiderSpider(scrapy.Spider):
    name = 'chocolatespider'
    allowed_domains = ['chocolate.co.uk']
    start_urls = ['https://www.chocolate.co.uk/collections/winter-sale']

    def parse(self, response):
        products = response.css('.product-item-meta')
        for product in products:
            product_link = product.css('a::attr(href)').get()
            product_name = product.css('a::text').get()
            

            yield {
                'product_name': product_name,
                'product_link': product_link
            }

            next_page = response.css('a.pagination__nav-item::attr("href")')[1].get()
            if next_page is not None:
                # next_page_url = 'https://www.chocolate.co.uk/collections/winter-sale' + next_page
                yield response.follow(next_page, callback=self.parse)




