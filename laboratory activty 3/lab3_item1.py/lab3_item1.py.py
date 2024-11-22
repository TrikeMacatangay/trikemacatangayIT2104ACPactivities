def roman_to_integer(roman_numeral: str) -> int:
    """
    Converts a Roman numeral to an integer.
    
    Args:
        roman_numeral (str): The Roman numeral as a string.
        
    Returns:
        int: The equivalent integer value, or -1 if the input is invalid.
    """
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    roman_numeral = roman_numeral.upper()
    total = 0
    prev_value = 0
    
    for char in reversed(roman_numeral):
        if char not in roman_values:
            return -1 
        
        current_value = roman_values[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    
    return total


def main():
    """
    Main function to handle user input and display the result.
    """
    roman_numeral = input("Enter a Roman numeral: ").strip()
    result = roman_to_integer(roman_numeral)
    
    if result == -1:
        print(f"The integer value of '{roman_numeral.upper()}' is: Invalid Roman numeral.")
    else:
        print(f"The integer value of '{roman_numeral.upper()}' is: {result}")


if __name__ == "__main__":
    main()
