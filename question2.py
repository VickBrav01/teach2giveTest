# Write a Python function that checks whether a word or phrase is palindrome or
# not.
# Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"


def check_name(phrase):
    word_Array = phrase.split(" ")

    converted = [word[::-1] for word in word_Array]
    result = " ".join(converted)

    if phrase == result:
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome")


check_name("racecar")
