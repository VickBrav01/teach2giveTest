# Write a program that accepts a string as input, capitalizes the first letter of each
# word in the string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"


def capitalize_words(input_string):
    result_string = input_string.title()

    return result_string


str_input = input("Enter a string: ")
output = capitalize_words(str_input)
print(f"Output: {output}")
