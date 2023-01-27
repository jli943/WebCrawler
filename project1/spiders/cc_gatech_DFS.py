import scrapy
from urllib.parse import urljoin


class CcGatechSpider(scrapy.Spider):
    name = 'cc_gatech_DFS'
    #allowed_domains = ['cc.gatech.edu']
    start_urls = ['http://cc.gatech.edu/']

    
    #visited.add(start_urls[0])
    count = 0
    max_count = 10

    def parse(self, response):
        self.page_count += 1
        base_url = response.url

        for link in response.css('a'):
            next_url = link.css('a::attr(href)').get()

            if next_url is not None:
                #if self.page_count < self.CLOSESPIDER_PAGECOUNT:
                    if next_url.startswith('https') and 'cc.gatech.edu' in next_url:
                        next_page = next_url
                        yield{'link': next_page}
                        #yield{"#": self.page_count}
                        yield response.follow(next_page, self.parse)
                    elif next_url.startswith('/'):
                        next_page = urljoin(base_url, next_url)
                        yield{'link': next_page}
                        #yield{"#": self.page_count}
                        yield response.follow(next_page, self.parse)

 # #self.page_count += 1
        # base_url = response.url

        # for link in response.css('a'):
        #     next_url = link.css('a::attr(href)').get()

        #     if next_url is not None:
        #         #if self.page_count < self.CLOSESPIDER_PAGECOUNT:
        #             if next_url.startswith('https') and 'cc.gatech.edu' in next_url:
        #                 next_page = next_url
        #                 yield{'link': next_page}
        #                 #yield{"#": self.page_count}
        #                 yield response.follow(next_page, self.parse)
        #             elif next_url.startswith('/'):
        #                 next_page = urljoin(base_url, next_url)
        #                 yield{'link': next_page}
        #                 #yield{"#": self.page_count}
        #                 yield response.follow(next_page, self.parse)