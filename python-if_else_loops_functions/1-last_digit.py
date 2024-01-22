#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
# ensures that last_digit is calculated on absolute value of number( positive)
if (last_digit > 5 and number > 0):
    result_string = (
        f"Last digit of {number} is {last_digit} and is greater than 5"
    )
elif (last_digit == 0):
    result_string = f"Last digit of {number} is {last_digit} and is 0"
else:
    result_string = (
        f"Last digit of {number} is -{last_digit} and is less than 6 and not 0"
    )

print(result_string)
