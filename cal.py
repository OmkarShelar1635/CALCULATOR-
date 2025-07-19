import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def power(self, a, b):
        return a ** b

    def square_root(self, a):
        if a < 0:
            return "Error: Square root of negative number"
        return math.sqrt(a)

def main():
    calc = Calculator()

    while True:
        print("-------Calculator Menu---------\n")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '7':
            print("Exiting Calculator.")
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Try again.")
            continue

        if choice == '6':
            a = float(input("Enter number: "))
            print("Result:", calc.square_root(a))
        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", calc.add(a, b))
            elif choice == '2':
                print("Result:", calc.subtract(a, b))
            elif choice == '3':
                print("Result:", calc.multiply(a, b))
            elif choice == '4':
                print("Result:", calc.divide(a, b))
            elif choice == '5':
                print("Result:", calc.power(a, b))

if __name__ == "__main__":
    main()
