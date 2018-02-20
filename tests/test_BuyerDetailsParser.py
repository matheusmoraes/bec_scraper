import unittest
from parser import BuyerDetailsParser
from settings import PROJECT_ROOT

class TestBuyerDetailsParser(unittest.TestCase):
    def setUp(self):
        file = open(PROJECT_ROOT + '/tests/resources/buyer-details.html', 'r')
        self.html_page = file.read()
        file.close()
        self.parser = BuyerDetailsParser(self.html_page)
        self.parser.parse()

    def test_columns_count(self):
        count = len(self.parser.columns)
        self.assertEqual(count, 12)

    def test_items_count(self):
        count = len(self.parser.items)
        self.assertEqual(count, 7)

    def test_columns_names(self):
        columns = self.parser.columns
        self.assertEqual(columns[2], 'ITEM')
        self.assertEqual(columns[3], 'CÓDIGO')
        self.assertEqual(columns[4], 'DESCRIÇÃO')
        self.assertEqual(columns[5], 'QTDE')
        self.assertEqual(columns[6], 'UNIDADE DE FORNECIMENTO')
        self.assertEqual(columns[7], 'MELHOR OFERTA')
        self.assertEqual(columns[8], 'ORIGEM')
        self.assertEqual(columns[9], 'APELIDO LICITANTE')
        self.assertEqual(columns[10], 'HABILITAÇÃO LICITANTE')
        self.assertEqual(columns[11], 'LICITANTE')

    def test_first_item(self):
        item = self.parser.items[0]
        self.assertEqual(item['ITEM'], '1')
        self.assertEqual(item['CÓDIGO'], '1000217')
        self.assertEqual(item['DESCRIÇÃO'], 'ADAPTADOR INTERM., PVC, ' \
                'C/CONECTOR, PINC, TUBO,02VIAS,20CM, ESTERIL')
        self.assertEqual(item['QTDE'], '8.895')
        self.assertEqual(item['UNIDADE DE FORNECIMENTO'], 'UNIDADE')
        self.assertEqual(item['MELHOR OFERTA'], '12.453,0000')
        self.assertEqual(item['ORIGEM'], 'LANCES')
        self.assertEqual(item['APELIDO LICITANTE'], 'FOR0802')
        self.assertEqual(item['HABILITAÇÃO LICITANTE'], 'HABILITADO')
        self.assertEqual(item['LICITANTE'], 'MP COMÉRCIO DE MATERIAIS ' \
                'HOSPITALARES LTDA.')
