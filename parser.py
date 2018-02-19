from bs4 import BeautifulSoup

class BaseParser():
    def __init__(self, html_page):
        if html_page:
            self.html_page = html_page
            self.soup = BeautifulSoup(self.html_page, 'html.parser')

    @property
    def html_page(self):
        return self._html_page

    @html_page.setter
    def html_page(self, value):
        self._html_page = value
        self.soup = BeautifulSoup(self.html_page, 'html.parser')

    def parse(self):
        raise Exception('Not implemented method')


class BuyerDetailsParser(BaseParser):
    

    def parse(self):
        self.items = []
        self.columns = []

        self.table = self.soup.find(id='ctl00_conteudo_dg')
        rows = self.table.find_all('tr')
        header = rows.pop(0)

        for column in header.find_all('td'):
            self.columns.append(column.get_text().upper())

        for item in rows:
            _item = {}
            for i, column in enumerate(item.find_all('td')):
                _item[self.columns[i]] = column.get_text().upper()
            self.items.append(_item)





