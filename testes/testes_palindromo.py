import unittest
from strings.testa_palindromo import eh_palindromo

class TestePalindromo(unittest.TestCase):
    def testa_plaindromo_simples(self):
        self.assertEqual(eh_palindromo("mussum"), True)
        self.assertEqual(eh_palindromo("ari"), False)
        self.assertEqual(eh_palindromo("afasfae"), False)
    def testa_palindromo_composto(self):
        self.assertEqual(eh_palindromo("subi no onibus"), True)
        self.assertEqual(eh_palindromo("subi  no onibus"), True) #com espaços irregulares
        self.assertEqual(eh_palindromo("Subi  no onibus"), True) #com letra mauscua

if __name__ == '__main__':
    unittest.main()
