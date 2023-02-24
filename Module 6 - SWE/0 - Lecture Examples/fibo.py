# Fibonacci numbers module
# https://docs.python.org/3/tutorial/modules.html

import sys


def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# if this module is called directly, take the command line
# argument and do something with it

if __name__ == "__main__":
    fib(int(sys.argv[1]))
