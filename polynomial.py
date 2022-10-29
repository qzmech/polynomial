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

        if isinstance(obj, list) and (obj != []) and isinstance(obj[0], int):
            self.coeffs = obj.copy()
            self.__trim()
            return

        if isinstance(obj, tuple) and (obj != ()):
            is_polynomial = True
            self.coeffs = list()
            for coeff in obj:
                if not isinstance(coeff, int):
                    is_polynomial = False
                    break
                self.coeffs.append(coeff)
            self.__trim()
            if is_polynomial:
                return

        if isinstance(obj, Polynomial):
            self.coeffs = obj.coeffs.copy()
            return

        raise TypeError(f"Polynomial: Wrong initial argument: {obj}")

    def add(self, obj):
        """
        Returns summa of self and other (int or Polynomial instance).

        :param obj: int, Polynomial
        :return: Polynomial
        """
        result = self.coeffs.copy()

        if isinstance(obj, int):
            result[-1] += obj
            return Polynomial(result)

        if isinstance(obj, Polynomial):
            coeffs_diff = len(result) - len(obj.coeffs)

            objs_coeffs = obj.coeffs.copy()
            if coeffs_diff > 0:
                objs_coeffs = ([0] * abs(coeffs_diff)) + objs_coeffs.copy()
            if coeffs_diff < 0:
                result = ([0] * abs(coeffs_diff)) + result.copy()

            for index in range(len(result)):
                result[index] += objs_coeffs[index]
            return Polynomial(result)

        raise TypeError(f"Polynomial: Wrong second addition argument type: {type(obj)}")

    def sub(self, obj):
        """
        Returns subtraction of self and other (int or Polynomial instance).

        :param obj: int, Polynomial
        :return: Polynomial
        """
        result = self.coeffs.copy()

        if isinstance(obj, int):
            result[-1] -= obj
            return Polynomial(result)

        if isinstance(obj, Polynomial):
            coeffs_diff = len(result) - len(obj.coeffs)

            objs_coeffs = obj.coeffs.copy()
            if coeffs_diff > 0:
                objs_coeffs = ([0] * abs(coeffs_diff)) + objs_coeffs.copy()
            if coeffs_diff < 0:
                result = ([0] * abs(coeffs_diff)) + result.copy()

            for index in range(len(result)):
                result[index] -= objs_coeffs[index]
            return Polynomial(result)

        raise TypeError(f"Polynomial: Wrong second subtraction argument type: {type(obj)}")

    def mul(self, obj):
        """
        Returns multiplication of self and other (int or Polynomial instance).

        :param obj: int, Polynomial
        :return: Polynomial
        """
        if isinstance(obj, int):
            result = Polynomial(self.coeffs.copy())
            for index in range(len(result.coeffs)):
                result.coeffs[index] *= obj
            result.__trim()
            return result

        if isinstance(obj, Polynomial):
            shift = (len(obj.coeffs) - 1)
            mul_coeffs = [0] * (shift + len(self.coeffs))

            for obj_index in range(len(obj.coeffs)):
                for self_index in range(len(self.coeffs)):
                    mul_coeffs[self_index + obj_index] += self.coeffs[self_index] * obj.coeffs[obj_index]
            result = Polynomial(mul_coeffs)
            return result

        raise TypeError(f"Polynomial: Wrong second multiplication argument type: {type(obj)}")

    def cmp(self, obj):
        """
        Returns bool for comparison of self and obj (int or Polynomial instance).

        :param obj: int, Polynomial
        :return: bool
        """
        if isinstance(obj, int):
            return (len(self.coeffs) == 1) and (self.coeffs[0] == obj)

        if isinstance(obj, Polynomial):
            if len(self.coeffs) != len(obj.coeffs):
                return False

            for index in range(len(self.coeffs)):
                if self.coeffs[index] != obj.coeffs[index]:
                    return False
            return True

        raise TypeError(f"Polynomial: Wrong comparison argument type: {type(obj)}")

    def __add__(self, obj):
        """
        Returns summa of self and other (int or Polynomial instance).

        :param obj: int, Polynomial
        :return: Polynomial
        """
        return self.add(obj)

    def __sub__(self, obj):
        """
        Returns subtraction of self and other (int or Polynomial instance).

        :param obj: int, Polynomial
        :return: Polynomial
        """
        return self.sub(obj)

    def __mul__(self, obj):
        """
        Returns multiplication of self and other (int or Polynomial instance).

        :param obj: int, Polynomial
        :return: Polynomial
        """
        return self.mul(obj)

    def __eq__(self, obj):
        """
        Returns bool for comparison of self and obj (int or Polynomial instance).

        :param obj: int, Polynomial
        :return: bool
        """
        return self.cmp(obj)

    def __radd__(self, obj):
        """
        Returns reverse summa of self and other (int or Polynomial instance).

        :param obj: int, Polynomial
        :return: Polynomial
        """
        return self.add(obj)

    def __rsub__(self, obj):
        """
        Returns reverse subtraction of self and other (int or Polynomial instance).

        :param obj: int, Polynomial
        :return: Polynomial
        """
        return -self.sub(obj)

    def __rmul__(self, obj):
        """
        Returns reverse multiplication of self and other (int or Polynomial instance).

        :param obj: int, Polynomial
        :return: Polynomial
        """
        return self.mul(obj)

    def __neg__(self):
        """
        Returns negative self.

        :return: bool
        """
        result = Polynomial(self.coeffs.copy())
        for index in range(len(result.coeffs)):
            result.coeffs[index] = -result.coeffs[index]

        return result

    def __str__(self):
        """
        Returns string format of self for std output.

        :return: string
        """
        self_len = len(self.coeffs)
        last_index = self_len - 1

        if self_len == 1:
            return f"{self.coeffs[0]}"

        result = ""

        for index in range(self_len):
            coeff = self.coeffs[index]
            if coeff == 0:
                continue

            sign = '-' if (coeff < 0) else '+' if (index > 0) else ''
            coeff = abs(coeff) if (abs(coeff) != 1) or (index == last_index) else ''
            power = f"^{last_index - index}" if (index < last_index - 1) else ''
            variable = 'x' if (index < last_index) else ''

            result += f"{sign}{coeff}{variable}{power}"

        return result

    def __repr__(self):
        """
        Returns internal representation of self.

        :return: string
        """
        return f"Polynomial({self.coeffs})"

    def __copy__(self):
        """
        Returns real copy of self.

        :return: Polynomial
        """
        return Polynomial(self.coeffs.copy())

    def __trim(self):
        """
        Removes non-significant zeros from the self.

        :return: None
        """
        index = 0
        last_index = len(self.coeffs) - 1
        while (index < last_index) and (self.coeffs[index] == 0):
            index += 1

        result = list()
        while index <= last_index:
            result.append(self.coeffs[index])
            index += 1

        self.coeffs = result
