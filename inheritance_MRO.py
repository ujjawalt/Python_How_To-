"""
Method Resolution Order in  Multiple Inheritance
MRO-> Priority given from left->right in inheriting class values
"""


class A:
    def __init__(self):
        print("init of A")

    def feature1(self):
        print("Feature 1-A")

    def feature2(self):
        print("Feature 2")


class B:
    def __init__(self):
        print("init of B")

    def feature1(self):
        print("Feature 1-B")

    def feature4(self):
        print("Feature 4")


"""
To get a different result replace class C(A, B)->class C(B, A)
"""


class C(A, B):
    def __init__(self):
        super().__init__()
        print("init of C")

    def feature5(self):
        print("Feature 3")

    # Using super() to call method of super class
    def feat(self):
        super().feature2()


c1 = C()
c1.feat()
c1.feature1()
