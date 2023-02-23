'''Create a simple calculus program as a script and as module.'''

def number_sum(number_one: int, number_two: int):
    return number_one + number_two

def number_subtraction(number_one: int, number_two: int):
    return number_one - number_two

def number_division(number_one: int, number_two: int):
    return number_one / number_two

def number_multiplication(number_one: int, number_two: int):
    return number_one * number_two

sum_result = number_sum(number_one=33, number_two=11)
print("Numbers sum result: ", sum_result)

subtraction_result = number_subtraction(number_one=33, number_two=11)
print("Numbers subraction result: ", subtraction_result)

division_result = number_division(number_one=33, number_two=11)
print("Numbers division result: ", division_result)

multiplication_result = number_multiplication(number_one=33, number_two=11)
print("Numbers multiplication result: ", multiplication_result)