#   https://www.lynda.com/Python-tutorials/Introducing-Python/604237/622567-4.html
def fib(n):
    """ Print a Fibonacci series upto n"""
    a, b = 0,1
    while b < n:
        print(b),
        a, b = b, a+b

fib(2000)