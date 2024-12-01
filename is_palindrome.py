"""
Question 2: Write a python function that checks whether a word or phrase is palindrome or not. 

    note: A palindrome is a word, phrase, or sentence that reads the same backwords as forward, eg madam, kayak, racecar or a phrase "nurses run"
"""


def is_palindrome(phrase):
    # join charcters and remove numbers then compare the word to the input word
    phrase = ''.join(c for c in phrase.lower() if c.isalnum())
    return phrase == phrase[::-1]

# use case
print(is_palindrome("madam"))
print(is_palindrome("kayak"))
print(is_palindrome("racecar"))
print(is_palindrome("nurses run"))