class Expr:
    def __init__(self, val):
        if isinstance(val, str):
            self.value = val
            self.prod = [(1, Expr(1))]
        else:
            raise Exception("Expr.__init(v) should be called only on strings")

    def __new__(cls, *args):
        v = args[0]
        if isinstance(v, str):
            return super().__new__(Expr)
        else:
            return v

    def __str__(self):
        def f(x):
            c, e = x
            if c == 0:
                return str(e)
            elif c == 1:
                return self.value + "*" + str(e)
            else:
                return self.value + "**" + str(c) + "*" + str(e)

        if len(self.prod) > 1:
            return "(" + "+".join(map(f, self.prod)) + ")"
        else:
            return "+".join(map(f, self.prod))

    def __eq__(self, other):
        if isinstance(other, Expr):
            if (not (self.value == other.value)) or not (len(self.prod) == len(other.prod)):
                return False
            else:
                b = True
                i = 0
                while b and i < len(self.prod):
                    c1, e1 = self.prod[i]
                    c2, e2 = other.prod[i]
                    b = b and c1 == c2 and e1 == e2
                    i += 1
                return b
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __call__(self, *args):
        d = args[0]
        v = d[self.value]
        if v == 0:
            c, e = self.prod[0]
            if c == 0:
                if isinstance(e, Expr):
                    return e(d)
                else:
                    return e
            else:
                return 0
        else:
            accu = 0
            for i in range(0, len(self.prod)):
                c, e = self.prod[i]
                if isinstance(e, Expr):
                    accu += (v ** c) * e(d)
                else:
                    accu += (v ** c) * e
            return accu

    def __add__(self, other):
        res = super().__new__(Expr)
        if isinstance(other, Expr):
            if self.value == other.value:
                res.value = self.value
                res.prod = []
                i = 0
                j = 0

                while i < len(self.prod) and j < len(other.prod):
                    c1, e1 = self.prod[i]
                    c2, e2 = other.prod[j]
                    if c1 == c2:
                        res.prod += [(c1, e1 + e2)]
                        i += 1
                        j += 1
                    elif c1 < c2:
                        res.prod += [(c1, e1)]
                        i += 1
                    else:
                        res.prod += [(c2, e2)]
                        j += 1
                res.prod += self.prod[i:len(self.prod)] + other.prod[j: len(other.prod)]
                return res
            elif self.value < other.value:
                res.value = self.value
                c1, e1 = self.prod[0]
                if c1 == 0:
                    res.prod = [(0, e1 + other)] + self.prod[1:len(self.prod)]
                else:
                    res.prod = [(0, other)] + self.prod
                return res
            else:
                return other + self
        else:
            res.value = self.value
            c1, e1 = self.prod[0]
            if c1 == 0:
                res.prod = [(0, e1 + other)] + self.prod[1:len(self.prod)]
            else:
                res.prod = [(0, other)] + self.prod
            return res

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self + other

    def __mul__(self, other):
        if isinstance(other, Expr):
            if self.value == other.value:
                accu = 0
                for i in range(0, len(self.prod)):
                    c1, e1 = self.prod[i]
                    for j in range(0, len(other.prod)):
                        c2, e2 = other.prod[j]
                        r = super().__new__(Expr)
                        r.value = self.value
                        r.prod = [(c1 + c2, e1 * e2)]
                        accu = accu + r
                return accu
            elif self.value < other.value:
                r = super().__new__(Expr)
                r.value = self.value
                r.prod = [(c, e * other) for (c, e) in self.prod]
                return r
            else:
                return other * self
        else:
            r = super().__new__(Expr)
            r.value = self.value
            r.prod = [(c, e * other) for (c, e) in self.prod]
            return r

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return self + (-1 * other)

    def __rsub__(self, other):
        return (-1) * self + other

    def __and__(self, other):
        return self * other

    def __rand__(self, other):
        return self * other

    def __or__(self, other):
        if isinstance(other, bool):
            if other:
                return True
            else:
                return self
        else:
            return self + other

    def __ror__(self, other):
        return self | other

    def __pow__(self, power):
        if isinstance(power, int):
            if power == 0:
                return 1
            elif power == 1:
                return self
            elif power > 1:
                return self * (self ** (power - 1))

    def rename_var(self, name, new_name):
        if name == self.value:
            accu = 0
            p = Expr(new_name)
            for (c, e) in self.prod:
                accu += (p ** c) * e
            return accu
        elif self.value < name:
            accu = 0
            p = Expr(self.value)
            for (c, e) in self.prod:
                if isinstance(e, Expr):
                    e = e.rename_var(name, new_name)
                accu += (p ** c) * e
            return accu
        else:
            return self
