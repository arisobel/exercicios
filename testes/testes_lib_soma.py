from unittest.case import TestCase
from lib_soma import soma


class LibsomaTestes(TestCase):
    def teste_soma(self):
        self.assertEqual(3, soma.soma(1, 2))
        self.assertEqual(5, soma.soma(3, 2))
