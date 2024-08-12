import scrapy


class BiliSpider(scrapy.Spider):
    name = "bili"
    allowed_domains = ["bilibili.com"]
    start_urls = ["https://bilibili.com"]

def parse(self, response):
    # 使用 XPath 提取信息
    for item in response.xpath('//div[@class="table-body-item"]'):
        title = item.xpath('.//a[@class="text-[#1fab89] table-body-item-words-word"]/span/text()').get()
        rank1 = item.xpath('.//div[@class="table-body-item-rank"]/span[1]/text()').get()
        rank2 = item.xpath('.//div[@class="table-body-item-rank"]/span[2]/text()').get()
        fluctuation = item.xpath('.//div[@class="table-body-item-rank-fluctuation"]/span/text()').get()

        # 输出信息
        self.log(f'Title: {title}, Rank1: {rank1}, Rank2: {rank2}, Fluctuation: {fluctuation}')

        # 如果需要将结果存储在文件或数据库中，可以在这里实现