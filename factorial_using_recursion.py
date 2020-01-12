"""
Returns the factorial of a number.
"""


def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


x = int(input("Enter a number to find factorial: "))
result = fact(x)
print(result)
