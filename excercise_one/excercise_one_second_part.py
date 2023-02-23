import calculus

first_number = int(input("Please enter first number: "))
second_number = int(input("Please enter second number: "))

numbers_addition_result = calculus.number_sum(first_number,second_number)
print(first_number, " + ", second_number, " = ", numbers_addition_result)

numbers_subtract_result = calculus.number_subtraction(first_number,second_number)
print(first_number, " - ", second_number, " = ", numbers_subtract_result)

numbers_division_result = calculus.number_division(first_number,second_number)
print(first_number, " / ", second_number, " = ", numbers_division_result)

numbers_multiplication_result = calculus.number_multiplication(first_number,second_number)
print(first_number, " * ", second_number, " = ", numbers_multiplication_result)
