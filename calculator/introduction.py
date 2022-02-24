"""Question 3- Write a short introduction and store it in a string"""
str_intro = """Hello everyone, My name is Kowsalya. 
I'm a second semester MIS student. 
I love to have friends and do painting in my leisure time. 
I also love to travel and shopping."""

print(str_intro)

"""Question 4-Connect Q3 string with string containing ID in the end"""
str_id = "My Student ID is 31556115"
str_intro = str_intro + "\n" + str_id
print("\n======After concatenating ID with the introduction text=======\n")
print(str_intro)

"""Question 5-Check for the student ID at the end in question 4"""
print("\n===========================\n")
print("Does the introduction has an ID at the end:", str_intro.endswith('31556115'))
