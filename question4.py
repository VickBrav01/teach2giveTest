# Write a program that takes an integer as input and returns an integer with
# reversed digit ordering.


def int_reverse(int_value):
    convert_int = abs(int_value)
    result_str = str(convert_int)[::-1]
    result_int = int(result_str)

    if int_value < 0:
        return -result_int
    return result_int


int_value = int(input("Enter an number: "))
test_int = int_reverse(int_value)

print(test_int)
