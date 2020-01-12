"""
A class can be defined within a class and there are several ways to create the object
of inner class
"""


# Outer Class
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        # Inner class object creation inside the outer class
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    # Inner Class
    class Laptop:
        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = '8gb'

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('ujjwal', 1110)
# It will call the inner class show() also because it is being invoked
s1.show()

# Laptop class object outside the outer class
# Using the object of outer class
print(s1.lap.brand)

# Calling inner class method using the outer class object with inner class object
s1.lap.show()

# Directly creating object of inner class
lap2 = Student.Laptop()
lap2.show()
