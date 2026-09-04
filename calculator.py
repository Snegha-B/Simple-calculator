# 🧮 Python Simple Calculator

print("Python Simple Calculator")
print("-" * 30)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect the operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = input("Enter your choice: ")

if choice == "1":
    print("Result:", num1 + num2)

elif choice == "2":
    print("Result:", num1 - num2)

elif choice == "3":
    print("Result:", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Division by zero is not allowed")

elif choice == "5":
    print("Result:", num1 % num2)

else:
    print("Invalid choice")
