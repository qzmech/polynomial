import unittest
from polynomial import Polynomial


class TestPolynomialInit(unittest.TestCase):

    def testInitUsingConstInt(self):
        polynomial = Polynomial(1)
        self.assertEqual(polynomial.coeffs, [1])

    def testInitUsingListInts(self):
        polynomial = Polynomial([1, 2, 3])
        self.assertEqual(polynomial.coeffs, [1, 2, 3])

    def testInitUsingTupleInts(self):
        polynomial = Polynomial((1, 2, 3))
        self.assertEqual(polynomial.coeffs, [1, 2, 3])

    def testInitUsingPolynomial(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial(polynomial1)
        self.assertEqual(polynomial2.coeffs, [1, 2, 3])

    def testInitNotArgs(self):
        with self.assertRaises(TypeError):
            Polynomial()

    def testInitEmptyList(self):
        with self.assertRaises(TypeError):
            Polynomial([])

    def testInitEmptyTuple(self):
        with self.assertRaises(TypeError):
            Polynomial(())

    def testInitUsingListWithoutInts(self):
        with self.assertRaises(TypeError):
            Polynomial(['1', {1}, [1, 2]])

    def testInitUsingTupleWithoutInts(self):
        with self.assertRaises(TypeError):
            Polynomial(('1', {1}, [1, 2]))

    def testInitUsingListNotOnlyInts(self):
        with self.assertRaises(TypeError):
            Polynomial(['1', 1, {1}, [1, 2]])

    def testInitUsingTupleNotOnlyInts(self):
        with self.assertRaises(TypeError):
            Polynomial(('1', 1, {1}, [1, 2]))


class TestPolynomialArithmetic(unittest.TestCase):

    def testArithmeticAddTwoPolynomial1(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial1 + polynomial2
        self.assertEqual(polynomial3.coeffs, [4, 4, 4])

    def testArithmeticAddTwoPolynomial2(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([0, 0, 3, 2, 1])
        polynomial3 = polynomial1 + polynomial2
        self.assertEqual(polynomial3.coeffs, [4, 4, 4])

    def testArithmeticAddTwoPolynomial3(self):
        polynomial1 = Polynomial([0, 0, 0, 1, 2, 3])
        polynomial2 = Polynomial([0, 0, 3, 2, 1])
        polynomial3 = polynomial1 + polynomial2
        self.assertEqual(polynomial3.coeffs, [4, 4, 4])

    def testArithmeticAddTwoPolynomial4(self):
        polynomial1 = Polynomial([2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial1 + polynomial2
        self.assertEqual(polynomial3.coeffs, [3, 4, 4])

    def testArithmeticAddTwoPolynomial5(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([2, 1])
        polynomial3 = polynomial1 + polynomial2
        self.assertEqual(polynomial3.coeffs, [1, 4, 4])

    def testArithmeticSubTwoPolynomial(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial1 - polynomial2
        self.assertEqual(polynomial3.coeffs, [-2, 0, 2])

    def testArithmeticSubTwoPolynomial2(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([0, 0, 3, 2, 1])
        polynomial3 = polynomial1 - polynomial2
        self.assertEqual(polynomial3.coeffs, [-2, 0, 2])

    def testArithmeticSubTwoPolynomial3(self):
        polynomial1 = Polynomial([0, 0, 0, 1, 2, 3])
        polynomial2 = Polynomial([0, 0, 3, 2, 1])
        polynomial3 = polynomial1 - polynomial2
        self.assertEqual(polynomial3.coeffs, [-2, 0, 2])

    def testArithmeticSubTwoPolynomial4(self):
        polynomial1 = Polynomial([2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial1 - polynomial2
        self.assertEqual(polynomial3.coeffs, [-3, 0, 2])

    def testArithmeticSubTwoPolynomial5(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([2, 1])
        polynomial3 = polynomial1 - polynomial2
        self.assertEqual(polynomial3.coeffs, [1, 0, 2])

    def testArithmeticMulTwoPolynomial(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial1 * polynomial2
        self.assertEqual(polynomial3.coeffs, [3, 8, 14, 8, 3])

    def testArithmeticAddPolynomialAndOtherObj1(self):
        with self.assertRaises(TypeError):
            Polynomial([1, 2, 3]) + [5]

    def testArithmeticAddPolynomialAndOtherObj2(self):
        with self.assertRaises(TypeError):
            Polynomial([1, 2, 3]) + {3}

    def testArithmeticAddPolynomialAndOtherObj3(self):
        with self.assertRaises(TypeError):
            Polynomial([1, 2, 3]) + ("abc", "def")

    def testArithmeticAddTwoPolynomialReverse(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial2 + polynomial1
        self.assertEqual(polynomial3.coeffs, [4, 4, 4])

    def testArithmeticSubTwoPolynomialReverse(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial2 - polynomial1
        self.assertEqual(polynomial3.coeffs, [2, 0, -2])

    def testArithmeticMulTwoPolynomialReverse(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2, 1])
        polynomial3 = polynomial2 * polynomial1
        self.assertEqual(polynomial3.coeffs, [3, 8, 14, 8, 3])

    def testArithmeticCmpTwoPolynomialsEquals1(self):
        polynomial1 = Polynomial([1, 1, 1])
        polynomial2 = Polynomial([1, 1, 1])
        self.assertEqual(polynomial1, polynomial2)

    def testArithmeticCmpTwoPolynomialsEquals2(self):
        polynomial1 = Polynomial([1, 1, 1])
        polynomial2 = Polynomial([0, 0, 1, 1, 1])
        self.assertEqual(polynomial1, polynomial2)

    def testArithmeticCmpTwoPolynomialsEquals3(self):
        polynomial1 = Polynomial(0)
        polynomial2 = Polynomial([0, 0, 0])
        self.assertEqual(polynomial1, polynomial2)

    def testArithmeticCmpTwoPolynomialsEquals4(self):
        polynomial1 = Polynomial([0])
        polynomial2 = Polynomial(0)
        self.assertEqual(polynomial1, polynomial2)

    def testArithmeticCmpTwoPolynomialsNotEquals(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial([3, 2])
        self.assertNotEqual(polynomial1, polynomial2)

    def testArithmeticAddPolynomialAndConst(self):
        polynomial = Polynomial([1, 2, 3])
        polynomial2 = polynomial + 5
        self.assertEqual(polynomial2.coeffs, [1, 2, 8])

    def testArithmeticSubPolynomialAndConst(self):
        polynomial = Polynomial([1, 2, 3])
        polynomial2 = polynomial - 5
        self.assertEqual(polynomial2.coeffs, [1, 2, -2])

    def testArithmeticMulPolynomialAndConst(self):
        polynomial = Polynomial([1, 2, 3])
        polynomial2 = polynomial * 5
        self.assertEqual(polynomial2.coeffs, [5, 10, 15])

    def testArithmeticAddPolynomialAndConstReverse(self):
        polynomial = Polynomial([1, 2, 3])
        polynomial2 = 5 + polynomial
        self.assertEqual(polynomial2.coeffs, [1, 2, 8])

    def testArithmeticSubPolynomialAndConstReverse(self):
        polynomial = Polynomial([1, 2, 3])
        polynomial2 = 5 - polynomial
        self.assertEqual(polynomial2.coeffs, [-1, -2, 2])

    def testArithmeticMulPolynomialAndConstReverse(self):
        polynomial = Polynomial([1, 2, 3])
        polynomial2 = 5 * polynomial
        self.assertEqual(polynomial2.coeffs, [5, 10, 15])

    def testArithmeticCmpPolynomialAndConstEquals(self):
        polynomial = Polynomial([5])
        self.assertEqual(polynomial == 5, True)

    def testArithmeticCmpPolynomialAndConstEqualsReverse(self):
        polynomial = Polynomial([5])
        self.assertEqual(5 == polynomial, True)

    def testArithmeticCmpPolynomialAndConstNotEquals1(self):
        polynomial = Polynomial([8])
        self.assertEqual(polynomial == 5, False)

    def testArithmeticCmpPolynomialAndConstNotEquals2(self):
        polynomial = Polynomial([5, 1])
        self.assertEqual(polynomial == 5, False)


class TestPolynomialOperations(unittest.TestCase):

    def testOperationsStr1(self):
        polynomial = Polynomial([-1])
        self.assertEqual(f"{polynomial}", "-1")

    def testOperationsStr2(self):
        polynomial = Polynomial([1])
        self.assertEqual(f"{polynomial}", "1")

    def testOperationsStr3(self):
        polynomial = Polynomial([0])
        self.assertEqual(f"{polynomial}", "0")

    def testOperationsStr4(self):
        polynomial = Polynomial([1, -2, 3, -4, 5])
        self.assertEqual(f"{polynomial}", "x^4-2x^3+3x^2-4x+5")

    def testOperationsStr5(self):
        polynomial = Polynomial([-1, -2, -1, -4, 0, 6, -8, -1])
        self.assertEqual(f"{polynomial}", "-x^7-2x^6-x^5-4x^4+6x^2-8x-1")

    def testOperationsStr6(self):
        polynomial = Polynomial([0, 0, 0])
        self.assertEqual(f"{polynomial}", "0")

    def testOperationsRepr1(self):
        polynomial = Polynomial([-1, -2, 1, -4, 0, 6, -8, -1])
        self.assertEqual(f"{polynomial.__repr__()}", "Polynomial([-1, -2, 1, -4, 0, 6, -8, -1])")

    def testOperationsRepr2(self):
        polynomial = Polynomial([0])
        self.assertEqual(f"{polynomial.__repr__()}", "Polynomial([0])")

    def testOperationsRepr3(self):
        polynomial = Polynomial([0, 0, 0])
        self.assertEqual(f"{polynomial.__repr__()}", "Polynomial([0])")

    def testOperationsTrueCopyInt(self):
        polynomial1 = Polynomial(1)
        polynomial2 = Polynomial(polynomial1)
        polynomial1.coeffs.append(42)
        self.assertNotEqual(polynomial1.coeffs, polynomial2.coeffs)

    def testOperationsTrueCopyPolynomialBasedOnList(self):
        polynomial1 = Polynomial([1, 2, 3])
        polynomial2 = Polynomial(polynomial1)
        polynomial1.coeffs.append(42)
        self.assertNotEqual(polynomial1.coeffs, polynomial2.coeffs)

    def testOperationsTrueCopyPolynomialBasedOnTuple(self):
        polynomial1 = Polynomial((1, 2, 3))
        polynomial2 = Polynomial(polynomial1)
        polynomial1.coeffs.append(42)
        self.assertNotEqual(polynomial1.coeffs, polynomial2.coeffs)


if __name__ == '__main__':
    unittest.main()
