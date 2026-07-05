print("Welcome to the Calculator Program!")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = int(input("Please select an operation (1-4): "))
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("You selected operation:", operation)
def add(x, y):
    return x + y    
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
if operation == 1:
    result = add(num1, num2)
    print("The result is:", result)
elif operation == 2:
    result = subtract(num1, num2)
    print("The result is:", result)
elif operation == 3:
    result = multiply(num1, num2)
    print("The result is:", result)
elif operation == 4:
    result = divide(num1, num2)
    print("The result is:", result)