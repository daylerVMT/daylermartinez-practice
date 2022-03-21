import unittest
from src.calculator import Calculator

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result= self.calculator.add(2, 3)
        self.assertEqual(5, result)

    def test_add_not_equals(self):
        result = self.calculator.add(2, 2)
        self.assertNotEqual(5, result)

    def test_validate_age(self):
        result = self.calculator.valid_age(5)
        self.assertTrue(result)

    def test_validate_invalid_age(self):
        result = self.calculator.valid_age(-5)
        self.assertFalse(result)

    def test_max(self):
        result = self.calculator.max(3,5,2)
        self.assertEqual(5, result)

    def test_max_firstNum(self):
        result = self.calculator.max(10,2,8)
        self.assertEqual(10, result)

    def test_max_endNum(self):
        result = self.calculator.max(1, 2, 8)
        self.assertEqual(8, result)

    def test_isVocal(self):
        result = self.calculator.isVocal("a")
        self.assertEqual("es vocal", result)

    def test_isVocal_or_num(self):
        result = self.calculator.isVocal("1")
        self.assertEqual("es numero", result)

    def test_isVocal_or_consonant(self):
        result = self.calculator.isVocal("j")
        self.assertEqual("es consonante", result)

    def test_isVocal_error(self):
        result = self.calculator.isVocal("d")
        self.assertNotEqual("es numero", result)

    def test_inversa_harcodeado(self):
        result = self.calculator.inversa("AT16 Python")
        self.assertEqual("nohtyP 61TA", result)

    def test_inversa(self):
        result = self.calculator.inversa("mouse")
        self.assertEqual("esuom", result)

    def test_inversa_fallo(self):
        result = self.calculator.inversa("AT16 Python")
        self.assertNotEqual("AT16 Python", result)

    def test_inversa_errornumeros(self):
        result = self.calculator.inversa("AT16 Skynet")
        self.assertNotEqual("tenykS 16AT", result)

    def test_palindromo(self):
        result = self.calculator.palindromo("oruro")
        self.assertTrue(True, result)

    def test_palindromo_false(self):
        result = self.calculator.palindromo("sucre")
        self.assertFalse(False, result)

    def test_palindromo_false(self):
        result = self.calculator.palindromo("Mar")
        self.assertFalse(result)

    def test_palindromo_false(self):
        result = self.calculator.palindromo("arenera")
        self.assertTrue(result)

    def test_array_simple(self):
        list1 = (2, 5, 5)
        result = self.calculator.array(list1)
        self.assertEquals([5, 2, 4], result)

    def test_array(self):
        list1 = (5, 6, 8, 10, 6, 6, 4, 7, 9)
        result = self.calculator.array(list1)
        self.assertEquals([10, 4, 6], result)

    def test_array_fail(self):
        list1 = (5, 6, 8, 10, 6, 6, 4, 7, 9)
        result = self.calculator.array(list1)
        self.assertNotEquals([0, 0, 0], result)

    def test_array_todo5(self):
        result = self.calculator.array((5, 5, 5, 5, 5, 5, 5, 5, 5))
        self.assertEqual((5, 5, 5), result)

    def test_array_todo5(self):
        result = self.calculator.array((5, 5, 5, 5, 5, 5, 5, 5, 5))
        self.assertNotEqual((5, 5, 5), result)

    def test_paises(self):
        result = self.calculator.paises(("Bolivia", "Argentina",  "Peru", "Chile"))
        self.assertEqual("Argentina", result)

    def test_paises_endStr(self):
        result = self.calculator.paises(("Bolivia",  "Peru", "Chile", "Argentina"))
        self.assertEqual("Argentina", result)

    def test_binario(self):
        result = self.calculator.binario(9)
        self.assertEqual(1001, result)

    def test_binario_rango_mayor10(self):
        result = self.calculator.binario(20)
        self.assertEqual(10100, result)

    def test_binario_rango_mayor10(self):
        result = self.calculator.binario(20)
        self.assertEqual("rango no aceptado", result)

    def test_cantidadChar(self):
        result = self.calculator.cantidadChar("todos los caracteres de este string")
        self.assertEqual(35, result)

    def test_cantidadChar_false(self):
        result = self.calculator.cantidadChar("todos los caracteres de este string")
        self.assertNotEqual(34, result)

    def test_cantidadChar_sin_espacios(self):
        result = self.calculator.cantidadChar("todos los caracteres de este string")
        self.assertNotEqual(30, result)

    def test_cantidadChar_cortos(self):
        result = self.calculator.cantidadChar(" ")
        self.assertEqual(1, result)

    def test_cantidadChar_ninguno(self):
        result = self.calculator.cantidadChar("")
        self.assertEqual(0, result)






