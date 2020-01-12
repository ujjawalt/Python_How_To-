"""
Single Level Inheritance- A single class is inherited by another class
"""


class A:
    def method1(self):
        print("Method 1 of class A")

    def method2(self):
        print("Method 2 of class A")


class B(A):
    def method3(self):
        print("Method 3 of class B")

    def method4(self):
        print("Method 4 of class B")


b1 = B()
b1.method1()
b1.method2()
b1.method3()
b1.method4()
