import unittest
from polynomial import Polynomial


class TestPolynomialArithmetic(unittest.TestCase):

    def test_arithmetic_add_two_polynomials_1(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial1 + polynomial2
        self.assertEqual(polynomial3.coeffs, [4, 4, 4])

    def test_arithmetic_add_two_polynomials_2(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([0, 0, 3, 2, 1])
        polynomial3 = polynomial1 + polynomial2
        self.assertEqual(polynomial3.coeffs, [4, 4, 4])

    def test_arithmetic_add_two_polynomials_3(self):
        polynomial1 = Polynomial([0, 0, 0, 1, 2, 3])
        polynomial2 = Polynomial([0, 0, 3, 2, 1])
        polynomial3 = polynomial1 + polynomial2
        self.assertEqual(polynomial3.coeffs, [4, 4, 4])

    def test_arithmetic_add_two_polynomials_4(self):
        polynomial1 = Polynomial([2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial1 + polynomial2
        self.assertEqual(polynomial3.coeffs, [3, 4, 4])

    def test_arithmetic_add_two_polynomials_5(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([2, 1])
        polynomial3 = polynomial1 + polynomial2
        self.assertEqual(polynomial3.coeffs, [1, 4, 4])

    def test_arithmetic_sub_two_polynomials_1(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial1 - polynomial2
        self.assertEqual(polynomial3.coeffs, [-2, 0, 2])

    def test_arithmetic_sub_two_polynomials_2(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([0, 0, 3, 2, 1])
        polynomial3 = polynomial1 - polynomial2
        self.assertEqual(polynomial3.coeffs, [-2, 0, 2])

    def test_arithmetic_sub_two_polynomials_3(self):
        polynomial1 = Polynomial([0, 0, 0, 1, 2, 3])
        polynomial2 = Polynomial([0, 0, 3, 2, 1])
        polynomial3 = polynomial1 - polynomial2
        self.assertEqual(polynomial3.coeffs, [-2, 0, 2])

    def test_arithmetic_sub_two_polynomials_4(self):
        polynomial1 = Polynomial([2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial1 - polynomial2
        self.assertEqual(polynomial3.coeffs, [-3, 0, 2])

    def test_arithmetic_sub_two_polynomials_5(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([2, 1])
        polynomial3 = polynomial1 - polynomial2
        self.assertEqual(polynomial3.coeffs, [1, 0, 2])

    def test_arithmetic_mul_two_polynomials_1(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial1 * polynomial2
        self.assertEqual(polynomial3.coeffs, [3, 8, 14, 8, 3])

    def test_arithmetic_mul_two_polynomials_2(self):
        polynomial1 = Polynomial([0])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial1 * polynomial2
        self.assertEqual(polynomial3.coeffs, [0])

    def test_arithmetic_mul_two_polynomials_3(self):
        polynomial1 = Polynomial([3, 2, 1])
        polynomial2 = Polynomial([0])
        polynomial3 = polynomial1 * polynomial2
        self.assertEqual(polynomial3.coeffs, [0])

    def test_arithmetic_mul_two_polynomials_4(self):
        polynomial1 = Polynomial([1])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial1 * polynomial2
        self.assertEqual(polynomial3.coeffs, [3, 2, 1])

    def test_arithmetic_mul_two_polynomials_5(self):
        polynomial1 = Polynomial([1, -2, 0, -4, 5])
        polynomial2 = Polynomial([3, 0, 1])
        polynomial3 = polynomial1 * polynomial2
        self.assertEqual(polynomial3.coeffs, [3, -6, 1, -14, 15, -4, 5])

    def test_arithmetic_add_polynomial_and_other_obj_1(self):
        with self.assertRaises(TypeError):
            Polynomial([1, 2, 3]) + [5]

    def test_arithmetic_add_polynomial_and_other_obj_2(self):
        with self.assertRaises(TypeError):
            Polynomial([1, 2, 3]) + {3}

    def test_arithmetic_add_polynomial_and_other_obj_3(self):
        with self.assertRaises(TypeError):
            Polynomial([1, 2, 3]) + ("abc", "def")

    def test_arithmetic_add_two_polynomials_reverse(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial2 + polynomial1
        self.assertEqual(polynomial3.coeffs, [4, 4, 4])

    def test_arithmetic_sub_two_polynomials_reverse(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial2 - polynomial1
        self.assertEqual(polynomial3.coeffs, [2, 0, -2])

    def test_arithmetic_mul_two_polynomials_reverse(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial2 * polynomial1
        self.assertEqual(polynomial3.coeffs, [3, 8, 14, 8, 3])

    def test_arithmetic_cmp_two_polynomials_equals_1(self):
        polynomial1 = Polynomial([1, 1, 1])
        polynomial2 = Polynomial([1, 1, 1])
        self.assertEqual(polynomial1, polynomial2)

    def test_arithmetic_cmp_two_polynomials_equals_2(self):
        polynomial1 = Polynomial([1, 1, 1])
        polynomial2 = Polynomial([0, 0, 1, 1, 1])
        self.assertEqual(polynomial1, polynomial2)

    def test_arithmetic_cmp_two_polynomials_equals_3(self):
        polynomial1 = Polynomial(0)
        polynomial2 = Polynomial([0, 0, 0])
        self.assertEqual(polynomial1, polynomial2)

    def test_arithmetic_cmp_two_polynomials_equals_4(self):
        polynomial1 = Polynomial([0])
        polynomial2 = Polynomial(0)
        self.assertEqual(polynomial1, polynomial2)

    def test_arithmetic_cmp_two_polynomials_not_equals(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2])
        self.assertNotEqual(polynomial1, polynomial2)

    def test_arithmetic_add_polynomial_and_const(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = polynomial1 + 5
        self.assertEqual(polynomial2.coeffs, [1, 2, 8])

    def test_arithmetic_sub_polynomial_and_const(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = polynomial1 - 5
        self.assertEqual(polynomial2.coeffs, [1, 2, -2])

    def test_arithmetic_mul_polynomial_and_const(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = polynomial1 * 5
        self.assertEqual(polynomial2.coeffs, [5, 10, 15])

    def test_arithmetic_add_polynomial_and_const_reverse(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = 5 + polynomial1
        self.assertEqual(polynomial2.coeffs, [1, 2, 8])

    def test_arithmetic_sub_polynomial_and_const_reverse(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = 5 - polynomial1
        self.assertEqual(polynomial2.coeffs, [-1, -2, 2])

    def test_arithmetic_mul_polynomial_and_const_reverse(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = 5 * polynomial1
        self.assertEqual(polynomial2.coeffs, [5, 10, 15])

    def test_arithmetic_cmp_polynomial_and_const_equals(self):
        polynomial = Polynomial([5])
        self.assertEqual(polynomial, 5)

    def test_arithmetic_cmp_polynomial_and_const_equals_reverse(self):
        polynomial = Polynomial([5])
        self.assertEqual(5, polynomial)

    def test_arithmetic_cmp_polynomial_and_const_not_equals_1(self):
        polynomial = Polynomial([8])
        self.assertNotEqual(polynomial, 5)

    def test_arithmetic_cmp_polynomial_and_const_not_equals_2(self):
        polynomial = Polynomial([5, 1])
        self.assertNotEqual(polynomial, 5)


if __name__ == '__main__':
    unittest.main()
