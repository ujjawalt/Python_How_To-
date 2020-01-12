"""
Polymorphism using Duck Typing
ide instance changes according to the class which initialises it.
"""


class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running.....")


class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running.....")


class Laptop:
    def code(self, ide):
        ide.execute()


lap1 = Laptop()
ide = PyCharm()
lap1.code(ide)
print()
ide = MyEditor()
lap1.code(ide)
