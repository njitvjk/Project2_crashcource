"""Question 8:create a class that contains some properties and a method.
The properties should have “name”, “age”,  and “major”.
The method should print out a string that contains the above properties."""


class Profile:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def print_profile(self):
        print(f"Hello ! My Name is {self.name}, I'm {self.age} years old and I am pursuing {self.major}")


my_profile = Profile("Kowsalya", 33, "MIS")
my_profile.print_profile()
