from splinter import Browser
from crawler import NegotiationItensCrawler
from crawler import BuyersCrawler
from downloader import Downloader
from storage import Storage

class BECSpider():

    root_url ='https://www.bec.sp.gov.br/becsp/aspx/DetalheOCItens.aspx' \
            '?chave=&detalhe=1'

    def crawl(self):
        self.downloader = Downloader()

        self.items_crawler = NegotiationItensCrawler(
                self.downloader, self.root_url)
        self.buyers_crawler = BuyersCrawler(self.downloader)
        self.storage = Storage()
        
        for item in self.items_crawler.items():
            self.items_crawler.visit_item(item)
            cleaned_item = self.items_crawler.clean_item(item)
            cleaned_item['buyers'] = []
            for buyer in self.buyers_crawler.items():
                print(buyer)
                cleaned_item['buyers'].append(buyer)
            print(); print()
            self.storage.save_item(cleaned_item)


        self.downloader.quit()


if __name__ == '__main__':
    spider = BECSpider()
    spider.crawl()
