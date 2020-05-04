from unittest import TestCase
from unittest.mock import patch
from strings.data_extenso import *

class TesteEntrada(TestCase):
    @patch('get_input',return_value('10/10/2005'))
    def test_entrada(self, input):
        self.assertEqual(data_extenso(), "10 de outubro de 2005")


