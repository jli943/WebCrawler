import scrapy
import matplotlib.pyplot as plt
import csv

import datetime

class CcGatechSpider(scrapy.Spider):

    name = "cc_gatech"
    start_urls = ["https://www.cc.gatech.edu/"]
    allowed_domains = ["gatech.edu"]
    count = 0
    keywords_dict = {}

    keywords = []
    urls = []

    start_time = datetime.datetime.now()

    def closed(self, reason):
        print('#', self.count)
        # for keyword, urls in self.keywords_dict.items():
        #     yield {'keyword': keyword, 'urls': list(urls)}
        my_dict = self.keywords_dict
        with open('Keyword_URL_10.csv', 'w') as f:
            for key in my_dict.keys():
                f.write("%s,%s\n"%(key,my_dict[key]))
        
        self.plot_data(self.keywords, self.urls)

        elapsed_time = datetime.datetime.now() - self.start_time
        pages_per_minute = self.crawler.stats.get_value('response_received_count') / (elapsed_time.total_seconds() / 60)
        print(f'Pages per minute: {pages_per_minute}')



    def parse(self, response):
        self.count+=1
        # if self.count >self.settings.get('CLOSESPIDER_PAGECOUNT'):
        #     for keyword, urls in self.keywords_dict.items():
        #         yield {'keyword': keyword, 'urls': list(urls)}

        #     self.plot_data(self.keywords, self.urls)
            
        
        text = response.css('title::text').get()
        # yield {"Title":text}
        # yield {"URL": response.url}
        # yield {"#": self.count}

        if text is not None:
            for keyword in text.split():
                if keyword not in self.keywords_dict:
                    self.keywords_dict[keyword] = set()
                self.keywords_dict[keyword].add(response.url)

        self.keywords.append(len(self.keywords_dict))
        self.urls.append(self.count)

        for link in response.xpath('*//a/@href').getall():
            yield response.follow(link, self.parse)

    def plot_data(self, keyword, url):
        plt.plot(url, keyword)
        plt.xlabel('Number of URLs Visited')
        plt.ylabel('Number of Keywords Extracted')
        plt.title('Crawl Speed: Keywords Extracted vs URLs Visited')
        plt.show()