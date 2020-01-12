"""
Multiple Inheritance- Two or more different class are inherited by the same class.
"""


class A:
    def method1(self):
        print("Method 1 of class A")

    def method2(self):
        print("Method 2 of class A")


class B:
    def method3(self):
        print("Method 3 of class B")

    def method4(self):
        print("Method 4 of class B")


class C(A, B):
    def method5(self):
        print("Method 5 of class C")


b1 = B()
b1.method3()
b1.method4()

c1 = C()
c1.method1()
c1.method2()
c1.method3()
c1.method4()
c1.method5()
