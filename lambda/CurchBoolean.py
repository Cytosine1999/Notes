import Combinator

# $ for lambda

# $ t f. t
TRUE = lambda t: lambda f: t
# $ t f. f
FALSE = lambda t: lambda f: f

# transfer from Church Booleans to python bool
ToBool = lambda p: p(True)(False)
# transfer from python bool to Church Booleans
FromBool = lambda p: TRUE if p else FALSE

# operations
# $ p t f: p FALSE TRUE t f
Not = lambda p: lambda t: lambda f: p(FALSE)(TRUE)(t)(f)
# $ p q t f: p q p t f
And = lambda p: lambda q: lambda t: lambda f: p(q)(p)(t)(f)
# $ p q t f: p p q t f
Or = lambda p: lambda q: lambda t: lambda f: p(p)(q)(t)(f)
# $ p q t f: p (Not q) q t f
Xor = lambda p: lambda q: lambda t: lambda f: p(Not(q))(q)(t)(f)

if __name__ == '__main__':
    print('Church Boolean TRUE:', ToBool(TRUE))
    print('Church Boolean FALSE:', ToBool(FALSE))
    print('Church Boolean operation Not TRUE:', ToBool(Not(TRUE)))
    print('Church Boolean operation Not FALSE:', ToBool(Not(FALSE)))
    print('Church Boolean operation And TRUE TRUE:', ToBool(And(TRUE)(TRUE)))
    print('Church Boolean operation And TRUE FALSE:', ToBool(And(TRUE)(FALSE)))
    print('Church Boolean operation And FALSE TRUE:', ToBool(And(FALSE)(TRUE)))
    print('Church Boolean operation And FALSE FALSE:', ToBool(And(FALSE)(FALSE)))
    print('Church Boolean operation Or TRUE TRUE:', ToBool(Or(TRUE)(TRUE)))
    print('Church Boolean operation Or TRUE FALSE:', ToBool(Or(TRUE)(FALSE)))
    print('Church Boolean operation Or FALSE TRUE:', ToBool(Or(FALSE)(TRUE)))
    print('Church Boolean operation Or FALSE FALSE:', ToBool(Or(FALSE)(FALSE)))
    print('Church Boolean operation Xor TRUE TRUE:', ToBool(Xor(TRUE)(TRUE)))
    print('Church Boolean operation Xor TRUE FALSE:', ToBool(Xor(TRUE)(FALSE)))
    print('Church Boolean operation Xor FALSE TRUE:', ToBool(Xor(FALSE)(TRUE)))
    print('Church Boolean operation Xor FALSE FALSE:', ToBool(Xor(FALSE)(FALSE)))
