class Student:
    school = 'ABC School'

    @classmethod
    def info(cls, value):
        cls.school = value
        return cls.school

    @staticmethod
    def info_class():
        print("This is the static method, it has nothing to do with the class or instance Variables.")


s1 = Student
print(Student.info('University'))
Student.info_class()
