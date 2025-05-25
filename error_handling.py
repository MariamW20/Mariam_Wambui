def get_valid_number(prompt):
    """
    Function to get a valid number from user input with error handling.
    Uses an infinite loop until valid input is provided.
    """
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            print("Error: Please enter a valid number!")
            print("Invalid input detected. Try again.\n")

def divide_numbers():
    """
    Main function to perform division with comprehensive error handling.
    """
    print("=== Division Calculator with Error Handling ===")
    print("This program will divide two numbers you provide.\n")
    
    while True:
        try:
            # Get first number
            print("Enter the first number (numerator):")
            num1 = get_valid_number("First number: ")
            
            # Get second number
            print("\nEnter the second number (denominator):")
            num2 = get_valid_number("Second number: ")
            
            # Check for division by zero
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                print("The denominator cannot be zero. Please try again.\n")
                continue
            
            # Perform division
            result = num1 / num2
            
            # Display result
            print(f"\n✓ Success!")
            print(f"Result: {num1} ÷ {num2} = {result}")
            print(f"Rounded result: {round(result, 4)}")
            
            # Ask if user wants to continue
            while True:
                try:
                    continue_choice = input("\nDo you want to perform another division? (y/n): ").lower().strip()
                    if continue_choice in ['y', 'yes']:
                        print("\n" + "="*50)
                        break
                    elif continue_choice in ['n', 'no']:
                        print("Thank you for using the Division Calculator!")
                        return
                    else:
                        print("Please enter 'y' for yes or 'n' for no.")
                except KeyboardInterrupt:
                    print("\n\nProgram interrupted by user. Goodbye!")
                    return
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.\n")
            
if __name__ == "__main__":
    divide_numbers()
    
    