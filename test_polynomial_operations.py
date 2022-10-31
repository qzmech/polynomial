import unittest
from polynomial import Polynomial


class TestPolynomialOperations(unittest.TestCase):

    def test_operations_str_1(self):
        polynomial = Polynomial([-1])
        self.assertEqual(f"{polynomial}", "-1")

    def test_operations_str_2(self):
        polynomial = Polynomial([1])
        self.assertEqual(f"{polynomial}", "1")

    def test_operations_str_3(self):
        polynomial = Polynomial([0])
        self.assertEqual(f"{polynomial}", "0")

    def test_operations_str_4(self):
        polynomial = Polynomial([1, -2, 3, -4, 5])
        self.assertEqual(f"{polynomial}", "x^4-2x^3+3x^2-4x+5")

    def test_operations_str_5(self):
        polynomial = Polynomial([-1, -2, -1, -4, 0, 6, -8, -1])
        self.assertEqual(f"{polynomial}", "-x^7-2x^6-x^5-4x^4+6x^2-8x-1")

    def test_operations_str_6(self):
        polynomial = Polynomial([0, 0, 0])
        self.assertEqual(f"{polynomial}", "0")

    def test_operations_repr_1(self):
        polynomial = Polynomial([-1, -2, 1, -4, 0, 6, -8, -1])
        self.assertEqual(f"{polynomial.__repr__()}", "Polynomial([-1, -2, 1, -4, 0, 6, -8, -1])")

    def test_operations_repr_2(self):
        polynomial = Polynomial([0])
        self.assertEqual(f"{polynomial.__repr__()}", "Polynomial([0])")

    def test_operations_repr_3(self):
        polynomial = Polynomial([0, 0, 0])
        self.assertEqual(f"{polynomial.__repr__()}", "Polynomial([0])")

    def test_operations_true_copy_int(self):
        polynomial1 = Polynomial(1)
        polynomial2 = Polynomial(polynomial1)
        polynomial1.coeffs.append(42)
        self.assertNotEqual(polynomial1.coeffs, polynomial2.coeffs)

    def test_operations_trueCopy_polynomial_created_via_list(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial(polynomial1)
        polynomial1.coeffs.append(42)
        self.assertNotEqual(polynomial1.coeffs, polynomial2.coeffs)

    def test_operations_trueCopy_polynomial_created_via_tuple(self):
        polynomial1 = Polynomial((1, 2, 3))
        polynomial2 = Polynomial(polynomial1)
        polynomial1.coeffs.append(42)
        self.assertNotEqual(polynomial1.coeffs, polynomial2.coeffs)

    def test_operations_operator_addition_doesnt_change_self(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial1 + polynomial2
        self.assertEqual(polynomial1.coeffs, [1, 2, 3])
        self.assertEqual(polynomial2.coeffs, [3, 2, 1])

    def test_operations_operator_subtraction_doesnt_change_self(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial1 - polynomial2
        self.assertEqual(polynomial1.coeffs, [1, 2, 3])
        self.assertEqual(polynomial2.coeffs, [3, 2, 1])

    def test_operations_operator_multiplication_doesnt_change_self(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial1 * polynomial2
        self.assertEqual(polynomial1.coeffs, [1, 2, 3])
        self.assertEqual(polynomial2.coeffs, [3, 2, 1])

    def test_operations_get_item_polynomial_1(self):
        polynomial = Polynomial([1, 2, 3])
        self.assertEqual(polynomial[0], (3, 0))

    def test_operations_get_item_polynomial_2(self):
        polynomial = Polynomial([1, 2, 3])
        self.assertEqual(polynomial[1], (2, 1))

    def test_operations_get_item_polynomial_3(self):
        with self.assertRaises(IndexError):
            Polynomial([1, 2, 3])[-1] # noqa

    def test_operations_get_item_polynomial_4(self):
        with self.assertRaises(IndexError):
            result = Polynomial([1, 2, 3])[4] # noqa

    def test_operations_self_validation_1(self):
        with self.assertRaises(AttributeError):
            polynomial = Polynomial([1, 2, 3])
            polynomial.coeffs = []
            f"{polynomial}"

    def test_operations_self_validation_2(self):
        with self.assertRaises(AttributeError):
            polynomial = Polynomial([1, 2, 3])
            polynomial.coeffs = ()
            f"{polynomial}"

    def test_operations_self_validation_3(self):
        with self.assertRaises(AttributeError):
            polynomial = Polynomial([1, 2, 3])
            polynomial.coeffs = ['1', '2', '3']
            f"{polynomial}"


if __name__ == '__main__':
    unittest.main()
