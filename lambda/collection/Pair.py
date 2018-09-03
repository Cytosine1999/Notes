# $ a b f. f a b
ChurchPair = lambda a: lambda b: lambda f: f(a)(b)
# $ a b. a
First = lambda a: lambda b: a
# $ a b. b
Second = lambda a: lambda b: b

if __name__ == '__main__':
    from ChurchNumeral import FromInt, ToInt

    first = FromInt(int(input('Input first integer: ')))
    second = FromInt(int(input('Input second integer: ')))
    pair = ChurchPair(first)(second)
    print('First number:', ToInt(pair(First)))
    print('Second number:', ToInt(pair(Second)))
