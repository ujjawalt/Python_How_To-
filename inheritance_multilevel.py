"""
Multilevel Inheritance- Class A->B->C There are steps in inheritance
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


class C(B):
    def method5(self):
        print("Method 5 of class C")


c1 = C()
c1.method1()
c1.method2()
c1.method3()
c1.method4()
c1.method5()
