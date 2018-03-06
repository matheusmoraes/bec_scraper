from parser import BuyerDetailsParser
from time import sleep
from log import log

class UninplementedMethod(Exception):
    pass

class Crawler:
    '''
    Base class for Crawlers. 
    Each crawler represents a page section to interact with e.g a table.
    '''
    def __init__(self, downloader):
        self._downloader = downloader

    '''
    Abs method that returns a generator containing the final product 
    of a crawler e.g a table row.
    '''
    def items(self):
        if False:
            yield {}
        raise UninplementedMethod


class NegotiationItensCrawler(Crawler):

    _visited_cods = []

    def __init__(self, downloader, root_url):
        super(NegotiationItensCrawler, self).__init__(downloader)
        self.root_url = root_url
        self.buyers_crawler = BuyersCrawler(downloader)

    def items(self):
        while True:
            item = self.next_item()
            if not item:
                break
            log.info('Found item: %s' % self.clean_item(item))
            yield item

    def next_item(self):
        '''
        Find items list. Returns first non-visited item if exists.
        '''
        self._downloader.visit(self.root_url)
        table = self._get_table()
        rows = table.find_by_tag('tr')
        header = rows.pop(0)
        return self._find_non_visited_item(rows)


    def _get_table(self):
        table_xpath = '//table[@id="ctl00_ContentPlaceHolder1_gvItens"]'
        table = self._downloader.find_by_xpath(table_xpath).first
        return table

    def _find_non_visited_item(self, rows):
        for item in rows:
            cod = item.find_by_tag('a').first.text
            if not cod in self._visited_cods:
                return item


    def visit_item(self, item):
        cleaned = self.clean_item(item)
        link = item.find_by_tag('a').first
        self._downloader.click_element(link)
        sleep(2)
        self._visited_cods.append(cleaned['cod'])

    def clean_item(self, item):
        cleaned_item = {}

        link = item.find_by_tag('a').first.text
        name = item.find_by_tag('td')[1].text

        cleaned_item['cod'] = link
        cleaned_item['name'] = name
        cleaned_item['buyers'] = []

        return cleaned_item

                
class BuyersCrawler(Crawler):
    def items(self):
        table_xpath = '//table[@id="ctl00_ContentPlaceHolder1_gvOCs"]'
        table = self._downloader.find_by_xpath(table_xpath).first
        rows = table.find_by_tag('tr')
        header = rows.pop(0)
        for buyer_info in self._find_buyers(rows):
            log.info('Found buyer: %s' % buyer_info)
            yield buyer_info

    def _find_buyers(self, rows):
        infos = []
        for buyer_row in rows:
            tds = buyer_row.find_by_tag('td')
            link = buyer_row.find_by_tag('a').first

            buyer_info = {}
            buyer_info['offer_id'] = link.text
            buyer_info['details_url'] = link['href']
            buyer_info['unit_name'] = tds[1].text
            buyer_info['details'] = []

            infos.append(buyer_info)
        return infos


class BuyerDetailsCrawler(Crawler):

    def visit_item(self, url):
        self._downloader.visit(url)

    def items(self):
        parser = BuyerDetailsParser(self._downloader.get_html())
        parser.parse()
        for parsed_item in parser.items:
            log.info('Found item details: %s' % parsed_item)
            yield parsed_item






