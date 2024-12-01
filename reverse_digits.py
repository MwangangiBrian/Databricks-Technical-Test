"""
    Question 4: Write a program that takes an integer as input and returns an integer with reversed digit ordering.
    
"""

def reverse_digits(integer):
    num= abs(integer)
    # convert integer to string
    num_str = str(num)
    # reverse string and remove any leading zeros
    reversed_str = num_str[::-1].lstrip("0")
    if integer > 0:
        return int(reversed_str)
    elif integer < 0:
        return -int(reversed_str)

    else:
        return integer

#use case
print(reverse_digits(500))
print(reverse_digits(-56))
print(reverse_digits(-90))
print(reverse_digits(91))
