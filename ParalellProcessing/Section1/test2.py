def fib(n):
    """ Print a Fibonacci series upto n"""
    a, b = 0,1
    while b < n:
        print(b),
        a, b = b, a+b

fib(2000)