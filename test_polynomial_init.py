import unittest
from polynomial import Polynomial


class TestPolynomialInit(unittest.TestCase):

    def test_init_using_constInt(self):
        polynomial = Polynomial(1)
        self.assertEqual(polynomial.coeffs, [1])

    def test_init_using_list_ints(self):
        polynomial = Polynomial([1, 2, 3])
        self.assertEqual(polynomial.coeffs, [1, 2, 3])

    def test_init_using_tuple_ints(self):
        polynomial = Polynomial((1, 2, 3))
        self.assertEqual(polynomial.coeffs, [1, 2, 3])

    def test_init_using_polynomial(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial(polynomial1)
        self.assertEqual(polynomial2.coeffs, [1, 2, 3])

    def test_init_float(self):
        with self.assertRaises(TypeError):
            Polynomial(12.1)

    def test_init_string(self):
        with self.assertRaises(TypeError):
            Polynomial("abc")

    def test_init_char(self):
        with self.assertRaises(TypeError):
            Polynomial('a')

    def test_init_dict(self):
        with self.assertRaises(TypeError):
            Polynomial({})

    def test_init_empty_list(self):
        with self.assertRaises(TypeError):
            Polynomial([])

    def test_init_empty_tuple(self):
        with self.assertRaises(TypeError):
            Polynomial(())

    def test_init_using_list_without_ints(self):
        with self.assertRaises(TypeError):
            Polynomial(['1', {1}, [1, 2]])

    def test_init_using_tuple_without_ints(self):
        with self.assertRaises(TypeError):
            Polynomial(('1', {1}, [1, 2]))

    def test_init_using_list_not_only_ints(self):
        with self.assertRaises(TypeError):
            Polynomial(['1', 1, {1}, [1, 2]])

    def test_init_using_tuple_not_only_ints(self):
        with self.assertRaises(TypeError):
            Polynomial(('1', 1, {1}, [1, 2]))


if __name__ == '__main__':
    unittest.main()
