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


class TableParser(BaseParser):
    def parse_table(self, table):
        self.items = []
        self.columns = []
        rows = table.find_all('tr')
        header = rows.pop(0)

        self.parse_columns(header)
        self.parse_items(rows)

    def parse_columns(self, header):
        for column in header.find_all('td'):
            self.columns.append(self.clean_column_name(column))

    def clean_column_name(self, column):
        return column.get_text().upper().replace('.', '')

    def parse_items(self, rows):
        for item in rows:
            _item = {}
            for i, column in enumerate(item.find_all('td')):
                _item[self.columns[i]] = column.get_text().upper()
            self.items.append(_item)


class BuyerDetailsParser(TableParser):
    def parse(self):
        table = self.find_table()
        self.parse_table(table)

    def find_table(self):
        return self.soup.find(id='ctl00_conteudo_dg')





