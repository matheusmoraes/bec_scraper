from splinter import Browser
from crawler import NegotiationItensCrawler
from crawler import BuyersCrawler
from downloader import Downloader

class BECSpider():

    root_url ='https://www.bec.sp.gov.br/becsp/aspx/DetalheOCItens.aspx' \
            '?chave=&detalhe=1'

    def crawl(self):
        self.downloader = Downloader()

        self.items_crawler = NegotiationItensCrawler(
                self.downloader, self.root_url)
        self.buyers_crawler = BuyersCrawler(self.downloader)
        
        for item in self.items_crawler.items():
            print(self.items_crawler.clean_item(item))
            self.items_crawler.visit_item(item)
            for buyer in self.buyers_crawler.items():
                print(buyer)

            print(); print()


        self.downloader.quit()


if __name__ == '__main__':
    spider = BECSpider()
    spider.crawl()
