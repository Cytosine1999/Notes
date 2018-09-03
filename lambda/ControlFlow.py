from CurchBoolean import TRUE, FALSE, FromBool, ToBool
from ChurchNumeral import ZERO, ONE, FromInt, ToInt
import Combinator

# control flow
# $ p a b: p a b
IfElse = lambda p: lambda a: lambda b: p(a)(b)
#
Loop = lambda a: Combinator.Y1(lambda x: lambda a: IfElse(a)(x(a - 1))(a))

if __name__ == '__main__':
    print('Control flow IfElse TRUE 0 1:', ToInt(IfElse(TRUE)(ZERO)(ONE)))
    print('Control flow IfElse FALSE 0 1:', ToInt(IfElse(FALSE)(ZERO)(ONE)))
