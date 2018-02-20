from splinter import Browser
from crawler import NegotiationItensCrawler
from crawler import BuyersCrawler
from crawler import BuyerDetailsCrawler
from downloader import Downloader
from downloader import ElementNotPresent
from parser import BuyerDetailsParser
from storage import Storage
import traceback

class BECSpider():

    root_url ='https://www.bec.sp.gov.br/becsp/aspx/DetalheOCItens.aspx' \
            '?chave=&detalhe=1'

    def __init__(self):
        self.downloader = Downloader()
        self.items_crawler = NegotiationItensCrawler(
                self.downloader, self.root_url)
        self.buyers_crawler = BuyersCrawler(self.downloader)
        self.storage = Storage()
        self.items = []

    def crawl(self):
        self.crawl_items()
        self.details_crawler = BuyerDetailsCrawler(self.downloader, self.items)
        self.crawl_details_for_items() 
        self.storage.save_items(self.items)
        self.downloader.quit()

    def crawl_items(self):
        try:
            for item in self.items_crawler.items():
                self.crawl_buyers_for_item(item)
        except Exception(e):
            traceback.print_exc()

    def crawl_details_for_items(self):
        items_with_details = []
        for item in self.details_crawler.items():
            items_with_details.append(item)
        self.items = items_with_details

    def crawl_buyers_for_item(self, item):
        try:
            cleaned_item = self.items_crawler.clean_item(item)
            cleaned_item['buyers'] = []
            self.items_crawler.visit_item(item)
            for buyer in self.buyers_crawler.items():
                cleaned_item['buyers'].append(buyer)
            self.items.append(cleaned_item)
        except ElementNotPresent:
            pass


if __name__ == '__main__':
    spider = BECSpider()
    spider.crawl()
