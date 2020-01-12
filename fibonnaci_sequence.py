"""
Fibonacci Sequence: 0 1 2 3 5 8 13......
"""


def fib(n):
    a = 0
    b = 1
    if n == 0:
        print("Length of series cannot be zero")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a+b
            a = b
            b = c
            print(c)


x = int(input("Enter the length of Fibonacci sequence: "))
fib(x)
