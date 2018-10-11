# $ for lambda

# Church numerals
# $ s z. z
ZERO = lambda s: lambda z: z
# $ s z. s z
ONE = lambda s: lambda z: s(z)
# $ s z. s (s z)
TWO = lambda s: lambda z: s(s(z))
# $ s z. s (s (s z))
THREE = lambda s: lambda z: s(s(s(z)))

# transfer from Church numerals to python Int
ToInt = lambda f: f(lambda n: n + 1)(0)
# transfer from python Int to Church numerals
FromInt = lambda n: lambda s: lambda z: (lambda f: (lambda x: x(x))(lambda x: f(lambda n: x(x)(n))))(
    lambda g: lambda n: z if n == 0 else s(g(n - 1)))(n)


def pyPrint(*args, **kwargs):
    print(*obj)
    return lambda x: x()


def PrintInt(function):
    print(ToInt(function))
    return lambda x: x()


def InputInt(str):
    return FromInt(int(input(str)))


# operations
# $ n s z. s (n s z)
Inc = lambda n: lambda s: lambda z: s(n(s)(z))
# $ n s z. n ($ g h. h (g s)) ($ u. z) ($ u. u)
Dec = lambda n: lambda s: lambda z: n(lambda g: lambda h: h(g(s)))(lambda u: z)(lambda u: u)
# $ n m s z: n s (m s z)
Add = lambda n: lambda m: lambda s: lambda z: n(s)(m(s)(z))
# $ n m s z: m Dec n s z
Sub = lambda n: lambda m: lambda s: lambda z: m(Dec)(n)(s)(z)
# $ n m s z: n (m s) z
Mul = lambda n: lambda m: lambda s: lambda z: n(m(s))(z)
# $ n m s z: m n s z
Exp = lambda n: lambda m: lambda s: lambda z: m(n)(s)(z)

if __name__ == "__main__":
    VAR = InputInt('Please input an integer: ')
    print('Church numeral 0 :', ToInt(ZERO))
    print('Church numeral 1 :', ToInt(ONE))
    print('Church numeral', ToInt(VAR), ':', ToInt(VAR))
    print('Church numeral operation Inc', ToInt(VAR), ':', ToInt(Inc(VAR)))
    print('Church numeral operation Dec', ToInt(VAR), ':', ToInt(Dec(VAR)))
    print('Church numeral operation Add', ToInt(VAR), '3 :', ToInt(Add(VAR)(THREE)))
    print('Church numeral operation Sub', ToInt(VAR), '3 :', ToInt(Sub(VAR)(THREE)))
    print('Church numeral operation Mul', ToInt(VAR), '3 :', ToInt(Mul(VAR)(THREE)))
    print('Church numeral operation Exp', ToInt(VAR), '3 :', ToInt(Exp(VAR)(THREE)))
