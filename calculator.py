#THIS IS MY CALCULATOR IN PYTHON 
def calculator():

    print("--- Simple Python Calculator ---")
    print("Enter 'exit' to quit")

    while True:
        try:
            user_input = input("\nEnter calculation (e.g., 10 + 5): ").strip()

            if user_input.lower() == 'exit':
                print("Goodbye!")
                break

            parts = user_input.split()
            
            if len(parts) != 3:
                print("Usage: [Number] [Operator] [Number] (Example: 5 + 5)")
                continue

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            if operator == '+':
                result = num1 + num2
            else:
                if operator == '-':
                    result = num1 - num2
                else:
                    if operator == '*':
                        result = num1 * num2
                    else:
                        if operator == '/':
                            if num2 != 0:
                                result = num1 / num2
                            else:
                                result = "Error: Division by zero"
                        else:
                            result = "Invalid Operator (Use +, -, *, /)"

            print(f"Result: {result}")

        except ValueError:
            print("Error: Please enter valid numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    calculator()
