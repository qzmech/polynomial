# polynomial
Simple polynomial class with basic operations

## Features
Polynomial in one variable with integer coefficients in the same order as in the classical notation.
    
For example, `Polynomial([1, -2, 3])` means x^2 - 2x + 3

Supported operations:

* addition, addition with a constant (both sides)

* subtraction, subtraction with a constant (both sides)

* multiplication, multiplication by a constant (both sides)

* comparison (`==`), constant comparison (both sides)

* converting to string `str(p)` like `"x^2-2x+3"`

* print the internal representation of the object `repr(p)` in the style of `"Polynomial([1, 2, -4])"`

* copying in `Polynomial(p)` style, where `p` is an object of class `Polynomial`

* the list of coefficients (list) can be obtained/modified as `p.coeffs`

## How to use in projects

1) import `polynomial` module
2) create an instance of the class (eg. `Polynomial(5)`, `Polynomial([1, 2])`, `Polynomial((1, 2, 3))`, `Polynomial(p)`), list and tuple contain only integers, `p` is an instance of the Polynomial
3) use the arithmetic methods of the polynomial class

## How to run unit-tests

Run next Python scripts depending on OS.

Linux:
    
    python3 <path>/polynomial/test_polynomial_init.py
    python3 <path>/polynomial/test_polynomial_arithmetic.py
    python3 <path>/polynomial/test_polynomial_operations.py

Windows:
    
    python.exe <path>\polynomial\test_polynomial_init.py
    python.exe <path>\polynomial\test_polynomial_arithmetic.py
    python.exe <path>\polynomial\test_polynomial_operations.py
