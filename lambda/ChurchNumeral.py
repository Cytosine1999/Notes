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
    FOUR = FromInt(4)
    print('Church numeral 0:', ToInt(ZERO))
    print('Church numeral 1:', ToInt(ONE))
    print('Church numeral 4:', ToInt(FOUR))
    print('Church numeral operation Inc 4:', ToInt(Inc(FOUR)))
    print('Church numeral operation Dec 4:', ToInt(Dec(FOUR)))
    print('Church numeral operation Add 4 3:', ToInt(Add(FOUR)(THREE)))
    print('Church numeral operation Sub 4 3:', ToInt(Sub(FOUR)(THREE)))
    print('Church numeral operation Mul 4 3:', ToInt(Mul(FOUR)(THREE)))
    print('Church numeral operation Exp 4 3:', ToInt(Exp(FOUR)(THREE)))
