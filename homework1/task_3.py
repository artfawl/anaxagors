class currency:
    __slots__ = ["price", "_value", "_typ"]
    price = {'gbp': 1, 'rub': 94, 'usd': 1.3, 'eur': 1.15, 'cny': 9}

    def __init__(self, value, typ='gbp'):
        if type(value) != int and type(value) != float:
            raise ValueError
        self._value = value / self.price[typ]
        self._typ = typ

    def settyp(self, typ: str):
        if typ not in self.price:
            raise ValueError
        self._value = self._value * self.price[self._typ] / self.price[typ]

    def setvalue(self, value):
        if type(value) != int and type(value) != float:
            raise ValueError
        self._value = value / self.price[self._typ]

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            other = currency(other, self._typ)
        res = currency(0, self._typ)
        res._value = self._value + other._value
        return res

    def __radd__(self, other):
        res = currency(other, self._typ)
        res._value += self._value
        return res

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            other = currency(other, self._typ)
        res = currency(0, self._typ)
        res._value = self._value - other._value
        return res

    def __rsub__(self, other):
        res = currency(other, self._typ)
        res._value -= self._value
        return res

    def __str__(self):
        return str(round(self._value * self.price[self._typ], 2)) + " " + self._typ

    def __repr__(self):
        return "currency(" + str(self._value * self.price[self._typ]) + "," + "\"" + self._typ + "\"" + ")"
