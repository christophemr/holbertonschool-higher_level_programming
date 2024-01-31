#!/usr/bin/python3


def roman_to_int(roman_string):
    # Check if the input is empty or not a string
    if not roman_string or type(roman_string) != str:
        # If the input is invalid
        return 0
    # Initialize a variable to store the total Arabic value
    total = 0
    # Dictionary mapping Roman numerals to their corresponding Arabic values
    roman_to_arabic = {'M': 1000, 'D': 500,
                       'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    # Iterate through the reversed Roman numeral string
    for roman_numeral in reversed(roman_string):
        # Get the Arabic value of the current Roman numeral
        arabic_value = roman_to_arabic[roman_numeral]
        # Update the total based on the conversion logic
        if total < arabic_value * 5:
          # If the total is less than 5 times the current Arabic value, add the value
            total += arabic_value
        else:
            # Otherwise, subtract the value (for cases like IV or IX)
            total -= arabic_value
      # Return the final total Arabic value
    return total
