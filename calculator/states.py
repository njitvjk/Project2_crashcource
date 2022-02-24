"""Question 1- this function takes 5 arguments - states and returns a list.
prefix * has been used to receive multiple arguments"""


def return_states(*states):
    state_list = []
    for i in states:
        state_list.append(i)

    return state_list


"""Question1 :passing states to function and print the list
    f string has been used to print the states """
st_list = return_states("AL", "CA", "GA", "NJ", "FL")
print(f"The states in the list are {st_list}")

"""Question2 :lower case the returned list and sort it"""

for i in range(len(st_list)):
    st_list[i] = st_list[i].lower()
print(f" The state list after converting to lower case: {st_list}")
st_list.sort()
print(f" The state list after sorting in ascending order: {st_list}")
st_list.sort(reverse=True)
print(f" The state list after sorting in descending order: {st_list}")
