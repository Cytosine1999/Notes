Y0 = lambda f: (lambda x: x(x)())(lambda x: f(x(x)()))
Y1 = lambda f: (lambda x: x(x)())(lambda x: lambda a: f(x(x)(a)))
