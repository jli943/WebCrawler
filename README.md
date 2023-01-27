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

## Change the number of pages you want to crawel in setting.py 

```bash
CLOSESPIDER_PAGECOUNT=1000
```

##  Change the output file

The spider will output the extracted data in CSV format. Details in cc_gatech.py
```bash
with open('Keyword_URL_1000.csv', 'w') as f:
   for key in my_dict.keys():
         f.write("%s,%s\n"%(key,my_dict[key]))
```

## Plot (keywords extracted)/(pages) 

Crawl Statistics will plot when spider finished.
```bash
def plot_data(self, keyword, url):
        plt.plot(url, keyword)
        plt.xlabel('Number of URLs Visited')
        plt.ylabel('Number of Keywords Extracted')
        plt.title('Crawl Speed: Keywords Extracted vs URLs Visited')
        plt.show()
```

# Students Contributions

Junwei Li 
jli943@gatech.edu

# Note

Please be aware that crawling and extracting data from websites without their permission is against their terms of service and could be illegal. Make sure to read and understand a website's terms of service before crawling it.


