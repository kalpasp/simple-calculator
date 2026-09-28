def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("==============================")
    print("      SIMPLE CALCULATOR")
    print("==============================")

    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Calculator closed.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                result = add(a, b)

            elif choice == "2":
                result = subtract(a, b)

            elif choice == "3":
                result = multiply(a, b)

            elif choice == "4":
                result = divide(a, b)

            print("Result:", result)

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
