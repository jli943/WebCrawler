# Introduction

This project utilizes the Scrapy framework to crawl and extract data from websites and collect the statistcs from the website. Collect every title in each page and split them into keywords, final index the keyword with URL.


# 1.Installation and Run

Install scrapy the run the spider
This repository is valided with, but not limited to, python3.10 and scrapy2.7
```bash
cd project
pip install Scrapy
scrapy crawl cc_gatech
```

# 2.Spider Customization

You can customize the spider to crawl and extract data from specific websites and elements by editing the <spider_name>.py file in the spiders directory. In this file, is cc_gatech.py
The spider is configured to follow links and extract data from the specified elements on the pages it visits. You can edit the allowed_domains, start_urls, and rules attributes to control the behavior of the spider.

## 2.1 Change the seed websites in cc_gatech.py

```bash
start_urls = ["https://www.cc.gatech.edu/"]
```

## 2.2 Change the number of pages you want to crawel in setting.py 

```bash
CLOSESPIDER_PAGECOUNT=1000
```

##  2.3 Change the output file

The spider will output the extracted data in CSV format. Details in cc_gatech.py
```bash
with open('Keyword_URL_1000.csv', 'w') as f:
   for key in my_dict.keys():
         f.write("%s,%s\n"%(key,my_dict[key]))
```

## 2.4 Plot (keywords extracted)/(pages) 

Crawl Statistics will plot when spider finished.
```bash
def plot_data(self, keyword, url):
        plt.plot(url, keyword)
        plt.xlabel('Number of URLs Visited')
        plt.ylabel('Number of Keywords Extracted')
        plt.title('Crawl Speed: Keywords Extracted vs URLs Visited')
        plt.show()
```

# 3. Sourece Code
Spider source code
```bash
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
        with open('Keyword_URL_1000.csv', 'w') as f:
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
```

# 4. Students Contributions

Junwei Li 
jli943@gatech.edu

# 5. Note

Please be aware that crawling and extracting data from websites without their permission is against their terms of service and could be illegal. Make sure to read and understand a website's terms of service before crawling it.


