def is_perfect_number(number: int) -> bool:
    """
    Determines if a number is a perfect number.
    
    Args:
        number (int): The number to check.
        
    Returns:
        bool: True if the number is a perfect number, False otherwise.
    """
    if number <= 0:
        return False
    
    sum_of_divisors = sum(divisor for divisor in range(1, number) if number % divisor == 0)
    return sum_of_divisors == number


def main():
    """
    Main function to handle user input and determine if the number is perfect.
    """
    user_input = input("Enter a number: ").strip()
    
    try:
        number = int(user_input)
        if is_perfect_number(number):
            print(f"{number} is a perfect number.")
        else:
            print(f"{number} is not a perfect number.")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
