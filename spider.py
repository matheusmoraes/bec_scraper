from splinter import Browser
from crawler import NegotiationItensCrawler
from crawler import BuyersCrawler
from crawler import BuyerDetailsCrawler
from downloader import Downloader
from downloader import ElementNotPresent
from parser import BuyerDetailsParser
from storage import Storage
from log import log
import traceback
from pyvirtualdisplay import Display

class BECSpider():

    display = Display(visible=0, size=(1024, 768))
    display.start()
    
    root_url ='https://www.bec.sp.gov.br/becsp/aspx/DetalheOCItens.aspx' \
            '?chave=&detalhe=1'

    def __init__(self):
        log.info('Starting BEC Spider')
        self.downloader = Downloader()
        self.items_crawler = NegotiationItensCrawler(
                self.downloader, self.root_url)
        self.buyers_crawler = BuyersCrawler(self.downloader)
        self.details_crawler = BuyerDetailsCrawler(self.downloader)
        self.storage = Storage()
        self.items = []

    def crawl(self):
        self.crawl_items()
        self.downloader.quit()
        self.display.stop()

    def crawl_items(self):
        try:
            for item in self.items_crawler.items():
                self.crawl_buyers_for_item(item)
        except Exception as e:
            log.warning('FATAL: %s' % e)
            traceback.print_exc()

    def crawl_buyers_for_item(self, item):
        try:
            cleaned_item = self.items_crawler.clean_item(item)
            self.items_crawler.visit_item(item)

            for buyer in self.buyers_crawler.items():
                cleaned_item['buyers'].append(buyer)

                self.details_crawler.visit_item(buyer['details_url'])

                for detailed_item in self.details_crawler.items():
                    buyer['details'].append(detailed_item)
            # End of cicle
            self.storage.save_item(cleaned_item)

        except ElementNotPresent:
            pass


if __name__ == '__main__':
    spider = BECSpider()
    spider.crawl()
