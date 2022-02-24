"""Question 6:Create a function that accepts your name, age,
and major as input and output a dictionary that stores such information.
Please use “name”, “age”, and “major” as keys to store information"""


def my_profile(name, age, major):
    """ Function to return dict """
    profile_dict = dict()
    profile_dict["name"] = name
    profile_dict["age"] = age
    profile_dict["major"] = major

    return profile_dict


"""Question 6: Send profile input to function and print the output dictionary"""
dict_profile = my_profile("Kowsalya", "33", "MIS")
print("My Profile Dictionary returned from the function is :", dict_profile)

"""Question 7 Use loops to print the data stored in the dictionary in 6"""
print("====Print the data stored in profile dictionary====")
for key in dict_profile:
    print("key:", key, "Value:", dict_profile[key])
