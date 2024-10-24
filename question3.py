# Write a Python function to check whether a string is pangram or not. (Assume
# the string passed in does not have any punctuation)
# Note: Pangrams are words or sentences containing every letter of the
# alphabet at least once. For example: "The quick brown fox jumps over the
# lazy dog"


def check_if_pangram(input_str):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_str = input_str.lower()

    for letter in alphabet:
        if letter not in input_str:
            return False

    return True


check_sentence = "The quick brown fox jumps over the lazy dog"

if check_if_pangram(check_sentence):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")
