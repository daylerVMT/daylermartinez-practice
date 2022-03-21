import unittest
from src.calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        cal = Calculator()
        result= cal.add(2,2)
        self.assertEqual(5,result)

    def test_validate_age(self):
        cal = Calculator()
        result = cal.valid_age(5)
        self.assertTrue(result)

    def test_validate_invalid_age(self):
        cal = Calculator()
        result = cal.valid_age(-5)
        self.assertTrue(result)

    def test_max(self):
        cal = Calculator()
        result = cal.max(3,5,2)
        self.assertEqual(5, result)

    def test_max_firstNum(self):
        cal = Calculator()
        result = cal.max(10,2,8)
        self.assertEqual(10, result)

    def test_max_endNum(self):
        cal = Calculator()
        result = cal.max(1, 2, 8)
        self.assertEqual(8, result)

    def test_isVocal(self):
        cal = Calculator()
        result = cal.isVocal("a")
        self.assertEqual("es vocal", result)

    def test_isVocal_or_num(self):
        cal = Calculator()
        result = cal.isVocal(10)
        self.assertEqual("es numero", result)

    def test_isVocal_or_consonant(self):
        cal = Calculator()
        result = cal.isVocal("j")
        self.assertEqual("es consonante", result)

    def test_isVocal_error(self):
        cal = Calculator()
        result = cal.isVocal("d")
        self.assertEqual("es numero", result)

    def test_inversa_harcodeado(self):
        cal = Calculator()
        result = cal.inversa("AT16 Python")
        self.assertEqual("nohtyP 61TA", result)

    def test_inversa(self):
        cal = Calculator()
        result = cal.inversa("mouse")
        self.assertEqual("esuom", result)

    def test_inversa_fallo(self):
        cal = Calculator()
        result = cal.inversa("AT16 Python")
        self.assertNotEqual("AT16 Python", result)

    def test_inversa_errornumeros(self):
        cal = Calculator()
        result = cal.inversa("AT16 Skynet")
        self.assertNotEqual("tenykS 16AT", result)

    def test_palindromo(self):
        cal = Calculator()
        result = cal.palindromo("oruro")
        self.assertTrue(True, result)

    def test_palindromo_false(self):
        cal = Calculator()
        result = cal.palindromo("sucre")
        self.assertFalse(False, result)

    def test_palindromo_false(self):
        cal = Calculator()
        result = cal.palindromo("Mar")
        self.assertFalse(False, result)

    def test_palindromo_false(self):
        cal = Calculator()
        result = cal.palindromo("arenera")
        self.assertTrue(True, result)

    def test_array(self):
        cal = Calculator()
        list1 = [5, 6, 8, 10, 6, 6, 4, 7, 9]
        result = cal.array(list1)
        self.assertIsInstance([10, 4, 7], result)

    def test_array_fallo(self):
        cal = Calculator()
        list1 = [5, 6, 8, 10, 6, 6, 4, 7, 9]
        result = cal.array(list1)
        self.assertIsInstance([0, 0, 0], result)

    def test_array_todo5(self):
        cal = Calculator()
        result = cal.array((5, 5, 5, 5, 5, 5, 5, 5, 5))
        self.assertEqual((5, 5, 5), result)

    def test_array_todo5(self):
        cal = Calculator()
        result = cal.array((5, 5, 5, 5, 5, 5, 5, 5, 5))
        self.assertNotEqual((5, 5, 5), result)

    def test_paises(self):
        cal = Calculator()
        result = cal.paises(("Bolivia", "Argentina",  "Peru", "Chile"))
        self.assertEqual("Argentina", result)

    def test_paises(self):
        cal = Calculator()
        result = cal.paises(("Bolivia", "Argentina",  "Peru", "Chile"))
        self.assertNotEqual("Argentina", result)

    def test_binario(self):
        cal = Calculator()
        result = cal.binario(9)
        self.assertEqual(1001, result)

    def test_binario_rango_mayor10(self):
        cal = Calculator()
        result = cal.binario(20)
        self.assertEqual(10100, result)

    def test_binario_rango_mayor10(self):
        cal = Calculator()
        result = cal.binario(20)
        self.assertEqual("rango no aceptado", result)

    def test_cantidadChar(self):
        cal = Calculator()
        result = cal.cantidadChar("todos los caracteres deeste string")
        self.assertEqual(34, result)

    def test_cantidadChar_false(self):
        cal = Calculator()
        result = cal.cantidadChar("todos los caracteres deeste string")
        self.assertNotEqual(34, result)

    def test_cantidadChar_sin_espacios(self):
        cal = Calculator()
        result = cal.cantidadChar("todos los caracteres deeste string")
        self.assertEqual(30, result)

    def test_cantidadChar_cortos(self):
        cal = Calculator()
        result = cal.cantidadChar(" ")
        self.assertEqual(1, result)

    def test_cantidadChar_ninguno(self):
        cal = Calculator()
        result = cal.cantidadChar("")
        self.assertEqual(0, result)






