# Handling ZeroDivision Exception
# print(5/0)

# Using Try and except
try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero")

# File not found exception
filename = 'sample.txt'
try:
    with open(filename) as f:
        f.read()
except FileNotFoundError:
    print("file not found")



