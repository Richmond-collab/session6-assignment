def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return a times b."""
    return a * b


def divide(a, b):
    """Return a divided by b, or an error message if b is zero."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("=== Simple Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation (1-4): ")

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice.")
        return

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    else:
        result = divide(num1, num2)
        

    print(f"Result: {result}")


if __name__ == "__main__":
    main()