class Polynomial:

    def __init__(self, obj):
        """
        Implements a polynomial object and common methods like as add, sub, mul, cmp and others.

        Wrong arguments raise a TypeError exception
        Takes integers, list of integers (!= []), tuple of integers (!= ()) as param polynomial.
        """
        if isinstance(obj, int):
            self.coeffs = [obj]
            return

        if obj and isinstance(obj, list) and isinstance(obj[0], int):
            self.coeffs = obj.copy()
            self.__trim_zeroes()
            return

        if obj and isinstance(obj, tuple):
            valid = True
            self.coeffs = list()
            for coeff in obj:
                if not isinstance(coeff, int):
                    valid = False
                    break
                self.coeffs.append(coeff)
            if valid:
                self.__trim_zeroes()
                return

        if isinstance(obj, Polynomial):
            self.coeffs = obj.coeffs.copy()
            return

        raise TypeError(f"Polynomial: Wrong initial argument: {obj}")

    @staticmethod
    def __algorithm_add(first, second):
        """
        Returns a Polynomial result from an addition of the self and obj.

        :param first: int, Polynomial
        :param second: int, Polynomial
        :return: Polynomial
        """
        if not isinstance(first, (int, Polynomial)):
            raise TypeError(f"Polynomial: Wrong type of first argument to add: {type(first)}")

        if not isinstance(second, (int, Polynomial)):
            raise TypeError(f"Polynomial: Wrong type of second argument to add: {type(second)}")

        first_coeffs = Polynomial(first).coeffs
        second_coeffs = Polynomial(second).coeffs

        coeffs_diff = len(first_coeffs) - len(second_coeffs)

        if coeffs_diff < 0:
            first_coeffs = ([0] * abs(coeffs_diff)) + first_coeffs
        if coeffs_diff > 0:
            second_coeffs = ([0] * abs(coeffs_diff)) + second_coeffs

        for index, second_coeff in enumerate(second_coeffs):
            if second_coeff != 0:
                first_coeffs[index] += second_coeff

        return Polynomial(first_coeffs)

    @staticmethod
    def __algorithm_sub(first, second):
        """
        Returns a Polynomial result from a subtraction of the self and obj.

        :param first: int, Polynomial
        :param second: int, Polynomial
        :return: Polynomial
        """
        if not isinstance(first, (int, Polynomial)):
            raise TypeError(f"Polynomial: Wrong type of first argument to subtract: {type(first)}")

        if not isinstance(second, (int, Polynomial)):
            raise TypeError(f"Polynomial: Wrong type of second argument to subtract: {type(second)}")

        first_coeffs = Polynomial(first).coeffs
        second_coeffs = Polynomial(second).coeffs

        coeffs_diff = len(first_coeffs) - len(second_coeffs)

        if coeffs_diff < 0:
            first_coeffs = ([0] * abs(coeffs_diff)) + first_coeffs
        if coeffs_diff > 0:
            second_coeffs = ([0] * abs(coeffs_diff)) + second_coeffs

        for index, second_coeff in enumerate(second_coeffs):
            if second_coeff != 0:
                first_coeffs[index] -= second_coeff

        return Polynomial(first_coeffs)

    @staticmethod
    def __algorithm_mul(first, second):
        """
        Returns a Polynomial result from a multiplication of the self and obj.

        :param first: int, Polynomial
        :param second: int, Polynomial
        :return: Polynomial
        """
        if not isinstance(first, (int, Polynomial)):
            raise TypeError(f"Polynomial: Wrong type of first argument for multiplication: {type(first)}")

        if not isinstance(second, (int, Polynomial)):
            raise TypeError(f"Polynomial: Wrong type of second argument for multiplication: {type(second)}")

        first_coeffs = Polynomial(first).coeffs
        second_coeffs = Polynomial(second).coeffs

        result_power_extension = (len(second_coeffs) - 1)
        mul_coeffs = [0] * (result_power_extension + len(first_coeffs))

        for second_index, second_coeff in enumerate(second_coeffs):
            for first_index, first_coeff in enumerate(first_coeffs):
                mul_coeffs[first_index + second_index] += first_coeff * second_coeff

        return Polynomial(mul_coeffs)

    def add(self, obj):
        """
        Returns a Polynomial result from an addition of the self and obj.

        :param obj: int, Polynomial
        :return: Polynomial
        """
        self.__self_validate()

        self.coeffs = Polynomial.__algorithm_add(self, obj).coeffs

    def sub(self, obj):
        """
        Returns a Polynomial result from a subtraction of the self and obj.

        :param obj: int, Polynomial
        :return: Polynomial
        """
        self.__self_validate()

        self.coeffs = Polynomial.__algorithm_sub(self, obj).coeffs

    def mul(self, obj):
        """
        Returns a Polynomial result from a multiplication of the self and obj.

        :param obj: int, Polynomial
        :return: Polynomial
        """
        self.__self_validate()

        self.coeffs = Polynomial.__algorithm_mul(self, obj).coeffs

    def __add__(self, obj):
        """
        Returns a Polynomial result from a multiplication of the self and obj.

        :param obj: int, Polynomial
        :return: Polynomial
        """
        self.__self_validate()

        return Polynomial.__algorithm_add(self, obj)

    def __sub__(self, obj):
        """
        Returns a Polynomial result from a subtraction of the self and obj.

        :param obj: int, Polynomial
        :return: Polynomial
        """
        self.__self_validate()

        return Polynomial.__algorithm_sub(self, obj)

    def __mul__(self, obj):
        """
        Returns a Polynomial result from a multiplication of the self and obj.

        :param obj: int, Polynomial
        :return: Polynomial
        """
        self.__self_validate()

        return Polynomial.__algorithm_mul(self, obj)

    def __radd__(self, obj):
        """
        Returns a Polynomial result from an addition of obj and the self.

        :param obj: int, Polynomial
        :return: Polynomial
        """
        self.__self_validate()

        return Polynomial.__algorithm_add(self, obj)

    def __rsub__(self, obj):
        """
        Returns a Polynomial result from a subtraction of obj and the self.

        :param obj: int, Polynomial
        :return: Polynomial
        """
        self.__self_validate()

        return - Polynomial.__algorithm_sub(self, obj)

    def __rmul__(self, obj):
        """
        Returns a Polynomial result from a multiplication of obj and the self.

        :param obj: int, Polynomial
        :return: Polynomial
        """
        self.__self_validate()

        return Polynomial.__algorithm_mul(self, obj)

    def __neg__(self):
        """
        Returns the inverted signs of the eigenvalues.

        :return: Polynomial
        """
        self.__self_validate()

        result = Polynomial(self)

        for index in range(len(result.coeffs)):
            result.coeffs[index] = - result.coeffs[index]

        return result

    def cmp(self, obj):
        """
        Returns a boolean from a comparison of the self and obj.

        :param obj: int, Polynomial
        :return: bool
        """
        self.__self_validate()

        if isinstance(obj, int):
            return self.coeffs == [obj]

        if isinstance(obj, Polynomial):
            obj.__self_validate()

            return self.coeffs == obj.coeffs

        raise TypeError(f"Polynomial: Wrong argument type to compare: {type(obj)}")

    def __eq__(self, obj):
        """
        Returns a boolean from a comparison of the self and obj.

        :param obj: int, Polynomial
        :return: bool
        """
        return self.cmp(obj)

    def __str__(self):
        """
        Returns string format of the polynomial for stdout.

        :return: string
        """
        self.__self_validate()

        self_len = len(self.coeffs)
        last_index = self_len - 1

        if self_len == 1:
            return f"{self.coeffs[0]}"

        result = ""

        for index, coeff in enumerate(self.coeffs):
            if coeff != 0:
                sign = '-' if (coeff < 0) else '+' if (index > 0) else ''
                coeff = abs(coeff) if (abs(coeff) != 1) or (index == last_index) else ''
                power = f"x^{last_index - index}" if (index < last_index - 1) else 'x' if (index < last_index) else ''

                result += f"{sign}{coeff}{power}"

        return result

    def __repr__(self):
        """
        Returns internal representation of the self.

        :return: string
        """
        self.__self_validate()

        return f"Polynomial({self.coeffs})"

    def __copy__(self):
        """
        Returns a real copy of self.

        :return: Polynomial
        """
        self.__self_validate()

        return Polynomial(self)

    def __getitem__(self, index: int):
        """
        Returns the coefficient for a polynomial in powers.

        The return value is a tuple of 2 integers:
        the first element is the coefficient, the second is the degree corresponding to the coefficient.

        :param index: int
        :return: tuple(int, int)
        """
        self.__self_validate()

        last_index = len(self.coeffs) - 1

        if not 0 <= index < last_index:
            raise IndexError(f"Out of range for this {self.__repr__()} with length {len(self.coeffs)}: {index}")

        return self.coeffs[last_index - index], index

    def __self_validate(self):
        """
        Checking own coefficients to find list, empty list for own coefficients.

        Throws an AttributeError exception if the coefficients are: not a list, not a list of ints, an empty list.

        :return: None
        """

        if not self.coeffs:
            raise AttributeError(f"Polynomial: Self coeffs is not valid: list of coeffs is empty")
        if not isinstance(self.coeffs, list) or not isinstance(self.coeffs[0], int):
            raise AttributeError(f"Polynomial: Self coeffs is not valid: {type(self.coeffs)})")

    def __trim_zeroes(self):
        """
        Removes non-significant zeros from the self.

        :return: None
        """
        self.__self_validate()

        index = 0
        last_index = len(self.coeffs) - 1

        while (index < last_index) and (self.coeffs[index] == 0):
            index += 1

        self.coeffs = self.coeffs[index:]
