""" 
Question 5: Write a program that accepts a string as input, capitalizes the first letter of each word in the string,
and then returns the string
    Examples:
    "hi" => returns "Hi"
    "i love programming" => returns "I Love Programming"
     
"""

def title_case(str):
    title = str.title()
    return title

# use cases
print(title_case('i love programming'))