from splinter import Browser
from crawler import NegotiationItensCrawler
from crawler import BuyersCrawler
from downloader import Downloader
from downloader import ElementNotPresent
from parser import BuyerDetailsParser
from storage import Storage
import traceback

class BECSpider():

    root_url ='https://www.bec.sp.gov.br/becsp/aspx/DetalheOCItens.aspx' \
            '?chave=&detalhe=1'

    def crawl(self):
        self.downloader = Downloader()

        self.items_crawler = NegotiationItensCrawler(
                self.downloader, self.root_url)
        self.buyers_crawler = BuyersCrawler(self.downloader)
        self.storage = Storage()
        
        items = []
        try:
            for item in self.items_crawler.items():
                cleaned_item = self.items_crawler.clean_item(item)
                cleaned_item['buyers'] = []
                try:
                    self.items_crawler.visit_item(item)
                    for buyer in self.buyers_crawler.items():
                        cleaned_item['buyers'].append(buyer)
                    items.append(cleaned_item)
                except ElementNotPresent:
                    pass
        except Exception(e):
            traceback.print_exc()

        items_with_details = self.get_details(items)
        self.storage.save_items(items_with_details)

        self.downloader.quit()

    def get_details(self, items):
        for item in items:
            for buyer in item['buyers']:
                self.downloader.visit(buyer['details_url'])
                parser = BuyerDetailsParser(self.downloader.get_html())
                parser.parse()
                buyer['details'] = parser.items
        return items





if __name__ == '__main__':
    spider = BECSpider()
    spider.crawl()
