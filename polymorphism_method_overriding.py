"""
Polymorphism using Method Overriding.
This can be achieved in Inheritance.
Method of one class is overridden in other class to give different output.
"""


class A:
    def show(self):
        print("show() of A class")


class B(A):
    def show(self):
        print("Same show() method but in B class")


b1 = B()
b1.show()
