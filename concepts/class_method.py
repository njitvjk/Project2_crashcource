from datetime import date


class Student:
    def __init__(self, name, age):
        # data members (instance variables)
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))


Kiran = Student('Jessa', 20)
Kiran.show()

# create new object using the factory method
Nikhil = Student.calculate_age("Joy", 1995)
Nikhil.show()
