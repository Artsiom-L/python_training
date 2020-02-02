from functools import reduce


def luhn(code):
    code = reduce(str.__add__, filter(str.isdigit, code))
    result_sum = 0
    if len(code) % 2 != 0:
        print('Error: incorrect code length')
        return False
    is_odd = True
    for char in code:
        if is_odd:
            double_char = 2 * int(char)
            if double_char > 9:
                result_sum += double_char - 9
            else:
                result_sum += double_char
        else:
            result_sum += int(char)
        is_odd = not is_odd
    return result_sum % 10 == 0


user_code = input("Enter the card code: ")
print("Is valid: ", luhn(user_code))
