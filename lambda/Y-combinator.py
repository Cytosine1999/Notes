# =========================================== Y combinator ======================================================================
# Y = lambda f.(lambda x. x x)(lambda x. f(x x)) = lambda f.(lambda x. f(x x))(lambda x. f(x x))
# 
# =========================================== Y combinator python version =======================================================
Y = lambda f: (lambda x: f(x(x)()))(lambda x: f(x(x)()))
# ================================================ endless loop =================================================================
(lambda f: (lambda x: f(x(x)()))(lambda x: f(x(x)())))(lambda g: g())
# ================================ no parameter version (also endless loop) =====================================================
(lambda f: (lambda x: x(x))(lambda x: f(x(x)())))(lambda g: g())
# ================================================== with parameter version =====================================================
(lambda f:(lambda x: x(x))(lambda x: f(lambda n: x(x)(n))))(lambda g: lambda n: 1 if n in [1, 2] else g(n - 1) + g(n - 2))(10)
#   |         |               |           |                    |         |
# combinator recursion     wrapper pass_parameters         fibonacci calculate
# ===============================================================================================================================


# ================================================= the explicit version ========================================================
def combinator(fn):
    def recursion(function):
        return function(function)

    def wrapper(function):
        def pass_parameters(n):
            return function(function)(n)

        return fn(pass_parameters)

    return recursion(wrapper)


def fibonacci(recursive_call):
    def calculate(n):
        if n in [1, 2]:
            return 1
        else:
            return recursive_call(n - 1) + recursive_call(n - 2)

    return calculate


combinator(fibonacci)(10)
# ==============================================================================================================================


# =============================================== the computing proccess =======================================================
# this part cannot run in python!
#
# calculate:
combinator(fibonacci)(10)

    # calculate:
    combinator(fibonacci)

        # calling function combinator:
        #---------------------------------------------
        def combinator(fibonacci):
            def recursion(function):
                return function(function)

            def wrapper(function):
                def pass_parameters(n):
                    return function(function)(n)

                return fibonacci(pass_parameters)

            return recursion(wrapper)
        #---------------------------------------------

            # calculate:
            recursion(wrapper)

                # calling function recursion:
                #-------------------------------------------
                def recursion(wrapper):
                    return wrapper(wrapper)
                #-------------------------------------------

                    # calling function wrapper:
                    #----------------------------------------------
                    def wrapper(wrapper):
                        def pass_parameters(n):
                            return wrapper(wrapper)(n)

                        return fibonacci(pass_parameters)
                    #----------------------------------------------

                    # function returning:
                    return fibonacci(wrapper(wrapper)(n))

                # function returning:
                return fibonacci(lambda f: fn(lambda n: f(f)(n))(lambda f: fn(lambda n: f(f)(n)))(n))

            # calculate finished:
            fibonacci(lambda f: fn(lambda n: f(f)(n))(lambda f: fn(lambda n: f(f)(n)))(n))

        # function returning:
        return fibonacci(lambda f: fn(lambda n: f(f)(n))(lambda f: fn(lambda n: f(f)(n)))(n))

    # calculate finished:
    fibonacci(lambda f: fn(lambda n: f(f)(n))(lambda f: fn(lambda n: f(f)(n)))(n))

    # calculate:
    (fibonacci(lambda f: fn(lambda n: f(f)(n))(lambda f: fn(lambda n: f(f)(n)))(n)))(10)

    # calling fibonacci:
    (lambda n:
        1 if n in [1, 2] else (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(n - 1) +
        (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(n - 2)
    )(10)

    # if condition:
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(9) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling lambda wrapper:
    (fibonacci((lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(n - 1)))(9) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling fibonacci:
    (lambda n:
        1 if n in [1, 2] else ((lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(10))(n - 1) +
        ((lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(10))(n - 2)
    )(9) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # if condition:
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling lambda wrapper:
    (fibonacci((lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(n)))(8) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling fibonacci:
    (lambda n:
        1 if n in [1, 2] else ((lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8))(n - 1) +
        ((lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7))(n - 2)
    )(8) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling lambda wrapper, calling fibonacci and if condition:
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling lambda wrapper, calling fibonacci and if condition:
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(5) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # ----------------------------------------------------------------------------------

    # calling lambda wrapper, calling fibonacci and if condition:
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(2) +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(1) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(2) +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(3) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(4) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(5) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling lambda wrapper and calling fibonacci:
    (lambda n:
        1 if n in [1, 2] else ((lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8))(n - 1) +
        ((lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7))(n - 2)
    )(2) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(1) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(2) +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(3) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(4) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(5) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # if condition:
    1 +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(1) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(2) +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(3) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(4) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(5) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling fibonacci:
    1 +
    (lambda n:
        1 if n in [1, 2] else ((lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8))(n - 1) +
        ((lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7))(n - 2)
    )(1) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(2) +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(3) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(4) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(5) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # if condition:
    1 + 1 + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(2) +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(3) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(4) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(5) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # adding:
    2 + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(2) +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(3) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(4) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(5) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # ---------------------------------------------------------------------------------

    # calling lambda wrapper, calling fibonacci and if condition:
    3 +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(2) +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(1) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(4) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(5) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling fibonacci, if condition and adding:
    4 +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(1) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(4) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(5) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling lambda wrapper, calling fibonacci and if condition:
    5 +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(4) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(5) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # ---------------------------------------------------------------------------------

    # calling lambda wrapper, calling fibonacci and if condition:
    5 +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(2) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(1) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(2) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(5) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling fibonacci, if condition and adding:
    8 +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(5) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling lambda wrapper, calling fibonacci and if condition:
    8 +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(2) +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(1) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(2) +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(3) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling fibonacci, if condition and adding:
    11 +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(3) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling lambda wrapper, calling fibonacci and if condition:
    11 +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(2) +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(1) + 
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # calling fibonacci, if condition and adding:
    13 +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(6) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # ----------------------------------------------------------------------------------
    21 +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(7) +
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # ----------------------------------------------------------------------------------
    34 +  
    (lambda f: fibonacci(lambda n: f(f)(n)))(lambda f: fibonacci(lambda n: f(f)(n)))(8)

    # ----------------------------------------------------------------------------------

    55

    # computing finished
    return 55



















