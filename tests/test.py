class A:
    def __init__(self, gpioPort):
        self.gpioPort = gpioPort

    def p(self):
        print(self.gpioPort)


class B(A):
    pass


B(12).p()

C = type('C', (A,), dict({}))
print(C)
C(14).p()


def value(value=None):
    if value == None:
        return 'get_value'
    else:
        print(value)


def m(a, b, c=None, d=None):
    print(a, b, c, d)


m(1, 2)

print(value('set_value'))
print(value())


class A1:
    @property
    def p(self):
        return {"a": 10}


class AA(A1):
    @property
    def p(self):
        return super().p


a = AA()
print(a.p)