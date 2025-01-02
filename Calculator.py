def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def add(num1, num2):
    return num1 + num2

def main():
    print("Welcome to the Choice-Driven Calculator!")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")
    while True:
            choice = int(input("Enter your choice (1/2/3): "))
            
            if choice == 4:
                print("Exiting the program. Goodbye!")
                break
            
            if choice not in [1, 2, 3]:
                print("Invalid choice. Please choose 1, 2, or 3.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Dictionary to simulate case statements
            operations = {
                1: ("Addition", add),
                2: ("Subtract", subtract),
                3: ("Multiply", multiply)
            }
            
            operation_name, operation_func = operations[choice]
            result = operation_func(num1, num2)
            print(f"{operation_name} result: {result}")

if __name__ == "__main__":
    main()
