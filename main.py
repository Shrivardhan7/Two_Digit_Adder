# This program adds the digits in a 2 digit number. 
#e.g. if the input was 89, then the output should be 8 + 9 = 17
two_digit_number = input("Type a two digit number: ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)