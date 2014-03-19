# -*- coding: utf-8 -*-
# Fibonacci Sequence - Enter a number and have the
# program generate the Fibonacci sequence to that number
# or to the Nth number

def memoize(f):
    cache={}
    def decorated_function(*args):
        if args in cache: 
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
def fib(n):
    if n<2: return n
    return fib(n-2) + fib(n-1)


print fib(100)