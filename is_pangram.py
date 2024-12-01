"""
Question 3: Write a Python function that checks whether a string is a pangram or not.(Assume the string passed in in does not have any punctuation) 

    note: Pangrams are words or sentences containing every letter of the alphabet at least once. For example:"The quick
    brown fox jumps over the lazy dog"
    """

def is_pangram(sentence):
    sentence = set(sentence.lower())
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # compare characters on the alphabet to the sentence
    return alphabet.issubset(sentence)

# use case
print(is_pangram("The quick brown fox jumps over the lazy dog"))