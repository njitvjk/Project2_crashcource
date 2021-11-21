# type hinting
name: str
age: int

name = input("Your name?")
age = int(input("Your age?"))

# type hinting python functions
greeting = "Hello, {}, you're {} years old"


def greet(user: str, age: int) -> str:
    return greeting.format(user, age)


name = input("Your name?")
age = int(input("How old are you?"))

print(greet(name, age))

# type hinting class
from typing import Dict

class User:
    def __init__(self, name):
        self.name = name

users: Dict[int, User] = {
    1: User("Serdar"),
    2: User("Davis")
}

def inspect_user(user:User) -> None:
    print (user.name)

user1 = users[1]
inspect_user(user1)
