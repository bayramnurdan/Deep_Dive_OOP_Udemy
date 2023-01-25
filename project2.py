import operator


class Mod:
    """A  Mod class that is created as exercise to learn special methods in python """
    def __init__(self, value, modulus):
        if not isinstance(value, int) or not isinstance(modulus, int):
            raise ValueError("Value and modulus must be integer type!")
        if modulus <= 0:
            raise ValueError("Modulus must be greater then zero!")

        self._value = value % modulus  # store value as residue
        self._modulus = modulus

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property  # read only
    def modulus(self):
        return self._modulus

    def _get_value(self, other):
        """If an integer passed it returns residue from mod operation, if Mod object passed
        it returns object value"""
        if isinstance(other, int):
            return other % self.modulus
        if isinstance(other, Mod):
            return other.value
        raise TypeError("Incompatible types")

    def __eq__(self, other):
        other_value = self._get_value(other)  # other value is already a residue now and if type is incompatible it
        # will raise  Type error
        return self.value == other_value

    def __hash__(self):  # When eq method implemented hash function must be implemented as well to objects be hashable.
        return hash(self.value, self.modulus)

    def __repr__(self):
        return f"Mod({self.value}, {self.modulus})"

    def __int__(self):
        return self.value

    def __neg__(self):
        return Mod(-self.value, self.modulus)

    def _perform_operation(self, other, op, *, in_place=False):
        """ Make happen the required operation on values and returns new object or self object based on
        method is in place or not """
        other_value = self._get_value(other)
        new_value = op(self.value, other_value)

        if in_place:
            self.value = new_value % self.modulus
            return self
        else:
            return Mod(new_value, self.modulus)

    def __add__(self, other):
        return self._perform_operation(other, operator.add)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):  # in place operation returns same object
        return self._perform_operation(other, operator.add, in_place=True)

    def __sub__(self, other):
        return self._perform_operation(other, operator.sub)

    def __rsub__(self, other):
        if isinstance(other, int):
            new_value = -(self.value) + other
            return Mod(new_value, self.modulus)
        return NotImplemented

    def __isub__(self, other):  # in place returns same object
        return self._perform_operation(other, operator.sub, in_place=True)

    def __mul__(self, other):
        return self._perform_operation(other, operator.mul)

    def __imul__(self, other):  # in place return same object
        return self._perform_operation(other, operator.mul, in_place=True)

    def __pow__(self, other):
        return self._perform_operation(other, operator.pow)

    def __ipow__(self, other):
        return self._perform_operation(other, operator.pow, in_place=True)

    def __rmul__(self, other):
        return self * other

    def __lt__(self, other):
        other_value = self._get_value(other)
        return self.value < other_value

    def __le__(self, other):
        return self == other or self < other


