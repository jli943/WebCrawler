import scrapy
from urllib.parse import urljoin
import matplotlib.pyplot as plt
import datetime

class CcGatechSpider(scrapy.Spider):
    name = "cc_gatech_BFS"
    start_urls = ["https://copperpodip.com"]
    allowed_domains = ["copperpodip.com"]


    queue = list()
    queue.append(start_urls[0])
    visited = set()
    visited.add(start_urls[0])
    counter = 1
    keywords_dict = {}
    #By plot
    keywords = []
    urls = []
    # durations = []

    def parse(self, response):
        
        if self.queue:
            if self.counter > 1000:
                # for keyword, urls in self.keywords_dict.items():
                #     yield {'keyword': keyword, 'urls': list(urls)}
                #self.plot_data(self.keywords, self.urls)
                return

            #start_time = datetime.datetime.now()
            #add inpage_url into queue
            # for link in response.css('a'):
            #     inpage_url = link.css('a::attr(href)').get()
            #     if inpage_url is not None:
            #         if inpage_url.startswith('https') and (inpage_url not in self.visited) and (inpage_url not in self.queue):
            #             self.queue.append(inpage_url)
            #         elif inpage_url.startswith('/'):
            #             inpage_url = urljoin(response.url, inpage_url)
            #             if (inpage_url not in self.visited) and (inpage_url not in self.queue):
            #                 self.queue.append(inpage_url)

            #extract keyword in this page
            title = response.css('title::text').get()
            yield{"text": title}
            yield{"url": response.url}
            yield{"counter" : self.counter}
                # if text is not None:
                #     for keyword in text.split():
                #         if keyword not in self.keywords_dict:
                #             self.keywords_dict[keyword] = set()
                #         self.keywords_dict[keyword].add(response.url)
            #Crawl next URL
            for link in response.xpath('*//a/@href').getall():
                self.queue.append(link)
            next_url = self.queue.pop(0)
            yield{"queue":len(self.queue)}
            self.counter+=1
            self.keywords.append(len(self.keywords_dict))
            self.urls.append(len(self.visited))
            self.visited.add(next_url)
            # end_time = datetime.datetime.now()
            # duration = end_time - start_time
            # self.durations.append(duration.microseconds)
            yield response.follow(next_url, callback=self.parse)

        else:
            # for keyword, urls in self.keywords_dict.items():
            #         yield {'keyword': keyword, 'urls': list(urls)}
            #self.plot_data(self.keywords,self.urls)
            yield{"no URL"}
            return

    def plot_data(self, keyword, url):
        plt.plot(url, keyword)
        plt.xlabel('Number of URLs Visited')
        plt.ylabel('Number of Keywords Extracted')
        plt.title('Crawl Speed: Keywords Extracted vs URLs Visited')
        plt.show()

        # plt.plot(url, duration)
        # plt.xlabel('URLs')
        # plt.ylabel('Crawl Duration')
        # plt.title('Crawl Speed: URLs vs Duration')
        # plt.show()