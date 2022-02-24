# Step 0: Import numpy -- ALWAYS import all the libraries you need at the beginning!
import numpy as np


# Step 1: Function creation -- refer to the last lab for the syntax of function creation
# does our function take parameters?
# Create your function here:
def array_members(arr1, arr2):
    print("random_array", arr1)
    print("user_array", arr2)
    print(np.equal(arr1, arr2))
    return np.equal(arr1, arr2)


# Step 2: Create an array of four random integers between 1 and 10
random_arry = np.random.randint(0, 10, 4)

# Step 3: Print your numbers
print("Random array is:", random_arry)

# Step 4: Prompt the user to enter four numbers, ONE AT A TIME. Use a loop to store these four numbers in a new array
#  HINT 1: We could take all four numbers in through one line, but to practice loop, let's do it the hard way
#  HINT 2: You can start by creating an empty array -- np.array([]), then appending to it one at a time
#  HINT 3: Remember, input() only returns STRINGS. You need to turn them into integers

print("Enter four random values to guess:")
user_arry= np.array([])

for i in range(4):
    input_value = int(input("Enter Value:"))
    user_arry = np.append(user_arry, input_value)
#print(user_arry)


# Step 5: Now that you have the two arrays, you can compare them using array functions and decide whether the answers are correct
#  HINT 4: To compare two arrays, you can use array1 == array2 -- however, you have to use a variable to hold the result
#          The resulted array is an array of Boolean values. To quickly check whether it contains true value, you might want to
#          use the all() or any() function...


boolean_arry = array_members(random_arry, user_arry)
result = np.all(boolean_arry == True)
if result:
    print('Congratulations !! All values match, you have guessed it right')
else:
    print("Sorry! The values does not match. Please try again" )

