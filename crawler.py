from time import sleep

class UninplementedMethod(Exception):
    pass

class Crawler:
    def __init__(self, downloader):
        self._downloader = downloader

    def items(self):
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

        return cleaned_item

                
class BuyersCrawler(Crawler):
    def items(self):
        table_xpath = '//table[@id="ctl00_ContentPlaceHolder1_gvOCs"]'
        table = self._downloader.find_by_xpath(table_xpath).first
        rows = table.find_by_tag('tr')
        header = rows.pop(0)

        for buyer_row in rows:
            tds = buyer_row.find_by_tag('td')
            link = buyer_row.find_by_tag('a').first

            buyer_info = {}
            buyer_info['offer_id'] = link.text
            buyer_info['details_url'] = link['href']
            buyer_info['unit_name'] = tds[1].text

            yield buyer_info



